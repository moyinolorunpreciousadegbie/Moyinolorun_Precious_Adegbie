#!/usr/bin/env python3

#!/usr/bin/env python3 2744

def fn( y1, y2, yy1, yy2):
	if y2 > yy2 and yy1 > y1 :
		return yy2 - yy1
	
	if yy2 > y2 and y1 > yy1 :
		return y2 - y1
	
	
	
	if y2 > yy2 and yy2 > y1  and y1 > yy1 :
		return yy2 - y1
	if yy2 > y2 and y2 > yy1  and yy1 > y1 :
		return y2 - yy1
	
	
	
	
	
	if y2 > yy2 and y1 == yy1 :
		return yy2 - yy1
	if yy2 > y2 and y1 == yy1 :
		return y2 - y1
	
	
	if y2 == yy2  and y1 > yy1 :
		return y2 - y1 
	if y2 == yy2  and yy1 > y1 :
		return yy2 - yy1
	
	
	
	if y2 == yy2  and yy1 == y1 :
		return y2 - y1 # yy2 - yy1
	
	
	if y1 >  yy2:   # NO AREA SHARED
		return 0
	if yy1 > y2:
		return 0

	return 0
	
#!/usr/bin/env python3

class SegmentTree:
	def __init__(self):
		
		
		self.intercept = []
		self.cc = 0
		self.MIDS = []
		
	def  query( self, top, bottom,    left, right,  front, back, lis_range ) :
		# query(  [mn , mx] , lis_range ) :
		
		#if  (top ==   bottom  ) and ( left ==  right ) and ( front == back ): return
		
		#if [top,left,front , bottom, right, back]  == [4,4,4,  5,5,5] : print('JOY')
		
		
		
		
		
		
		
		mid_t_bo = (top + bottom) // 2    ######
		
		                               ######
		
		
		                               #   #
		mid_l_r = (left + right) // 2  #   #
		
		
		
		
		mid_f_ba = (front + back) // 2 
		
		
		
		
		#mid_t_bo = top + ( (bottom - top) // 2 )
		#mid_l_r = left + ( (right - left) // 2 )
		#mid_f_ba = front + ( (back - front) // 2 )
		
