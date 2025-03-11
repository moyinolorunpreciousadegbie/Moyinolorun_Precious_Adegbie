#!/usr/bin/env python3

#!/usr/bin/env python3
def Octree( x , y , z , x2 , y2 , z2 ):
	def Octree_8( x , y , z , x2 , y2 , z2 , LEVEL  , VISITED ) :
		if[x,y,z] == [0,4,4] : print(x , y , z , x2 , y2 , z2 )
		
		#if  x >= x2  or  y >=  y2 or   z >=  z2 :
		if  x > x2  or  y >  y2 or   z >  z2 :
			return
		#if LEVEL == 3 :  # 2    3,4
			#print(x , y , z , '                     ',x2 , y2 , z2 , '          ' , VISITED )
			#return
		
		_self_tlf_x , _self_tlf_y , _self_tlf_z , _self_brb_x ,  _self_brb_y ,  _self_brb_z   = x , y , z , x2 , y2 , z2
		
		
		x_min = _self_tlf_x
		y_min = _self_tlf_y
		z_min = _self_tlf_z
		
		x_max = _self_brb_x
		y_max = _self_brb_y
		z_max = _self_brb_z
		
		
		_000000000000001 = 0#   0.000000000000001 ##   <<<<<<   or zero 0 later  !!!!
		
		_2 = 2 #2.000000000000000  #########################################
		_3 = 3 #3.000000000000000
		
		_01 = 0
		
		mid_x = ( x_min + x_max ) //2
		mid_y = ( y_min + y_max ) //2
		mid_z = ( z_min + z_max ) //2
		
		MAT = [
		[x_min ,     y_min , z_min,                mid_x+_01, mid_y+_01,  mid_z+_01] ,    
		[mid_x+_01 , y_min , z_min,                x_max,     mid_y+_01,  mid_z+_01] ,
					 #          #                             ##          #
								#										  #
								#										  #
								#                                         #
			
		[x_min ,     mid_y+_01 , z_min,            mid_x+_01, y_max,  mid_z+_01] ,
		[mid_x+_01 , mid_y+_01 , z_min,            x_max,     y_max,  mid_z+_01] ,
				      ##            #                          ###    #
									#                                 #
									#                                 #
									#                                 #
			
		[x_min ,     y_min , mid_z+_01,                mid_x+_01, mid_y+_01,  z_max] ,  
		[mid_x+_01 , y_min , mid_z+_01,                x_max,     mid_y+_01,  z_max] ,
					 #          #                                 ##           #
								#                                              #
								#											   #
								# 											   #
			
		[x_min ,     mid_y+_01 , mid_z+_01,            mid_x+_01, y_max,  z_max] ,
		[mid_x+_01 , mid_y+_01 , mid_z+_01,            x_max,     y_max,  z_max]        ]
				      ##            #                             ###     #
						            #                                     #
									#									  #
									#									  #    
		
		
		
		
		for i in range(0, 8):
			if [ MAT[i][0]  , MAT[i][1],   MAT[i][2],     MAT[i][3] , MAT[i][4],  MAT[i][5] ]  in VISITED :
				continue
			if MAT[i][0]   >=   MAT[i][3] or      MAT[i][1] >=  MAT[i][4] or  MAT[i][2]  >= MAT[i][5]  :
				continue
			if [ MAT[i][0]  , MAT[i][1],   MAT[i][2],     MAT[i][3] , MAT[i][4],  MAT[i][5] ] not in VISITED :
				VISITED.append([ MAT[i][0]  , MAT[i][1],   MAT[i][2],     MAT[i][3] , MAT[i][4],  MAT[i][5] ])
				
			Octree_8(MAT[i][0]  , MAT[i][1],   MAT[i][2],     MAT[i][3] , MAT[i][4],  MAT[i][5], LEVEL + 1 , VISITED ) # 
			
			
			Octree_27(MAT[i][0]  , MAT[i][1],   MAT[i][2],     MAT[i][3] , MAT[i][4],  MAT[i][5], LEVEL + 1 , VISITED ) 
			
	def Octree_27( x , y , z , x2 , y2 , z2 , LEVEL  , VISITED ) :
		#if[x,y,z] == [0,4,4] : print(x , y , z , x2 , y2 , z2 )
		
		#if  x >= x2  or  y >=  y2 or   z >=  z2 :
		if  x > x2  or  y >  y2 or   z >  z2 :
			return
		#if LEVEL == 3 :  # 2    3,4
			#print(x , y , z , '                     ',x2 , y2 , z2 , '          ' , VISITED )
			#return
		
		_self_tlf_x , _self_tlf_y , _self_tlf_z , _self_brb_x ,  _self_brb_y ,  _self_brb_z   = x , y , z , x2 , y2 , z2
		
		
		x_min = _self_tlf_x
		y_min = _self_tlf_y
		z_min = _self_tlf_z
		
		x_max = _self_brb_x
		y_max = _self_brb_y
		z_max = _self_brb_z
		
		
		_000000000000001 = 0#   0.000000000000001 ##   <<<<<<   or zero 0 later  !!!!
		
		_2 = 2 #2.000000000000000  #########################################
		_3 = 3 #3.000000000000000
		_1_3x = x_min + ((x_max - x_min) / _3)
		_2_3x = x_min + (2 * ((x_max - x_min) / _3))
		
		_1_3y = y_min + ((y_max - y_min) / _3)
		_2_3y = y_min + (2 * ((y_max - y_min) / _3))
		
		_1_3z = z_min + ((z_max - z_min) / _3)
		_2_3z = z_min + (2 * ((z_max - z_min) / _3))
		
		
		_1_3x = x_min + ((x_max - x_min) // _3)
		_2_3x = x_min + (2 * ((x_max - x_min) // _3))
		
		_1_3y = y_min + ((y_max - y_min) // _3)
		_2_3y = y_min + (2 * ((y_max - y_min) // _3))
		
		_1_3z = z_min + ((z_max - z_min) // _3)
		_2_3z = z_min + (2 * ((z_max - z_min) // _3))
		
		MAT=[		  [ _self_tlf_x, _self_tlf_y, _self_tlf_z, _1_3x, _1_3y, _1_3z ] ,
			[_1_3x + _000000000000001, _self_tlf_y, _self_tlf_z, _2_3x, _1_3y, _1_3z ]   ,
				[_2_3x + _000000000000001, _self_tlf_y, _self_tlf_z, _self_brb_x, _1_3y, _1_3z]   ,
	[_self_tlf_x, _1_3y + _000000000000001, _self_tlf_z, _1_3x, _2_3y, _1_3z]  ,
		[_1_3x + _000000000000001, _1_3y + _000000000000001, _self_tlf_z, _2_3x, _2_3y, _1_3z]    ,
				[_2_3x + _000000000000001 , _1_3y + _000000000000001, _self_tlf_z, _self_brb_x, _2_3y, _1_3z]    ,
			[_self_tlf_x, _2_3y + _000000000000001, _self_tlf_z, _1_3x, _self_brb_y, _1_3z]  ,
				[_1_3x + _000000000000001, _2_3y + _000000000000001, _self_tlf_z, _2_3x, _self_brb_y, _1_3z ] ,									
				[_2_3x + _000000000000001, _2_3y + _000000000000001, _self_tlf_z, _self_brb_x, _self_brb_y, _1_3z]   ,
			
				#    _1_3z + _000000000000001    _2_3z
						[ _self_tlf_x, _self_tlf_y, _1_3z + _000000000000001, _1_3x, _1_3y, _2_3z ] ,					
					[_1_3x + _000000000000001, _self_tlf_y, _1_3z + _000000000000001, _2_3x, _1_3y, _2_3z ]   ,				
						[_2_3x + _000000000000001, _self_tlf_y, _1_3z + _000000000000001, _self_brb_x, _1_3y, _2_3z]   ,												
			[_self_tlf_x, _1_3y + _000000000000001, _1_3z + _000000000000001, _1_3x, _2_3y, _2_3z]  ,		
				[_1_3x + _000000000000001, _1_3y + _000000000000001, _1_3z + _000000000000001, _2_3x, _2_3y, _2_3z]   ,
						[_2_3x + _000000000000001 , _1_3y + _000000000000001, _1_3z + _000000000000001, _self_brb_x, _2_3y, _2_3z]    ,
					[_self_tlf_x, _2_3y + _000000000000001, _1_3z + _000000000000001, _1_3x, _self_brb_y, _2_3z]   ,
						[_1_3x + _000000000000001, _2_3y + _000000000000001, _1_3z + _000000000000001, _2_3x, _self_brb_y, _2_3z ]  ,
						[_2_3x + _000000000000001, _2_3y + _000000000000001, _1_3z + _000000000000001, _self_brb_x, _self_brb_y, _2_3z]   ,	
				#   _2_3z + _000000000000001       _self_brb_z
			
				[ _self_tlf_x, _self_tlf_y, _self_tlf_z, _1_3x, _1_3y, _self_brb_z ]   ,
			[_1_3x + _000000000000001, _self_tlf_y, _2_3z + _000000000000001 , _2_3x, _1_3y, _self_brb_z ]    ,
				[_2_3x + _000000000000001, _self_tlf_y, _2_3z + _000000000000001 , _self_brb_x, _1_3y, _self_brb_z]    ,
	[_self_tlf_x, _1_3y + _000000000000001, _2_3z + _000000000000001 , _1_3x, _2_3y, _self_brb_z]     ,
		[_1_3x + _000000000000001, _1_3y + _000000000000001, _2_3z + _000000000000001 , _2_3x, _2_3y, _self_brb_z]   ,   
				[_2_3x + _000000000000001 , _1_3y + _000000000000001, _2_3z + _000000000000001 , _self_brb_x, _2_3y, _self_brb_z]    ,
			[_self_tlf_x, _2_3y + _000000000000001, _2_3z + _000000000000001 , _1_3x, _self_brb_y, _self_brb_z]    ,
				[_1_3x + _000000000000001, _2_3y + _000000000000001, _2_3z + _000000000000001 , _2_3x, _self_brb_y, _self_brb_z ]  ,
				[_2_3x + _000000000000001, _2_3y + _000000000000001, _2_3z + _000000000000001 , _self_brb_x, _self_brb_y, _self_brb_z]   ]
		
		
		_000000000000001 = 0
		MATT =[		  [ _self_tlf_x, _self_tlf_y, _self_tlf_z, _1_3x, _1_3y, _1_3z ] ,
			[_1_3x + _000000000000001, _self_tlf_y, _self_tlf_z, _2_3x, _1_3y, _1_3z ]   ,
				[_2_3x + _000000000000001, _self_tlf_y, _self_tlf_z, _self_brb_x, _1_3y, _1_3z]   ,
	[_self_tlf_x, _1_3y + _000000000000001, _self_tlf_z, _1_3x, _2_3y, _1_3z]  ,
		[_1_3x + _000000000000001, _1_3y + _000000000000001, _self_tlf_z, _2_3x, _2_3y, _1_3z]    ,
				[_2_3x + _000000000000001 , _1_3y + _000000000000001, _self_tlf_z, _self_brb_x, _2_3y, _1_3z]    ,
			[_self_tlf_x, _2_3y + _000000000000001, _self_tlf_z, _1_3x, _self_brb_y, _1_3z]  ,
				[_1_3x + _000000000000001, _2_3y + _000000000000001, _self_tlf_z, _2_3x, _self_brb_y, _1_3z ] ,									
				[_2_3x + _000000000000001, _2_3y + _000000000000001, _self_tlf_z, _self_brb_x, _self_brb_y, _1_3z]   ,
			
				#    _1_3z + _000000000000001    _2_3z
						[ _self_tlf_x, _self_tlf_y, _1_3z + _000000000000001, _1_3x, _1_3y, _2_3z ] ,					
					[_1_3x + _000000000000001, _self_tlf_y, _1_3z + _000000000000001, _2_3x, _1_3y, _2_3z ]   ,				
						[_2_3x + _000000000000001, _self_tlf_y, _1_3z + _000000000000001, _self_brb_x, _1_3y, _2_3z]   ,												
			[_self_tlf_x, _1_3y + _000000000000001, _1_3z + _000000000000001, _1_3x, _2_3y, _2_3z]  ,		
				[_1_3x + _000000000000001, _1_3y + _000000000000001, _1_3z + _000000000000001, _2_3x, _2_3y, _2_3z]   ,
						[_2_3x + _000000000000001 , _1_3y + _000000000000001, _1_3z + _000000000000001, _self_brb_x, _2_3y, _2_3z]    ,
					[_self_tlf_x, _2_3y + _000000000000001, _1_3z + _000000000000001, _1_3x, _self_brb_y, _2_3z]   ,
						[_1_3x + _000000000000001, _2_3y + _000000000000001, _1_3z + _000000000000001, _2_3x, _self_brb_y, _2_3z ]  ,
						[_2_3x + _000000000000001, _2_3y + _000000000000001, _1_3z + _000000000000001, _self_brb_x, _self_brb_y, _2_3z]   ,	
				#   _2_3z + _000000000000001       _self_brb_z
			
				[ _self_tlf_x, _self_tlf_y, _self_tlf_z, _1_3x, _1_3y, _self_brb_z ]   ,
			[_1_3x + _000000000000001, _self_tlf_y, _2_3z + _000000000000001 , _2_3x, _1_3y, _self_brb_z ]    ,
				[_2_3x + _000000000000001, _self_tlf_y, _2_3z + _000000000000001 , _self_brb_x, _1_3y, _self_brb_z]    ,
	[_self_tlf_x, _1_3y + _000000000000001, _2_3z + _000000000000001 , _1_3x, _2_3y, _self_brb_z]     ,
		[_1_3x + _000000000000001, _1_3y + _000000000000001, _2_3z + _000000000000001 , _2_3x, _2_3y, _self_brb_z]   ,   
				[_2_3x + _000000000000001 , _1_3y + _000000000000001, _2_3z + _000000000000001 , _self_brb_x, _2_3y, _self_brb_z]    ,
			[_self_tlf_x, _2_3y + _000000000000001, _2_3z + _000000000000001 , _1_3x, _self_brb_y, _self_brb_z]    ,
				[_1_3x + _000000000000001, _2_3y + _000000000000001, _2_3z + _000000000000001 , _2_3x, _self_brb_y, _self_brb_z ]  ,
				[_2_3x + _000000000000001, _2_3y + _000000000000001, _2_3z + _000000000000001 , _self_brb_x, _self_brb_y, _self_brb_z]   ]
		
		
		
		
		for i in range(0, 27):
			if [ MAT[i][0]  , MAT[i][1],   MAT[i][2],     MAT[i][3] , MAT[i][4],  MAT[i][5] ]  in VISITED :
				continue
			if MAT[i][0]   >=   MAT[i][3] or      MAT[i][1] >=  MAT[i][4] or  MAT[i][2]  >= MAT[i][5]  :
				continue
			if [ MAT[i][0]  , MAT[i][1],   MAT[i][2],     MAT[i][3] , MAT[i][4],  MAT[i][5] ] not in VISITED :
				VISITED.append([ MAT[i][0]  , MAT[i][1],   MAT[i][2],     MAT[i][3] , MAT[i][4],  MAT[i][5] ])
				
			Octree_27(MAT[i][0]  , MAT[i][1],   MAT[i][2],     MAT[i][3] , MAT[i][4],  MAT[i][5], LEVEL + 1 , VISITED ) # 
			
			#Octree_8(MAT[i][0]  , MAT[i][1],   MAT[i][2],     MAT[i][3] , MAT[i][4],  MAT[i][5], LEVEL + 1 , VISITED ) # 
			
	LEVEL = 0
	VISITED = []
	
	#Octree_8( x , y , z , x2 , y2 , z2 , LEVEL  , VISITED ) 
	Octree_27( x , y , z , x2 , y2 , z2 , LEVEL  , VISITED ) 
	
	print(    VISITED , len(VISITED) )
	
	
###############################################################################################################################################################

	
	
	
	
Octree( 0 , 0 , 0 , 5 , 5 , 5 ) 
print()
print()
#Octree__( 0 , 0 , 0 , 5 , 5 , 5 ) 		

		

"""		
		
		
		
				#print(C," <-  C")
		#print()
		#print(_self_tlf_x," tlf x")
		#print()
		#print(_1_3x ," 0.3 x ", _1_3x + _000000000000001)
		#print()
		#print(_2_3x ," 0.6 x ", _2_3x + _000000000000001)
		#print()
		#print(_self_brb_x," brb x")
		#print()
		
		#print(_self_tlf_y," tlf y")
		#print()
		#print(_1_3y ," 0.3 y ", _1_3y + _000000000000001)
		#print()
		#print(_2_3y ," 0.6 y ", _2_3y + _000000000000001)
		#print()
		#print(_self_brb_y," brb y")
		#print()
		
		#print(_self_tlf_z," tlf z")
		#print()
		#print(_1_3z ," 0.3 z ", _1_3z + _000000000000001)
		#print()
		#print(_2_3z ," 0.6 z ", _2_3z + _000000000000001)
		#print()
		#print(_self_brb_z," brb z")
		#print()
		
		
		
MAT[i][0]  , MAT[i][1],   MAT[i][2],     MAT[i][3] , MAT[i][4],  MAT[i][5] 

+           +             +                  -           -         -
0           0             0                  0           0         0   xxxx


+           +             +                  -           -         -   # <<<<<<
+           +             +                  0           -         -    
+           +             +                  -           0         -
+           +             +                  -           -         0

+           +             +                  0           0         -
+           +             +                  0           -         0
+           +             +                  -           0         0
########################################################################
+           +             +                  -           -         -   
+           +             +                  0           -         -   # <<<<<< 
+           +             +                  -           0         -
+           +             +                  -           -         0

+           +             +                  0           0         -
+           +             +                  0           -         0
+           +             +                  -           0         0
########################################################################
+           +             +                  -           -         -   
+           +             +                  0           -         -    
+           +             +                  -           0         -   # <<<<<<
+           +             +                  -           -         0

+           +             +                  0           0         -
+           +             +                  0           -         0
+           +             +                  -           0         0
########################################################################
+           +             +                  -           -         -  
+           +             +                  0           -         -   
+           +             +                  -           0         -
+           +             +                  -           -         0   # <<<<<<

+           +             +                  0           0         -
+           +             +                  0           -         0
+           +             +                  -           0         0
########################################################################
+           +             +                  -           -         -   
+           +             +                  0           -         -    
+           +             +                  -           0         -
+           +             +                  -           -         0

+           +             +                  0           0         -    # <<<<<<
+           +             +                  0           -         0
+           +             +                  -           0         0
########################################################################
+           +             +                  -           -         -   
+           +             +                  0           -         -    
+           +             +                  -           0         -
+           +             +                  -           -         0

+           +             +                  0           0         -   
+           +             +                  0           -         0     # <<<<<<
+           +             +                  -           0         0
########################################################################
+           +             +                  -           -         -   
+           +             +                  0           -         -    
+           +             +                  -           0         -
+           +             +                  -           -         0

+           +             +                  0           0         -   
+           +             +                  0           -         0
+           +             +                  -           0         0    # <<<<<<
########################################################################




if [ MAT[i][0]  , MAT[i][1],   MAT[i][2],     MAT[i][3] , MAT[i][4],  MAT[i][5] ]  in VISITED :
	continue
if MAT[i][0]   >=   MAT[i][3] or      MAT[i][1] >=  MAT[i][4] or  MAT[i][2]  >= MAT[i][5]  :
	continue
if [ MAT[i][0]  , MAT[i][1],   MAT[i][2],     MAT[i][3] , MAT[i][4],  MAT[i][5] ] not in VISITED :
	VISITED.append([ MAT[i][0]  , MAT[i][1],   MAT[i][2],     MAT[i][3] , MAT[i][4],  MAT[i][5] ])
	
Octree_(MAT[i][0]  , MAT[i][1],   MAT[i][2],     MAT[i][3] , MAT[i][4],  MAT[i][5], LEVEL + 1 , VISITED ) # 

#_________________________________________________________________


for j in range(MAT[i][0]  ,  MAT[i][3]):
	for k in range(MAT[i][1]  ,  MAT[i][4]):
		for l in range(MAT[i][2]  ,  MAT[i][5]):
			if [ MAT[i][0]  , MAT[i][1],   MAT[i][2],     MAT[i][3] , MAT[i][4],  MAT[i][5] ]  in VISITED :
				continue
			if MAT[i][0]   >=   MAT[i][3] or      MAT[i][1] >=  MAT[i][4] or  MAT[i][2]  >= MAT[i][5]  :
				continue
			if [ MAT[i][0]  , MAT[i][1],   MAT[i][2],     MAT[i][3] , MAT[i][4],  MAT[i][5] ] not in VISITED :
				VISITED.append([ MAT[i][0]  , MAT[i][1],   MAT[i][2],     MAT[i][3] , MAT[i][4],  MAT[i][5] ])
				
			Octree_(MAT[i][0]  , MAT[i][1],   MAT[i][2],     MAT[i][3] , MAT[i][4],  MAT[i][5], LEVEL + 1 , VISITED ) # 
			########################################################################################################


"""