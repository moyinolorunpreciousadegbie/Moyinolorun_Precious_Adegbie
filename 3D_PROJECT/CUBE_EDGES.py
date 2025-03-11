#!/usr/bin/env python3

#X1_Y1_Z1 = [0:3]
#X2_Y2_Z3 = [3:6]

X1_Y1_Z1 = [0 for i in range(3)]
X2_Y2_Z2 = [10 for i in range(3)]

#print(tlf, brb)
al = ["x","y","z"]

q = []


qqq = []
m = {}
c = 0
X_ULT = []
Y_ULT = []
Z_ULT = []

xx = []
yy = []
zz = []


xx_ = []
yy_ = []
zz_ = []

ccc = []

x_y_z_s_2 = ['-','-','-']
x_y_z_s_1 = ['+','+','+']

corn = []

EDGES = [ (X2_Y2_Z2[0] , X2_Y2_Z2[1], X2_Y2_Z2[2] ,("X2 Y2 Z2"),['-','-','-'])    ]

for i in range(3):
	ct = []
	#q.append(brb)
	#print(brb[0:i] ,  tlf[i], brb[i+1:])
	
	tem = X2_Y2_Z2[0:i] +  [X1_Y1_Z1[i]] + X2_Y2_Z2[i+1:]
	
	ts = x_y_z_s_2[0:i] +  [x_y_z_s_1[i]] + x_y_z_s_2[i+1:]
	#print(tem, "prev   ", al[i])
	#q.append(brb)
		#q.append(tem)
		#c += 1 
		
	X, Y, Z =  X2_Y2_Z2
	ct.append((X , Y, Z ,("X2 Y2 Z2"),['-','-','-']))
		
	if [X , Y, Z] not in corn : corn.append([X , Y, Z])
		
	X__ , Y__, Z__ = 'X2 ' , 'Y2 ' , 'Z2'
#   x     y    z
	#x_s , y_s , z_s = '-','-','-'
		
	xi , yi, zi = tem
	
	x_s , y_s , z_s = ts
	
	if xi == X1_Y1_Z1[0] and yi == X2_Y2_Z2[1] and zi == X2_Y2_Z2[2] :
			 #
		X__ = 'X1 '
	if xi == X2_Y2_Z2[0] and yi == X1_Y1_Z1[1] and zi == X2_Y2_Z2[2] :
		                            #
		Y__ = 'Y1 '
	if xi == X2_Y2_Z2[0] and yi == X2_Y2_Z2[1] and zi == X1_Y1_Z1[2]:
		                                                  #
		Z__ = 'Z1'
	
	ct.append((xi, yi, zi  , (X__+Y__+Z__),[x_s , y_s , z_s]))
	
	if [xi, yi, zi] not in corn : corn.append([xi, yi, zi])
	
	if (xi, yi, zi  , (X__+Y__+Z__)) not  in EDGES :
		EDGES.append(   (xi, yi, zi  , (X__+Y__+Z__),[x_s , y_s , z_s]) )
	
	xx = []
	yy = []
	zz = []
	if i not in m :
		m[i] = [X2_Y2_Z2]
	m[i].append(tem)	
	
	#cc = 0
	for j in range(3):
		if j == i : continue
		if j != i :
			
			temp = tem[0:j] +  [X1_Y1_Z1[j]] + tem[j+1:]
			
			tss = ts[0:j] +  [x_y_z_s_1[j]] + ts[j+1:]
			
			xii , yii, zii = temp
			X_1 , Y_1, Z_1 = 'X2 ' , 'Y2 ' , 'Z2'
		 #  x     y     z
		
			#X_s, Y_s , Z_s = '- ' , '- ' , '-'
			
			
			
			if [xii, yii, zii] not in corn : corn.append([xii, yii, zii ])
			
			X_s, Y_s , Z_s = tss
			
			if xii == X1_Y1_Z1[0] and yii == X1_Y1_Z1[1] and zii == X2_Y2_Z2[2] :
					  #                       #
				X_1 = 'X1 '
				Y_1 = 'Y1 '
		
				X_s = '+'
				Y_s = '+'
			if xii == X1_Y1_Z1[0] and yii == X2_Y2_Z2[1] and zii == X1_Y1_Z1[2] :
					  #                                             #
				X_1 = 'X1 '
				Z_1 = 'Z1'
				
				X_s = '+'
				Z_s = '+'
			if xii == X2_Y2_Z2[0] and yii == X1_Y1_Z1[1] and zii == X1_Y1_Z1[2] :
									          #					     #
				Y_1 = 'Y1 ' 
				Z_1 = 'Z1'
				
				Y_s = '+'
				Z_s = '+'
				
			
			
			ct.append((xii , yii, zii,(X_1+Y_1+Z_1),[X_s , Y_s , Z_s]))
			
			if [xii, yii, zii] not in corn : corn.append([xii, yii, zii ])
			
			
			if (xii , yii, zii,(X_1+Y_1+Z_1),[X_s , Y_s , Z_s]) not  in EDGES :
				EDGES.append(  (xii , yii, zii,(X_1+Y_1+Z_1),[X_s , Y_s , Z_s])  )
				
				
				
			X_e, Y_e, Z_e = X1_Y1_Z1 
			
			
			
			
			ct.append((X_e, Y_e, Z_e, ("X1 Y1 Z1"),  ['+','+','+']))
			if [ X_e, Y_e, Z_e] not in corn :corn.append([X_e, Y_e, Z_e ])
			ccc.append(ct)
			#print(ct)
			ct.pop()
			ct.pop()
			
			
			
			m[i].append(temp)
			m[i].append(X1_Y1_Z1)
			#print(m[i], "THIS", len(m[i]))
			#q.append(m[i].copy())
			xx = []
			yy = []
			zz = []
			for x, y, z in  m[i].copy()  :
												#
				X_ULT.append(x)
				Y_ULT.append(y)
				Z_ULT.append(z)
				
			
				
			m[i].pop()
			m[i].pop()
			