########################################################################################################################################################		
		if [top,left,front , bottom, right, back]  in self.intercept  :  return
		#if [top,mid_t_bo,bottom,     left,mid_l_r,right,   front,mid_f_ba,back] in self.MIDS : return
		#if [mid_t_bo  ,  mid_l_r    ,   mid_f_ba] in self.MIDS : return
		
		#self.MIDS.append( [top,mid_t_bo,bottom,     left,mid_l_r,right,   front,mid_f_ba,back]  )
		##############################
		cn  = 0 
		for  qtop, qleft ,   qfront      ,   qbottom, qright ,   qback in lis_range:
			if (qbottom <= top or bottom <= qtop or top >= bottom) or (qright <= left or right <= qleft or left >= right) or (qback<=front or back <=qfront or front>=back ):                                                                                        
				#  0                  0                              123 qright     123 right                                 0                  0 
				#  1 qbottom          1 bottom                     left 456      qleft 456                                    1 qback            1 back 
				#            2 top             2 qtop      																	         2 front           2 qfront
				#            3 				   3 																				     3 				   3
				
				
				return
			if ( qtop <= top and bottom <= qbottom ) and   ( qleft <= left and right <= qright ) and  ( qfront <= front and back <= qback ): # FITS ONE THEN COUNT ++
			# FULLY IN ^^^^^^
			
			#if fn(top , bottom , qtop , qbottom )  and fn( left , right, qleft , qright, )  and fn( front , back , qfront , qback ) :
				cn += 1
			
			#if cn == 2 : # FITS ALL
				if [top,left,front , bottom, right, back] not in self.intercept : self.intercept.append([top,left,front , bottom, right, back ])
		##############################
			
			
			
			
			
			
			
			
			
			
			
			
			
		if  (top == mid_t_bo < bottom and top + 1 == bottom and mid_t_bo + 1 == bottom ) and ( left == mid_l_r < right and left + 1 == right and mid_l_r + 1 == right ) and ( front == mid_f_ba < back and front + 1 == back and mid_f_ba + 1 == back ): 
			#print('MMMM')
			
			return
		
		
		
		if  (top < mid_t_bo == bottom and top == mid_t_bo - 1  and top  == bottom - 1  ) and ( left < mid_l_r == right and left == mid_l_r - 1 and         left == right - 1 ) and ( front < mid_f_ba == back and front == mid_f_ba - 1 and front == back - 1 ): 
			#print('NNNN')
			return
		
		
		
		
		
		
		cm = 0
		
		# t l f
		# * 
		if (top == mid_t_bo < bottom and top + 1 == bottom and mid_t_bo + 1 == bottom )  and left < mid_l_r < right  and front < mid_f_ba < back : # X
			if [mid_t_bo  ,  mid_l_r    ,   mid_f_ba] in self.MIDS : return
			if [mid_t_bo  ,  mid_l_r    ,   mid_f_ba] not in self.MIDS :
			#if [top,mid_t_bo,bottom,     left,mid_l_r,right,   front,mid_f_ba,back] not in self.MIDS :
				#self.MIDS.append([top,mid_t_bo,bottom,     left,mid_l_r,right,   front,mid_f_ba,back])
				
				top, bottom,left, right, front, back = lis_range[0][0], lis_range[0][3] , lis_range[0][1],lis_range[0][4] ,lis_range[0][2] , lis_range[0][5] 
				#_, _,left, right, front, back = lis_range[0][0], lis_range[0][3] , lis_range[0][1], lis_range[0][4] , lis_range[0][2] , lis_range[0][5]
				#top, bottom = lis_range[0][0], lis_range[0][3]      # , lis_range[0][1],lis_range[0][4] ,        lis_range[0][2] , lis_range[0][5]
				
				
			# new  mid_t_bo    mid_l_r       mid_f_ba
				#self.MIDS.append([top,mid_t_bo,bottom,     left,mid_l_r,right,   front,mid_f_ba,back])
				#self.MIDS.append([top,mid_t_bo+1,bottom,     left,mid_l_r+1,right,   front,mid_f_ba+1,back]) 
				self.MIDS.append([mid_t_bo  ,  mid_l_r    ,   mid_f_ba])
				#self.MIDS.append([mid_t_bo +1 ,  mid_l_r +1   ,   mid_f_ba+1])
			cm += 1
			pass
		
		
		
		
	
	
	
		# t l f
		# 	* 
		if  ( left == mid_l_r < right and left + 1 == right and mid_l_r + 1 == right )  and top < mid_t_bo < bottom  and front < mid_f_ba < back : # X
			if [mid_t_bo  ,  mid_l_r    ,   mid_f_ba] in self.MIDS : return
			if [mid_t_bo  ,  mid_l_r    ,   mid_f_ba] not in self.MIDS :
			#if [top,mid_t_bo,bottom,     left,mid_l_r,right,   front,mid_f_ba,back] not in self.MIDS :
				#self.MIDS.append([top,mid_t_bo,bottom,     left,mid_l_r,right,   front,mid_f_ba,back])
				
				
				top, bottom,left, right, front, back = lis_range[0][0], lis_range[0][3], lis_range[0][1], lis_range[0][4] , lis_range[0][2] , lis_range[0][5] 
				#top, bottom,_, _, front, back = lis_range[0][0], lis_range[0][3] , lis_range[0][1], lis_range[0][4] , lis_range[0][2] , lis_range[0][5]
				#left, right =  lis_range[0][1],lis_range[0][4]  #,        lis_range[0][2] , lis_range[0][5]
				
			# new  mid_t_bo    mid_l_r       mid_f_ba
				#self.MIDS.append([top,mid_t_bo,bottom,     left,mid_l_r,right,   front,mid_f_ba,back])
				#self.MIDS.append([top,mid_t_bo+1,bottom,     left,mid_l_r+1,right,   front,mid_f_ba+1,back]) 
				self.MIDS.append([mid_t_bo  ,  mid_l_r    ,   mid_f_ba])
				#self.MIDS.append([mid_t_bo +1 ,  mid_l_r +1   ,   mid_f_ba+1])
			cm += 1
			pass
			
		
	
	
		# t l f
		#     * 
		if ( front == mid_f_ba < back and front + 1 == back and mid_f_ba + 1 == back )  and top < mid_t_bo < bottom and left < mid_l_r < right  : # X
			if [mid_t_bo  ,  mid_l_r    ,   mid_f_ba] in self.MIDS : return
			if [mid_t_bo  ,  mid_l_r    ,   mid_f_ba] not in self.MIDS :
			#if [top,mid_t_bo,bottom,     left,mid_l_r,right,   front,mid_f_ba,back] not in self.MIDS :
				#self.MIDS.append([top,mid_t_bo,bottom,     left,mid_l_r,right,   front,mid_f_ba,back])
				
				
				top, bottom,left, right, front, back = lis_range[0][0], lis_range[0][3] , lis_range[0][1], lis_range[0][4] , lis_range[0][2] , lis_range[0][5]
				#top, bottom,left, right, _, _ = lis_range[0][0], lis_range[0][3] , lis_range[0][1], lis_range[0][4] , lis_range[0][2] , lis_range[0][5]
				#front, back =  lis_range[0][2] , lis_range[0][5]
				
				
			# new  mid_t_bo    mid_l_r       mid_f_ba
				#self.MIDS.append([top,mid_t_bo,bottom,     left,mid_l_r,right,   front,mid_f_ba,back])
				#self.MIDS.append([top,mid_t_bo+1,bottom,     left,mid_l_r+1,right,   front,mid_f_ba+1,back]) 
				self.MIDS.append([mid_t_bo  ,  mid_l_r    ,   mid_f_ba])
				#self.MIDS.append([mid_t_bo +1 ,  mid_l_r +1   ,   mid_f_ba+1]) 
				
			cm += 1
			
			pass
	
		
	########################################################################################################################################################	
		
		# t l f
		# * *
		if (top == mid_t_bo < bottom and top + 1 == bottom and mid_t_bo + 1 == bottom )  and  ( left == mid_l_r < right and left + 1 == right and mid_l_r + 1 == right )  and front < mid_f_ba < back : # X
			if [mid_t_bo  ,  mid_l_r    ,   mid_f_ba] in self.MIDS : return
			if [mid_t_bo  ,  mid_l_r    ,   mid_f_ba] not in self.MIDS :
			#if [top,mid_t_bo,bottom,     left,mid_l_r,right,   front,mid_f_ba,back] not in self.MIDS :
				#self.MIDS.append([top,mid_t_bo,bottom,     left,mid_l_r,right,   front,mid_f_ba,back])
				
				#top, bottom,left, right, front, back = lis_range[0][0],lis_range[0][3] , lis_range[0][1], lis_range[0][4] , lis_range[0][2] , lis_range[0][5] 
				#_, _,_, _, front, back = lis_range[0][0], lis_range[0][3] , lis_range[0][1], lis_range[0][4] , lis_range[0][2] , lis_range[0][5] 
				top, bottom,      left, right = lis_range[0][0],lis_range[0][3] ,            lis_range[0][1], lis_range[0][4]  
				
			# new  mid_t_bo    mid_l_r       mid_f_ba
				#self.MIDS.append([top,mid_t_bo,bottom,     left,mid_l_r,right,   front,mid_f_ba,back])
				#self.MIDS.append([top,mid_t_bo+1,bottom,     left,mid_l_r+1,right,   front,mid_f_ba+1,back]) 
				self.MIDS.append([mid_t_bo  ,  mid_l_r    ,   mid_f_ba])
				#self.MIDS.append([mid_t_bo +1 ,  mid_l_r +1   ,   mid_f_ba+1])
			cm += 1
			pass
		
		
		
		# t l f
		# *   *
		if  (top == mid_t_bo < bottom and top + 1 == bottom and mid_t_bo + 1 == bottom ) and left < mid_l_r < right   and ( front == mid_f_ba < back and front + 1 == back and mid_f_ba + 1 == back )  : # X
			if [mid_t_bo  ,  mid_l_r    ,   mid_f_ba] in self.MIDS : return
			if [mid_t_bo  ,  mid_l_r    ,   mid_f_ba] not in self.MIDS :
			#if [top,mid_t_bo,bottom,     left,mid_l_r,right,   front,mid_f_ba,back] not in self.MIDS :
				#self.MIDS.append([top,mid_t_bo,bottom,     left,mid_l_r,right,   front,mid_f_ba,back])
				
				#top, bottom,left, right, front, back = lis_range[0][0], lis_range[0][3], lis_range[0][1], lis_range[0][4] , lis_range[0][2] , lis_range[0][5] 
				#_, _,left, right, _, _ = lis_range[0][0], lis_range[0][3] , lis_range[0][1], lis_range[0][4] , lis_range[0][2] , lis_range[0][5]
				top, bottom,       front, back = lis_range[0][0], lis_range[0][3],           lis_range[0][2] , lis_range[0][5] 
				
				
			# new  mid_t_bo    mid_l_r       mid_f_ba
				#self.MIDS.append([top,mid_t_bo,bottom,     left,mid_l_r,right,   front,mid_f_ba,back])
				#self.MIDS.append([top,mid_t_bo+1,bottom,     left,mid_l_r+1,right,   front,mid_f_ba+1,back]) 
				self.MIDS.append([mid_t_bo  ,  mid_l_r    ,   mid_f_ba])
				#self.MIDS.append([mid_t_bo +1 ,  mid_l_r +1   ,   mid_f_ba+1])
			cm += 1
			pass
		
		
	
		# t l f
		#   * *
		if top < mid_t_bo < bottom and ( left == mid_l_r < right and left + 1 == right and mid_l_r + 1 == right ) and ( front == mid_f_ba < back and front + 1 == back and mid_f_ba + 1 == back ) : # X
			if [mid_t_bo  ,  mid_l_r    ,   mid_f_ba] in self.MIDS : return
			if [mid_t_bo  ,  mid_l_r    ,   mid_f_ba] not in self.MIDS :
			#if [top,mid_t_bo,bottom,     left,mid_l_r,right,   front,mid_f_ba,back] not in self.MIDS :
				#self.MIDS.append([top,mid_t_bo,bottom,     left,mid_l_r,right,   front,mid_f_ba,back])
				
				
				#top, bottom,left, right, front, back = lis_range[0][0],lis_range[0][3] , lis_range[0][1], lis_range[0][4] , lis_range[0][2] , lis_range[0][5] 
				#top, bottom,_, _, _, _ = lis_range[0][0], lis_range[0][3] , lis_range[0][1], lis_range[0][4] , lis_range[0][2] , lis_range[0][5] 
				left, right,        front, back =  lis_range[0][1], lis_range[0][4] ,             lis_range[0][2] , lis_range[0][5] 
				
				
			# new  mid_t_bo    mid_l_r       mid_f_ba
				#self.MIDS.append([top,mid_t_bo,bottom,     left,mid_l_r,right,   front,mid_f_ba,back])
				#self.MIDS.append([top,mid_t_bo+1,bottom,     left,mid_l_r+1,right,   front,mid_f_ba+1,back]) 
				self.MIDS.append([mid_t_bo  ,  mid_l_r    ,   mid_f_ba])
				#self.MIDS.append([mid_t_bo +1 ,  mid_l_r +1   ,   mid_f_ba+1]) 
				
				
			cm += 1
		
			pass
		
		
		#mid_t_bo = (top + bottom) // 2    
		#mid_l_r = (left + right) // 2  
		#mid_f_ba = (front + back) // 2 
		
		
		
		
		
		if top < mid_t_bo < bottom   and left < mid_l_r < right  and front < mid_f_ba < back :
		#if  top <= mid_t_bo < bottom   and left <= mid_l_r < right  and front <= mid_f_ba < back :
			#self.query( top, mid_t_bo,    left, right, front, back ,  lis_range )
			#self.query( mid_t_bo, bottom, left, right, front, back ,  lis_range )
			
			if [ top , left , front ,  bottom ,  right ,  mid_f_ba  ] not in self.intercept :
				self.query( top, bottom, left, right, front, mid_f_ba ,  lis_range  )
				
			if [ top , left , mid_f_ba ,  bottom ,  right ,  back  ] not in self.intercept :
				self.query( top, bottom, left, right, mid_f_ba, back ,  lis_range  )
				
			if [ top , left , front ,  bottom ,  mid_l_r ,  back  ] not in self.intercept :
				self.query( top, bottom, left, mid_l_r, front, back ,  lis_range  )
				
			if [ top , left , front ,  bottom ,  mid_l_r ,  mid_f_ba  ] not in self.intercept :
				self.query( top, bottom, left, mid_l_r, front, mid_f_ba ,  lis_range  )
				
			if [ top , left , mid_f_ba ,  bottom ,  mid_l_r ,  back  ] not in self.intercept :
				self.query( top, bottom, left, mid_l_r, mid_f_ba, back ,  lis_range  )
				
			if [ top , mid_l_r , front ,  bottom ,  right ,  back  ] not in self.intercept :
				self.query( top, bottom, mid_l_r, right, front, back ,  lis_range  )
				
			if [ top , mid_l_r , front ,  bottom ,  right ,  mid_f_ba  ] not in self.intercept :
				self.query( top, bottom, mid_l_r, right, front, mid_f_ba ,  lis_range  )
				
			if [ top , mid_l_r , mid_f_ba ,  bottom ,  right ,  back  ] not in self.intercept :
				self.query( top, bottom, mid_l_r, right, mid_f_ba, back ,  lis_range  )
				
			if [ top , left , front ,  mid_t_bo ,  right ,  back  ] not in self.intercept :
				self.query( top, mid_t_bo, left, right, front, back ,  lis_range  )
				
			if [ top , left , front ,  mid_t_bo ,  right ,  mid_f_ba  ] not in self.intercept :
				self.query( top, mid_t_bo, left, right, front, mid_f_ba ,  lis_range  )
				
			if [ top , left , mid_f_ba ,  mid_t_bo ,  right ,  back  ] not in self.intercept :
				self.query( top, mid_t_bo, left, right, mid_f_ba, back ,  lis_range  )
				
			if [ top , left , front ,  mid_t_bo ,  mid_l_r ,  back  ] not in self.intercept :
				self.query( top, mid_t_bo, left, mid_l_r, front, back ,  lis_range  )
				
			if [ top , left , front ,  mid_t_bo ,  mid_l_r ,  mid_f_ba  ] not in self.intercept :
				self.query( top, mid_t_bo, left, mid_l_r, front, mid_f_ba ,  lis_range  )
				
			if [ top , left , mid_f_ba ,  mid_t_bo ,  mid_l_r ,  back  ] not in self.intercept :
				self.query( top, mid_t_bo, left, mid_l_r, mid_f_ba, back ,  lis_range  )
				
			if [ top , mid_l_r , front ,  mid_t_bo ,  right ,  back  ] not in self.intercept :
				self.query( top, mid_t_bo, mid_l_r, right, front, back ,  lis_range  )
				
			if [ top , mid_l_r , front ,  mid_t_bo ,  right ,  mid_f_ba  ] not in self.intercept :
				self.query( top, mid_t_bo, mid_l_r, right, front, mid_f_ba ,  lis_range  )
				
			if [ top , mid_l_r , mid_f_ba ,  mid_t_bo ,  right ,  back  ] not in self.intercept :
				self.query( top, mid_t_bo, mid_l_r, right, mid_f_ba, back ,  lis_range  )
				
			if [ mid_t_bo , left , front ,  bottom ,  right ,  back  ] not in self.intercept :
				self.query( mid_t_bo, bottom, left, right, front, back ,  lis_range  )
				
			if [ mid_t_bo , left , front ,  bottom ,  right ,  mid_f_ba  ] not in self.intercept :
				self.query( mid_t_bo, bottom, left, right, front, mid_f_ba ,  lis_range  )
				
			if [ mid_t_bo , left , mid_f_ba ,  bottom ,  right ,  back  ] not in self.intercept :
				self.query( mid_t_bo, bottom, left, right, mid_f_ba, back ,  lis_range  )
				
			if [ mid_t_bo , left , front ,  bottom ,  mid_l_r ,  back  ] not in self.intercept :
				self.query( mid_t_bo, bottom, left, mid_l_r, front, back ,  lis_range  )
				
			if [ mid_t_bo , left , front ,  bottom ,  mid_l_r ,  mid_f_ba  ] not in self.intercept :
				self.query( mid_t_bo, bottom, left, mid_l_r, front, mid_f_ba ,  lis_range  )
				
			if [ mid_t_bo , left , mid_f_ba ,  bottom ,  mid_l_r ,  back  ] not in self.intercept :
				self.query( mid_t_bo, bottom, left, mid_l_r, mid_f_ba, back ,  lis_range  )
				
			if [ mid_t_bo , mid_l_r , front ,  bottom ,  right ,  back  ] not in self.intercept :
				self.query( mid_t_bo, bottom, mid_l_r, right, front, back ,  lis_range  )
				
			if [ mid_t_bo , mid_l_r , front ,  bottom ,  right ,  mid_f_ba  ] not in self.intercept :
				self.query( mid_t_bo, bottom, mid_l_r, right, front, mid_f_ba ,  lis_range  )
				
			if [ mid_t_bo , mid_l_r , mid_f_ba ,  bottom ,  right ,  back  ] not in self.intercept :
				self.query( mid_t_bo, bottom, mid_l_r, right, mid_f_ba, back ,  lis_range  )
				
				
				
				
			#if top < mid_t_bo < bottom   and ( left == mid_l_r < right and left + 1 == right and mid_l_r + 1 == right ) and ( front == mid_f_ba < back and front + 1 == back and mid_f_ba + 1 == back ) :
			#self.query( top, mid_t_bo,    left, right, front, back ,  lis_range )
			#self.query( mid_t_bo, bottom, left, right, front, back ,  lis_range )
				
				
				
				
				
				
				
		mid_t_bo +=1 
		
		
		
		
		
		mid_l_r +=1 
		
		
		
		
		mid_f_ba +=1
		
		##########
		#########
		########
		#self.MIDS.append([top,mid_t_bo+1,bottom,     left,mid_l_r+1,right,   front,mid_f_ba+1,back]) 
		
		#return
		if  top < mid_t_bo < bottom   and left < mid_l_r < right  and front < mid_f_ba < back  :#and cm == 0 :
		#if  top < mid_t_bo <= bottom   and left < mid_l_r <= right  and front < mid_f_ba <= back  :
			#self.query( top, mid_t_bo,    left, right, front, back ,  lis_range )
			#self.query( mid_t_bo, bottom, left, right, front, back ,  lis_range )
			
			if [ top , left , front ,  bottom ,  right ,  mid_f_ba  ] not in self.intercept :
				self.query( top, bottom, left, right, front, mid_f_ba ,  lis_range  )
				
			if [ top , left , mid_f_ba ,  bottom ,  right ,  back  ] not in self.intercept :
				self.query( top, bottom, left, right, mid_f_ba, back ,  lis_range  )
				
			if [ top , left , front ,  bottom ,  mid_l_r ,  back  ] not in self.intercept :
				self.query( top, bottom, left, mid_l_r, front, back ,  lis_range  )
				
			if [ top , left , front ,  bottom ,  mid_l_r ,  mid_f_ba  ] not in self.intercept :
				self.query( top, bottom, left, mid_l_r, front, mid_f_ba ,  lis_range  )
				
			if [ top , left , mid_f_ba ,  bottom ,  mid_l_r ,  back  ] not in self.intercept :
				self.query( top, bottom, left, mid_l_r, mid_f_ba, back ,  lis_range  )
				
			if [ top , mid_l_r , front ,  bottom ,  right ,  back  ] not in self.intercept :
				self.query( top, bottom, mid_l_r, right, front, back ,  lis_range  )
				
			if [ top , mid_l_r , front ,  bottom ,  right ,  mid_f_ba  ] not in self.intercept :
				self.query( top, bottom, mid_l_r, right, front, mid_f_ba ,  lis_range  )
				
			if [ top , mid_l_r , mid_f_ba ,  bottom ,  right ,  back  ] not in self.intercept :
				self.query( top, bottom, mid_l_r, right, mid_f_ba, back ,  lis_range  )
				
			if [ top , left , front ,  mid_t_bo ,  right ,  back  ] not in self.intercept :
				self.query( top, mid_t_bo, left, right, front, back ,  lis_range  )
				
			if [ top , left , front ,  mid_t_bo ,  right ,  mid_f_ba  ] not in self.intercept :
				self.query( top, mid_t_bo, left, right, front, mid_f_ba ,  lis_range  )
				
			if [ top , left , mid_f_ba ,  mid_t_bo ,  right ,  back  ] not in self.intercept :
				self.query( top, mid_t_bo, left, right, mid_f_ba, back ,  lis_range  )
				
			if [ top , left , front ,  mid_t_bo ,  mid_l_r ,  back  ] not in self.intercept :
				self.query( top, mid_t_bo, left, mid_l_r, front, back ,  lis_range  )
				
			if [ top , left , front ,  mid_t_bo ,  mid_l_r ,  mid_f_ba  ] not in self.intercept :
				self.query( top, mid_t_bo, left, mid_l_r, front, mid_f_ba ,  lis_range  )
				
			if [ top , left , mid_f_ba ,  mid_t_bo ,  mid_l_r ,  back  ] not in self.intercept :
				self.query( top, mid_t_bo, left, mid_l_r, mid_f_ba, back ,  lis_range  )
				
			if [ top , mid_l_r , front ,  mid_t_bo ,  right ,  back  ] not in self.intercept :
				self.query( top, mid_t_bo, mid_l_r, right, front, back ,  lis_range  )
				
			if [ top , mid_l_r , front ,  mid_t_bo ,  right ,  mid_f_ba  ] not in self.intercept :
				self.query( top, mid_t_bo, mid_l_r, right, front, mid_f_ba ,  lis_range  )
				
			if [ top , mid_l_r , mid_f_ba ,  mid_t_bo ,  right ,  back  ] not in self.intercept :
				self.query( top, mid_t_bo, mid_l_r, right, mid_f_ba, back ,  lis_range  )
				
			if [ mid_t_bo , left , front ,  bottom ,  right ,  back  ] not in self.intercept :
				self.query( mid_t_bo, bottom, left, right, front, back ,  lis_range  )
				
			if [ mid_t_bo , left , front ,  bottom ,  right ,  mid_f_ba  ] not in self.intercept :
				self.query( mid_t_bo, bottom, left, right, front, mid_f_ba ,  lis_range  )
				
			if [ mid_t_bo , left , mid_f_ba ,  bottom ,  right ,  back  ] not in self.intercept :
				self.query( mid_t_bo, bottom, left, right, mid_f_ba, back ,  lis_range  )
				
			if [ mid_t_bo , left , front ,  bottom ,  mid_l_r ,  back  ] not in self.intercept :
				self.query( mid_t_bo, bottom, left, mid_l_r, front, back ,  lis_range  )
				
			if [ mid_t_bo , left , front ,  bottom ,  mid_l_r ,  mid_f_ba  ] not in self.intercept :
				self.query( mid_t_bo, bottom, left, mid_l_r, front, mid_f_ba ,  lis_range  )
				
			if [ mid_t_bo , left , mid_f_ba ,  bottom ,  mid_l_r ,  back  ] not in self.intercept :
				self.query( mid_t_bo, bottom, left, mid_l_r, mid_f_ba, back ,  lis_range  )
				
			if [ mid_t_bo , mid_l_r , front ,  bottom ,  right ,  back  ] not in self.intercept :
				self.query( mid_t_bo, bottom, mid_l_r, right, front, back ,  lis_range  )
				
			if [ mid_t_bo , mid_l_r , front ,  bottom ,  right ,  mid_f_ba  ] not in self.intercept :
				self.query( mid_t_bo, bottom, mid_l_r, right, front, mid_f_ba ,  lis_range  )
				
			if [ mid_t_bo , mid_l_r , mid_f_ba ,  bottom ,  right ,  back  ] not in self.intercept :
				self.query( mid_t_bo, bottom, mid_l_r, right, mid_f_ba, back ,  lis_range  )
				
			return
		return
	
	
			#if top < mid_t_bo < bottom   and ( left == mid_l_r < right and left + 1 == right and mid_l_r + 1 == right ) and ( front == mid_f_ba < back and front + 1 == back and mid_f_ba + 1 == back ) :
			#self.query( top, mid_t_bo,    left, right, front, back ,  lis_range )
			#self.query( mid_t_bo, bottom, left, right, front, back ,  lis_range )
	
	
	
