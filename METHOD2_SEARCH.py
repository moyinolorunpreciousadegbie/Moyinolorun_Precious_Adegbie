#!/usr/bin/env python3



class SEIS:
	def __init__(self, tup,tup2, LO, LO2, px, go, vis, vis2 ,  pos_neg , FIG, NFIG, plsize , pls_circ_square, matrix, matrix2):
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
		
		self.mp = {}
		
		self.mx = float('-inf')
		self.mn = float('inf')
		
		self.matrix = matrix
		self.matrix2 = matrix2
		
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
	
	
	def rip_N(self, ax,by,cz, seismic_data , mn, mp , _18, x2,y2,z2):
		if 0<=ax<=x2 and  0<=by<=y2 and 0<=cz<=z2  :
			if self.check_neg(seismic_data, _18, ax,by,cz)  and [ax,by,cz] not in self.LO:
				#print("ATLEAST")
				x_coords, y_coords , z_coords = ax,by,cz                # Z1 <<<<
				mp[(ax,by)] = min(cz , self.mn) #  UPPER HORIZON IN RANGE    # |  radius(upper minimum, MIN.)
				#mp[(ax,by)] = max(cz , self.mx)								# |
				self.LO.append([ax,by,cz]) #                            # Z2
				if self.sepe[0] :
					self.xj.append(ax)
					self.yj.append(by)
					self.zj.append(cz)
				if self.sepe2[0] :
					if not (ax,by) in self.area :
						self.area[(ax,by)] = []
					self.area[(ax,by)].append(cz)
					
					#self.rip_N(self, ax,by,cz, seismic_data , mn, mp , _18, x2,y2,z2)
					
					
	def rip_P(self, ax,by,cz, seismic_data , mn, mp , _18, x2,y2,z2):
		if 0<=ax<=x2 and  0<=by<=y2 and 0<=cz<=z2  :
			if self.check_pos(seismic_data, _18, ax,by,cz)  and [ax,by,cz] not in self.LO:
				#print("ATLEAST")
				x_coords, y_coords , z_coords = ax,by,cz                # Z1 <<<<
				mp[(ax,by)] = min(cz , self.mn) #  UPPER HORIZON IN RANGE    # |  radius(upper minimum, MIN.)
				#mp[(ax,by)] = max(cz , self.mx)								# |
				self.LO.append([ax,by,cz]) #                            # Z2
				if self.sepe[0] :
					self.xj.append(ax)
					self.yj.append(by)
					self.zj.append(cz)
				if self.sepe2[0] :
					if not (ax,by) in self.area :
						self.area[(ax,by)] = []
					self.area[(ax,by)].append(cz)
					
					#self.rip_P(self, ax,by,cz, seismic_data , mn, mp , _18, x2,y2,z2)
	########################################################################################################################################################################################################################################################################################################################
					
	def slope1(self,xyz,rad,radZ,seismic_data, _18,x2,y2,z2,       mirror_rad, mir_mat):
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
		incd = (rad * stp)
		for i in range(lenght):
			for j in range(0,radZ, stp):#<<<<<<<< radZ                                   STEP THE radz
			
			
			
				######################################################
			
				mirt = mir_mat
				# - -
				# - +
				# + -
				# + +
			
				mab = [[ x1y1z1[0] , x1y1z1[1] + i , x1y1z1[2] + j] ,#z
				[x1y1z1[0] + i, x1y1z1[1]  , x1y1z1[2] + j] ,#z
				#[x1y1z1[0] + i, x1y1z1[1] + j , x1y1z1[2] ] , 
					
				[x2y2z2[0] , x2y2z2[1] - i , x2y2z2[2] - j] ,#z
				[x2y2z2[0] - i, x2y2z2[1]  , x2y2z2[2] - j] ,#z
				#[x2y2z2[0] - i, x2y2z2[1] - j , x2y2z2[2] ] ,
					
				[mirt[0][0] + i   , mirt[0][1] , x1y1z1[2] + j] ,#z
				[mirt[0][0]    , mirt[0][1] + i, x1y1z1[2] + j] ,#z
					
				[mirt[0][0] + i   , mirt[0][1] , x2y2z2[2] - j] ,#z
				[mirt[0][0]    , mirt[0][1] + i, x2y2z2[2] - j] ,#z
					
				#[mirt[0][0] + i   , mirt[0][1] + j , x1y1z1[2] ] , 
				#[mirt[0][0] + i   , mirt[0][1] + j , x2y2z2[2] ] ,
					
					
					
					
				[mirt[1][0] + i   , mirt[1][1] , x1y1z1[2] + j] ,#z
				[mirt[1][0]    , mirt[1][1] - i, x1y1z1[2] + j] ,#z
					
				[mirt[1][0] + i   , mirt[1][1] , x2y2z2[2] - j] ,#z
				[mirt[1][0]    , mirt[1][1] - i, x2y2z2[2] - j] ,#z
					
				#[mirt[1][0] + i   , mirt[1][1] - j , x1y1z1[2] ] ,
				#[mirt[1][0] + i   , mirt[1][1] - j , x2y2z2[2] ] ,
					
					
					
				[mirt[2][0] - i   , mirt[2][1] , x1y1z1[2] + j] ,#z
				[mirt[2][0]    , mirt[2][1] + i, x1y1z1[2] + j] ,#z
					
				[mirt[2][0] - i   , mirt[2][1] , x2y2z2[2] - j] ,#z
				[mirt[2][0]    , mirt[2][1] + i, x2y2z2[2] - j] ,#z
					
				#[mirt[2][0] - i   , mirt[2][1] + j , x1y1z1[2] ] ,
				#[mirt[2][0] - i   , mirt[2][1] + j , x2y2z2[2] ] ,
					
					
					
				[mirt[3][0] - i   , mirt[3][1] , x1y1z1[2] + j] ,#z
				[mirt[3][0]    , mirt[3][1] - i, x1y1z1[2] + j] ,#z
					
				[mirt[3][0] - i   , mirt[3][1] , x2y2z2[2] - j] ,#z
				[mirt[3][0]    , mirt[3][1] - i, x2y2z2[2] - j] ,#z
					
				#[mirt[3][0] - i   , mirt[3][1] - j , x1y1z1[2] ] ,
				#[mirt[3][0] - i   , mirt[3][1] - j , x2y2z2[2] ] 
				]
			
				######################################################
			
			
				# 20
				x, y, z = mab[0]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[1]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[2]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[3]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[4]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[5]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[6]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[7]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[8]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[9]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[10]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[11]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[12]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[13]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[14]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[15]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[16]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[17]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[18]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[19]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
					
					
				mab = [
				#######################
				[mirt[0][0] +(stp*incd) - i   , mirt[0][1]+(stp*incd) , x1y1z1[2] + j] ,#z
				[mirt[0][0]+(stp*incd)    , mirt[0][1]+(stp*incd)  - i, x1y1z1[2] + j] ,#z
					
				[mirt[0][0]+(stp*incd) - i   , mirt[0][1]+(stp*incd) , x2y2z2[2] - j] ,#z
				[mirt[0][0]+(stp*incd)    , mirt[0][1]+(stp*incd) - i, x2y2z2[2] - j] ,#z
					
				#[mirt[0][0]-(stp*incd) - i   , mirt[0][1]-(stp*incd) - j , x1y1z1[2] ] , 
				#[mirt[0][0]-(stp*incd) - i   , mirt[0][1]-(stp*incd) - j , x2y2z2[2] ] ,
					
					
					
					
				[mirt[1][0]+(stp*incd) - i   , mirt[1][1]-(stp*incd) , x1y1z1[2] + j] ,#z
				[mirt[1][0]+(stp*incd)    , mirt[1][1]-(stp*incd) + i, x1y1z1[2] + j] ,#z
					
				[mirt[1][0]+(stp*incd) - i   , mirt[1][1]-(stp*incd) , x2y2z2[2] - j] ,#z
				[mirt[1][0]+(stp*incd)    , mirt[1][1]-(stp*incd) + i, x2y2z2[2] - j] ,#z
					
				#[mirt[1][0]-(stp*incd) - i   , mirt[1][1]-(stp*incd) + j , x1y1z1[2] ] ,
				#[mirt[1][0]-(stp*incd) - i   , mirt[1][1]-(stp*incd) + j , x2y2z2[2] ] ,
					
					
					
				[mirt[2][0]-(stp*incd) + i   , mirt[2][1]+(stp*incd) , x1y1z1[2] + j] ,#z
				[mirt[2][0]-(stp*incd)    , mirt[2][1]+(stp*incd) - i, x1y1z1[2] + j] ,#z
					
				[mirt[2][0]-(stp*incd) + i   , mirt[2][1]+(stp*incd) , x2y2z2[2] - j] ,#z
				[mirt[2][0]-(stp*incd)    , mirt[2][1]+(stp*incd) - i, x2y2z2[2] - j] ,#z
					
				#[mirt[2][0]-(stp*incd) + i   , mirt[2][1]-(stp*incd) - j , x1y1z1[2] ] ,
				#[mirt[2][0]-(stp*incd) + i   , mirt[2][1]-(stp*incd) - j , x2y2z2[2] ] ,
					
					
					
				[mirt[3][0]-(stp*incd) + i   , mirt[3][1]-(stp*incd) , x1y1z1[2] + j] ,#z
				[mirt[3][0]-(stp*incd)    , mirt[3][1]-(stp*incd) + i, x1y1z1[2] + j] ,#z
					
				[mirt[3][0]-(stp*incd) + i   , mirt[3][1]-(stp*incd) , x2y2z2[2] - j] ,#z
				[mirt[3][0]-(stp*incd)    , mirt[3][1]-(stp*incd) + i, x2y2z2[2] - j] ,#z
					
				#[mirt[3][0]-(stp*incd) + i   , mirt[3][1]-(stp*incd) + j , x1y1z1[2] ] ,
				#[mirt[3][0]-(stp*incd) + i   , mirt[3][1]-(stp*incd) + j , x2y2z2[2] ] 
				]
			
				x, y, z = mab[0]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[1]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[2]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[3]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[4]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[5]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[6]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[7]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[8]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[9]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[10]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[11]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[12]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[13]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[14]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[15]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
					
					
					
				########################################################################################################			
					
					
					
					
		for  k , v in mp.items():
			x_coords , y_coords = k[0], k[1]
			z_coords = v # minimum, horizon
			self.FIG.add_trace(self.go.Scatter3d(x=[x_coords], y=[y_coords], z=[z_coords], mode='markers', marker=dict(size=[self.plsize],
				color=[ red_blue[0] ] , symbol= self.pls_circ_square ) ))
			self.xm.append(x_coords)
			self.ym.append(y_coords)
			self.zm.append(z_coords)
			#self.matrix[y_coords][x_coords] = z_coords
			#self.matrix2[y_coords][x_coords] = seismic_data[z_coords,y_coords,x_coords]
			if self.plot2[0] :
				fig = self.go.Figure(self.go.Surface(
					
					x = [int(x_coords),int(x_coords+1)],
					y = [int(y_coords),int(y_coords+1)],
					z=[[z_coords]*2 for v in range(2)] 
					, colorscale=[[0, red_blue[0]  ], [1, red_blue[0] ]]    ))
				
				self.tup += fig.data 
				#self.FIG =  self.go.Figure(data= self.tup )
				
				
				
	#########################################################################################################################################################################################################################################################################################################################
				
	def slope2(self,xyz,rad,seismic_data,_18,x2,y2,z2,       mirror_rad, mir_mat):
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
				######################################################
			
				mirt = mir_mat
				# - -
				# - +
				# + -
				# + +
			
				mab = [[ x1y1z1[0] , x1y1z1[1] + i , x1y1z1[2] + j] ,#z
				[x1y1z1[0] + i, x1y1z1[1]  , x1y1z1[2] + j] ,#z
				#[x1y1z1[0] + i, x1y1z1[1] + j , x1y1z1[2] ] , 
					
				[x2y2z2[0] , x2y2z2[1] - i , x2y2z2[2] - j] ,#z
				[x2y2z2[0] - i, x2y2z2[1]  , x2y2z2[2] - j] ,#z
				#[x2y2z2[0] - i, x2y2z2[1] - j , x2y2z2[2] ] ,
					
				[mirt[0][0] + i   , mirt[0][1] , x1y1z1[2] + j] ,#z
				[mirt[0][0]    , mirt[0][1] + i, x1y1z1[2] + j] ,#z
					
				[mirt[0][0] + i   , mirt[0][1] , x2y2z2[2] - j] ,#z
				[mirt[0][0]    , mirt[0][1] + i, x2y2z2[2] - j] ,#z
					
				#[mirt[0][0] + i   , mirt[0][1] + j , x1y1z1[2] ] , 
				#[mirt[0][0] + i   , mirt[0][1] + j , x2y2z2[2] ] ,
					
					
					
					
				[mirt[1][0] + i   , mirt[1][1] , x1y1z1[2] + j] ,#z
				[mirt[1][0]    , mirt[1][1] - i, x1y1z1[2] + j] ,#z
					
				[mirt[1][0] + i   , mirt[1][1] , x2y2z2[2] - j] ,#z
				[mirt[1][0]    , mirt[1][1] - i, x2y2z2[2] - j] ,#z
					
				#[mirt[1][0] + i   , mirt[1][1] - j , x1y1z1[2] ] ,
				#[mirt[1][0] + i   , mirt[1][1] - j , x2y2z2[2] ] ,
					
					
					
				[mirt[2][0] - i   , mirt[2][1] , x1y1z1[2] + j] ,#z
				[mirt[2][0]    , mirt[2][1] + i, x1y1z1[2] + j] ,#z
					
				[mirt[2][0] - i   , mirt[2][1] , x2y2z2[2] - j] ,#z
				[mirt[2][0]    , mirt[2][1] + i, x2y2z2[2] - j] ,#z
					
				#[mirt[2][0] - i   , mirt[2][1] + j , x1y1z1[2] ] ,
				#[mirt[2][0] - i   , mirt[2][1] + j , x2y2z2[2] ] ,
					
					
					
				[mirt[3][0] - i   , mirt[3][1] , x1y1z1[2] + j] ,#z
				[mirt[3][0]    , mirt[3][1] - i, x1y1z1[2] + j] ,#z
					
				[mirt[3][0] - i   , mirt[3][1] , x2y2z2[2] - j] ,#z
				[mirt[3][0]    , mirt[3][1] - i, x2y2z2[2] - j] ,#z
					
				#[mirt[3][0] - i   , mirt[3][1] - j , x1y1z1[2] ] ,
				#[mirt[3][0] - i   , mirt[3][1] - j , x2y2z2[2] ] 
				]
			
				######################################################
			
			
				# 20
				x, y, z = mab[0]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[1]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[2]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[3]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[4]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[5]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[6]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[7]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[8]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[9]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[10]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[11]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[12]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[13]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[14]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[15]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[16]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[17]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[18]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[19]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
					
					
				mab = [
				#######################
				[mirt[0][0] +(stp*incd) - i   , mirt[0][1]+(stp*incd) , x1y1z1[2] + j] ,#z
				[mirt[0][0]+(stp*incd)    , mirt[0][1]+(stp*incd)  - i, x1y1z1[2] + j] ,#z
					
				[mirt[0][0]+(stp*incd) - i   , mirt[0][1]+(stp*incd) , x2y2z2[2] - j] ,#z
				[mirt[0][0]+(stp*incd)    , mirt[0][1]+(stp*incd) - i, x2y2z2[2] - j] ,#z
					
				#[mirt[0][0]-(stp*incd) - i   , mirt[0][1]-(stp*incd) - j , x1y1z1[2] ] , 
				#[mirt[0][0]-(stp*incd) - i   , mirt[0][1]-(stp*incd) - j , x2y2z2[2] ] ,
					
					
					
					
				[mirt[1][0]+(stp*incd) - i   , mirt[1][1]-(stp*incd) , x1y1z1[2] + j] ,#z
				[mirt[1][0]+(stp*incd)    , mirt[1][1]-(stp*incd) + i, x1y1z1[2] + j] ,#z
					
				[mirt[1][0]+(stp*incd) - i   , mirt[1][1]-(stp*incd) , x2y2z2[2] - j] ,#z
				[mirt[1][0]+(stp*incd)    , mirt[1][1]-(stp*incd) + i, x2y2z2[2] - j] ,#z
					
				#[mirt[1][0]-(stp*incd) - i   , mirt[1][1]-(stp*incd) + j , x1y1z1[2] ] ,
				#[mirt[1][0]-(stp*incd) - i   , mirt[1][1]-(stp*incd) + j , x2y2z2[2] ] ,
					
					
					
				[mirt[2][0]-(stp*incd) + i   , mirt[2][1]+(stp*incd) , x1y1z1[2] + j] ,#z
				[mirt[2][0]-(stp*incd)    , mirt[2][1]+(stp*incd) - i, x1y1z1[2] + j] ,#z
					
				[mirt[2][0]-(stp*incd) + i   , mirt[2][1]+(stp*incd) , x2y2z2[2] - j] ,#z
				[mirt[2][0]-(stp*incd)    , mirt[2][1]+(stp*incd) - i, x2y2z2[2] - j] ,#z
					
				#[mirt[2][0]-(stp*incd) + i   , mirt[2][1]-(stp*incd) - j , x1y1z1[2] ] ,
				#[mirt[2][0]-(stp*incd) + i   , mirt[2][1]-(stp*incd) - j , x2y2z2[2] ] ,
					
					
					
				[mirt[3][0]-(stp*incd) + i   , mirt[3][1]-(stp*incd) , x1y1z1[2] + j] ,#z
				[mirt[3][0]-(stp*incd)    , mirt[3][1]-(stp*incd) + i, x1y1z1[2] + j] ,#z
					
				[mirt[3][0]-(stp*incd) + i   , mirt[3][1]-(stp*incd) , x2y2z2[2] - j] ,#z
				[mirt[3][0]-(stp*incd)    , mirt[3][1]-(stp*incd) + i, x2y2z2[2] - j] ,#z
					
				#[mirt[3][0]-(stp*incd) + i   , mirt[3][1]-(stp*incd) + j , x1y1z1[2] ] ,
				#[mirt[3][0]-(stp*incd) + i   , mirt[3][1]-(stp*incd) + j , x2y2z2[2] ] 
				]
			
				x, y, z = mab[0]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[1]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[2]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[3]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[4]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[5]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[6]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[7]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[8]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[9]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[10]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[11]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[12]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[13]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[14]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[15]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
					
					
					
				########################################################################################################			
					
					
					
					
					
					
		for  k , v in mp.items():
			x_coords , y_coords = k[0], k[1]
			z_coords = v # minimum, horizon
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
				
	def slope3(self,xyz,rad,seismic_data, _18,x2,y2,z2,       mirror_rad, mir_mat):
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
				######################################################
			
				mirt = mir_mat
				# - -
				# - +
				# + -
				# + +
			
				mab = [[ x1y1z1[0] , x1y1z1[1] + i , x1y1z1[2] + j] ,#z
				[x1y1z1[0] + i, x1y1z1[1]  , x1y1z1[2] + j] ,#z
				#[x1y1z1[0] + i, x1y1z1[1] + j , x1y1z1[2] ] , 
					
				[x2y2z2[0] , x2y2z2[1] - i , x2y2z2[2] - j] ,#z
				[x2y2z2[0] - i, x2y2z2[1]  , x2y2z2[2] - j] ,#z
				#[x2y2z2[0] - i, x2y2z2[1] - j , x2y2z2[2] ] ,
					
				[mirt[0][0] + i   , mirt[0][1] , x1y1z1[2] + j] ,#z
				[mirt[0][0]    , mirt[0][1] + i, x1y1z1[2] + j] ,#z
					
				[mirt[0][0] + i   , mirt[0][1] , x2y2z2[2] - j] ,#z
				[mirt[0][0]    , mirt[0][1] + i, x2y2z2[2] - j] ,#z
					
				#[mirt[0][0] + i   , mirt[0][1] + j , x1y1z1[2] ] , 
				#[mirt[0][0] + i   , mirt[0][1] + j , x2y2z2[2] ] ,
					
					
					
					
				[mirt[1][0] + i   , mirt[1][1] , x1y1z1[2] + j] ,#z
				[mirt[1][0]    , mirt[1][1] - i, x1y1z1[2] + j] ,#z
					
				[mirt[1][0] + i   , mirt[1][1] , x2y2z2[2] - j] ,#z
				[mirt[1][0]    , mirt[1][1] - i, x2y2z2[2] - j] ,#z
					
				#[mirt[1][0] + i   , mirt[1][1] - j , x1y1z1[2] ] ,
				#[mirt[1][0] + i   , mirt[1][1] - j , x2y2z2[2] ] ,
					
					
					
				[mirt[2][0] - i   , mirt[2][1] , x1y1z1[2] + j] ,#z
				[mirt[2][0]    , mirt[2][1] + i, x1y1z1[2] + j] ,#z
					
				[mirt[2][0] - i   , mirt[2][1] , x2y2z2[2] - j] ,#z
				[mirt[2][0]    , mirt[2][1] + i, x2y2z2[2] - j] ,#z
					
				#[mirt[2][0] - i   , mirt[2][1] + j , x1y1z1[2] ] ,
				#[mirt[2][0] - i   , mirt[2][1] + j , x2y2z2[2] ] ,
					
					
					
				[mirt[3][0] - i   , mirt[3][1] , x1y1z1[2] + j] ,#z
				[mirt[3][0]    , mirt[3][1] - i, x1y1z1[2] + j] ,#z
					
				[mirt[3][0] - i   , mirt[3][1] , x2y2z2[2] - j] ,#z
				[mirt[3][0]    , mirt[3][1] - i, x2y2z2[2] - j] ,#z
					
				#[mirt[3][0] - i   , mirt[3][1] - j , x1y1z1[2] ] ,
				#[mirt[3][0] - i   , mirt[3][1] - j , x2y2z2[2] ] 
				]
			
				######################################################
			
			
				# 20
				x, y, z = mab[0]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[1]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[2]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[3]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[4]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[5]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[6]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[7]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[8]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[9]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[10]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[11]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[12]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[13]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[14]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[15]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[16]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[17]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[18]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[19]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
					
					
				mab = [
				#######################
				[mirt[0][0] +(stp*incd) - i   , mirt[0][1]+(stp*incd) , x1y1z1[2] + j] ,#z
				[mirt[0][0]+(stp*incd)    , mirt[0][1]+(stp*incd)  - i, x1y1z1[2] + j] ,#z
					
				[mirt[0][0]+(stp*incd) - i   , mirt[0][1]+(stp*incd) , x2y2z2[2] - j] ,#z
				[mirt[0][0]+(stp*incd)    , mirt[0][1]+(stp*incd) - i, x2y2z2[2] - j] ,#z
					
				#[mirt[0][0]-(stp*incd) - i   , mirt[0][1]-(stp*incd) - j , x1y1z1[2] ] , 
				#[mirt[0][0]-(stp*incd) - i   , mirt[0][1]-(stp*incd) - j , x2y2z2[2] ] ,
					
					
					
					
				[mirt[1][0]+(stp*incd) - i   , mirt[1][1]-(stp*incd) , x1y1z1[2] + j] ,#z
				[mirt[1][0]+(stp*incd)    , mirt[1][1]-(stp*incd) + i, x1y1z1[2] + j] ,#z
					
				[mirt[1][0]+(stp*incd) - i   , mirt[1][1]-(stp*incd) , x2y2z2[2] - j] ,#z
				[mirt[1][0]+(stp*incd)    , mirt[1][1]-(stp*incd) + i, x2y2z2[2] - j] ,#z
					
				#[mirt[1][0]-(stp*incd) - i   , mirt[1][1]-(stp*incd) + j , x1y1z1[2] ] ,
				#[mirt[1][0]-(stp*incd) - i   , mirt[1][1]-(stp*incd) + j , x2y2z2[2] ] ,
					
					
					
				[mirt[2][0]-(stp*incd) + i   , mirt[2][1]+(stp*incd) , x1y1z1[2] + j] ,#z
				[mirt[2][0]-(stp*incd)    , mirt[2][1]+(stp*incd) - i, x1y1z1[2] + j] ,#z
					
				[mirt[2][0]-(stp*incd) + i   , mirt[2][1]+(stp*incd) , x2y2z2[2] - j] ,#z
				[mirt[2][0]-(stp*incd)    , mirt[2][1]+(stp*incd) - i, x2y2z2[2] - j] ,#z
					
				#[mirt[2][0]-(stp*incd) + i   , mirt[2][1]-(stp*incd) - j , x1y1z1[2] ] ,
				#[mirt[2][0]-(stp*incd) + i   , mirt[2][1]-(stp*incd) - j , x2y2z2[2] ] ,
					
					
					
				[mirt[3][0]-(stp*incd) + i   , mirt[3][1]-(stp*incd) , x1y1z1[2] + j] ,#z
				[mirt[3][0]-(stp*incd)    , mirt[3][1]-(stp*incd) + i, x1y1z1[2] + j] ,#z
					
				[mirt[3][0]-(stp*incd) + i   , mirt[3][1]-(stp*incd) , x2y2z2[2] - j] ,#z
				[mirt[3][0]-(stp*incd)    , mirt[3][1]-(stp*incd) + i, x2y2z2[2] - j] ,#z
					
				#[mirt[3][0]-(stp*incd) + i   , mirt[3][1]-(stp*incd) + j , x1y1z1[2] ] ,
				#[mirt[3][0]-(stp*incd) + i   , mirt[3][1]-(stp*incd) + j , x2y2z2[2] ] 
				]
			
				x, y, z = mab[0]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[1]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[2]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[3]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[4]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[5]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[6]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[7]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[8]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[9]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[10]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[11]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[12]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[13]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[14]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				x, y, z = mab[15]
				if self.pos_neg[0] == "Negative" : 
					red_blue[0] = "red" # SWITCH TO blue
					self.rip_N( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
				if self.pos_neg[0] == "Positive" :
					red_blue[0] = "blue" # SWITCH TO red
					self.rip_P( x,y,z, seismic_data , mn, mp , _18, x2,y2,z2)
					
					
					
				########################################################################################################			
					
					
					
					
					
					
		for  k , v in mp.items():
			x_coords , y_coords = k[0], k[1]
			z_coords = v # minimum, horizon
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
		
		step = 24 # 21 # 17 # 11 # 8 # 4 # 1
		
		mirror_rad = VOL_AREA
		
		mir_mat = [	[xyz[0]-mirror_rad, xyz[1]-mirror_rad]  ,
					[xyz[0]-mirror_rad, xyz[1]+mirror_rad]  ,
					[xyz[0]+mirror_rad, xyz[1]-mirror_rad]  ,
					[xyz[0]+mirror_rad, xyz[1]+mirror_rad] ]
		
		for V_AREA in range(1,VOL_AREA, step):
			radi = V_AREA
			
			
			
			
			
			# - -
			# - +
			# + -
			# + +
																			#                                                                          #
			if ((0 <= X + radi <= x2) or (0<= Y + radi <= y2)) or  ((0 <= X - radi <= x2) or (0<= Y + radi <= y2)) or ((0 <= X + radi <= x2) or (0<= Y - radi <= y2)) or ((0 <= X - radi <= x2) or (0<= Y - radi <= y2)) : # ATLEAST 1 MUST BE IN BOUNDS
						            #                       #
				self.slope1(xyz,radi,radZ,seismic_data,_18,x2,y2,z2,       mirror_rad, mir_mat) # FLATEST
				#self.slope2(xyz,radi,seismic_data,_18,x2,y2,z2,       mirror_rad, mir_mat)
				#self.slope3(xyz,radi,seismic_data,_18,x2,y2,z2,       mirror_rad, mir_mat) # SLOPPIEST
			
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
matrix =   np.full(   ( len(seismic_data[0]) , len(seismic_data[0][0])  )   , 525 ) # np.zeros(( len(seismic_data[0]) , len(seismic_data[0][0])  ))
matrix2 =  np.full(   ( len(seismic_data[0]) , len(seismic_data[0][0])  )   , 0 )
W = SEIS( tup,tup2, LO, LO2, px, go, vis, vis2 ,  pos_neg , FIG, NFIG , plsize, pls_circ_square, matrix, matrix2)

X_, Y_,  Z_ = 334, 344, 525 # 2,400,496 # 6,354,621 # 0,0,0 #<<<<<<<
rad = 0
radZ = 36 * 2 # 128 # 0
_18 = 3 # 2.5...
tuo = tuple()
plt = go.Figure()
W.horizon(X_, Y_,  Z_ ,    rad,  radZ ,  _18, pos_neg,      px, go, plt, tuo,  seismic_data )


###############################################################################################################################################################


X = len(seismic_data[0][0]) # 170,750   INLINE
Y = len(seismic_data[0]) # 170,750    CROSSLINE
Z = len(seismic_data)

x2 = len(seismic_data[0][0]) -1 # 170,750
y2 = len(seismic_data[0]) -1 # 170,750
z2 = len(seismic_data) -1
inline  = X_#300 # 250

crossline = Y_#250# 600

twt_z = Z_#500
_001 = 0.00001

_000001 = 1 # 0.001
																	#                            Y
#####m1 = [ [ (i * _000001) for i in range(Z)] for y in range( Y) ]
y1_ = [0,Y]
x1_ = [ inline , inline + _001 ]
col1 = seismic_data[:,:,inline].T#.tolist()

#print([col1.shape],[len(m1),len( m1[0] )])


#                                          X
#####m2 = [ [ (i * _000001) for x in range(X)]  for i in range(Z) ]
y2_ = [crossline , crossline + _001 ]
x2_ = [0,X]
col2 = seismic_data[:,crossline,:]#.tolist()
#print([col2.shape],[len(m2),len( m2[0] )])


#print(col1.min(), col2.min() )
#print(col1.min()*-1, col2.min()*-1 )
#col1 = col1 + (col1.min()*-1)
#col2 = col2 + (col2.min()*-1)

#print(m1.shape , col1.shape)
#print(m2.shape , col2.shape)

#y1_ = [i for i in range( Z)]#[0,Y]                                                        #
#x1_ = [(i*_001) + inline for i in range( Z)]#[ inline , inline + _001 ]   Z>Y             #
																																														#
																																														#
#y2_ = [(i*_001) + crossline for i in range( Z)] # [crossline , crossline + _001 ]   Z>X   #
#x2_ = [i for i in range( Z)]# [0,X]

y1_ = []
x1_ = []

y2_ = []
x2_ = []

pllll = []

for i in range(Z):
		y1_.append(i)#[0,Y]
		x1_.append( (i*_001) + inline )
#x1_ = [(i*_001) + inline for i in range( Z)]#[ inline , inline + _001 ]   Z>Y
		y2_.append( (i*_001) + crossline  )
		x2_.append(i)#[0,Y]
	
		pllll.append((i * _000001))
	
x1_ = np.array(x1_ )
y1_ = np.array(y1_ )
#m1 = np.array(m1 )

x2_ = np.array(x2_ )
y2_ = np.array(y2_ )
#m2 = np.array(m2 )

#plane = go.Surface(x= x1_ , y=y1_, z= m1, surfacecolor=col1  , colorscale= 'Picnic', opacity=1) #<<<<
#plane2 = go.Surface(x= x2_ , y=y2_, z= m2, surfacecolor=col2  , colorscale= 'Picnic', opacity=1) #<<<<

#twt_z
col3 = seismic_data[twt_z,:,:]
vj =  ( (_000001 * Z) / Z ) * twt_z
#####m3 = [ [vj ] * X for _ in range(Y) ]


																	#                            Y
#####m1 = [ [ (i * _000001) for i in range(Z)] for y in range( Y) ]
#                                          X
#####m2 = [ [ (i * _000001) for x in range(X)]  for i in range(Z) ]

mc = max([X,Y,Z])
m1 = []
m2 = []
m3 = []

Y_r = []
X_r = []
for i in range(mc):
	if i < Y : # m1 and m3
			_ =  pllll
			m1.append(_)
	
			__ = [vj ] * X
			m3.append( __ )
	if i < Z :
			_ii = [ (i * _000001)] * X
			m2.append(_ii)
		
	if i < X :
		X_r.append(i)
	if i < Y :
		Y_r.append(i)
		
			
m1 = np.array(m1 )
m2 = np.array(m2 )

m3 = np.array(m3 )


plane = go.Surface(x= x1_ , y=y1_, z= m1, surfacecolor=col1  , colorscale= 'Picnic', opacity=1) #<<<<
plane2 = go.Surface(x= x2_ , y=y2_, z= m2, surfacecolor=col2  , colorscale= 'Picnic', opacity=1) #<<<<

plane3 = go.Surface(x= x2_ , y=y1_, z= m3, surfacecolor=col3  , colorscale= 'Picnic', opacity=1) #<<<<

print([len(col1),len( col1[0] )],[len(m1),len( m1[0] )])
print([len(col2),len( col2[0] )],[len(m2),len( m2[0] )])




#plane4 = go.Surface(x= x2_ , y=y1_, z= W.matrix , surfacecolor=  W.matrix2  , colorscale= 'Earth', opacity=0.3) #<<<<
#plane4 = go.Surface(x= X_r , y=Y_r, z= W.matrix , surfacecolor=  W.matrix2  , colorscale= 'Picnic', opacity=1) #<<<<


W.FIG.add_traces([plane])
W.FIG.add_traces([plane2])

W.FIG.add_traces([plane3])

#W.FIG.add_traces([plane4])

W.FIG.update_layout(
		autosize=False,
		width=1150,#800
		height=950,#800
		margin=dict(l=65, r=50, b=65, t=90) ,  scene=dict(zaxis=dict(autorange='reversed'))
	)

###############################################################################################################################################################


print("DONE", len(W.xm))


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




mir_mat__ = [[xyz[0]-mirror_rad, xyz[1]-mirror_rad, xyz[2]-mirror_rad]  ,
			[xyz[0]-mirror_rad, xyz[1]-mirror_rad, xyz[2]+mirror_rad]  ,
			[xyz[0]-mirror_rad, xyz[1]+mirror_rad, xyz[2]-mirror_rad]  ,
			[xyz[0]-mirror_rad, xyz[1]+mirror_rad, xyz[2]+mirror_rad]  ,
			[xyz[0]+mirror_rad, xyz[1]-mirror_rad, xyz[2]-mirror_rad]  ,
			[xyz[0]+mirror_rad, xyz[1]-mirror_rad, xyz[2]+mirror_rad]  ,
			[xyz[0]+mirror_rad, xyz[1]+mirror_rad, xyz[2]-mirror_rad]  ,
			[xyz[0]+mirror_rad, xyz[1]+mirror_rad, xyz[2]+mirror_rad] ]
		
mir_mat_ = [[xyz[0]-mirror_rad, xyz[1]-mirror_rad, xyz[2]-(mirror_rad//2)]  ,
			[xyz[0]-mirror_rad, xyz[1]-mirror_rad, xyz[2]+(mirror_rad//2)]  ,
			[xyz[0]-mirror_rad, xyz[1]+mirror_rad, xyz[2]-(mirror_rad//2)]  ,
			[xyz[0]-mirror_rad, xyz[1]+mirror_rad, xyz[2]+(mirror_rad//2)]  ,
			[xyz[0]+mirror_rad, xyz[1]-mirror_rad, xyz[2]-(mirror_rad//2)]  ,
			[xyz[0]+mirror_rad, xyz[1]-mirror_rad, xyz[2]+(mirror_rad//2)]  ,
			[xyz[0]+mirror_rad, xyz[1]+mirror_rad, xyz[2]-(mirror_rad//2)]  ,
			[xyz[0]+mirror_rad, xyz[1]+mirror_rad, xyz[2]+(mirror_rad//2)] ]

mir_mat = [[xyz[0]-mirror_rad, xyz[1]-mirror_rad, xyz[2]-(radZ//2)]  ,
			[xyz[0]-mirror_rad, xyz[1]-mirror_rad, xyz[2]+(radZ//2)]  ,
			[xyz[0]-mirror_rad, xyz[1]+mirror_rad, xyz[2]-(radZ//2)]  ,
			[xyz[0]-mirror_rad, xyz[1]+mirror_rad, xyz[2]+(radZ//2)]  ,
			[xyz[0]+mirror_rad, xyz[1]-mirror_rad, xyz[2]-(radZ//2)]  ,
			[xyz[0]+mirror_rad, xyz[1]-mirror_rad, xyz[2]+(radZ//2)]  ,
			[xyz[0]+mirror_rad, xyz[1]+mirror_rad, xyz[2]-(radZ//2)]  ,
			[xyz[0]+mirror_rad, xyz[1]+mirror_rad, xyz[2]+(radZ//2)] ]
		

######################################################################
mir_mat__ = [[xyz[0]-mirror_rad, xyz[1]-mirror_rad, xyz[2]-radi]  ,
[xyz[0]-mirror_rad, xyz[1]-mirror_rad, xyz[2]+radi]  ,
[xyz[0]-mirror_rad, xyz[1]+mirror_rad, xyz[2]-radi]  ,
[xyz[0]-mirror_rad, xyz[1]+mirror_rad, xyz[2]+radi]  ,
[xyz[0]+mirror_rad, xyz[1]-mirror_rad, xyz[2]-radi]  ,
[xyz[0]+mirror_rad, xyz[1]-mirror_rad, xyz[2]+radi]  ,
[xyz[0]+mirror_rad, xyz[1]+mirror_rad, xyz[2]-radi]  ,
[xyz[0]+mirror_rad, xyz[1]+mirror_rad, xyz[2]+radi] ]

mir_mat_ = [[xyz[0]-mirror_rad, xyz[1]-mirror_rad, xyz[2]-(radi//2)]  ,
[xyz[0]-mirror_rad, xyz[1]-mirror_rad, xyz[2]+(radi//2)]  ,
[xyz[0]-mirror_rad, xyz[1]+mirror_rad, xyz[2]-(radi//2)]  ,
[xyz[0]-mirror_rad, xyz[1]+mirror_rad, xyz[2]+(radi//2)]  ,
[xyz[0]+mirror_rad, xyz[1]-mirror_rad, xyz[2]-(radi//2)]  ,
[xyz[0]+mirror_rad, xyz[1]-mirror_rad, xyz[2]+(radi//2)]  ,
[xyz[0]+mirror_rad, xyz[1]+mirror_rad, xyz[2]-(radi//2)]  ,
[xyz[0]+mirror_rad, xyz[1]+mirror_rad, xyz[2]+(radi//2)] ]

mir_mat = [[xyz[0]-mirror_rad, xyz[1]-mirror_rad, xyz[2]-(radZ//2)]  ,
[xyz[0]-mirror_rad, xyz[1]-mirror_rad, xyz[2]+(radZ//2)]  ,
[xyz[0]-mirror_rad, xyz[1]+mirror_rad, xyz[2]-(radZ//2)]  ,
[xyz[0]-mirror_rad, xyz[1]+mirror_rad, xyz[2]+(radZ//2)]  ,
[xyz[0]+mirror_rad, xyz[1]-mirror_rad, xyz[2]-(radZ//2)]  ,
[xyz[0]+mirror_rad, xyz[1]-mirror_rad, xyz[2]+(radZ//2)]  ,
[xyz[0]+mirror_rad, xyz[1]+mirror_rad, xyz[2]-(radZ//2)]  ,
[xyz[0]+mirror_rad, xyz[1]+mirror_rad, xyz[2]+(radZ//2)] ]




######################################################

mirt = mir_mat


mab = [[ x1y1z1[0] , x1y1z1[1] + i , x1y1z1[2] + j] ,#z
[x1y1z1[0] + i, x1y1z1[1]  , x1y1z1[2] + j] ,#z
#[x1y1z1[0] + i, x1y1z1[1] + j , x1y1z1[2] ] , 

[x2y2z2[0] , x2y2z2[1] - i , x2y2z2[2] - j] ,#z
[x2y2z2[0] - i, x2y2z2[1]  , x2y2z2[2] - j] ,#z
#[x2y2z2[0] - i, x2y2z2[1] - j , x2y2z2[2] ] ,

[mirt[0][0] + i   , mirt[0][1] , x1y1z1[2] + j] ,#z
[mirt[0][0]    , mirt[0][1] + i, x1y1z1[2] + j] ,#z

[mirt[0][0] + i   , mirt[0][1] , x2y2z2[2] - j] ,#z
[mirt[0][0]    , mirt[0][1] + i, x2y2z2[2] - j] ,#z

#[mirt[0][0] + i   , mirt[0][1] + j , x1y1z1[2] ] , 
#[mirt[0][0] + i   , mirt[0][1] + j , x2y2z2[2] ] ,




[mirt[1][0] + i   , mirt[1][1] , x1y1z1[2] + j] ,#z
[mirt[1][0]    , mirt[1][1] - i, x1y1z1[2] + j] ,#z

[mirt[1][0] + i   , mirt[1][1] , x2y2z2[2] - j] ,#z
[mirt[1][0]    , mirt[1][1] - i, x2y2z2[2] - j] ,#z

#[mirt[1][0] + i   , mirt[1][1] - j , x1y1z1[2] ] ,
#[mirt[1][0] + i   , mirt[1][1] - j , x2y2z2[2] ] ,



[mirt[2][0] - i   , mirt[2][1] , x1y1z1[2] + j] ,#z
[mirt[2][0]    , mirt[2][1] + i, x1y1z1[2] + j] ,#z

[mirt[2][0] - i   , mirt[2][1] , x2y2z2[2] - j] ,#z
[mirt[2][0]    , mirt[2][1] + i, x2y2z2[2] - j] ,#z

#[mirt[2][0] - i   , mirt[2][1] + j , x1y1z1[2] ] ,
#[mirt[2][0] - i   , mirt[2][1] + j , x2y2z2[2] ] ,



[mirt[3][0] - i   , mirt[3][1] , x1y1z1[2] + j] ,#z
[mirt[3][0]    , mirt[3][1] - i, x1y1z1[2] + j] ,#z

[mirt[3][0] - i   , mirt[3][1] , x2y2z2[2] - j] ,#z
[mirt[3][0]    , mirt[3][1] - i, x2y2z2[2] - j] ,#z

#[mirt[3][0] - i   , mirt[3][1] - j , x1y1z1[2] ] ,
#[mirt[3][0] - i   , mirt[3][1] - j , x2y2z2[2] ] 
]

######################################################


# 20
x, y, z = mab[0]
x, y, z = mab[1]
x, y, z = mab[2]
x, y, z = mab[3]
x, y, z = mab[4]
x, y, z = mab[5]
x, y, z = mab[6]
x, y, z = mab[7]
x, y, z = mab[8]
x, y, z = mab[9]
x, y, z = mab[10]
x, y, z = mab[11]
x, y, z = mab[12]
x, y, z = mab[13]
x, y, z = mab[14]
x, y, z = mab[15]
x, y, z = mab[16]
x, y, z = mab[17]
x, y, z = mab[18]
x, y, z = mab[19]



"""