EDGES.append(  (X1_Y1_Z1[0] , X1_Y1_Z1[1], X1_Y1_Z1[2] ,("X1 Y1 Z1"), ['+','+','+'])    )	

if [X1_Y1_Z1[0] , X1_Y1_Z1[1], X1_Y1_Z1[2]] not in corn : corn.append([X1_Y1_Z1[0] , X1_Y1_Z1[1], X1_Y1_Z1[2]])


			
			
#print( X_ULT[0:4], Y_ULT[0:4] , Z_ULT[0:4] )# 1
#print()
#print( X_ULT[4:8], Y_ULT[4:8] , Z_ULT[4:8] )# 2
#print()
#print( X_ULT[8:12], Y_ULT[8:12] , Z_ULT[8:12] )# 3
#print()
#print( X_ULT[12:16], Y_ULT[12:16] , Z_ULT[12:16] )# 4
#print()
#print( X_ULT[16:20], Y_ULT[16:20] , Z_ULT[16:20] )# 5
#print()
#print( X_ULT[20:24], Y_ULT[20:24] , Z_ULT[20:24] )# 6
#print()

					
#print(X_ULT)
#print()
#print(Y_ULT)
#print()
#print(Z_ULT)
#print()




_1  = X_ULT[0:4], Y_ULT[0:4] , Z_ULT[0:4] 

_2  = X_ULT[4:8], Y_ULT[4:8] , Z_ULT[4:8] 

_3  = X_ULT[8:12], Y_ULT[8:12] , Z_ULT[8:12] 

_4  = X_ULT[12:16], Y_ULT[12:16] , Z_ULT[12:16] 

_5  = X_ULT[16:20], Y_ULT[16:20] , Z_ULT[16:20] 

_6  = X_ULT[20:24], Y_ULT[20:24] , Z_ULT[20:24] 


't l f '    'b r ba '   

't l ba '   'b r f '

't r f '   'b l ba '

't r ba '   'b l f '

print( EDGES , len(EDGES))
print()
print(corn , len(corn))


F = [[8,8,8,   10, 10, 10],  [6,6,6,   9, 9, 9] ,
[1, 7, 7,   4,10,10], [0, 5, 5,   3,9,9],
[0, 0, 6, 3, 3, 10], [1, 1, 5, 2, 4, 7],
[0, 0, 0, 3,2,3],  [2, 1, 2, 4,3,4],
[0, 7, 0, 3, 10, 3], [2, 5, 2, 3, 8, 5], 
[7, 0, 7, 8, 3, 10] , [5, 2, 7, 7, 5, 9] ,
[7, 0, 0 , 10, 3, 3] ,[5, 2, 2 , 9, 5, 5] ,
[8, 8, 0 , 10, 10, 3] , [7, 7, 2 , 9, 10, 4] ] 