def lengthOfLIS( lis_range ) :
	
	rangg = []
	mn_x = float('inf')
	mx_x = -float('inf')
	
	mn_y = float('inf')
	mx_y = -float('inf')
	
	mn_z = float('inf')
	mx_z = -float('inf')
	
	#for y , x, z, y2, x2, z2 in lis_range:
		#mn_y = min(mn_y, y)
		#mx_y = max(mx_y, y2)
	
	
		#mn_x = min(mn_x, x)
		#mx_x = max(mx_x, x2)
	
		#mn_z = min(mn_z, z)
		#mx_z = max(mx_z, z2)
	
	segmentTree = SegmentTree()
	
	# [0,0,0,  5, 5, 5]
	#  t l f   bo r  ba
	#  0 1 2   3  4  5
	
	top, bottom,    left, right,  front, back = lis_range[0] , lis_range[3] ,  lis_range[1] , lis_range[4] , lis_range[2] , lis_range[5] 
	
	#top, bottom,    left, right,  front, back = mn_y , mx_y ,  mn_x , mx_x  , mn_z , mx_z 
	
	#lis_range = [top,left,front,   bottom+1,right+1,back+1 ]
	#segmentTree.query( top, bottom,    left, right,  front, back, lis_range ) 
	segmentTree.query( top, bottom,    left, right,  front, back, [lis_range] ) 
	#segmentTree.query( top, bottom+1,    left, right+1,  front, back+1, [lis_range] ) 
	#print(segmentTree.MIDS )
	return segmentTree.intercept  , len(segmentTree.intercept ) #  max(segmentTree.intercept)  -  min(segmentTree.intercept) 
