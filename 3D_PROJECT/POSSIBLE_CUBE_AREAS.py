#!/usr/bin/env python3


def product(x,y,z,     x2,y2,z2):
	
	
	mn = float('inf')
	mx = -float('inf')
	
	mn_xyz = min([x,y,z])
	
	mx_xyz = max([x2,y2,z2])
	
	
	RR = max([x2-x,y2-y,z2-z])
	
	
	print(int(mn_xyz) , int(mx_xyz) )
	
	xx =  []
	yy =  []
	zz =  []
	for i in range(int(mn_xyz) , int(mx_xyz)  ) :
		for j in range(1, RR+1 ) :
			_1 = j
			if x <= i <= x2 and  x <= i+_1 <= x2   and y <= i <= y2 and y <= i+_1 <= y2 :
				if [i,i+_1] not in xx : xx.append([i,i+_1])
				if [i,i+_1] not in yy : yy.append([i,i+_1])
				
			if x <= i <= x2 and  x <= i+_1 <= x2   and z <= i <= z2 and z <= i+_1 <= z2 :
				if [i,i+_1] not in xx : xx.append([i,i+_1])
				if [i,i+_1] not in zz : zz.append([i,i+_1])
				
			if y <= i <= y2 and  y <= i+_1 <= y2   and z <= i <= z2 and z <= i+_1 <= z2 :
				if [i,i+_1] not in yy : yy.append([i,i+_1])
				if [i,i+_1] not in zz : zz.append([i,i+_1])
				
				
			if x <= i <= x2 and  x <= i+_1 <= x2   and y <= i <= y2 and  y <= i+_1 <= y2   and z <= i <= z2 and z <= i+_1 <= z2 :
				if [i,i+_1] not in xx : xx.append([i,i+_1])
				if [i,i+_1] not in yy : yy.append([i,i+_1])
				if [i,i+_1] not in zz : zz.append([i,i+_1])
				
				
			if x <= i <= x2 and  x <= i+_1 <= x2 :
				if [i,i+_1] not in xx : xx.append([i,i+_1])
				
			if y <= i <= y2 and  y <= i+_1 <= y2 :
				if [i,i+_1] not in yy : yy.append([i,i+_1])
				
			if z <= i <= z2 and  z <= i+_1 <= z2 :
				if [i,i+_1] not in zz : zz.append([i,i+_1])
	
	
	print(xx)
	print()
	print(yy)
	print()
	print(zz)
	print()
	
	pools = [xx,yy,zz]

	q = []
	result = [[]]
	cn= 0
	for pool in pools: # [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]
		
		q = []
		for x in result :
			if  len( x ) == len(xx) * len(yy) * len(zz)   : break
			
			for y in pool : # [0, 1]
				
				cn += 1
				#if  len( x+[y] ) == (repeat * len(iterables)  )  : print(x+[y] , cn) # 365     876
				if  len(  x+[y]  ) == len(xx) * len(yy) * len(zz)   : print(x+[y] )
				
				
				if x+[y] not in q :
					q.append( x+[y]   )
				#
				
		result = q
		
		
		
	print(result , len(result),   len(xx) * len(yy) * len(zz) )
	return result



#product(  0,0,0,     5,5,5   )


print()

product(  0,0,0,     7,7,7   )


print()





# 01 02 03 04 05  1  5  15        15 x 15 x 15   = 3375
# 12 13 14 15     2  4  10        x    y    z
# 23 24 25        3  3  6
# 34 35           4  2  3
# 45              5  1  1
#                 