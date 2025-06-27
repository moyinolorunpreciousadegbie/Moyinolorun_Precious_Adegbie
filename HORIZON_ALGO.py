#!/usr/bin/env python3

#.. code:: ipython3

	import os
	import sys
	import numpy as np
	import segyio 
	from matplotlib import pyplot as plt
	from tkinter import *
	from tkinter import filedialog
	import ipywidgets as widgets
	from ipywidgets import interact
	
	import plotly.express as px
	import plotly.graph_objects as go
	
#.. code:: ipython3

	def load_segy_file():
		'''
		Function to load a segy file
		
		Return file path of loaded segy file
		'''
		
		global filepath
		
		# Open file name
		file = filedialog.askopenfilename(initialdir = os.getcwd(),
		title = "Please select 2D/3D post-stack seismic data in segy format",
		filetypes = [('sgy files','*.sgy'),('segy files','*.segy'),('All files','*.*')])
		filepath = file
		print("File_path: {0}".format(filepath))
		
	# Create root window
	root = Tk()
	root.geometry('300x200')  
	root.title('AB')
	
	# Open button to click in a GUI toolkit
	open_button1 = Button(root, text = "Open a File", command = load_segy_file)
	open_button2 = Button(root, text = "Close the Window", command = root.destroy)
	open_button1.pack()
	open_button2.pack()
	
	# Run the application
	root.mainloop()
	
.. code:: ipython3

	def identify_seismic_data_parameters(filepath_in):    
		"""     
		Function to identify data type as 2D or 3D and Post-Stack or Pre-Stack as well as seismic amplitude traces and geometry-related parameters
		
		Parameter:
		----------
		filepath_in (str): file path of loaded segy file
		
		Returns:
		--------
		data_display (numpy.ndarray): Seismic amplitude traces to plot
		data_type, seismic_data_shape, cdp_no, sample_rate, twt , inline_number, xline_number, diff_inline, diff_xline    
	
		Author: Amir Abbas Babasafari (AB)
		"""
		
		with segyio.open(    filepath_in, ignore_geometry=True) as f: #  filepath_in, ignore_geometry=True) as f:
			data_format = f.format
		
		# Supported inline and crossline byte locations
		inline_xline = [[189,193], [9,13], [9,21], [5,21]]
		state = False
		
		# Read segy data with the specified byte location of geometry 
		for k, byte_loc in enumerate(inline_xline):
			
			try:
				with segyio.open(filepath_in, iline = byte_loc[0], xline = byte_loc[1], ignore_geometry=False) as f:
					# Get the attributes
					seismic_data = segyio.tools.cube(f)
					n_traces = f.tracecount    
					# data = f.trace.raw[:].T 
					# tr = f.bin[segyio.BinField.Traces]
					tr = f.attributes(segyio.TraceField.TraceNumber)[-1]
					if not isinstance(tr, int):
						tr = f.attributes(segyio.TraceField.TraceNumber)[-2] + 1
					tr = int(tr[0])
					spec = segyio.spec()
					spec.sorting = f.sorting
					data_sorting = spec.sorting == segyio.TraceSortingFormat.INLINE_SORTING
					twt = f.samples
					sample_rate = segyio.tools.dt(f) / 1000
					n_samples = f.samples.size
					
					# TRACE_SEQUENCE_FILE _ byte location:5
					TraceSequenceFile = []
					# FieldRecord _ byte location:9
					Field_Record = []
					# Trace_Field _ byte location:13
					Trace_Field = []
					# CDP _ byte location:21
					CDP = []
					# INLINE_3D _ byte location:189
					Inline_3D = []
					# CROSSLINE_3D _ byte location:193
					Crossline_3D = []
					
					for i in range(n_traces):
						trace_no = f.attributes(segyio.TraceField.TRACE_SEQUENCE_FILE)[i]; TraceSequenceFile.append(trace_no)
						field_record = f.attributes(segyio.TraceField.FieldRecord)[i]; Field_Record.append(field_record)
						trace_field = f.attributes(segyio.TraceField.TraceNumber)[i]; Trace_Field.append(trace_field)
						cdp = f.attributes(segyio.TraceField.CDP)[i]; CDP.append(cdp)
						inline = f.attributes(segyio.TraceField.INLINE_3D)[i]; Inline_3D.append(inline)
						xline = f.attributes(segyio.TraceField.CROSSLINE_3D)[i]; Crossline_3D.append(xline)
						
				inline3d = np.unique(Inline_3D)
				crossline3d = np.unique(Crossline_3D)
				fieldrecord = np.unique(Field_Record)
				tracefield = np.unique(Trace_Field)
				tracesequence = np.unique(TraceSequenceFile)
				cdpnumber = np.unique(CDP)
				
				state = True
				
			except:
				pass
				
			if state:
				
				# Identify data as 2D/3D and Post-stack/Pre-stack
				if len(seismic_data.shape) == 3:
					if seismic_data.shape[0] != 1:
						data_type = 'Post-stack 3D'
					else:
						if n_traces > tr > 1:   
							data_type = 'Post-stack 3D'
						else:
							data_type = 'Post-stack 2D'
							
				else:        
					if len(f.offsets) > 1:
						if seismic_data.shape[0] == 1:
							data_type = 'Pre-Stack 2D'
						else:
							data_type = 'Pre-Stack 3D'    
					else:
						print('Error, Please check inline and crossline byte locations')
						
				# create geometry-related parameters
				if k==0:
					inline_number = inline3d 
					xline_number = crossline3d
				elif k==1:
					inline_number = fieldrecord 
					xline_number = tracefield
				elif k==2:
					inline_number = fieldrecord 
					xline_number = cdpnumber
				elif k==3:
					inline_number = tracesequence 
					xline_number = cdpnumber
					
				if data_type == 'Post-stack 3D':
					if len(inline_number) == 1 or len(xline_number) == 1:
						pass
					else:
						break
				else:
					break
				
				
		# reshape seismic data to the corresponding format based on data type
		try:
			inline, cdp, samples = seismic_data.shape
		except:
			print("Error, data was not loaded successfully, this could happen due to unsupported data format: {0}.".format(data_format)) 
			print("In addition, please check inline and crossline byte locations, that might not be supported in this script.")  
			print("Data format 4-byte IBM float and 4-byte IEEE float are supported.")
			
			
		if data_type == 'Post-stack 2D':
			data_display = seismic_data.reshape(cdp, samples).T
			cdp_no = np.arange(n_traces) 
			
			diff_inline = 1
			diff_xline = 1
			
			print('Data Type: {0}'.format(data_type))
			print('Seismic Data Shape (Time sample, CDP number) : {0}'.format(data_display.shape))
			
		elif data_type == 'Post-stack 3D':
			if inline == 1 and tr > 1 and n_traces % tr == 0:  
				inline_no =  n_traces / tr
				data_display = seismic_data.reshape(int(inline_no), int(tr), int(samples)).T
				xline_number = np.arange(tr)
				inline_number = np.arange(inline_no)
				cdp_no = xline_number
				
			else:  
				data_display = seismic_data.reshape(inline, cdp, samples).T
				cdp_no = np.arange(cdp)
				
			diff_inline = np.diff(inline_number)[0]
			diff_xline = np.diff(xline_number)[0]
			
			print('Data Type: {0}'.format(data_type))
			print('Seismic Data Shape (Time sample, crossline number, inline number) : {0}'.format(data_display.shape))
			
		return data_display, data_type, data_display.shape, cdp_no, sample_rate, twt, inline_number, xline_number, diff_inline, diff_xline
	filepath = "/Users/moyinolorunadegbie/Downloads/Nanuq 3D AK.SGY"
	data_display, data_type, seismic_data_shape, cdp_no, sample_rate, twt , inline_number, xline_number, diff_inline, diff_xline= identify_seismic_data_parameters(filepath)
	