L = [
#[0,0,0,  9,9,9],   ###########
	
[3,3,3,  6,6,6],      #3456
[4,4,4,  7,7,7],      # 4567
[4,4,4,  6,6,6],      # 456
[3,3,3,  7,7,7],      #34567 <<<<<<<<<
[0,0,0,  7,7,7],   #01234567
[3,3,3,  9,9,9],      #3456789
]

#print( lengthOfLIS( L )   )

x,y,z = [5]*3  # 5-6 LIMIT !!!
print( lengthOfLIS( [0,0,0,  x,y,z] )   )

#  01  1             1 x 1 x 1 =  1
#



#  01 02  2 3      3 x 3 x 3 =   27
#  12     1 1


# 01 02 03  3   6       6 x 6 x 6 = 216   
# 12 13     2   3
# 23        1   1


# 01 02 03 04 4   10      10 x 10 x 10 = 1000   
# 12 13 14    3   6
# 23 24       2   3
# 34          1   1


# 01 02 03 04 05  5   15        15 x 15 x 15   = 3375
# 12 13 14 15     4   10        x    y    z
# 23 24 25        3   6
# 34 35           2   3
# 45              1   1
#                 


# 01 02 03 04 05 06  6   21        21 x 21 x 21   = 9261
# 12 13 14 15 16     5   15        x    y    z
# 23 24 25 26        4   10
# 34 35 36           3   6
# 45 46              2   2
# 56                 1   1

