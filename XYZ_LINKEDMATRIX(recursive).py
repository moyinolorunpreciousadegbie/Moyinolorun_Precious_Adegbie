class LinkedList:
	def __init__(self, value=None, up=None, down = None, left=None, right=None ,  topleft=None  , topright=None , bottomleft=None , bottomright=None ,
		
	above= None,
	below=None,
		
	upabove =None,
	downbelow =None,
		
	upbelow  =None,
	downabove =None,
		
	rightbelow  =None,
	leftabove =None,
		
	leftbelow =None,
	rightabove =None,
		
		
	bottomleftbelow =None,
	toprightabove =None,
		
	toprightbelow =None,
	bottomleftabove =None,
		
		
	bottomrightbelow =None,
	topleftabove =None, 
		
	topleftbelow =None  ,
	bottomrightabove=None):
		
		
		
		self.value = value
		self.up = up
		self.down = down
		self.left = left
		self.right = right 
		
		
		self.topleft = topleft
		self.topright = topright
		
		self.bottomleft = bottomleft
		self.bottomright = bottomright
		
		
		###############################
		# 3D
		self.above = above  # ^
		self.below = below # V
		
		self.upabove = upabove  # ^
		self.downbelow = downbelow # V
		
		self.upbelow = upbelow  # ^
		self.downabove = downabove # V
		
		self.rightbelow = rightbelow
		self.leftabove = leftabove
		
		self.leftbelow = leftbelow
		self.rightabove = rightabove
		
		
		self.bottomleftbelow = bottomleftbelow
		self.toprightabove = toprightabove
		
		self.toprightbelow = toprightbelow
		self.bottomleftabove = bottomleftabove
		
		
		self.bottomrightbelow = bottomrightbelow
		self.topleftabove = topleftabove
		
		self.topleftbelow = topleftbelow
		self.bottomrightabove = bottomrightabove
		
		
##########################################################################################################################################################################		
		
		
		
		
		
