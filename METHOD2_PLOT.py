#!/usr/bin/env python3

#!/usr/bin/env python3

xyz = [5,5,5]
stp = 4
radZ = 7

_25 = 25
mirror_rad = _25
mir_mat = [	[xyz[0]-mirror_rad, xyz[1]-mirror_rad]  ,
			[xyz[0]-mirror_rad, xyz[1]+mirror_rad]  ,
			[xyz[0]+mirror_rad, xyz[1]-mirror_rad]  ,
			[xyz[0]+mirror_rad, xyz[1]+mirror_rad] ]
		
xyz_n = []
xx=[]
yy=[]
zz=[]

incd = 1
for rad in range(1,_25+1,stp):
	#rad = 5 # rad X 1,2,3,4,5,6,7...... n
	# SLOPIEST HORIZON
	
	
	
	
	x1y1z1 = []
	x2y2z2 = []
	ind = 0
	for i in xyz :
		if ind == len(xyz)-1:
			x1y1z1.append(i-(radZ//2)  ) #<<<<<<<< radZ
			x2y2z2.append(i+(radZ//2)  ) #<<<<<<<< radZ
		if ind < len(xyz)-1:	
			x1y1z1.append(i-rad) 
			x2y2z2.append(i+rad  )
		ind+=1
		
	#print(x1y1z1)
	#print(x2y2z2)
	
	lenght = (rad * 2) + 1
	
	for i in range(lenght):
		for j in range(radZ):
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
                                                				#######################
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
			
			x, y, z = mab[0]
			if [x,y,z] not in xyz_n:
				xyz_n.append([x,y,z])
				xx.append(x)
				yy.append(y)
				zz.append(z)
			x, y, z = mab[1]
			if [x,y,z] not in xyz_n:
				xyz_n.append([x,y,z])
				xx.append(x)
				yy.append(y)
				zz.append(z)
			x, y, z = mab[2]
			if [x,y,z] not in xyz_n:
				xyz_n.append([x,y,z])
				xx.append(x)
				yy.append(y)
				zz.append(z)
			x, y, z = mab[3]
			if [x,y,z] not in xyz_n:
				xyz_n.append([x,y,z])
				xx.append(x)
				yy.append(y)
				zz.append(z)
			x, y, z = mab[4]
			if [x,y,z] not in xyz_n:
				xyz_n.append([x,y,z])
				xx.append(x)
				yy.append(y)
				zz.append(z)
			x, y, z = mab[5]
			if [x,y,z] not in xyz_n:
				xyz_n.append([x,y,z])
				xx.append(x)
				yy.append(y)
				zz.append(z)
			x, y, z = mab[6]
			if [x,y,z] not in xyz_n:
				xyz_n.append([x,y,z])
				xx.append(x)
				yy.append(y)
				zz.append(z)
			x, y, z = mab[7]
			if [x,y,z] not in xyz_n:
				xyz_n.append([x,y,z])
				xx.append(x)
				yy.append(y)
				zz.append(z)
			x, y, z = mab[8]
			if [x,y,z] not in xyz_n:
				xyz_n.append([x,y,z])
				xx.append(x)
				yy.append(y)
				zz.append(z)
			x, y, z = mab[9]
			if [x,y,z] not in xyz_n:
				xyz_n.append([x,y,z])
				xx.append(x)
				yy.append(y)
				zz.append(z)
			x, y, z = mab[10]
			if [x,y,z] not in xyz_n:
				xyz_n.append([x,y,z])
				xx.append(x)
				yy.append(y)
				zz.append(z)
			x, y, z = mab[11]
			if [x,y,z] not in xyz_n:
				xyz_n.append([x,y,z])
				xx.append(x)
				yy.append(y)
				zz.append(z)
			x, y, z = mab[12]
			if [x,y,z] not in xyz_n:
				xyz_n.append([x,y,z])
				xx.append(x)
				yy.append(y)
				zz.append(z)
			x, y, z = mab[13]
			if [x,y,z] not in xyz_n:
				xyz_n.append([x,y,z])
				xx.append(x)
				yy.append(y)
				zz.append(z)
			x, y, z = mab[14]
			if [x,y,z] not in xyz_n:
				xyz_n.append([x,y,z])
				xx.append(x)
				yy.append(y)
				zz.append(z)
			x, y, z = mab[15]
			if [x,y,z] not in xyz_n:
				xyz_n.append([x,y,z])
				xx.append(x)
				yy.append(y)
				zz.append(z)
			x, y, z = mab[16]
			if [x,y,z] not in xyz_n:
				xyz_n.append([x,y,z])
				xx.append(x)
				yy.append(y)
				zz.append(z)
			x, y, z = mab[17]
			if [x,y,z] not in xyz_n:
				xyz_n.append([x,y,z])
				xx.append(x)
				yy.append(y)
				zz.append(z)
			x, y, z = mab[18]
			if [x,y,z] not in xyz_n:
				xyz_n.append([x,y,z])
				xx.append(x)
				yy.append(y)
				zz.append(z)
			x, y, z = mab[19]
			if [x,y,z] not in xyz_n:
				xyz_n.append([x,y,z])
				xx.append(x)
				yy.append(y)
				zz.append(z)
				
			##########################################################################################################################################	
			# - -
			# - +
			# + -
			# + +
			
			mab = [
			#######################
			[mirt[0][0] +(stp*incd) - i   , mirt[0][1]+(stp*incd) , x1y1z1[2] + j] ,#z
			[mirt[0][0]+(stp*incd)    , mirt[0][1]+(stp*incd)  - i, x1y1z1[2] + j] ,#z
				
			[mirt[0][0]+(stp*incd) - i   , mirt[0][1]+(stp*incd) , x2y2z2[2] - j] ,#z
			[mirt[0][0]+(stp*incd)    , mirt[0][1]+(stp*incd) - i, x2y2z2[2] - j] ,#z
				
			#[mirt[0][0]+(stp*incd) - i   , mirt[0][1]+(stp*incd) - j , x1y1z1[2] ] , 
			#[mirt[0][0]+(stp*incd) - i   , mirt[0][1]+(stp*incd) - j , x2y2z2[2] ] ,
				
				
				
				
			[mirt[1][0]+(stp*incd) - i   , mirt[1][1]-(stp*incd) , x1y1z1[2] + j] ,#z
			[mirt[1][0]+(stp*incd)    , mirt[1][1]-(stp*incd) + i, x1y1z1[2] + j] ,#z
				
			[mirt[1][0]+(stp*incd) - i   , mirt[1][1]-(stp*incd) , x2y2z2[2] - j] ,#z
			[mirt[1][0]+(stp*incd)    , mirt[1][1]-(stp*incd) + i, x2y2z2[2] - j] ,#z
				
			#[mirt[1][0]+(stp*incd) - i   , mirt[1][1]-(stp*incd) + j , x1y1z1[2] ] ,
			#[mirt[1][0]+(stp*incd) - i   , mirt[1][1]-(stp*incd) + j , x2y2z2[2] ] ,
				
				
				
			[mirt[2][0]-(stp*incd) + i   , mirt[2][1]+(stp*incd) , x1y1z1[2] + j] ,#z
			[mirt[2][0]-(stp*incd)    , mirt[2][1]+(stp*incd) - i, x1y1z1[2] + j] ,#z
				
			[mirt[2][0]-(stp*incd) + i   , mirt[2][1]+(stp*incd) , x2y2z2[2] - j] ,#z
			[mirt[2][0]-(stp*incd)    , mirt[2][1]+(stp*incd) - i, x2y2z2[2] - j] ,#z
				
			#[mirt[2][0]-(stp*incd) + i   , mirt[2][1]+(stp*incd) - j , x1y1z1[2] ] ,
			#[mirt[2][0]-(stp*incd) + i   , mirt[2][1]+(stp*incd) - j , x2y2z2[2] ] ,
				
				
				
			[mirt[3][0]-(stp*incd) + i   , mirt[3][1]-(stp*incd) , x1y1z1[2] + j] ,#z
			[mirt[3][0]-(stp*incd)    , mirt[3][1]-(stp*incd) + i, x1y1z1[2] + j] ,#z
				
			[mirt[3][0]-(stp*incd) + i   , mirt[3][1]-(stp*incd) , x2y2z2[2] - j] ,#z
			[mirt[3][0]-(stp*incd)    , mirt[3][1]-(stp*incd) + i, x2y2z2[2] - j] ,#z
				
			#[mirt[3][0]-(stp*incd) + i   , mirt[3][1]-(stp*incd) + j , x1y1z1[2] ] ,
			#[mirt[3][0]-(stp*incd) + i   , mirt[3][1]-(stp*incd) + j , x2y2z2[2] ] 
			]
			
			
			x, y, z = mab[0]
			if [x,y,z] not in xyz_n:
				xyz_n.append([x,y,z])
				xx.append(x)
				yy.append(y)
				zz.append(z)
			x, y, z = mab[1]
			if [x,y,z] not in xyz_n:
				xyz_n.append([x,y,z])
				xx.append(x)
				yy.append(y)
				zz.append(z)
			x, y, z = mab[2]
			if [x,y,z] not in xyz_n:
				xyz_n.append([x,y,z])
				xx.append(x)
				yy.append(y)
				zz.append(z)
			x, y, z = mab[3]
			if [x,y,z] not in xyz_n:
				xyz_n.append([x,y,z])
				xx.append(x)
				yy.append(y)
				zz.append(z)
			x, y, z = mab[4]
			if [x,y,z] not in xyz_n:
				xyz_n.append([x,y,z])
				xx.append(x)
				yy.append(y)
				zz.append(z)
			x, y, z = mab[5]
			if [x,y,z] not in xyz_n:
				xyz_n.append([x,y,z])
				xx.append(x)
				yy.append(y)
				zz.append(z)
			x, y, z = mab[6]
			if [x,y,z] not in xyz_n:
				xyz_n.append([x,y,z])
				xx.append(x)
				yy.append(y)
				zz.append(z)
			x, y, z = mab[7]
			if [x,y,z] not in xyz_n:
				xyz_n.append([x,y,z])
				xx.append(x)
				yy.append(y)
				zz.append(z)
			x, y, z = mab[8]
			if [x,y,z] not in xyz_n:
				xyz_n.append([x,y,z])
				xx.append(x)
				yy.append(y)
				zz.append(z)
			x, y, z = mab[9]
			if [x,y,z] not in xyz_n:
				xyz_n.append([x,y,z])
				xx.append(x)
				yy.append(y)
				zz.append(z)
			x, y, z = mab[10]
			if [x,y,z] not in xyz_n:
				xyz_n.append([x,y,z])
				xx.append(x)
				yy.append(y)
				zz.append(z)
			x, y, z = mab[11]
			if [x,y,z] not in xyz_n:
				xyz_n.append([x,y,z])
				xx.append(x)
				yy.append(y)
				zz.append(z)
			x, y, z = mab[12]
			if [x,y,z] not in xyz_n:
				xyz_n.append([x,y,z])
				xx.append(x)
				yy.append(y)
				zz.append(z)
			x, y, z = mab[13]
			if [x,y,z] not in xyz_n:
				xyz_n.append([x,y,z])
				xx.append(x)
				yy.append(y)
				zz.append(z)
			x, y, z = mab[14]
			if [x,y,z] not in xyz_n:
				xyz_n.append([x,y,z])
				xx.append(x)
				yy.append(y)
				zz.append(z)
			x, y, z = mab[15]
			if [x,y,z] not in xyz_n:
				xyz_n.append([x,y,z])
				xx.append(x)
				yy.append(y)
				zz.append(z)
			
	incd += 1
			
				
#print(xx,len(xx))
#print(yy,len(yy))
#print(zz, len(zz))
			
import plotly.graph_objects as go


tttt = tuple()

#x, y, z = [5], [5] , [5]
x, y, z = [ xyz[0] ] ,  [ xyz[1] ]  , [ xyz[2] ]

fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z,
                                   mode='markers', marker=dict(#size=[10],
						color=["blue"] , symbol="square" )   )])

fig2 = go.Figure(data=[go.Scatter3d(x=xx, y=yy, z=zz,
                                   mode='markers', marker=dict(#size=[10],
						color=["red"]*len(xx) , symbol="square" )   )])

tttt += fig.data + fig2.data


FIG =  go.Figure(data=tttt )
FIG.update_layout(
		autosize=False,
		width=1150,#800
		height=950,#800
		margin=dict(l=65, r=50, b=65, t=90) ,  scene=dict(zaxis=dict(autorange='reversed'))
	)
FIG.show()