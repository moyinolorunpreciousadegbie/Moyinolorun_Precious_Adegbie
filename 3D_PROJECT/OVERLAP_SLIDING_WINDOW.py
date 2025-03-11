#!/usr/bin/env python3

def lengthOfLIS( L ) :
	mn_x = float('inf')
	mx_x = -float('inf')
	
	mn_y = float('inf')
	mx_y = -float('inf')
	
	mn_z = float('inf')
	mx_z = -float('inf')
	for x , y, z, x2, y2, z2 in L :   ### <<<<<<<<<<<<<<<<<<	
	#for y , x, z, y2, x2, z2 in L :
		mn_x = min(mn_x, x)
		mx_x = max(mx_x, x2)
	
		mn_y = min(mn_y, y)
		mx_y = max(mx_y, y2)
	
		mn_z = min(mn_z, z)
		mx_z = max(mx_z, z2)
		
		
	mx_all = max([mx_x,mx_y,mx_z])
	mn_all = min([mn_x,mn_y,mn_z]) 
	
	t = mx_all - mn_all 

	
	FI = mn_all
	LS = mx_all
	
	#print(FI,LS, '---',t)
	
	def check_x(L, R1,R2 , seen_x,xr,ANS):
		#if seen_x[0] == True : return
		#if ANS[0] !=0 and ANS[3] != 0 : return
		if  ANS[0] != 'SEEN' and ANS[3] != 'SEEN' and (R1 < R2 < ANS[0]  or ANS[3] < R1 < R2  ): return
		if  ANS[0] != 'SEEN' and ANS[3] != 'SEEN' and  (ANS[0] >= R1  or R2 <= ANS[3] ) : return 
		 
		 
		C = 0
		for x , y, z, x2, y2, z2 in L :
		#for y , x, z, y2, x2, z2 in L :
			if x <= R1 < R2 <= x2 :
				C+=1
				if C == 2 :
					if  ANS[0] != 'SEEN' and ANS[0]  < R1   :
						R1 = ANS[0]
					if  ANS[3] != 'SEEN' and  R2 < ANS[3]  :
						R2 = ANS[3]
					ANS[0]=R1
					ANS[3]=R2
					seen_x[0] = True
					xr[0] = R2 - R1
					#print(R1,R2,'x')
					return
		return
					  
			
	def check_y(L, R1,R2 , seen_y, yr,ANS):
		#if seen_y[0] == True : return
		#if ANS[1] !=0 and ANS[4] != 0 : return
		if  ANS[1] != 'SEEN' and ANS[4] != 'SEEN' and (R1 < R2 < ANS[1]  or ANS[4] < R1 < R2  ): return
		if  ANS[1] != 'SEEN' and ANS[4] != 'SEEN' and  (ANS[1] >= R1  or R2 <= ANS[4] ) : return 
		
		C = 0
		for x , y, z, x2, y2, z2 in L :
		#for y , x, z, y2, x2, z2 in L :
			if y <= R1 < R2 <= y2 :
				C+=1
				if C == 2 :
					if  ANS[1] != 'SEEN' and ANS[1]  < R1   :
						R1 = ANS[1]
					if  ANS[4] != 'SEEN' and R2 < ANS[4]  :
						R2 = ANS[4]
					ANS[1]=R1
					ANS[4]=R2
					seen_y[0] = True
					yr[0] = R2 - R1
					#print(R1,R2,'y')
					return
		return
				
			
	def check_z(L, R1,R2 , seen_z,zr,ANS):
		#if seen_z[0] == True : return
		#if ANS[2] !=0 and ANS[5] != 0 : return
		if  ANS[2] != 'SEEN' and ANS[5] != 'SEEN' and (R1 < R2 < ANS[2]  or ANS[5] < R1 < R2  ): return
		if  ANS[2] != 'SEEN' and ANS[5] != 'SEEN' and  (ANS[2] >= R1  or R2 <= ANS[5] ) : return 
			
		C = 0
		for x , y, z, x2, y2, z2 in L :
		#for y , x, z, y2, x2, z2 in L :
			if z <= R1 < R2 <= z2 :
				C+=1
				if C == 2 :
					if  ANS[2] != 'SEEN' and ANS[2]  < R1   :
						R1 = ANS[2]
					if  ANS[5] != 'SEEN' and R2 < ANS[5]  :
						R2 = ANS[5]
					ANS[2]=R1
					ANS[5]=R2
					seen_z[0] = True
					zr[0] = R2 - R1
					#print(R1,R2,'z')
					return
		return
				
	seen_x = [False]
	seen_y = [False]
	seen_z = [False]
	
	ANS = ['SEEN']*6
	
	
	xr = [float('inf')]
	yr = [float('inf')]
	zr = [float('inf')]
	
	T = t
	for i in range(t,0,-1):
		
	#for i in range(1,t+1)
		#if seen_x == [True] and  seen_y == [True] and  seen_z == [True] : break
		#print(i , t-i+1)
		togo = t-i+1
		
		ii = 0
		
		
		if xr[0] != float('inf') and ( T < xr[0]    ) and           yr[0] != float('inf') and ( T < yr[0]    )   and             zr[0] != float('inf') and ( T < zr[0]    ) : break
		
		for rn in range(togo):
			#print([rn+FI,i+ii+FI])
			#
			
			
			
			
			#print(LS-(i+ii) , LS-rn  ,"------",rn+FI,i+ii+FI )
			H , HH = LS-(i+ii) , LS-rn 
			
			if xr[0] != float('inf') and ( (i+ii+FI) -  (rn+FI) < xr[0] or  HH - H < xr[0]    ) and           yr[0] != float('inf') and ( (i+ii+FI) -  (rn+FI) < yr[0] or  HH - H < yr[0]    )   and             zr[0] != float('inf') and ( (i+ii+FI) -  (rn+FI) < zr[0] or  HH - H < zr[0]    ) : break
			
			#if seen_x == False : 
			check_x(  L, rn+FI,i+ii+FI , seen_x,xr,ANS)
			#if seen_y == False : 
			check_y(  L, rn+FI,i+ii+FI , seen_y,yr,ANS)
			#if seen_z == False : 
			check_z(  L, rn+FI,i+ii+FI , seen_z,zr,ANS)
			
			
			check_x(  L, H , HH, seen_x,xr,ANS)
			#if seen_y == False : 
			check_y(  L, H , HH, seen_y,yr,ANS)
			#if seen_z == False : 
			check_z(  L, H , HH , seen_z,zr,ANS)
			ii+=1
			#print(ANS, seen_x, seen_y, seen_z)
		T -=1
	return ANS 
			#return [ANS[1], ANS[0] , ANS[2] ,  ANS[4], ANS[3] , ANS[5] ]




