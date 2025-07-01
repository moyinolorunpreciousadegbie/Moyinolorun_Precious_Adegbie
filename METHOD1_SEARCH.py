#!/usr/bin/env python3

class SEI:
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
	def horizon(self, X, Y,  Z ,    rad,  radZ , _18,  pos_neg,      px, go, plt, tuo,  seismic_data ):
		serf = [[-1, -1, -1]  ,
			[-1, -1, 0]  ,
			[-1, -1, 1]  ,
			[-1, 0, -1]  ,
			[-1, 0, 0]  ,
			[-1, 0, 1]  ,
			[-1, 1, -1]  ,
			[-1, 1, 0]  ,
			[-1, 1, 1]  ,
			[0, -1, -1]  ,
			[0, -1, 0]  ,
			[0, -1, 1]  ,
			[0, 1, -1]  ,
			[0, 1, 0]  ,
			[0, 1, 1]  ,
			[1, -1, -1]  ,
			[1, -1, 0]  ,
			[1, -1, 1]  ,
			[1, 0, -1]  ,
			[1, 0, 0]  ,
			[1, 0, 1]  ,
			[1, 1, -1]  ,
			[1, 1, 0]  ,
			[1, 1, 1]  ,  ]
		
		x_span = rad#5 # 11
		y_span = rad#5 # 11
		z_span = radZ#10 # 36
		z_step = 7 # 1
		span_xyz = []
		#for i in range(x_span-1,x_span):
			#for j in range(y_span-1,y_span):
		for k in range(1,z_span,z_step):# or    subsets(    (range(1,z_span))    )
					#print( [i,j,k] ) # pick from any 
			span_xyz.append( [x_span,x_span,k] )
					
		q= [   [[X,Y,Z]]   ]
		visited_xy = []
		visited_xyz = []
		
		
	
		
		xL = len(seismic_data[0][0]) -1
		yL = len(seismic_data[0]) -1 
		zL = len(seismic_data) -1  
		
		while q:
			path = q.pop() #  [[X,Y,Z]] 
			xx,yy,zz = path[-1] # X,Y,Z 
			
			for i ,j ,k in serf: # [1, 1, 1]
				for xx_n,yy_n,zz_n in span_xyz :
					nx,ny,nz = xx+(i*xx_n) , yy+(j*yy_n),  zz+(k*zz_n)
					temp_path = path.copy()                                # WITH IN RAD UP-/DOWN+
					if ((0<=nx<=xL)and(0<=ny<=yL)and(0<=nz<=zL))  and (Z-rad<=nz<=Z+rad) and [nx,ny,nz ] not in visited_xyz and [nx,ny,nz ] not in path  : #and ( self.check_neg( seismic_data, _18, nx,ny,nz) or self.check_pos( seismic_data, _18, nx,ny,nz)):
						red_blue = ["EM"]
						if seismic_data[nz,ny,nx ] <0 :
							red_blue[0] = "red"
						if 0<seismic_data[nz,ny,nx ]  :
							red_blue[0] = "blue"
						temp_path.append([nx,ny,nz ])#  [[X,Y,Z]] >>>>> [[X,Y,Z], [nx,ny,nz ]   ] 
						#print(path, '-------',temp_path )
						x_coords, y_coords, z_coords = nx,ny,nz
						if self.check_neg( seismic_data, _18, nx,ny,nz) or self.check_pos( seismic_data, _18, nx,ny,nz ) :
							self.FIG.add_trace(self.go.Scatter3d(x=[x_coords], y=[y_coords], z=[z_coords], mode='markers', marker=dict(size=[self.plsize], color=[ red_blue[0] ] , symbol= self.pls_circ_square ) ))
						q.append(temp_path)
						visited_xyz.append( [nx,ny,nz ])
				
		print(len(visited_xyz))
		pass
		
		
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

W = SEI( tup,tup2, LO, LO2, px, go, vis, vis2 ,  pos_neg , FIG, NFIG , plsize, pls_circ_square)
		
X_, Y_,  Z_ = 334, 344, 525 # 2,400,496 # 6,354,621 # 0,0,0 #<<<<<<<
rad = 40 # 50 # 100 # 11
radZ = 36 #* 2 # 128 # 0
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
inline  = X_ # 300 # 250

crossline = Y_ # 250# 600

twt_z = Z_ # 500
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

for i in range(mc):
    if i < Y : # m1 and m3
        _ =  pllll
        m1.append(_)
	
        __ = [vj ] * X
        m3.append( __ )
    if i < Z :
        _ii = [ (i * _000001)] * X
        m2.append(_ii)
		
m1 = np.array(m1 )
m2 = np.array(m2 )

m3 = np.array(m3 )


plane = go.Surface(x= x1_ , y=y1_, z= m1, surfacecolor=col1  , colorscale= 'Picnic', opacity=1) #<<<<
plane2 = go.Surface(x= x2_ , y=y2_, z= m2, surfacecolor=col2  , colorscale= 'Picnic', opacity=1) #<<<<

plane3 = go.Surface(x= x2_ , y=y1_, z= m3, surfacecolor=col3  , colorscale= 'Picnic', opacity=1) #<<<<

print([len(col1),len( col1[0] )],[len(m1),len( m1[0] )])
print([len(col2),len( col2[0] )],[len(m2),len( m2[0] )])




W.FIG.add_traces([plane])
W.FIG.add_traces([plane2])

W.FIG.add_traces([plane3])



###############################################################################################################################################################


print("DONE" )





W.FIG.update_layout(
		autosize=False,
		width=1150,#800
		height=950,#800
		margin=dict(l=65, r=50, b=65, t=90)
	)
W.FIG.show()
