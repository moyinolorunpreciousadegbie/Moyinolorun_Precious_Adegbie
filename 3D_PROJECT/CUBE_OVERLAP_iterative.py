#!/usr/bin/env python3

def lengthOfLIS( lis_range ) :
	
	rangg = []
	mn_x = float('inf')
	mx_x = -float('inf')
	
	mn_y = float('inf')
	mx_y = -float('inf')
	
	mn_z = float('inf')
	mx_z = -float('inf')
	
	temp = []
	#for y , x, z, y2, x2, z2 in lis_range:
	#   t   l  f  bo  r    ba
	for x , y, z, x2, y2, z2 in lis_range:   ### <<<<<<<<<<<<<<<<<<,
		mn_y = min(mn_y, y)
		mx_y = max(mx_y, y2)
	
	
		mn_x = min(mn_x, x)
		mx_x = max(mx_x, x2)
	
		mn_z = min(mn_z, z)
		mx_z = max(mx_z, z2)
	
		if [y , y2 ,  x , x2  , z , z2 ] not in temp : temp.append( [y , y2 ,  x , x2  , z , z2 ] )
	
	
	
	#segmentTree = SegmentTree()
	
	# [0,0,0,  5, 5, 5]
	#  t l f   bo r  ba
	#  0 1 2   3  4  5
	
	#top, bottom,    left, right,  front, back = lis_range[0] , lis_range[3] ,  lis_range[1] , lis_range[4] , lis_range[2] , lis_range[5] 
	
	top, bottom,    left, right,  front, back = mn_y , mx_y ,  mn_x , mx_x  , mn_z , mx_z 
	#left, right,  top, bottom,   front, back = mn_x , mx_x ,  mn_y , mx_y  , mn_z , mx_z   ### <<<<<<<<<<<<<<<<<<,
	top, bottom,    left, right,  front, back = mn_x , mx_x ,  mn_y , mx_y  , mn_z , mx_z 
	TIS = [top, bottom,    left, right,  front, back]
	#      top, bottom,    left, right,  front, back
	#TIS = [ left, right,  top, bottom,     front, back] ### <<<<<<<<<<<<<<<<<<,
	
	#lis_range = [top,left,front,   bottom+1,right+1,back+1 ]
	
	
	#segmentTree.query( top, bottom,    left, right,  front, back, lis_range , TIS) 
	
	#segmentTree.query( left, right,   top, bottom,    front, back, lis_range , TIS) 
	
	self_mn__x = float('inf')
	self_mx__x = -float('inf')
	
	self_mn__y = float('inf')
	self_mx__y = -float('inf')
	
	self_mn__z = float('inf')
	self_mx__z = -float('inf')
	
	q = [[top, bottom,    left, right,  front, back]]
	
	#q = [[ left, right, top, bottom,  front, back]]
	#intercept = [[top, bottom,    left, right,  front, back]]
	
	intercept = []
	
	ans = []
	
	while q:#q :#and  q[-1][0] < q[-1][1] or   q[-1][2] < q[-1][3] or   q[-1][4] < q[-1][5] :   #  q[0] < q[3] or   q[1] < q[4] or   q[2] < q[5] :
		top, bottom,    left, right,  front, back = q.pop()
		#left, right, top, bottom,  front, back = q.pop()
		
		if   [top, bottom,    left, right,  front, back]  in intercept :
			continue
	
		#if [left, right, top, bottom,  front, back] in intercept : continue
	
		intercept.append( [top, bottom,    left, right,  front, back]  )
		#intercept.append( [left, right, top, bottom,  front, back]  )
	
		
		#print([left, right,  top, bottom,     front, back])
		
		mid_t_bo = (top + bottom) // 2    ######
	
									######
	
	
									#   #
		mid_l_r = (left + right) // 2  #   #
	
	
	
	
		mid_f_ba = (front + back) // 2 
		
		
		
	
	
	##########################################################
		cn = 0
		for qleft,  qtop , qfront,  qright ,   qbottom ,   qback in lis_range:
		#for  qtop, qleft ,   qfront      ,   qbottom, qright ,   qback in lis_range:
			if (qbottom < top or bottom < qtop or top > bottom) or (qright < left or right < qleft or left > right) or (qback<front or back <qfront or front>back ):                                                                                        
				#  0                  0                              123 qright     123 right                                 0                  0 
				#  1 qbottom          1 bottom                     left 456      qleft 456                                    1 qback            1 back 
				#            2 top             2 qtop      																	         2 front           2 qfront
				#            3 				   3 																				     3 				   3
				
				
				continue
				#pass
			if ( qtop <= top and bottom <= qbottom ) and   ( qleft <= left and right <= qright ) and  ( qfront <= front and back <= qback ): # FITS ONE THEN COUNT ++
			# FULLY IN ^^^^^^
			
			#if fn(top , bottom , qtop , qbottom )  and fn( left , right, qleft , qright, )  and fn( front , back , qfront , qback ) :
				#print(qtop ,'<=', top , bottom ,'<=',  qbottom ,'  ',   qleft ,'<=',  left , right ,'<=',  qright , qfront,'<=',  front, back ,'<=',  qback  )
				cn += 1
			
				if cn == 2 : # FITS ALL
					if [top,left,front , bottom, right, back] not in ans : 
						ans.append([top,left,front , bottom, right, back ])
						#print([top,left,front , bottom, right, back ])
						self_mn__y = min(self_mn__y , left)
						self_mx__y = max(self_mx__y , right)
						
						self_mn__x = min(self_mn__x , top)
						self_mx__x = max(self_mx__x , bottom)
						
						self_mn__z = min(self_mn__z , front)
						self_mx__z = max(self_mx__z , back)
						break
						#break
		##############################
		cn = 0
			
			
			
			
			
		if  (top == mid_t_bo < bottom and top + 1 == bottom and mid_t_bo + 1 == bottom ) and ( left == mid_l_r < right and left + 1 == right and mid_l_r + 1 == right ) and ( front == mid_f_ba < back and front + 1 == back and mid_f_ba + 1 == back ): 
			
			#print(top, bottom,    left, right,  front, back,"UP")
			#break
			continue
			#pass
	
	
	
		if  (top < mid_t_bo == bottom and top == mid_t_bo - 1  and top  == bottom - 1  ) and ( left < mid_l_r == right and left == mid_l_r - 1 and         left == right - 1 ) and ( front < mid_f_ba == back and front == mid_f_ba - 1 and front == back - 1 ): 
			#print(top, bottom,    left, right,  front, back,"DOWN")
			#break
			continue
			#pass
			
			
		
	
	
	
	
	
	
		if 3==5 and (top == mid_t_bo < bottom and top + 1 == bottom and mid_t_bo + 1 == bottom )  and left < mid_l_r < right  and front < mid_f_ba < back : 
																										#                       #
			#print('CASE 1')
			# left < mid_l_r < right  and front < mid_f_ba < back 
			
			if [top, left, front, bottom, right, mid_f_ba] not in intercept :
				q.append([top, bottom, left, right, front, mid_f_ba ])
			if [top, left, mid_f_ba, bottom, right, back] not in intercept :
				q.append([top, bottom, left, right, mid_f_ba, back ])
			if [top, left, front, bottom, mid_l_r, back] not in intercept :
				q.append([top, bottom, left, mid_l_r, front, back ])
			if [top, left, front, bottom, mid_l_r, mid_f_ba] not in intercept :
				q.append([top, bottom, left, mid_l_r, front, mid_f_ba ])
			if [top, left, mid_f_ba, bottom, mid_l_r, back] not in intercept :
				q.append([top, bottom, left, mid_l_r, mid_f_ba, back ])
			if [top, mid_l_r, front, bottom, right, back] not in intercept :
				q.append([top, bottom, mid_l_r, right, front, back ])
			if [top, mid_l_r, front, bottom, right, mid_f_ba] not in intercept :
				q.append([top, bottom, mid_l_r, right, front, mid_f_ba ])
			if [top, mid_l_r, mid_f_ba, bottom, right, back] not in intercept :
				q.append([top, bottom, mid_l_r, right, mid_f_ba, back ])
			continue                           #
		      #                                                  															#
		if 3==5 and top < mid_t_bo < bottom  and ( left == mid_l_r < right and left + 1 == right and mid_l_r + 1 == right )  and front < mid_f_ba < back : 
			
			#print('CASE 2')
			# top < mid_t_bo < bottom   and front < mid_f_ba < back
			if [top, left, front, bottom, right, mid_f_ba] not in intercept :
				q.append([top, bottom, left, right, front, mid_f_ba ])
			if [top, left, mid_f_ba, bottom, right, back] not in intercept :
				q.append([top, bottom, left, right, mid_f_ba, back ])
			if [top, left, front, mid_t_bo, right, back] not in intercept :
				q.append([top, mid_t_bo, left, right, front, back ])
			if [top, left, front, mid_t_bo, right, mid_f_ba] not in intercept :
				q.append([top, mid_t_bo, left, right, front, mid_f_ba ])
			if [top, left, mid_f_ba, mid_t_bo, right, back] not in intercept :
				q.append([top, mid_t_bo, left, right, mid_f_ba, back ])
			if [mid_t_bo, left, front, bottom, right, back] not in intercept :
				q.append([mid_t_bo, bottom, left, right, front, back ])
			if [mid_t_bo, left, front, bottom, right, mid_f_ba] not in intercept :
				q.append([mid_t_bo, bottom, left, right, front, mid_f_ba ])
			if [mid_t_bo, left, mid_f_ba, bottom, right, back] not in intercept :
				q.append([mid_t_bo, bottom, left, right, mid_f_ba, back ])
			continue	
		                                                   # 
			
			
		       #                             #
		if  3==5 and top < mid_t_bo < bottom   and left < mid_l_r < right  and ( front == mid_f_ba < back and front + 1 == back and mid_f_ba + 1 == back ):  
			
			#print('CASE 3')
			# top < mid_t_bo < bottom   and left < mid_l_r < right 
			if [top, left, front, bottom, mid_l_r, back] not in intercept :
				q.append([top, bottom, left, mid_l_r, front, back ])
			if [top, mid_l_r, front, bottom, right, back] not in intercept :
				q.append([top, bottom, mid_l_r, right, front, back ])
			if [top, left, front, mid_t_bo, right, back] not in intercept :
				q.append([top, mid_t_bo, left, right, front, back ])
			if [top, left, front, mid_t_bo, mid_l_r, back] not in intercept :
				q.append([top, mid_t_bo, left, mid_l_r, front, back ])
			if [top, mid_l_r, front, mid_t_bo, right, back] not in intercept :
				q.append([top, mid_t_bo, mid_l_r, right, front, back ])
			if [mid_t_bo, left, front, bottom, right, back] not in intercept :
				q.append([mid_t_bo, bottom, left, right, front, back ])
			if [mid_t_bo, left, front, bottom, mid_l_r, back] not in intercept :
				q.append([mid_t_bo, bottom, left, mid_l_r, front, back ])
			if [mid_t_bo, mid_l_r, front, bottom, right, back] not in intercept :
				q.append([mid_t_bo, bottom, mid_l_r, right, front, back ])
			continue	
			             # 
			
			
			
		       #
		if  3==5 and top < mid_t_bo < bottom  and ( left == mid_l_r < right and left + 1 == right and mid_l_r + 1 == right ) and ( front == mid_f_ba < back and front + 1 == back and mid_f_ba + 1 == back ): 
			
			#print('CASE 4')
			# top < mid_t_bo < bottom 
			
			if [top, left, front, mid_t_bo, right, back] not in intercept :
				q.append([top, mid_t_bo, left, right, front, back ])
			if [mid_t_bo, left, front, bottom, right, back] not in intercept :
				q.append([mid_t_bo, bottom, left, right, front, back ])
			continue
			
			
																										#
		if 3==5 and (top == mid_t_bo < bottom and top + 1 == bottom and mid_t_bo + 1 == bottom )  and left < mid_l_r < right and ( front == mid_f_ba < back and front + 1 == back and mid_f_ba + 1 == back ): 
			
			#print('CASE 5')
			# left < mid_l_r < right
			if [top, left, front, bottom, mid_l_r, back] not in intercept :
				q.append([top, bottom, left, mid_l_r, front, back ])
			if [top, mid_l_r, front, bottom, right, back] not in intercept :
				q.append([top, bottom, mid_l_r, right, front, back ])
			continue
			
			
		if 3==5 and  (top == mid_t_bo < bottom and top + 1 == bottom and mid_t_bo + 1 == bottom ) and ( left == mid_l_r < right and left + 1 == right and mid_l_r + 1 == right ) and front < mid_f_ba < back :  
			                  #
			#print('CASE 6')
			# front < mid_f_ba < back
			if [top, left, front, bottom, right, mid_f_ba] not in intercept :
				q.append([top, bottom, left, right, front, mid_f_ba ])
			if [top, left, mid_f_ba, bottom, right, back] not in intercept :
				q.append([top, bottom, left, right, mid_f_ba, back ])
			continue
			
	
		if top < mid_t_bo < bottom  and left < mid_l_r < right and front < mid_f_ba < back  :
	
			#if  top < mid_t_bo < bottom   or left < mid_l_r < right  or front < mid_f_ba < back :
		
			
			if [top, left, front, mid_t_bo, mid_l_r, mid_f_ba] not in intercept :
				q.append([top, mid_t_bo, left, mid_l_r, front, mid_f_ba ])
			if [top, left, mid_f_ba, mid_t_bo, mid_l_r, back] not in intercept :
				q.append([top, mid_t_bo, left, mid_l_r, mid_f_ba, back ])
			if [top, mid_l_r, front, mid_t_bo, right, mid_f_ba] not in intercept :
				q.append([top, mid_t_bo, mid_l_r, right, front, mid_f_ba ])
			if [top, mid_l_r, mid_f_ba, mid_t_bo, right, back] not in intercept :
				q.append([top, mid_t_bo, mid_l_r, right, mid_f_ba, back ])
			if [mid_t_bo, left, front, bottom, mid_l_r, mid_f_ba] not in intercept :
				q.append([mid_t_bo, bottom, left, mid_l_r, front, mid_f_ba ])
			if [mid_t_bo, left, mid_f_ba, bottom, mid_l_r, back] not in intercept :
				q.append([mid_t_bo, bottom, left, mid_l_r, mid_f_ba, back ])
			if [mid_t_bo, mid_l_r, front, bottom, right, mid_f_ba] not in intercept :
				q.append([mid_t_bo, bottom, mid_l_r, right, front, mid_f_ba ])
			if [mid_t_bo, mid_l_r, mid_f_ba, bottom, right, back] not in intercept :
				q.append([mid_t_bo, bottom, mid_l_r, right, mid_f_ba, back ])
				
				#continue
	
	#print(intercept)
				#print(ans,'ANS', len(ans))
	return [self_mn__x ,  self_mn__y  , self_mn__z , self_mx__y , self_mx__x , self_mx__z ]   
			



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