def fn(xyz):
	#dim = [[ [ [0]* X for X in range(len(xyz[Z][Y] )) ] for Y in range(len(xyz[Z] ))]  for Z in range(len(xyz))]
	#dim = [[ [ [None]*len(list(range(len(xyz[Z][Y]))) )   ] for Y in range(len(xyz[Z]))  ]for Z in range(len(xyz))]
	#dim = [[ [ [None]*len(list(range(len(xyz[Z][Y]))) )   ] for Y in range(len(xyz[Z]))  ]for Z in range(len(xyz))]
	MAT =  []
	
	dim = [[]for i  in range(len(xyz[0] ))]
	dim2 = [[]for i  in range(len(xyz[0] ))]
	#dim = xyz
	#print(dim)
	def dfs(cn ,xyz,  dim , dim2 , MAT, z,y,x, z1,y1,x1,   z2,y2,x2  ):
		
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
		
		
		cn += 1
		
		#print(cn, dim)
		#dim[y2].append( xyz[z2][y2][x2]  )   #  APPEND HERE
		
		
		if x2 < len(xyz[z2][y2] ) :#and y2 < len(xyz[z2]) and z2 < len(xyz):
			#dim[z2][y2][x2]  = xyz[z2][y2][x2]  * 10
			
			#print(dim[y2][x2] )
			#print(dim,  xyz[z2][y2][x2]*10)
			
			
			R0C0 = LinkedList( xyz[z2][y2][x2] ) 
			#R0C0 = LinkedList( xyz[z1][y1][x1] ) 
			NONE = LinkedList( "None") 
			l = xyz[z2]
			h = z2
			r = y2
			c = x2
			count = 0
			
			
			if len(dim[r]) == r and   len(dim[r]) == c  and r-1== -1 and c-1== -1        and  r == 0 and c == 0         and  len(dim[r]) == 0 :
				#print("1", end=" ")
				R0C0.up = NONE          #   ##
				R0C0.down = NONE        #   #
				
				R0C0.left = NONE
				R0C0.right = NONE
				
				dim[r].append(R0C0)  
				
			if len(dim[r]) == c    and r==0 and 0<=c-1< c <len(l[r])  :
				#print("2", end=" ")
				R0C0.up = NONE
				R0C0.down = NONE
				
				R0C0.left = dim[r][c-1]  #
				dim[r][c-1].right = R0C0 #
				R0C0.right = NONE
				
				dim[r].append(R0C0) 
				
			if len(dim[r-1]) <= len(dim[r])    and  0<=r-1<r<len(l) and c>= len(dim[r-1]) :
				#print("SPECIAL CASE", end=" ")
				R0C0.up = NONE
				R0C0.down = NONE
				
				R0C0.left = dim[r][c-1]  #
				dim[r][c-1].right = R0C0 #
				R0C0.right = NONE
				
				dim[r].append(R0C0) 
				
				
			if dim[r-1] != []    and 0<=r-1<len(l) and c==0  and c <= len(dim[r-1])-1 and len(dim[r-1])>0:
				#print("3", end=" ")
				R0C0.up = dim[r-1][c]  #                            ######################
				dim[r-1][c].down = R0C0 #
				R0C0.down = NONE
				
				R0C0.left = NONE
				R0C0.right = NONE
				
				dim[r].append(R0C0) 
				
				
			if len(dim[r]) == c  and  dim[r-1] != []        and 0<=r-1<len(l) and 0<=c-1<len(l[r])  and c <= len(dim[r-1])-1 and len(dim[r-1])>0 and len(dim[r]) >=1:
				#print(dim, len(dim[r]) ,"HERE",c )
				#print("4", end=" ")
				R0C0.up = dim[r-1][c]  #
				dim[r-1][c].down = R0C0 #
				R0C0.down = NONE
				
				R0C0.left = dim[r][c-1]  #
				dim[r][c-1].right = R0C0 #
				R0C0.right = NONE
				
				dim[r].append(R0C0) 
				
			###############################################################
				
				
				
			########################
			# DIAGONAL
				
			R0C0.topleft = NONE  # DEFAULT will be changed accordingly
			R0C0.topright = NONE
			R0C0.bottomright = NONE
			R0C0.bottomleft = NONE
			
			NONE.topleft = R0C0  # DEFAULT will be changed accordingly
			NONE.topright = R0C0
			NONE.bottomright = R0C0
			NONE.bottomleft = R0C0
			
			
			if (r == 0 ) and (c == 0 and dim2[r]==[] and len(dim2[r]) == 0 ) :
				
				#print("0 R, 0 C, HERE",l[r][c])
				R0C0.topleft = NONE  # v
				R0C0.topright = NONE
				
				NONE.bottomright = R0C0 # ^
				NONE.bottomleft = R0C0
				dim2[r].append(R0C0) 
				count += 1
				
				
				
			if (r == 0 ) and (1 <=  c  and len(dim2[r])>=1) :
				
				#print("0 R HERE",l[r][c])
				R0C0.topleft = NONE  # v
				R0C0.topright = NONE
				
				NONE.bottomright = R0C0 # ^
				NONE.bottomleft = R0C0
				dim2[r].append(R0C0) 
				count += 1
				
			if (c == 0 and dim2[r]==[])  and len(dim2[r]) == 0 and          dim2[r-1] != [] and len(dim2[r-1])>0:
				#print("0 C HERE",l[r][c])
				R0C0.topleft = NONE
				R0C0.bottomleft = NONE # >
				
				
				NONE.bottomright = R0C0 # <
				NONE.topright = R0C0 
				dim2[r].append(R0C0) 
				count += 1
				
			if len(dim2[r]) + 1 == len(dim2[r-1]) and  1<=r<=len(l)-1 and 1<=c<=len(l[r])-1  and   dim2[r-1] != []   and len(dim2[r-1]) >=1 and c+1 == len(dim2[r-1])  and c == len(dim2[r]) :
				#print("> 1 HERE",l[r][c])
				R0C0.topleft = dim2[r-1][c-1] 
				dim2[r-1][c-1].bottomright = R0C0
				dim2[r].append(R0C0) 
				count += 1
				
			if  len(dim2[r])  == len(dim2[r-1])  and   1<=r<=len(l)-1 and 1<=c<=len(l[r])-1 and   dim2[r-1] != []   and len(dim2[r-1]) >=1 and c==len(dim2[r-1])  and c == len(dim2[r]):
				#print("> 2 HERE",l[r][c])
				R0C0.topleft = dim2[r-1][c-1] 
				dim2[r-1][c-1].bottomright = R0C0
				dim2[r].append(R0C0) 
				count += 1
				
			if len(dim2[r]) + 2 <= len(dim2[r-1]) and  1<=r<=len(l)-1 and 1<=c<=len(l[r])-1  and   dim2[r-1] != []   and len(dim2[r-1]) >=1 and c+1<=len(dim2[r-1]) and c == len(dim2[r]):
				#print("> 3 HERE",l[r][c])
				R0C0.topleft = dim2[r-1][c-1] 
				R0C0.topright = dim2[r-1][c+1] 
				
				dim2[r-1][c-1].bottomright = R0C0
				dim2[r-1][c+1].bottomleft = R0C0
				
				dim2[r].append(R0C0) 
				count += 1
				
			if len(dim2[r]) > len(dim2[r-1]) and  1<=r<=len(l)-1 and len(l[r-1])<=c<=len(l[r])-1 and  len(dim2[r-1])>=1   and dim2[r-1] != [] and c > len(dim2[r-1])        and c == len(dim2[r]):
				#print("> 4 HERE",l[r][c])
				R0C0.topleft = NONE
				R0C0.topright = NONE
				NONE.bottomright = R0C0
				NONE.bottomleft = R0C0
				dim2[r].append(R0C0) 
				count += 1
				
			##########
			
			## 3D
				
			R0C0.above= NONE
			R0C0.below=NONE
			
			R0C0.upabove =NONE
			R0C0.downbelow =NONE
			
			R0C0.upbelow  =NONE
			R0C0.downabove =NONE
			
			R0C0.rightbelow  =NONE
			R0C0.leftabove =NONE
			
			R0C0.leftbelow =NONE
			R0C0.rightabove =NONE
			
			
			R0C0.bottomleftbelow =NONE
			R0C0.toprightabove =NONE
			
			R0C0.toprightbelow =NONE
			R0C0.bottomleftabove = NONE
			
			
			R0C0.bottomrightbelow = NONE
			R0C0.topleftabove = NONE
			
			R0C0.topleftbelow = NONE 
			R0C0.bottomrightabove= NONE
			
			
			############
			
			h = z2
			
			
			if  h > 0 :# and h < len(xyz):
			
				#R0C0 = LinkedList( xyz[z2][y2][x2] ) 
			
				R0C0.above= NONE
				R0C0.below=NONE
			
				R0C0.upabove =NONE
				R0C0.downbelow =NONE
			
				R0C0.upbelow  =NONE
				R0C0.downabove =NONE
			
				R0C0.rightbelow  =NONE
				R0C0.leftabove =NONE
			
				R0C0.leftbelow =NONE
				R0C0.rightabove =NONE
			
			
				R0C0.bottomleftbelow =NONE
				R0C0.toprightabove =NONE
			
				R0C0.toprightbelow =NONE
				R0C0.bottomleftabove = NONE
			
			
				R0C0.bottomrightbelow = NONE
				R0C0.topleftabove = NONE
			
				R0C0.topleftbelow = NONE 
				R0C0.bottomrightabove= NONE
			#############################################################################################      1st
			
			# DONT MESS WITH THE MINUS - 1
			
			
				if 0 <= r  < len(MAT[h-1])  and  0 <= c  < len(MAT[h-1][r])  :# and mat[h-1][r][c] != None      :
					MAT[h-1][r][c].below = R0C0 # mat[h][r][c]
					R0C0.above = MAT[h-1][r][c]#
					#MAT[h][r][c].above = MAT[h-1][r][c]#
					
				
				
				
				
				
				if 0 <= r-1 < len(MAT[h-1])  and  0 <= c  < len(MAT[h-1][r-1])  :# and  mat[h-1][r-1][c] != None   :
					MAT[h-1][r-1][c].downbelow = R0C0 # mat[h][r][c]
					R0C0.upabove = MAT[h-1][r-1][c]#
					#MAT[h][r][c].upabove = MAT[h-1][r-1][c]#
					
				if 0 <= r+1  < len(MAT[h-1])  and  0 <= c  < len(MAT[h-1][r+1])  :# and   mat[h-1][r+1][c] != None   :
					MAT[h-1][r+1][c].upbelow = R0C0 # mat[h][r][c]
					R0C0.downabove = MAT[h-1][r+1][c]#
					#MAT[h][r][c].downabove = MAT[h-1][r+1][c]#
					
				if 0 <= r  < len(MAT[h-1])  and  0 <= c-1  < len(MAT[h-1][r]) :#  and   mat[h-1][r][c-1] != None  :
					MAT[h-1][r][c-1].rightbelow = R0C0 # mat[h][r][c]
					R0C0.leftabove = MAT[h-1][r][c-1]#
					#MAT[h][r][c].leftabove = MAT[h-1][r][c-1]#
					
				if 0 <= r  < len(MAT[h-1])  and  0 <= c+1  < len(MAT[h-1][r])  :# and   mat[h-1][r][c+1] != None  :
					MAT[h-1][r][c+1].leftbelow = R0C0 # mat[h][r][c]
					R0C0.rightabove = MAT[h-1][r][c+1]
					#MAT[h][r][c].rightabove = MAT[h-1][r][c+1]
					
				
				
				
				
				if 0 <= r-1  < len(MAT[h-1])  and  0 <= c+1  < len(MAT[h-1][r-1])  :# and   mat[h-1][r-1][c+1] != None  :
					MAT[h-1][r-1][c+1].bottomleftbelow = R0C0 # mat[h][r][c]
					R0C0.toprightabove = MAT[h-1][r-1][c+1]
					#MAT[h][r][c].toprightabove = MAT[h-1][r-1][c+1]
					
				if 0 <= r+1  < len(MAT[h-1])  and  0 <= c-1  < len(MAT[h-1][r+1])  :# and  mat[h-1][r+1][c-1] != None  :
					MAT[h-1][r+1][c-1].toprightbelow = R0C0 # mat[h][r][c]
					R0C0.bottomleftabove = MAT[h-1][r+1][c-1]
					#MAT[h][r][c].bottomleftabove = MAT[h-1][r+1][c-1]
					
				
				if 0 <= r-1 < len(MAT[h-1])  and  0 <= c-1  < len(MAT[h-1][r-1])  :# and  mat[h-1][r-1][c-1] != None  :
					MAT[h-1][r-1][c-1].bottomrightbelow = R0C0 # mat[h][r][c]
					R0C0.topleftabove = MAT[h-1][r-1][c-1]
					#MAT[h][r][c].topleftabove = MAT[h-1][r-1][c-1]
					
				if 0 <= r+1  < len(MAT[h-1])  and  0 <= c+1  < len(MAT[h-1][r+1]) :# and  mat[h-1][r+1][c+1] != None  :
					MAT[h-1][r+1][c+1].topleftbelow = R0C0 # mat[h][r][c]
					R0C0.bottomrightabove = MAT[h-1][r+1][c+1]
					#MAT[h][r][c].bottomrightabove = MAT[h-1][r+1][c+1]
					
					
				#######################################################################################################################
				 
				if   r+1  <= len(MAT[h-1])  and  c+1  <= len(MAT[h-1][r])  :# and mat[h-1][r][c] != None      :
					MAT[h-1][r][c].below = R0C0 # mat[h][r][c]
					R0C0.above = MAT[h-1][r][c]#
					#MAT[h][r][c].above = MAT[h-1][r][c]#
	
	
	
	
	
	
				#print( MAT[h-1], r,dim , xyz[h-1],"jkk",xyz[h][r][c])
				#MAT[h-1] = dim
				if r > 0 and  r <= len(MAT[h-1])    and  c+1  <= len(MAT[h-1][r-1])  :# and  mat[h-1][r-1][c] != None   :  # r-1
					MAT[h-1][r-1][c].downbelow = R0C0 # mat[h][r][c]
					R0C0.upabove = MAT[h-1][r-1][c]#
					#mat[h][r][c].upabove = mat[h-1][r-1][c]#
	
				if  r+2  <= len(MAT[h-1])  and  c+1  <= len(MAT[h-1][r]) :# and MAT[h-1][r+1] != []:# and   mat[h-1][r+1][c] != None   : # r and r + 1
					#print(MAT[h-1][r+1],c,"ccccc")
					MAT[h-1][r+1][c].upbelow = R0C0 # mat[h][r][c]
					R0C0.downabove = MAT[h-1][r+1][c]#
					#mat[h][r][c].downabove = mat[h-1][r+1][c]#
	
				if r +1 <= len(MAT[h-1])  and  c  <= len(MAT[h-1][r]) :#  and   mat[h-1][r][c-1] != None  :
					MAT[h-1][r][c-1].rightbelow = R0C0 # mat[h][r][c]
					R0C0.leftabove = MAT[h-1][r][c-1]#
					#mat[h][r][c].leftabove = mat[h-1][r][c-1]#
	
				if   r+1  <= len(MAT[h-1])  and  c+2  <= len(MAT[h-1][r])                   :# and   mat[h-1][r][c+1] != None  :
					MAT[h-1][r][c+1].leftbelow = R0C0 # mat[h][r][c]
					R0C0.rightabove = MAT[h-1][r][c+1]
					#mat[h][r][c].rightabove = mat[h-1][r][c+1]
	
	
	
	
	
				if r>0 and    r  <= len(MAT[h-1])  and  c+2  <= len(MAT[h-1][r-1])  :# and   mat[h-1][r-1][c+1] != None  :  # r - 1
					MAT[h-1][r-1][c+1].bottomleftbelow = R0C0 # mat[h][r][c]
					R0C0.toprightabove = MAT[h-1][r-1][c+1]
					#mat[h][r][c].toprightabove = mat[h-1][r-1][c+1]
	
				if r+2  <= len(MAT[h-1])  and  c  <= len(MAT[h-1][r+1])  :#and MATT[h-1][r+1] != []:# and  mat[h-1][r+1][c-1] != None  : # r and r+1
					MAT[h-1][r+1][c-1].toprightbelow = R0C0 # mat[h][r][c]
					R0C0.bottomleftabove = MAT[h-1][r+1][c-1]
					#mat[h][r][c].bottomleftabove = mat[h-1][r+1][c-1]
	
	
				if r>0 and r <= len(MAT[h-1])  and  c  <= len(MAT[h-1][r-1])  :# and  mat[h-1][r-1][c-1] != None  :  # r - 1
					MAT[h-1][r-1][c-1].bottomrightbelow = R0C0 # mat[h][r][c]
					R0C0.topleftabove = MAT[h-1][r-1][c-1]
					#mat[h][r][c].topleftabove = mat[h-1][r-1][c-1]
	
				if   r+2  <= len(MAT[h-1])  and   c+2  <= len(MAT[h-1][r+1]) :#and MAT[h-1][r+1] != []:# and  mat[h-1][r+1][c+1] != None  : # r and r +1
					#print(MAT[h-1][r+1])
					MAT[h-1][r+1][c+1].topleftbelow = R0C0 # mat[h][r][c]
					R0C0.bottomrightabove = MAT[h-1][r+1][c+1]
					#mat[h][r][c].bottomrightabove = mat[h-1][r+1][c+1]
				
			
			
			
			
			
			
			
			###### LAST
			#dim[y2].append( xyz[z2][y2][x2] * 10 ) 
			#print(dim)
			#######
			#dim[y2][x2]  = xyz[z2][y2][x2]  * 10
			#print(cn, (z1,y1,x1),(z2,y2,x2) )
		
		#dfs(cn ,xyz, dim , dim2 ,  MAT,   z,y,x, z2,y2,x2,   z2,y2,x2+1  )
		dfs(cn ,xyz, dim , dim2 ,   MAT,   z,y,x, z1,y1,x1,   z2,y2,x2+1  )
	
	cn = 0
	dfs(cn , xyz, dim, dim2 ,  MAT,  0,0,0, 0,0,0,   0,0,0  )
	
	return MAT
	
				