"""




if y2  ==  len(xyz[z2] )  :
	
	if z2 +1  ==  len(xyz )  :
		####################################################
		####################################################^^^^^^^^^^^^
		#t_dim = [[]for i  in range(len(xyz[z2] ))]				
		#print('fffffffff', z2, MAT[-1],xyz[z2], t_dim)
		#MAT.append( t_dim )
		MAT.append( dim )
		return 
	#print("____________________________________")
	MAT.append( dim )
	dim =  [[]for i  in range(len(xyz[z2+1] ))]
	dim2 =  [[]for i  in range(len(xyz[z2+1] ))]
	dfs(cn ,xyz, dim    ,dim2 ,  MAT,   z,y,x, z1,y1,x1,   z2+1,0,0  )
	return






if  x2  ==  len(xyz[z2][y2] ) :  #and y2 +1 < len(xyz[z2] )  :#and  z2+1 <  len(xyz )   :

	dfs(cn ,xyz, dim ,dim2 ,  MAT,   z,y,x, z1,y1,x1,   z2,y2+1,0  )
	return

if z2  ==  len(xyz )  :

	return 		









print('left < mid_l_r < right  and front < mid_f_ba < back ')

o = [ ['top', ', ','bottom']   ,  ['top',', ','mid_t_bo'] , [ 'mid_t_bo',', ','bottom'] ]
oo = [                            [', left',', ','mid_l_r'] , [ ', mid_l_r',', ', 'right'] ]
ooo = [                          [', front',', ','mid_f_ba'],  [', mid_f_ba',', ','back'] ]

s =''

q = []
for i in o :
	for j in oo :
		for k in ooo :
			all = i + j + k
			f = 'self.query( ' 
			for a in all :
				f += a
				
			if f in q :
				continue
			if f not in q : q.append(f)
			print(f, ',  lis_range )')
			
print()
print("######################################################################################################################################################")
print()

print('top < mid_t_bo < bottom   and front < mid_f_ba < back')

o = [                                ['top',', ','mid_t_bo'] , [ 'mid_t_bo',', ','bottom'] ]
oo = [ [', left',', ','right']   ,   [', left',', ','mid_l_r'] , [ ', mid_l_r',', ', 'right'] ]
ooo = [                             [', front',', ','mid_f_ba'],  [', mid_f_ba',', ','back'] ]

s =''

q = []
for i in o :
	for j in oo :
		for k in ooo :
			all = i + j + k
			f = 'self.query( ' 
			for a in all :
				f += a
				
			if f in q :
				continue
			if f not in q : q.append(f)
			print(f, ',  lis_range )')
			
			
print()
print("######################################################################################################################################################")
print()
			
print('top < mid_t_bo < bottom   and left < mid_l_r < right ')
	
o = [                               ['top',', ','mid_t_bo'] , [ 'mid_t_bo',', ','bottom'] ]
oo = [ [', left',', ','right']   ,   [', left',', ','mid_l_r'] , [ ', mid_l_r',', ', 'right'] ]
ooo = [ [', front',', ','back']   ,  [', front',', ','mid_f_ba'],  [', mid_f_ba',', ','back'] ]

s =''

q = []
for i in o :
	for j in oo :
		for k in ooo :
			all = i + j + k
			f = 'self.query( ' 
			for a in all :
				f += a
				
			if f in q :
				continue
			if f not in q : q.append(f)
			print(f, ',  lis_range )')
			
			
print()
print("######################################################################################################################################################")
print()


#######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################



print('top < mid_t_bo < bottom ')

o = [                                ['top',', ','mid_t_bo'] , [ 'mid_t_bo',', ','bottom'] ]
oo = [ [', left',', ','right']   ,   [', left',', ','mid_l_r'] , [ ', mid_l_r',', ', 'right'] ]
ooo = [ [', front',', ','back']   ,  [', front',', ','mid_f_ba'],  [', mid_f_ba',', ','back'] ]

s =''

q = []
for i in o :
	for j in oo :
		for k in ooo :
			all = i + j + k
			f = 'self.query( ' 
			for a in all :
				f += a
				
			if f in q :
				continue
			if f not in q : q.append(f)
			print(f, ',  lis_range )')
	
print()
print("######################################################################################################################################################")
print()


print('left < mid_l_r < right')

o = [ ['top', ', ','bottom']   ,  ['top',', ','mid_t_bo'] , [ 'mid_t_bo',', ','bottom'] ]
oo = [                            [', left',', ','mid_l_r'] , [ ', mid_l_r',', ', 'right'] ]
ooo = [ [', front',', ','back']   ,  [', front',', ','mid_f_ba'],  [', mid_f_ba',', ','back'] ]

s =''

q = []
for i in o :
	for j in oo :
		for k in ooo :
			all = i + j + k
			f = 'self.query( ' 
			for a in all :
				f += a
				
			if f in q :
				continue
			if f not in q : q.append(f)
			print(f, ',  lis_range )')
			
print()
print("######################################################################################################################################################")
print()


print('front < mid_f_ba < back')


o = [ ['top', ', ','bottom']   ,  ['top',', ','mid_t_bo'] , [ 'mid_t_bo',', ','bottom'] ]
oo = [ [', left',', ','right']   ,   [', left',', ','mid_l_r'] , [ ', mid_l_r',', ', 'right'] ]
ooo = [                            [', front',', ','mid_f_ba'],  [', mid_f_ba',', ','back'] ]

s =''

q = []
for i in o :
	for j in oo :
		for k in ooo :
			all = i + j + k
			f = 'self.query( ' 
			for a in all :
				f += a
				
			if f in q :
				continue
			if f not in q : q.append(f)
			print(f, ',  lis_range )')
			

print()
print("######################################################################################################################################################")
print()

#   top < mid_t_bo < bottom   and left < mid_l_r < right  and front < mid_f_ba < back :
"""