#[[2, 2, 2], [9, 9, 9], [8, 8, 2], [2, 3, 7], [8, 2, 2], [1, 9, 9], [7, 3, 7], [2, 8, 2]]
"""
if [top, left, front, bottom, right, mid_f_ba] not in intercept :
	q.append([top, bottom, left, right, front, mid_f_ba ])     
if [top, left, mid_f_ba, bottom, right, back] not in intercept :
	q.append([top, bottom, left, right, mid_f_ba, back ])     
if [top, left, front, bottom, mid_l_r, back] not in intercept :
	q.append([top, bottom, left, mid_l_r, front, back ])     
if [top, left, front, bottom, mid_l_r, mid_f_ba] not in intercept :
	q.append([top, bottom, left, mid_l_r, front, mid_f_ba ])     
if [top, left, mid_f_ba, bottom, mid_l_r, back] not in intercept :
	q.append([top, bottom, left, mid_l_r, mid_f_ba, back ])     
if [top, mid_l_r, front, bottom, right, back] not in intercept :
	q.append([top, bottom, mid_l_r, right, front, back ])     
if [top, mid_l_r, front, bottom, right, mid_f_ba] not in intercept :
	q.append([top, bottom, mid_l_r, right, front, mid_f_ba ])     
if [top, mid_l_r, mid_f_ba, bottom, right, back] not in intercept :
	q.append([top, bottom, mid_l_r, right, mid_f_ba, back ])     
if [top, left, front, mid_t_bo, right, back] not in intercept :
	q.append([top, mid_t_bo, left, right, front, back ])     
if [top, left, front, mid_t_bo, right, mid_f_ba] not in intercept :
	q.append([top, mid_t_bo, left, right, front, mid_f_ba ])    
if [top, left, mid_f_ba, mid_t_bo, right, back] not in intercept :
	q.append([top, mid_t_bo, left, right, mid_f_ba, back ])    
if [top, left, front, mid_t_bo, mid_l_r, back] not in intercept :
	q.append([top, mid_t_bo, left, mid_l_r, front, back ])    
if [top, left, front, mid_t_bo, mid_l_r, mid_f_ba] not in intercept :
	q.append([top, mid_t_bo, left, mid_l_r, front, mid_f_ba ])     
if [top, left, mid_f_ba, mid_t_bo, mid_l_r, back] not in intercept :
	q.append([top, mid_t_bo, left, mid_l_r, mid_f_ba, back ])     
if [top, mid_l_r, front, mid_t_bo, right, back] not in intercept :
	q.append([top, mid_t_bo, mid_l_r, right, front, back ])     
if [top, mid_l_r, front, mid_t_bo, right, mid_f_ba] not in intercept :
	q.append([top, mid_t_bo, mid_l_r, right, front, mid_f_ba ])     
if [top, mid_l_r, mid_f_ba, mid_t_bo, right, back] not in intercept :
	q.append([top, mid_t_bo, mid_l_r, right, mid_f_ba, back ])     
if [mid_t_bo, left, front, bottom, right, back] not in intercept :
	q.append([mid_t_bo, bottom, left, right, front, back ])     
if [mid_t_bo, left, front, bottom, right, mid_f_ba] not in intercept :
	q.append([mid_t_bo, bottom, left, right, front, mid_f_ba ])     
if [mid_t_bo, left, mid_f_ba, bottom, right, back] not in intercept :
	q.append([mid_t_bo, bottom, left, right, mid_f_ba, back ])     
if [mid_t_bo, left, front, bottom, mid_l_r, back] not in intercept :
	q.append([mid_t_bo, bottom, left, mid_l_r, front, back ])     
if [mid_t_bo, left, front, bottom, mid_l_r, mid_f_ba] not in intercept :
	q.append([mid_t_bo, bottom, left, mid_l_r, front, mid_f_ba ])     
if [mid_t_bo, left, mid_f_ba, bottom, mid_l_r, back] not in intercept :
	q.append([mid_t_bo, bottom, left, mid_l_r, mid_f_ba, back ])     
if [mid_t_bo, mid_l_r, front, bottom, right, back] not in intercept :
	q.append([mid_t_bo, bottom, mid_l_r, right, front, back ])     
if [mid_t_bo, mid_l_r, front, bottom, right, mid_f_ba] not in intercept :
	q.append([mid_t_bo, bottom, mid_l_r, right, front, mid_f_ba ])     
if [mid_t_bo, mid_l_r, mid_f_ba, bottom, right, back] not in intercept :
	q.append([mid_t_bo, bottom, mid_l_r, right, mid_f_ba, back ])



# works as well but slow
"""