.. parsed-literal::
	
	Data Type: Post-stack 3D
	Seismic Data Shape (Time sample, crossline number, inline number) : (1000, 729, 717)
	
	
.. code:: ipython3

	#############
	#############
	#############
	#############
	#############
	#############
	
.. code:: ipython3

	#!/usr/bin/env python3
	
	
	
	class SEIS:
		def __init__(self, tup,tup2, LO, LO2, px, go, vis, vis2 ,  pos_neg , FIG, NFIG, plsize , pls_circ_square):
			self.tup = tup
			self.tup2 = tup2
			
			self.LO = LO
			self.LO2 = LO2
			
			self.px = px
			self.go = go
			
			self.vis = vis
			self.vis2 = vis2
			
			self.pos_neg =  pos_neg
			
			self.FIG = FIG
			self.NFIG = NFIG
			self.plsize = plsize
			self.pls_circ_square = pls_circ_square
			
			self.xj = []
			self.yj = []
			self.zj = []
			
			
			self.xm = []
			self.ym = []
			self.zm = []
			
			
			self.area = {}
			
			self.sepe = [False] ## <<<<<
			
			self.sepe2 = [False] ## <<<<<
			
			self.plot2 = [False] ## <<<<<
			
			self.reduce_z = 1 # 10 ############################
			
		def check_pos(self, seismic_data, _18, x,y,z):
			CL , RW, UP_DOW  = x,y,z
			if seismic_data[ UP_DOW , RW , CL ] < -_18     :
				return   True
			return False
		
		def check_neg(self, seismic_data, _18, x,y,z):
			CL , RW, UP_DOW  = x,y,z
			if _18 < seismic_data[ UP_DOW , RW , CL] :
				return   True
			return False
		
		
		########################################################################################################################################################################################################################################################################################################################
		def slope1(self,xyz,rad,radZ,seismic_data, _18,x2,y2,z2):
			#xyz = [5,5,5]
			#rad = 25 # rad X 1,2,3,4,5,6,7...... n
			#radZ = 7 # DONT CHANGE , radZ = rad , incase of slopier horizon
			x1y1z1 = []
			x2y2z2 = []
			ind = 0
			for i in xyz :
				if ind == len(xyz)-1:
					x1y1z1.append(i-(radZ//2)  ) #<<<<<<<< radZ
					x2y2z2.append(i+(radZ//2)  ) #<<<<<<<< radZ
					break
				x1y1z1.append(i-rad) 
				x2y2z2.append(i+rad  )
				ind+=1
				
			#print(x1y1z1)
			#print(x2y2z2)
				
			lenght = (rad * 2) + 1
			xyz_n = []
			xx=[]
			yy=[]
			zz=[]
			mp = {}
			mx = float('-inf')
			mn = float('inf')
			red_blue = ['EMPTY']
			stp = 7 # 1
			for i in range(lenght):
				for j in range(0,radZ, stp):#<<<<<<<< radZ                                   STEP THE radz
					ax,by,cz =  x1y1z1[0] , x1y1z1[1] + i , x1y1z1[2] + j#z
					aax,bby,ccz =  x1y1z1[0] + i, x1y1z1[1]  , x1y1z1[2] + j#z
					aaax,bbby,cccz =  x1y1z1[0] + i, x1y1z1[1] + j , x1y1z1[2] 
				
					ax_,by_,cz_ =  x2y2z2[0] , x2y2z2[1] - i , x2y2z2[2] - j#z
					aax_,bby_,ccz_ =  x2y2z2[0] - i, x2y2z2[1]  , x2y2z2[2] - j#z
					aaax_,bbby_,cccz_ =  x2y2z2[0] - i, x2y2z2[1] - j , x2y2z2[2] 
				
					if [ax,by,cz] not in xyz_n:
						xyz_n.append([ax,by,cz])
						xx.append(ax)
						yy.append(by)
						zz.append(cz)
					if [aax,bby,ccz] not in xyz_n:
						xyz_n.append([aax,bby,ccz])
						xx.append(aax)
						yy.append(bby)
						zz.append(ccz)
					if [aaax,bbby,cccz] not in xyz_n:
						#xyz_n.append([aaax,bbby,cccz]) #
						#xx.append(aaax) #
						#yy.append(bbby) #
						#zz.append(cccz) #
						pass
						
						
					if [ax_,by_,cz_] not in xyz_n:
						xyz_n.append([ax_,by_,cz_])
						xx.append(ax_)
						yy.append(by_)
						zz.append(cz_)
					if [aax_,bby_,ccz_] not in xyz_n:
						xyz_n.append([aax_,bby_,ccz_])
						xx.append(aax_)
						yy.append(bby_)
						zz.append(ccz_)
					if [aaax_,bbby_,cccz_] not in xyz_n:
						#xyz_n.append([aaax_,bbby_,cccz_]) #
						#xx.append(aaax_) #
						#yy.append(bbby_) #
						#zz.append(cccz_) #
						pass
						
						
					if self.pos_neg[0] == "Negative" :
						red_blue[0] = "red"
						if 0<=ax<=x2 and  0<=by<=y2 and 0<=cz<=z2  :
							if self.check_neg(seismic_data, _18, ax,by,cz)  and [ax,by,cz] not in self.LO:
								#print("ATLEAST")
								x_coords, y_coords , z_coords = ax,by,cz                # Z1 <<<<
								mp[(ax,by)] = min(cz , mn) #  UPPER HORIZON IN RANGE    # |  radius(upper minimum, MIN.)
								#mp[(ax,by)] = max(cz , mx)								# |
								self.LO.append([ax,by,cz]) #                            # Z2
								if self.sepe[0] :
									self.xj.append(ax)
									self.yj.append(by)
									self.zj.append(cz)
								if self.sepe2[0] :
									if not (ax,by) in self.area :
										self.area[(ax,by)] = []
									self.area[(ax,by)].append(cz)
									
						if 0<=aax<=x2 and  0<=bby<=y2 and 0<=ccz<=z2  :
							if self.check_neg(seismic_data, _18, aax,bby,ccz)  and [aax,bby,ccz] not in self.LO:
								x_coords, y_coords , z_coords = aax,bby,ccz
								mp[(aax,bby)] = min(ccz , mn) #  UPPER HORIZON IN RANGE
								#mp[(aax,bby)] = max(ccz , mx)
								self.LO.append([aax,bby,ccz])
								if self.sepe[0] :
									self.xj.append(aax)
									self.yj.append(bby)
									self.zj.append(ccz)
								if self.sepe2[0] :
									if not (aax,bby) in self.area :
										self.area[(aax,bby)] = []
									self.area[(aax,bby)].append(ccz)
									
						#if 0<=aaax<=x2 and  0<=bbby<=y2 and 0<=cccz<=z2  :
							#if self.check_neg(seismic_data, _18, aaax,bbby,cccz)  and [aaax,bbby,cccz] not in self.LO:
								#x_coords, y_coords , z_coords = aaax,bbby,cccz
								#mp[(aaax,bbby)] = min(cccz , mn) #  UPPER HORIZON IN RANGE
								#mp[(aaax,bbby)] = max(cccz , mx) 
								#self.LO.append([aaax,bbby,cccz])
								#if self.sepe[0] :
									#self.xj.append(aaax)
									#self.yj.append(bbby)
									#self.zj.append(cccz)
								#if self.sepe2[0] :
									#if not (aaax,bbby) in self.area :
										#self.area[(aaax,bbby)] = []
									#self.area[(aaax,bbby)].append(cccz)
									
									
									
						if 0<=ax_<=x2 and  0<=by_<=y2 and 0<=cz_<=z2  :
							if self.check_neg(seismic_data, _18, ax_,by_,cz_)  and [ax_,by_,cz_] not in self.LO:
								x_coords, y_coords , z_coords = ax_,by_,cz_
								mp[(ax_,by_)] = min(cz_ , mn) #  UPPER HORIZON IN RANGE
								#mp[(ax_,by_)] = max(cz_ , mx)
								self.LO.append([ax_,by_,cz_])
								if self.sepe[0] :
									self.xj.append(ax_)
									self.yj.append(by_)
									self.zj.append(cz_)
								if self.sepe2[0] :
									if not (ax_,by_) in self.area :
										self.area[(ax_,by_)] = []
									self.area[(ax_,by_)].append(cz_)
									
						if 0<=aax_<=x2 and  0<=bby_<=y2 and 0<=ccz_<=z2  :
							if self.check_neg(seismic_data, _18, aax_,bby_,ccz_)  and [aax_,bby_,ccz_] not in self.LO:
								x_coords, y_coords , z_coords = aax_,bby_,ccz_
								mp[(aax_,bby_)] = min(ccz_ , mn) #  UPPER HORIZON IN RANGE
								#mp[(aax_,bby_)] = max(ccz_ , mx)
								self.LO.append([aax_,bby_,ccz_])
								if self.sepe[0] :
									self.xj.append(aax_)
									self.yj.append(bby_)
									self.zj.append(ccz_)
								if self.sepe2[0] :
									if not (aax_,bby_) in self.area :
										self.area[(aax_,bby_)] = []
									self.area[(aax_,bby_)].append(ccz_)
									
						#if 0<=aaax_<=x2 and  0<=bbby_<=y2 and 0<=cccz_<=z2  :
							#if self.check_neg(seismic_data, _18, aaax_,bbby_,cccz_)  and [aaax_,bbby_,cccz_] not in self.LO:
								#x_coords, y_coords , z_coords = aaax_,bbby_,cccz_
								#mp[(aaax_,bbby_)] = min(cccz_ , mn) #  UPPER HORIZON IN RANGE
								#mp[(aaax_,bbby_)] = max(cccz_ , mx)
								#self.LO.append([aaax_,bbby_,cccz_])
								#if self.sepe[0] :
									#self.xj.append(aaax_)
									#self.yj.append(bbby_)
									#self.zj.append(cccz_)
								#if self.sepe2[0] :
									#if not (aaax_,bbby_) in self.area :
										#self.area[(aaax_,bbby_)] = []
									#self.area[(aaax_,bbby_)].append(cccz_)
									
					########################################################################################################			
					if self.pos_neg[0] == "Positive" :
						red_blue[0] = "blue"
						if 0<=ax<=x2 and  0<=by<=y2 and 0<=cz<=z2  :
							if self.check_pos(seismic_data, _18, ax,by,cz)  and [ax,by,cz] not in self.LO:
								#print("ATLEAST")
								x_coords, y_coords , z_coords = ax,by,cz                # Z1 <<<<
								mp[(ax,by)] = min(cz , mn) #  UPPER HORIZON IN RANGE    # |  radius(upper minimum, MIN.)
								#mp[(ax,by)] = max(cz , mx)								# |
								self.LO.append([ax,by,cz]) #                            # Z2
								if self.sepe[0] :
									self.xj.append(ax)
									self.yj.append(by)
									self.zj.append(cz)
								if self.sepe2[0] :
									if not (ax,by) in self.area :
										self.area[(ax,by)] = []
									self.area[(ax,by)].append(cz)
									
						if 0<=aax<=x2 and  0<=bby<=y2 and 0<=ccz<=z2  :
							if self.check_pos(seismic_data, _18, aax,bby,ccz)  and [aax,bby,ccz] not in self.LO:
								x_coords, y_coords , z_coords = aax,bby,ccz
								mp[(aax,bby)] = min(ccz , mn) #  UPPER HORIZON IN RANGE
								#mp[(aax,bby)] = max(ccz , mx)
								self.LO.append([aax,bby,ccz])
								if self.sepe[0] :
									self.xj.append(aax)
									self.yj.append(bby)
									self.zj.append(ccz)
								if self.sepe2[0] :
									if not (aax,bby) in self.area :
										self.area[(aax,bby)] = []
									self.area[(aax,bby)].append(ccz)
									
						#if 0<=aaax<=x2 and  0<=bbby<=y2 and 0<=cccz<=z2  :
							#if self.check_pos(seismic_data, _18, aaax,bbby,cccz)  and [aaax,bbby,cccz] not in self.LO:
								#x_coords, y_coords , z_coords = aaax,bbby,cccz
								#mp[(aaax,bbby)] = min(cccz , mn) #  UPPER HORIZON IN RANGE
								#mp[(aaax,bbby)] = max(cccz , mx) 
								#self.LO.append([aaax,bbby,cccz])
								#if self.sepe[0] :
									#self.xj.append(aaax)
									#self.yj.append(bbby)
									#self.zj.append(cccz)
								#if self.sepe2[0] :
									#if not (aaax,bbby) in self.area :
										#self.area[(aaax,bbby)] = []
									#self.area[(aaax,bbby)].append(cccz)
									
									
									
						if 0<=ax_<=x2 and  0<=by_<=y2 and 0<=cz_<=z2  :
							if self.check_pos(seismic_data, _18, ax_,by_,cz_)  and [ax_,by_,cz_] not in self.LO:
								x_coords, y_coords , z_coords = ax_,by_,cz_
								mp[(ax_,by_)] = min(cz_ , mn) #  UPPER HORIZON IN RANGE
								#mp[(ax_,by_)] = max(cz_ , mx)
								self.LO.append([ax_,by_,cz_])
								if self.sepe[0] :
									self.xj.append(ax_)
									self.yj.append(by_)
									self.zj.append(cz_)
								if self.sepe2[0] :
									if not (ax_,by_) in self.area :
										self.area[(ax_,by_)] = []
									self.area[(ax_,by_)].append(cz_)
									
						if 0<=aax_<=x2 and  0<=bby_<=y2 and 0<=ccz_<=z2  :
							if self.check_pos(seismic_data, _18, aax_,bby_,ccz_)  and [aax_,bby_,ccz_] not in self.LO:
								x_coords, y_coords , z_coords = aax_,bby_,ccz_
								mp[(aax_,bby_)] = min(ccz_ , mn) #  UPPER HORIZON IN RANGE
								#mp[(aax_,bby_)] = max(ccz_ , mx)
								self.LO.append([aax_,bby_,ccz_])
								if self.sepe[0] :
									self.xj.append(aax_)
									self.yj.append(bby_)
									self.zj.append(ccz_)
								if self.sepe2[0] :
									if not (aax_,bby_) in self.area :
										self.area[(aax_,bby_)] = []
									self.area[(aax_,bby_)].append(ccz_)
									
						#if 0<=aaax_<=x2 and  0<=bbby_<=y2 and 0<=cccz_<=z2  :
							#if self.check_pos(seismic_data, _18, aaax_,bbby_,cccz_)  and [aaax_,bbby_,cccz_] not in self.LO:
								#x_coords, y_coords , z_coords = aaax_,bbby_,cccz_
								#mp[(aaax_,bbby_)] = min(cccz_ , mn) #  UPPER HORIZON IN RANGE
								#mp[(aaax_,bbby_)] = max(cccz_ , mx)
								#self.LO.append([aaax_,bbby_,cccz_])
								#if self.sepe[0] :
									#self.xj.append(aaax_)
									#self.yj.append(bbby_)
									#self.zj.append(cccz_)
								#if self.sepe2[0] :
									#if not (aaax_,bbby_) in self.area :
										#self.area[(aaax_,bbby_)] = []
									#self.area[(aaax_,bbby_)].append(cccz_)
									
									
			for  k , v in mp.items():
				x_coords , y_coords = k[0], k[1]
				z_coords = v # / self.reduce_z # minimum, horizon
				self.FIG.add_trace(self.go.Scatter3d(x=[x_coords], y=[y_coords], z=[z_coords]  , mode='markers', marker=dict(size=[self.plsize],
						color=[ red_blue[0] ] , symbol= self.pls_circ_square ) ))
				self.xm.append(x_coords)
				self.ym.append(y_coords)
				self.zm.append(z_coords)
				
				if self.plot2[0] :
					fig = self.go.Figure(self.go.Surface(
						
						x = [int(x_coords),int(x_coords+1)],
						y = [int(y_coords),int(y_coords+1)],
						z=[[z_coords]*2 for v in range(2)] 
						, colorscale=[[0, red_blue[0]  ], [1, red_blue[0] ]]    ))
					
					self.tup += fig.data 
					#self.FIG =  self.go.Figure(data= self.tup )
					
					
					
		#########################################################################################################################################################################################################################################################################################################################
					
		def slope2(self,xyz,rad,seismic_data,_18,x2,y2,z2):
			#xyz = [5,5,5]
			#rad = 25 # rad X 1,2,3,4,5,6,7...... n
			#radZ = 7 # DONT CHANGE , radZ = rad , incase of slopier horizon
			
			x1y1z1 = []
			x2y2z2 = []
			ind = 0
			for i in xyz :
				if ind == len(xyz)-1:
					x1y1z1.append(i-(rad//2)  )  #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
					x2y2z2.append(i+(rad//2)  )  #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
					break
				x1y1z1.append(i-rad) 
				x2y2z2.append(i+rad  )
				ind+=1
				
			#print(x1y1z1)
			#print(x2y2z2)
				
			lenght = (rad * 2) + 1
			xyz_n = []
			xx=[]
			yy=[]
			zz=[]
			mp = {}
			mx = float('-inf')
			mn = float('inf')
			red_blue = ['EMPTY']
			stp = 1
			for i in range(lenght):
				for j in range(0,rad,stp): #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<                                        STEP THE rad
					ax,by,cz =  x1y1z1[0] , x1y1z1[1] + i , x1y1z1[2] + j#z
					aax,bby,ccz =  x1y1z1[0] + i, x1y1z1[1]  , x1y1z1[2] + j#z
					aaax,bbby,cccz =  x1y1z1[0] + i, x1y1z1[1] + j , x1y1z1[2] 
				
					ax_,by_,cz_ =  x2y2z2[0] , x2y2z2[1] - i , x2y2z2[2] - j#z
					aax_,bby_,ccz_ =  x2y2z2[0] - i, x2y2z2[1]  , x2y2z2[2] - j#z
					aaax_,bbby_,cccz_ =  x2y2z2[0] - i, x2y2z2[1] - j , x2y2z2[2] 
				
					if [ax,by,cz] not in xyz_n:
						xyz_n.append([ax,by,cz])
						xx.append(ax)
						yy.append(by)
						zz.append(cz)
					if [aax,bby,ccz] not in xyz_n:
						xyz_n.append([aax,bby,ccz])
						xx.append(aax)
						yy.append(bby)
						zz.append(ccz)
					if [aaax,bbby,cccz] not in xyz_n:
						#xyz_n.append([aaax,bbby,cccz]) #
						#xx.append(aaax) #
						#yy.append(bbby) #
						#zz.append(cccz) #
						pass
						
						
					if [ax_,by_,cz_] not in xyz_n:
						xyz_n.append([ax_,by_,cz_])
						xx.append(ax_)
						yy.append(by_)
						zz.append(cz_)
					if [aax_,bby_,ccz_] not in xyz_n:
						xyz_n.append([aax_,bby_,ccz_])
						xx.append(aax_)
						yy.append(bby_)
						zz.append(ccz_)
					if [aaax_,bbby_,cccz_] not in xyz_n:
						#xyz_n.append([aaax_,bbby_,cccz_]) #
						#xx.append(aaax_) #
						#yy.append(bbby_) #
						#zz.append(cccz_) #
						pass
						
						
					if self.pos_neg[0] == "Negative" :
						red_blue[0] = "red"
						if 0<=ax<=x2 and  0<=by<=y2 and 0<=cz<=z2  :
							if self.check_neg(seismic_data, _18, ax,by,cz)  and [ax,by,cz] not in self.LO:
								#print("ATLEAST")
								x_coords, y_coords , z_coords = ax,by,cz                # Z1 <<<<
								mp[(ax,by)] = min(cz , mn) #  UPPER HORIZON IN RANGE    # |  radius(upper minimum, MIN.)
								#mp[(ax,by)] = max(cz , mx)								# |
								self.LO.append([ax,by,cz]) #                            # Z2
								if self.sepe[0] :
									self.xj.append(ax)
									self.yj.append(by)
									self.zj.append(cz)
								if self.sepe2[0] :
									if not (ax,by) in self.area :
										self.area[(ax,by)] = []
									self.area[(ax,by)].append(cz)
									
						if 0<=aax<=x2 and  0<=bby<=y2 and 0<=ccz<=z2  :
							if self.check_neg(seismic_data, _18, aax,bby,ccz)  and [aax,bby,ccz] not in self.LO:
								x_coords, y_coords , z_coords = aax,bby,ccz
								mp[(aax,bby)] = min(ccz , mn) #  UPPER HORIZON IN RANGE
								#mp[(aax,bby)] = max(ccz , mx)
								self.LO.append([aax,bby,ccz])
								if self.sepe[0] :
									self.xj.append(aax)
									self.yj.append(bby)
									self.zj.append(ccz)
								if self.sepe2[0] :
									if not (aax,bby) in self.area :
										self.area[(aax,bby)] = []
									self.area[(aax,bby)].append(ccz)
									
						#if 0<=aaax<=x2 and  0<=bbby<=y2 and 0<=cccz<=z2  :
							#if self.check_neg(seismic_data, _18, aaax,bbby,cccz)  and [aaax,bbby,cccz] not in self.LO:
								#x_coords, y_coords , z_coords = aaax,bbby,cccz
								#mp[(aaax,bbby)] = min(cccz , mn) #  UPPER HORIZON IN RANGE
								#mp[(aaax,bbby)] = max(cccz , mx) 
								#self.LO.append([aaax,bbby,cccz])
								#if self.sepe[0] :
									#self.xj.append(aaax)
									#self.yj.append(bbby)
									#self.zj.append(cccz)
								#if self.sepe2[0] :
									#if not (aaax,bbby) in self.area :
										#self.area[(aaax,bbby)] = []
									#self.area[(aaax,bbby)].append(cccz)
									
									
									
						if 0<=ax_<=x2 and  0<=by_<=y2 and 0<=cz_<=z2  :
							if self.check_neg(seismic_data, _18, ax_,by_,cz_)  and [ax_,by_,cz_] not in self.LO:
								x_coords, y_coords , z_coords = ax_,by_,cz_
								mp[(ax_,by_)] = min(cz_ , mn) #  UPPER HORIZON IN RANGE
								#mp[(ax_,by_)] = max(cz_ , mx)
								self.LO.append([ax_,by_,cz_])
								if self.sepe[0] :
									self.xj.append(ax_)
									self.yj.append(by_)
									self.zj.append(cz_)
								if self.sepe2[0] :
									if not (ax_,by_) in self.area :
										self.area[(ax_,by_)] = []
									self.area[(ax_,by_)].append(cz_)
									
						if 0<=aax_<=x2 and  0<=bby_<=y2 and 0<=ccz_<=z2  :
							if self.check_neg(seismic_data, _18, aax_,bby_,ccz_)  and [aax_,bby_,ccz_] not in self.LO:
								x_coords, y_coords , z_coords = aax_,bby_,ccz_
								mp[(aax_,bby_)] = min(ccz_ , mn) #  UPPER HORIZON IN RANGE
								#mp[(aax_,bby_)] = max(ccz_ , mx)
								self.LO.append([aax_,bby_,ccz_])
								if self.sepe[0] :
									self.xj.append(aax_)
									self.yj.append(bby_)
									self.zj.append(ccz_)
								if self.sepe2[0] :
									if not (aax_,bby_) in self.area :
										self.area[(aax_,bby_)] = []
									self.area[(aax_,bby_)].append(ccz_)
									
						#if 0<=aaax_<=x2 and  0<=bbby_<=y2 and 0<=cccz_<=z2  :
							#if self.check_neg(seismic_data, _18, aaax_,bbby_,cccz_)  and [aaax_,bbby_,cccz_] not in self.LO:
								#x_coords, y_coords , z_coords = aaax_,bbby_,cccz_
								#mp[(aaax_,bbby_)] = min(cccz_ , mn) #  UPPER HORIZON IN RANGE
								#mp[(aaax_,bbby_)] = max(cccz_ , mx)
								#self.LO.append([aaax_,bbby_,cccz_])
								#if self.sepe[0] :
									#self.xj.append(aaax_)
									#self.yj.append(bbby_)
									#self.zj.append(cccz_)
								#if self.sepe2[0] :
									#if not (aaax_,bbby_) in self.area :
										#self.area[(aaax_,bbby_)] = []
									#self.area[(aaax_,bbby_)].append(cccz_)
									
					########################################################################################################			
					if self.pos_neg[0] == "Positive" :
						red_blue[0] = "blue"
						if 0<=ax<=x2 and  0<=by<=y2 and 0<=cz<=z2  :
							if self.check_pos(seismic_data, _18, ax,by,cz)  and [ax,by,cz] not in self.LO:
								#print("ATLEAST")
								x_coords, y_coords , z_coords = ax,by,cz                # Z1 <<<<
								mp[(ax,by)] = min(cz , mn) #  UPPER HORIZON IN RANGE    # |  radius(upper minimum, MIN.)
								#mp[(ax,by)] = max(cz , mx)								# |
								self.LO.append([ax,by,cz]) #                            # Z2
								if self.sepe[0] :
									self.xj.append(ax)
									self.yj.append(by)
									self.zj.append(cz)
								if self.sepe2[0] :
									if not (ax,by) in self.area :
										self.area[(ax,by)] = []
									self.area[(ax,by)].append(cz)
									
						if 0<=aax<=x2 and  0<=bby<=y2 and 0<=ccz<=z2  :
							if self.check_pos(seismic_data, _18, aax,bby,ccz)  and [aax,bby,ccz] not in self.LO:
								x_coords, y_coords , z_coords = aax,bby,ccz
								mp[(aax,bby)] = min(ccz , mn) #  UPPER HORIZON IN RANGE
								#mp[(aax,bby)] = max(ccz , mx)
								self.LO.append([aax,bby,ccz])
								if self.sepe[0] :
									self.xj.append(aax)
									self.yj.append(bby)
									self.zj.append(ccz)
								if self.sepe2[0] :
									if not (aax,bby) in self.area :
										self.area[(aax,bby)] = []
									self.area[(aax,bby)].append(ccz)
									
						#if 0<=aaax<=x2 and  0<=bbby<=y2 and 0<=cccz<=z2  :
							#if self.check_pos(seismic_data, _18, aaax,bbby,cccz)  and [aaax,bbby,cccz] not in self.LO:
								#x_coords, y_coords , z_coords = aaax,bbby,cccz
								#mp[(aaax,bbby)] = min(cccz , mn) #  UPPER HORIZON IN RANGE
								#mp[(aaax,bbby)] = max(cccz , mx) 
								#self.LO.append([aaax,bbby,cccz])
								#if self.sepe[0] :
									#self.xj.append(aaax)
									#self.yj.append(bbby)
									#self.zj.append(cccz)
								#if self.sepe2[0] :
									#if not (aaax,bbby) in self.area :
										#self.area[(aaax,bbby)] = []
									#self.area[(aaax,bbby)].append(cccz)
									
									
									
						if 0<=ax_<=x2 and  0<=by_<=y2 and 0<=cz_<=z2  :
							if self.check_pos(seismic_data, _18, ax_,by_,cz_)  and [ax_,by_,cz_] not in self.LO:
								x_coords, y_coords , z_coords = ax_,by_,cz_
								mp[(ax_,by_)] = min(cz_ , mn) #  UPPER HORIZON IN RANGE
								#mp[(ax_,by_)] = max(cz_ , mx)
								self.LO.append([ax_,by_,cz_])
								if self.sepe[0] :
									self.xj.append(ax_)
									self.yj.append(by_)
									self.zj.append(cz_)
								if self.sepe2[0] :
									if not (ax_,by_) in self.area :
										self.area[(ax_,by_)] = []
									self.area[(ax_,by_)].append(cz_)
									
						if 0<=aax_<=x2 and  0<=bby_<=y2 and 0<=ccz_<=z2  :
							if self.check_pos(seismic_data, _18, aax_,bby_,ccz_)  and [aax_,bby_,ccz_] not in self.LO:
								x_coords, y_coords , z_coords = aax_,bby_,ccz_
								mp[(aax_,bby_)] = min(ccz_ , mn) #  UPPER HORIZON IN RANGE
								#mp[(aax_,bby_)] = max(ccz_ , mx)
								self.LO.append([aax_,bby_,ccz_])
								if self.sepe[0] :
									self.xj.append(aax_)
									self.yj.append(bby_)
									self.zj.append(ccz_)
								if self.sepe2[0] :
									if not (aax_,bby_) in self.area :
										self.area[(aax_,bby_)] = []
									self.area[(aax_,bby_)].append(ccz_)
									
						#if 0<=aaax_<=x2 and  0<=bbby_<=y2 and 0<=cccz_<=z2  :
							#if self.check_pos(seismic_data, _18, aaax_,bbby_,cccz_)  and [aaax_,bbby_,cccz_] not in self.LO:
								#x_coords, y_coords , z_coords = aaax_,bbby_,cccz_
								#mp[(aaax_,bbby_)] = min(cccz_ , mn) #  UPPER HORIZON IN RANGE
								#mp[(aaax_,bbby_)] = max(cccz_ , mx)
								#self.LO.append([aaax_,bbby_,cccz_])
								#if self.sepe[0] :
									#self.xj.append(aaax_)
									#self.yj.append(bbby_)
									#self.zj.append(cccz_)
								#if self.sepe2[0] :
									#if not (aaax_,bbby_) in self.area :
										#self.area[(aaax_,bbby_)] = []
									#self.area[(aaax_,bbby_)].append(cccz_)								
									
			for  k , v in mp.items():
				x_coords , y_coords = k[0], k[1]
				z_coords = v # / self.reduce_z # minimum, horizon
				self.FIG.add_trace(self.go.Scatter3d(x=[x_coords], y=[y_coords], z=[z_coords], mode='markers', marker=dict(size=[self.plsize],
					color=[ red_blue[0] ] , symbol= self.pls_circ_square ) ))
				self.xm.append(x_coords)
				self.ym.append(y_coords)
				self.zm.append(z_coords)
				
				if self.plot2[0] :
					fig = self.go.Figure(self.go.Surface(
						
						x = [int(x_coords),int(x_coords+1)],
						y = [int(y_coords),int(y_coords+1)],
						z=[[z_coords]*2 for v in range(2)] 
						, colorscale=[[0, red_blue[0]  ], [1, red_blue[0] ]]    ))
					
					self.tup += fig.data 
					#self.FIG =  self.go.Figure(data= self.tup )
					
		########################################################################################################################################################################################################################################################################################################################
					
		def slope3(self,xyz,rad,seismic_data, _18,x2,y2,z2):
			#xyz = [5,5,5]
			#rad = 6 # rad X 1,2,3,4,5,6,7...... n
			# SLOPIEST HORIZON
			x1y1z1 = []
			x2y2z2 = []
			for i in xyz :
				x1y1z1.append(i-rad) 
				x2y2z2.append(i+rad  )
				
			#print(x1y1z1)
			#print(x2y2z2)
				
			lenght = (rad * 2) + 1
			xyz_n = []
			xx=[]
			yy=[]
			zz=[]
			mp = {}
			mx = float('-inf')
			mn = float('inf')
			red_blue = ['EMPTY']
			stp = 1
			for i in range(lenght):
				for j in range(0,lenght,stp): #                                      STEP THE lenght
					ax,by,cz =  x1y1z1[0] , x1y1z1[1] + i , x1y1z1[2] + j#z
					aax,bby,ccz =  x1y1z1[0] + i, x1y1z1[1]  , x1y1z1[2] + j#z
					aaax,bbby,cccz =  x1y1z1[0] + i, x1y1z1[1] + j , x1y1z1[2] 
				
					ax_,by_,cz_ =  x2y2z2[0] , x2y2z2[1] - i , x2y2z2[2] - j#z
					aax_,bby_,ccz_ =  x2y2z2[0] - i, x2y2z2[1]  , x2y2z2[2] - j#z
					aaax_,bbby_,cccz_ =  x2y2z2[0] - i, x2y2z2[1] - j , x2y2z2[2] 
				
					if [ax,by,cz] not in xyz_n:
						xyz_n.append([ax,by,cz])
						xx.append(ax)
						yy.append(by)
						zz.append(cz)
					if [aax,bby,ccz] not in xyz_n:
						xyz_n.append([aax,bby,ccz])
						xx.append(aax)
						yy.append(bby)
						zz.append(ccz)
					if [aaax,bbby,cccz] not in xyz_n:
						#xyz_n.append([aaax,bbby,cccz]) #
						#xx.append(aaax) #
						#yy.append(bbby) #
						#zz.append(cccz) #
						pass
						
						
					if [ax_,by_,cz_] not in xyz_n:
						xyz_n.append([ax_,by_,cz_])
						xx.append(ax_)
						yy.append(by_)
						zz.append(cz_)
					if [aax_,bby_,ccz_] not in xyz_n:
						xyz_n.append([aax_,bby_,ccz_])
						xx.append(aax_)
						yy.append(bby_)
						zz.append(ccz_)
					if [aaax_,bbby_,cccz_] not in xyz_n:
						#xyz_n.append([aaax_,bbby_,cccz_]) #
						#xx.append(aaax_) #
						#yy.append(bbby_) #
						#zz.append(cccz_) #
						pass
						
						
					if self.pos_neg[0] == "Negative" :
						red_blue[0] = "red"
						if 0<=ax<=x2 and  0<=by<=y2 and 0<=cz<=z2  :
							if self.check_neg(seismic_data, _18, ax,by,cz)  and [ax,by,cz] not in self.LO:
								#print("ATLEAST")
								x_coords, y_coords , z_coords = ax,by,cz                # Z1 <<<<
								mp[(ax,by)] = min(cz , mn) #  UPPER HORIZON IN RANGE    # |  radius(upper minimum, MIN.)
								#mp[(ax,by)] = max(cz , mx)								# |
								self.LO.append([ax,by,cz]) #                            # Z2
								if self.sepe[0] :
									self.xj.append(ax)
									self.yj.append(by)
									self.zj.append(cz)
								if self.sepe2[0] :
									if not (ax,by) in self.area :
										self.area[(ax,by)] = []
									self.area[(ax,by)].append(cz)
									
						if 0<=aax<=x2 and  0<=bby<=y2 and 0<=ccz<=z2  :
							if self.check_neg(seismic_data, _18, aax,bby,ccz)  and [aax,bby,ccz] not in self.LO:
								x_coords, y_coords , z_coords = aax,bby,ccz
								mp[(aax,bby)] = min(ccz , mn) #  UPPER HORIZON IN RANGE
								#mp[(aax,bby)] = max(ccz , mx)
								self.LO.append([aax,bby,ccz])
								if self.sepe[0] :
									self.xj.append(aax)
									self.yj.append(bby)
									self.zj.append(ccz)
								if self.sepe2[0] :
									if not (aax,bby) in self.area :
										self.area[(aax,bby)] = []
									self.area[(aax,bby)].append(ccz)
									
						#if 0<=aaax<=x2 and  0<=bbby<=y2 and 0<=cccz<=z2  :
							#if self.check_neg(seismic_data, _18, aaax,bbby,cccz)  and [aaax,bbby,cccz] not in self.LO:
								#x_coords, y_coords , z_coords = aaax,bbby,cccz
								#mp[(aaax,bbby)] = min(cccz , mn) #  UPPER HORIZON IN RANGE
								#mp[(aaax,bbby)] = max(cccz , mx) 
								#self.LO.append([aaax,bbby,cccz])
								#if self.sepe[0] :
									#self.xj.append(aaax)
									#self.yj.append(bbby)
									#self.zj.append(cccz)
								#if self.sepe2[0] :
									#if not (aaax,bbby) in self.area :
										#self.area[(aaax,bbby)] = []
									#self.area[(aaax,bbby)].append(cccz)
									
									
									
						if 0<=ax_<=x2 and  0<=by_<=y2 and 0<=cz_<=z2  :
							if self.check_neg(seismic_data, _18, ax_,by_,cz_)  and [ax_,by_,cz_] not in self.LO:
								x_coords, y_coords , z_coords = ax_,by_,cz_
								mp[(ax_,by_)] = min(cz_ , mn) #  UPPER HORIZON IN RANGE
								#mp[(ax_,by_)] = max(cz_ , mx)
								self.LO.append([ax_,by_,cz_])
								if self.sepe[0] :
									self.xj.append(ax_)
									self.yj.append(by_)
									self.zj.append(cz_)
								if self.sepe2[0] :
									if not (ax_,by_) in self.area :
										self.area[(ax_,by_)] = []
									self.area[(ax_,by_)].append(cz_)
									
						if 0<=aax_<=x2 and  0<=bby_<=y2 and 0<=ccz_<=z2  :
							if self.check_neg(seismic_data, _18, aax_,bby_,ccz_)  and [aax_,bby_,ccz_] not in self.LO:
								x_coords, y_coords , z_coords = aax_,bby_,ccz_
								mp[(aax_,bby_)] = min(ccz_ , mn) #  UPPER HORIZON IN RANGE
								#mp[(aax_,bby_)] = max(ccz_ , mx)
								self.LO.append([aax_,bby_,ccz_])
								if self.sepe[0] :
									self.xj.append(aax_)
									self.yj.append(bby_)
									self.zj.append(ccz_)
								if self.sepe2[0] :
									if not (aax_,bby_) in self.area :
										self.area[(aax_,bby_)] = []
									self.area[(aax_,bby_)].append(ccz_)
									
						#if 0<=aaax_<=x2 and  0<=bbby_<=y2 and 0<=cccz_<=z2  :
							#if self.check_neg(seismic_data, _18, aaax_,bbby_,cccz_)  and [aaax_,bbby_,cccz_] not in self.LO:
								#x_coords, y_coords , z_coords = aaax_,bbby_,cccz_
								#mp[(aaax_,bbby_)] = min(cccz_ , mn) #  UPPER HORIZON IN RANGE
								#mp[(aaax_,bbby_)] = max(cccz_ , mx)
								#self.LO.append([aaax_,bbby_,cccz_])
								#if self.sepe[0] :
									#self.xj.append(aaax_)
									#self.yj.append(bbby_)
									#self.zj.append(cccz_)
								#if self.sepe2[0] :
									#if not (aaax_,bbby_) in self.area :
										#self.area[(aaax_,bbby_)] = []
									#self.area[(aaax_,bbby_)].append(cccz_)
									
					########################################################################################################			
					if self.pos_neg[0] == "Positive" :
						red_blue[0] = "blue"
						if 0<=ax<=x2 and  0<=by<=y2 and 0<=cz<=z2  :
							if self.check_pos(seismic_data, _18, ax,by,cz)  and [ax,by,cz] not in self.LO:
								#print("ATLEAST")
								x_coords, y_coords , z_coords = ax,by,cz                # Z1 <<<<
								mp[(ax,by)] = min(cz , mn) #  UPPER HORIZON IN RANGE    # |  radius(upper minimum, MIN.)
								#mp[(ax,by)] = max(cz , mx)								# |
								self.LO.append([ax,by,cz]) #                            # Z2
								if self.sepe[0] :
									self.xj.append(ax)
									self.yj.append(by)
									self.zj.append(cz)
								if self.sepe2[0] :
									if not (ax,by) in self.area :
										self.area[(ax,by)] = []
									self.area[(ax,by)].append(cz)
									
						if 0<=aax<=x2 and  0<=bby<=y2 and 0<=ccz<=z2  :
							if self.check_pos(seismic_data, _18, aax,bby,ccz)  and [aax,bby,ccz] not in self.LO:
								x_coords, y_coords , z_coords = aax,bby,ccz
								mp[(aax,bby)] = min(ccz , mn) #  UPPER HORIZON IN RANGE
								#mp[(aax,bby)] = max(ccz , mx)
								self.LO.append([aax,bby,ccz])
								if self.sepe[0] :
									self.xj.append(aax)
									self.yj.append(bby)
									self.zj.append(ccz)
								if self.sepe2[0] :
									if not (aax,bby) in self.area :
										self.area[(aax,bby)] = []
									self.area[(aax,bby)].append(ccz)
									
						#if 0<=aaax<=x2 and  0<=bbby<=y2 and 0<=cccz<=z2  :
							#if self.check_pos(seismic_data, _18, aaax,bbby,cccz)  and [aaax,bbby,cccz] not in self.LO:
								#x_coords, y_coords , z_coords = aaax,bbby,cccz
								#mp[(aaax,bbby)] = min(cccz , mn) #  UPPER HORIZON IN RANGE
								#mp[(aaax,bbby)] = max(cccz , mx) 
								#self.LO.append([aaax,bbby,cccz])
								#if self.sepe[0] :
									#self.xj.append(aaax)
									#self.yj.append(bbby)
									#self.zj.append(cccz)
								#if self.sepe2[0] :
									#if not (aaax,bbby) in self.area :
										#self.area[(aaax,bbby)] = []
									#self.area[(aaax,bbby)].append(cccz)
									
									
									
						if 0<=ax_<=x2 and  0<=by_<=y2 and 0<=cz_<=z2  :
							if self.check_pos(seismic_data, _18, ax_,by_,cz_)  and [ax_,by_,cz_] not in self.LO:
								x_coords, y_coords , z_coords = ax_,by_,cz_
								mp[(ax_,by_)] = min(cz_ , mn) #  UPPER HORIZON IN RANGE
								#mp[(ax_,by_)] = max(cz_ , mx)
								self.LO.append([ax_,by_,cz_])
								if self.sepe[0] :
									self.xj.append(ax_)
									self.yj.append(by_)
									self.zj.append(cz_)
								if self.sepe2[0] :
									if not (ax_,by_) in self.area :
										self.area[(ax_,by_)] = []
									self.area[(ax_,by_)].append(cz_)
									
						if 0<=aax_<=x2 and  0<=bby_<=y2 and 0<=ccz_<=z2  :
							if self.check_pos(seismic_data, _18, aax_,bby_,ccz_)  and [aax_,bby_,ccz_] not in self.LO:
								x_coords, y_coords , z_coords = aax_,bby_,ccz_
								mp[(aax_,bby_)] = min(ccz_ , mn) #  UPPER HORIZON IN RANGE
								#mp[(aax_,bby_)] = max(ccz_ , mx)
								self.LO.append([aax_,bby_,ccz_])
								if self.sepe[0] :
									self.xj.append(aax_)
									self.yj.append(bby_)
									self.zj.append(ccz_)
								if self.sepe2[0] :
									if not (aax_,bby_) in self.area :
										self.area[(aax_,bby_)] = []
									self.area[(aax_,bby_)].append(ccz_)
									
						#if 0<=aaax_<=x2 and  0<=bbby_<=y2 and 0<=cccz_<=z2  :
							#if self.check_pos(seismic_data, _18, aaax_,bbby_,cccz_)  and [aaax_,bbby_,cccz_] not in self.LO:
								#x_coords, y_coords , z_coords = aaax_,bbby_,cccz_
								#mp[(aaax_,bbby_)] = min(cccz_ , mn) #  UPPER HORIZON IN RANGE
								#mp[(aaax_,bbby_)] = max(cccz_ , mx)
								#self.LO.append([aaax_,bbby_,cccz_])
								#if self.sepe[0] :
									#self.xj.append(aaax_)
									#self.yj.append(bbby_)
									#self.zj.append(cccz_)
								#if self.sepe2[0] :
									#if not (aaax_,bbby_) in self.area :
										#self.area[(aaax_,bbby_)] = []
									#self.area[(aaax_,bbby_)].append(cccz_)								
									
			for  k , v in mp.items():
				x_coords , y_coords = k[0], k[1]
				z_coords = v # / self.reduce_z # minimum, horizon
				self.FIG.add_trace(self.go.Scatter3d(x=[x_coords], y=[y_coords], z=[z_coords], mode='markers', marker=dict(size=[self.plsize],
					color=[ red_blue[0] ] , symbol= self.pls_circ_square ) ))
				self.xm.append(x_coords)
				self.ym.append(y_coords)
				self.zm.append(z_coords)
				
				if self.plot2[0] :
					fig = self.go.Figure(self.go.Surface(
						
						x = [int(x_coords),int(x_coords+1)],
						y = [int(y_coords),int(y_coords+1)],
						z=[[z_coords]*2 for v in range(2)] 
						, colorscale=[[0, red_blue[0]  ], [1, red_blue[0] ]]    ))
					
					self.tup += fig.data 
					#self.FIG =  self.go.Figure(data= self.tup )
					
					
			#print(xx,len(xx))
			#print(yy,len(yy))
			#print(zz, len(zz))
					
					
					
		def horizon(self, X, Y,  Z ,    rad,  radZ , _18,  pos_neg,      px, go, plt, tuo,  seismic_data ):
			
			#X Y Z------>
			# <-------x2-X y2-Y z2-Z 
			x2 = len(seismic_data[0][0]) -1 # 
			y2 = len(seismic_data[0]) -1 #
			z2 = len(seismic_data) -1 # 
			
			VOL_AREA = max([X,Y,Z,    x2-X , y2-Y , z2-Z ])
			
			xyz = [X,Y,Z]
			
			step = 13 +1 # 11  # 8 # 4 # 1
			
			for V_AREA in range(1,VOL_AREA, step):
				radi = V_AREA
																				#                                                                          #
				if ((0 <= X + radi <= x2) or (0<= Y + radi <= y2)) or  ((0 <= X - radi <= x2) or (0<= Y + radi <= y2)) or ((0 <= X + radi <= x2) or (0<= Y - radi <= y2)) or ((0 <= X - radi <= x2) or (0<= Y - radi <= y2)) : # ATLEAST 1 MUST BE IN BOUNDS
										#                       #
					self.slope1(xyz,radi,radZ,seismic_data,_18,x2,y2,z2) # FLATEST
					#self.slope2(xyz,radi,seismic_data,_18,x2,y2,z2)
					#self.slope3(xyz,radi,seismic_data,_18,x2,y2,z2) # SLOPPIEST
				
					#print(V_AREA,"<<<<<", VOL_AREA )
				
	# import plotly.graph_objects as go
	# import plotly.express as px
				
				
	ln = len(data_display)-1
	
	seismic_data = data_display[:,:,:]# Z layer
	seismic_data = data_display
	
	STR = "Positive"
	#STR = "Negative"
	
	LO = []
	LO2 = []
	vis = []
	vis2 = []
	tup = tuple()
	tup2 = tuple()
	pos_neg = [STR]
	FIG= go.Figure()
	NFIG= go.Figure()
	plsize = 12
	pls_circ_square = "square"
	
	W = SEIS( tup,tup2, LO, LO2, px, go, vis, vis2 ,  pos_neg , FIG, NFIG , plsize, pls_circ_square)
	
	X, Y,  Z = 334, 344, 525 # 2,400,496 # 6,354,621 # 0,0,0 #<<<<<<<
	rad = 0
	radZ = 36 * 2 # 128 # 0
	_18 = 3 # 2.5...
	tuo = tuple()
	plt = go.Figure()
	W.horizon(X, Y,  Z ,    rad,  radZ ,  _18, pos_neg,      px, go, plt, tuo,  seismic_data )
	
	
	
	
	###############################################################################################################################################################
	
	
	X = len(seismic_data[0][0]) # 170,750   INLINE
	Y = len(seismic_data[0]) # 170,750    CROSSLINE
	Z = len(seismic_data)
	
	x2 = len(seismic_data[0][0]) -1 # 170,750
	y2 = len(seismic_data[0]) -1 # 170,750
	z2 = len(seismic_data) -1
	inline = 334
	crossline = 334
	x1 = [inline]* Y # 1 TO MANY
	#y1 = [crossline]*X
	z1 = [i for i in range(Z)]
	rc = seismic_data[:,:,inline].T.tolist()  # random surface colors   .tolist()
	#rc_ = seismic_data[:,crossline,:].T.tolist()
	
	
	
	#XU = [i for i in range(X)] 
	YU = [i for i in range(Y)] 
	
	
	plane = go.Surface(x=x1, y= YU , z=[ z1 for i in range(X) ], surfacecolor=rc , colorscale= 'Picnic' )
	
	#figure = go.Figure()
	W.FIG.add_traces([plane])
	
	
	###############################################################################################################################################################
	
	print("DONE", len(W.xm))
	
	W.FIG.update_layout(                                xaxis=dict(autorange='reversed') , yaxis=dict(autorange='reversed')  ,
			autosize=False,
			width=1150,#800
			height=950,#800
			margin=dict(l=65, r=50, b=65, t=90)
		
		
		)

	#W.FIG.update_layout(xaxis=dict(autorange='reversed'))
	#W.FIG.update_layout(yaxis=dict(autorange='reversed'))
	
	W.FIG.show()
	
	
	"""
	FI =  go.Figure(data= W.tup )
	FI.update_layout(
			autosize=False,
			width=1150,#800
			height=950,#800
			margin=dict(l=65, r=50, b=65, t=90)
		)
	FI.show()
	
	
	
	"""
	