#  <<<<<<<<







"""
# top, bottom,      top, mid_t_bo       mid_t_bo, bottom
# left, right       left, mid_l_r       mid_l_r, right
# front, back       front, mid_f_ba     mid_f_ba, back

#!/usr/bin/env python3

o = [ ['top', ', ','bottom']   ,  ['top',', ','mid_t_bo'] , [ 'mid_t_bo',', ','bottom'] ]
oo = [ [', left',', ','right']   ,   [', left',', ','mid_l_r'] , [ ', mid_l_r',', ', 'right'] ]
ooo = [ [', front',', ','back']   ,  [', front',', ','mid_f_ba'],  [', mid_f_ba',', ','back'] ]


_1 = [ ['top', ', ','bottom']   ,  ['top',', ','mid_t_bo'] , [ 'mid_t_bo',', ','bottom'] ]
_2 = [ [', left',', ','right']   ,   [', left',', ','mid_l_r'] , [ ', mid_l_r',', ', 'right'] ]
_3 = [ [', front',', ','back']   ,  [', front',', ','mid_f_ba'],  [', mid_f_ba',', ','back'] ]

s =''

q = []
for i in o :
	for j in oo :
		for k in ooo :
			all = i + j + k
			f = 'self.query( ' 
			ad = ''
			for a in all :
				f += a
				ad += a
				
			aded = [ all[0],all[3],all[6] ,', ',  all[2],', ',all[5],', ',all[8] 	 ]# ['top', ', ', 'bottom', ', left', ', ', 'right', ', front', ', ', 'back']
			if f in q :
				continue
			if f not in q : q.append(f)
			ade = ''
			for ja in aded :
				ade += ja
				ade += ' '
			print('if [',ade,'] not in self.intercept :')
			#print('self.intercept.append(',aded,')')
			print(f, ',  lis_range , temp )')  # self.query( top, bottom, left, right, front, mid_f_ba ,  lis_range )
			print()
			
			

			
			
q=( 'top', 'bottom', 'left', 'right', 'front', 'mid_f_ba' )
qq=( 'top', 'bottom', 'left', 'right', 'mid_f_ba', 'back'  )
	
s = ''
ss = ''

s +=   q[0] + ', ' + q[2] +', ' +q[4] +', '+  q[1]+', '+q[3]+', '+q[5] 	 
	
ss +=   qq[0] + ', ' + qq[2] +', ' +qq[4] +', '+  qq[1]+', '+qq[3]+', '+qq[5]  
	
print('if  [',s,'] not in self.intercept : ', )
print('if  [',ss,'] not in self.intercept : ', )
			
q=( 'top', 'bottom', 'left', 'mid_l_r',  'front', 'back'  ) # L  <<<<<< '
qq=( 'top', 'bottom', 'mid_l_r', 'right', 'front', 'back'  )



s = ''
ss = ''

s +=   q[0] + ', ' + q[2] +', ' +q[4] +', '+  q[1]+', '+q[3]+', '+q[5] 	 

ss +=   qq[0] + ', ' + qq[2] +', ' +qq[4] +', '+  qq[1]+', '+qq[3]+', '+qq[5]  

print('if  [',s,'] not in self.intercept : ', )
print('if  [',ss,'] not in self.intercept : ', )

#   top < mid_t_bo < bottom   and left < mid_l_r < right  and front < mid_f_ba < back :









#!/usr/bin/env python3






print('left < mid_l_r < right  and front < mid_f_ba < back ')

o = [   ['top', ', ','bottom']                                                                ]
oo = [                               [', left',', ','mid_l_r'] , [ ', mid_l_r',', ', 'right'] ]
ooo = [                             [', front',', ','mid_f_ba'],  [', mid_f_ba',', ','back'] ]

s =''

q = []
for i in o :
	for j in oo :
		for k in ooo :
			all = i + j + k
			f = 'self.query( ' 
			for a in all :
				f += a
				
			if f in q :
				continue
			if f not in q : q.append(f)
			print(f, ',  lis_range )')
			
print()
print("######################################################################################################################################################")
print()


print('top < mid_t_bo < bottom   and front < mid_f_ba < back')

o = [                               ['top',', ','mid_t_bo'] , [ 'mid_t_bo',', ','bottom'] ]
oo = [  [', left',', ','right']                                                             ]
ooo = [                             [', front',', ','mid_f_ba'],  [', mid_f_ba',', ','back'] ]

s =''

q = []
for i in o :
	for j in oo :
		for k in ooo :
			all = i + j + k
			f = 'self.query( ' 
			for a in all :
				f += a
				
			if f in q :
				continue
			if f not in q : q.append(f)
			print(f, ',  lis_range )')
			
print()
print("######################################################################################################################################################")
print()


print('top < mid_t_bo < bottom   and left < mid_l_r < right ')


o = [                                 ['top',', ','mid_t_bo'] , [ 'mid_t_bo',', ','bottom'] ]
oo = [                             [', left',', ','mid_l_r'] , [ ', mid_l_r',', ', 'right'] ]
ooo = [ [', front',', ','back']                                                             ]

s =''

q = []
for i in o :
	for j in oo :
		for k in ooo :
			all = i + j + k
			f = 'self.query( ' 
			for a in all :
				f += a
				
			if f in q :
				continue
			if f not in q : q.append(f)
			print(f, ',  lis_range )')
			
			
print()
print("######################################################################################################################################################")
print()


#######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################


print('top < mid_t_bo < bottom ')

o = [                           ['top',', ','mid_t_bo'] , [ 'mid_t_bo',', ','bottom'] ]
oo = [ [', left',', ','right']                                                           ]
ooo = [ [', front',', ','back']                                                         ]

s =''

q = []
for i in o :
	for j in oo :
		for k in ooo :
			all = i + j + k
			f = 'self.query( ' 
			for a in all :
				f += a
				
			if f in q :
				continue
			if f not in q : q.append(f)
			print(f, ',  lis_range )')
			
print()
print("######################################################################################################################################################")
print()


print('left < mid_l_r < right')

o = [    ['top', ', ','bottom']                                                               ]
oo = [                               [', left',', ','mid_l_r'] , [ ', mid_l_r',', ', 'right'] ]
ooo = [   [', front',', ','back']                                                            ]

s =''

q = []
for i in o :
	for j in oo :
		for k in ooo :
			all = i + j + k
			f = 'self.query( ' 
			for a in all :
				f += a
				
			if f in q :
				continue
			if f not in q : q.append(f)
			print(f, ',  lis_range )')
			
			
print()
print("######################################################################################################################################################")
print()

print('front < mid_f_ba < back')


o = [      ['top', ', ','bottom']                                                             ]
oo = [     [', left',', ','right']                                                            ]
ooo = [                                [', front',', ','mid_f_ba'],  [', mid_f_ba',', ','back'] ]

s =''

q = []
for i in o :
	for j in oo :
		for k in ooo :
			all = i + j + k
			f = 'self.query( ' 
			for a in all :
				f += a
				
			if f in q :
				continue
			if f not in q : q.append(f)
			print(f, ',  lis_range )')
			
			
print()
print("######################################################################################################################################################")
print()




"""