def printList2( dim): # dim == mat
	#currRow = dim[0][0][0]
	zc = 0
	for zz in dim :
		currRow  = zz[0][0]
		
		while currRow:
			yc = 0
			currCol = currRow
			while currCol:
				
				
				if currCol.left != None and currCol.right != None :
					
					
					space = ' '* (  len(str(currCol.left.value)) +  len("<-") + len(str(currCol.value))  )
					
					if currCol.up!= None :
						print(space, currCol.up.value)
						print(space+" ^")
					print(currCol.left.value, "<-",currCol.value,"->",currCol.right.value,end=" ")
					
					
					print('###################################################################')
					
					
					if currCol.above != None : print(currCol.value,	'above',	currCol.above.value )
					if currCol.below != None : print(currCol.value, 'below',	currCol.below.value )
					
					if currCol.upabove != None :print(currCol.value, 'upabove',	currCol.upabove.value )
					if  currCol.downbelow != None :print(currCol.value, 'downbelow',	currCol.downbelow.value )
					
					if currCol.upbelow != None :print(currCol.value, 'upbelow',	currCol.upbelow.value )
					if currCol.downabove != None :print(currCol.value, 'downabove',	currCol.downabove.value )
					
					if currCol.rightbelow != None :print(currCol.value, 'rightbelow',	currCol.rightbelow.value )
					if currCol.leftabove != None :print(currCol.value, 'leftabove',	currCol.leftabove.value )
					
					if currCol.leftbelow != None :print(currCol.value, 'leftbelow',	currCol.leftbelow.value )
					if currCol.rightabove != None :print(currCol.value, 'rightabove',	currCol.rightabove.value )
					
					
					if  currCol.bottomleftbelow != None :print(currCol.value, 'bottomleftbelow',	currCol.bottomleftbelow.value )
					if  currCol.toprightabove != None :print(currCol.value, 'toprightabove',	currCol.toprightabove.value )
					
					if currCol.toprightbelow != None :print(currCol.value, 'toprightbelow',	currCol.toprightbelow.value )
					if currCol.bottomleftabove != None :print(currCol.value, 'bottomleftabove',	currCol.bottomleftabove.value )
					
					
					if  currCol.bottomrightbelow != None :print(currCol.value, 'bottomrightbelow',	currCol.bottomrightbelow.value )
					if currCol.topleftabove != None :print(currCol.value, 'topleftabove',	currCol.topleftabove.value )
					
					if currCol.topleftbelow != None :print(currCol.value, 'topleftbelow',	currCol.topleftbelow.value )
					if currCol.bottomrightabove != None :print(currCol.value, 'bottomrightabove',	currCol.bottomrightabove.value )
					
					print('###################################################################')
					
					
					if currCol.down!= None :
						print()
						print(space+" V")
						print(space,currCol.down.value)
						
						
			#print(end=" ")
			#print()	
						
						
						
				currCol = currCol.right
				
			yc += 1
		#print(end=" ")
			print("------------------")
			print()
			
			
			
			
			currRow = currRow.down
			
			
		#if currRow.value == "None"   and  yc == len( dim[zc]) :
		zc += 1
		
		
xyz = [ [[1,2,3],
	[4,5,6]] ,
	
	[[7,8,9],        # <<<
	[10,11,12]]  ,
	
	[[13,14,15],
	[16,17,18]]  ]


          # 2
xyzz = [ [[1,2],                # 1
	     [3,4],
		 [5,6]] ,    # 3
		
		
		[[7,8],                 # 2
		[9,10],
		[11,12]] ,

		[[13,14],            #  3
		[15,16],
		[17,18]] ,

		[[20,21],           # 4
		[22,23],
		[24,25]]      ]


xyz = [ [[1,2,3],
	[4,5,6]] ,
	
	[[7,8,9],        # <<<
	[10,11,12],
	[13,14,15]]  ,
	
	[[13,14,15],
	[16,17,18]]  ]
		

#l = [[ [ [None]*len(list(range(len(xyz[Z][Y]))) )   ] for Y in range(len(xyz[Z]))  ]for Z in range(len(xyz))]

#print(l,"here")
#print()
#print()

#dim = [[]for i  in range(len(xyz[2] ))]
#print(dim)


o = fn(xyz)

printList2( o )