L = [[2,2,2,  3,3,3],   #  23
	[1,1,1,  3,3,3],   # 123
	[2,2,2,  4,4,4],   #  234
	[1,1,1,  4,4,4],   # 1234 <<<<<<<<<
	[0,0,0,  4,4,4],   #01234
	[1,1,1,  5,5,5],   # 12345
]









print(  lengthOfLIS( L ))
print()
print()



L = [
[0,0,0,  9,9,9],   ###########
	
[2,2,2,  5,5,5],   #  2345
[1,1,1,  4,4,4],   # 1234
[2,2,2,  4,4,4],   #  234
[1,1,1,  5,5,5],   # 12345 <<<<<<<<<
[0,0,0,  5,5,5],   #012345
[1,1,1,  6,6,6],   # 123456
]

print( lengthOfLIS( L )   )
print()

LL = [
#[0,0,0,  9,9,9],   ###########
	
[2,2,2,  3,3,3],   #  23
[1,1,1,  3,3,3],   # 123
[2,2,2,  4,4,4],   #  234
[1,1,1,  4,4,4],   # 1234 <<<<<<<<<
[0,0,0,  4,4,4],   #01234
[1,1,1,  5,5,5],   # 12345
]

print( lengthOfLIS( LL )   )
print()

LLL = [
	[1,1,1,  2,2,2],   #  12 <<<<<
	[0,0,0,  2,2,2],   # 012
	[1,1,1,  3,3,3],   #  123
]

print( lengthOfLIS( LLL )   )
print()


LLLL = [
	[1,1,1,  2,2,2],   #  12 <<<<<
	[0,0,0,  2,2,2],   # 012
	[1,1,1,  3,3,3],   #  123
	[7,7,7,  9,9,9],   #  ......789
]

print( lengthOfLIS( LLLL )   )
print()

LLLLL = [
	[1,1,1,  2,2,2],   #  12 <<<<<
	[0,0,0,  2,2,2],   # 012
	[1,1,1,  3,3,3],   #  123
	[7,7,7,  9,9,9],   #  ......789
	[6,6,6,  8,8,8],   #       678      DISJOINT CUBES WRORNG ANSWER !!!  USE UNION FIND ALGORITHM
]

print( lengthOfLIS( LLLLL )   )
print()


F = [[8,8,8,   10, 10, 10],  [6,6,6,   9, 9, 9] ,
[1, 7, 7,   4,10,10], [0, 5, 5,   3,9,9],
[0, 0, 6, 3, 3, 10], [1, 1, 5, 2, 4, 7],
[0, 0, 0, 3,2,3],  [2, 1, 2, 4,3,4],
[0, 7, 0, 3, 10, 3], [2, 5, 2, 3, 8, 5], 
[7, 0, 7, 8, 3, 10] , [5, 2, 7, 7, 5, 9] ,
[7, 0, 0 , 10, 3, 3] ,[5, 2, 2 , 9, 5, 5] ,
[8, 8, 0 , 10, 10, 3] , [7, 7, 2 , 9, 10, 4] ] 


print( lengthOfLIS( F )   )
print()
