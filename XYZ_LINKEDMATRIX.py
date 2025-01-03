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
		
		
		
		
		
		#  LinkedList(value)
class Solution:	
	def __init__(self):
		self.dim = []
		
	def ch(self, Zl):
		
		#h = 0##
		mat = []#Z
		
		
		NONE = LinkedList( "None") 
		
		count = 0 # row,col both == 0
		
		ind = 0
		for l in Zl:
			#l = Zl[ind]
		
			dim = [  [] for _ in range( len(l) )   ] 
		
			dim2 = [  [] for _ in range( len(l) )   ] 
		
			dim3 = [  [] for _ in range( len(l) )   ] 
			r=0
			c=0
			while  r < len(l)  :
		
			
			
				while c< len(l[r])           :
				#print(l[r][c], end="")
					R0C0 = LinkedList( l[r][c] ) 
				
				###############################################################
					if len(dim[r]) == r and   len(dim[r]) == c  and r-1== -1 and c-1== -1        and  r == 0 and c == 0         and  len(dim[r]) == 0 :
					#print("1", end=" ")
						R0C0.up = NONE
						R0C0.down = NONE
					
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
					
					
					
					h = ind
					#h = ind
					#h = z2
					
					
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
					
					
						if 0 <= r  < len(mat[h-1])  and  0 <= c  < len(mat[h-1][r])  :# and mat[h-1][r][c] != None      :
							mat[h-1][r][c].below = R0C0 # mat[h][r][c]
							R0C0.above = mat[h-1][r][c]#
							#MAT[h][r][c].above = MAT[h-1][r][c]#
					
					
					
					
					
					
						if 0 <= r-1 < len(mat[h-1])  and  0 <= c  < len(mat[h-1][r-1])  :# and  mat[h-1][r-1][c] != None   :
							mat[h-1][r-1][c].downbelow = R0C0 # mat[h][r][c]
							R0C0.upabove = mat[h-1][r-1][c]#
							#MAT[h][r][c].upabove = MAT[h-1][r-1][c]#
					
						if 0 <= r+1  < len(mat[h-1])  and  0 <= c  < len(mat[h-1][r+1])  :# and   mat[h-1][r+1][c] != None   :
							mat[h-1][r+1][c].upbelow = R0C0 # mat[h][r][c]
							R0C0.downabove = mat[h-1][r+1][c]#
							#MAT[h][r][c].downabove = MAT[h-1][r+1][c]#
					
						if 0 <= r  < len(mat[h-1])  and  0 <= c-1  < len(mat[h-1][r]) :#  and   mat[h-1][r][c-1] != None  :
							mat[h-1][r][c-1].rightbelow = R0C0 # mat[h][r][c]
							R0C0.leftabove = mat[h-1][r][c-1]#
							#MAT[h][r][c].leftabove = MAT[h-1][r][c-1]#
					
						if 0 <= r  < len(mat[h-1])  and  0 <= c+1  < len(mat[h-1][r])  :# and   mat[h-1][r][c+1] != None  :
							mat[h-1][r][c+1].leftbelow = R0C0 # mat[h][r][c]
							R0C0.rightabove = mat[h-1][r][c+1]
							#MAT[h][r][c].rightabove = MAT[h-1][r][c+1]
					
					
					
					
					
						if 0 <= r-1  < len(mat[h-1])  and  0 <= c+1  < len(mat[h-1][r-1])  :# and   mat[h-1][r-1][c+1] != None  :
							mat[h-1][r-1][c+1].bottomleftbelow = R0C0 # mat[h][r][c]
							R0C0.toprightabove = mat[h-1][r-1][c+1]
							#MAT[h][r][c].toprightabove = MAT[h-1][r-1][c+1]
					
						if 0 <= r+1  < len(mat[h-1])  and  0 <= c-1  < len(mat[h-1][r+1])  :# and  mat[h-1][r+1][c-1] != None  :
							mat[h-1][r+1][c-1].toprightbelow = R0C0 # mat[h][r][c]
							R0C0.bottomleftabove = mat[h-1][r+1][c-1]
							#MAT[h][r][c].bottomleftabove = MAT[h-1][r+1][c-1]
					
					
						if 0 <= r-1 < len(mat[h-1])  and  0 <= c-1  < len(mat[h-1][r-1])  :# and  mat[h-1][r-1][c-1] != None  :
							mat[h-1][r-1][c-1].bottomrightbelow = R0C0 # mat[h][r][c]
							R0C0.topleftabove = mat[h-1][r-1][c-1]
							#MAT[h][r][c].topleftabove = MAT[h-1][r-1][c-1]
					
						if 0 <= r+1  < len(mat[h-1])  and  0 <= c+1  < len(mat[h-1][r+1]) :# and  mat[h-1][r+1][c+1] != None  :
							mat[h-1][r+1][c+1].topleftbelow = R0C0 # mat[h][r][c]
							R0C0.bottomrightabove = mat[h-1][r+1][c+1]
							#MAT[h][r][c].bottomrightabove = MAT[h-1][r+1][c+1]
					
					
						#######################################################################################################################
					
						if   r+1  <= len(mat[h-1])  and  c+1  <= len(mat[h-1][r])  :# and mat[h-1][r][c] != None      :
							mat[h-1][r][c].below = R0C0 # mat[h][r][c]
							R0C0.above = mat[h-1][r][c]#
							#MAT[h][r][c].above = MAT[h-1][r][c]#
					
					
					
					
					
					
						#print( MAT[h-1], r,dim , xyz[h-1],"jkk",xyz[h][r][c])
						#MAT[h-1] = dim
						if r > 0 and  r <= len(mat[h-1])   and  c+1  <= len(mat[h-1][r-1])  :# and  mat[h-1][r-1][c] != None   :
							mat[h-1][r-1][c].downbelow = R0C0 # mat[h][r][c]
							R0C0.upabove = mat[h-1][r-1][c]#
							#mat[h][r][c].upabove = mat[h-1][r-1][c]#
					
						if  r+2  <= len(mat[h-1])  and  c+1  <= len(mat[h-1][r]) :# and MAT[h-1][r+1] != []:# and   mat[h-1][r+1][c] != None   : # r + 1
							#print(MAT[h-1][r+1],c,"ccccc")
							mat[h-1][r+1][c].upbelow = R0C0 # mat[h][r][c]
							R0C0.downabove = mat[h-1][r+1][c]#
							#mat[h][r][c].downabove = mat[h-1][r+1][c]#
					
						if r +1 <= len(mat[h-1])  and  c  <= len(mat[h-1][r]) :#  and   mat[h-1][r][c-1] != None  :
							mat[h-1][r][c-1].rightbelow = R0C0 # mat[h][r][c]
							R0C0.leftabove = mat[h-1][r][c-1]#
							#mat[h][r][c].leftabove = mat[h-1][r][c-1]#
					
						if   r+1  <= len(mat[h-1])  and  c+2  <= len(mat[h-1][r])                   :# and   mat[h-1][r][c+1] != None  :
							mat[h-1][r][c+1].leftbelow = R0C0 # mat[h][r][c]
							R0C0.rightabove = mat[h-1][r][c+1]
							#mat[h][r][c].rightabove = mat[h-1][r][c+1]
					
					
					
					
					
						if r>0 and    r  <= len(mat[h-1])  and  c+2  <= len(mat[h-1][r-1])  :# and   mat[h-1][r-1][c+1] != None  :  # r
							mat[h-1][r-1][c+1].bottomleftbelow = R0C0 # mat[h][r][c]
							R0C0.toprightabove = mat[h-1][r-1][c+1]
							#mat[h][r][c].toprightabove = mat[h-1][r-1][c+1]
					
						if r+2  <= len(mat[h-1])  and  c  <= len(mat[h-1][r+1])  :#and MATT[h-1][r+1] != []:# and  mat[h-1][r+1][c-1] != None  : # r+1
							mat[h-1][r+1][c-1].toprightbelow = R0C0 # mat[h][r][c]
							R0C0.bottomleftabove = mat[h-1][r+1][c-1]
							#mat[h][r][c].bottomleftabove = mat[h-1][r+1][c-1]
					
					
						if r>0 and r <= len(mat[h-1])  and  c  <= len(mat[h-1][r-1])  :# and  mat[h-1][r-1][c-1] != None  :  # r
							mat[h-1][r-1][c-1].bottomrightbelow = R0C0 # mat[h][r][c]
							R0C0.topleftabove = mat[h-1][r-1][c-1]
							#mat[h][r][c].topleftabove = mat[h-1][r-1][c-1]
					
						if   r+2  <= len(mat[h-1])  and   c+2  <= len(mat[h-1][r+1]) :#and MAT[h-1][r+1] != []:# and  mat[h-1][r+1][c+1] != None  : # r +1
							#print(MAT[h-1][r+1])
							mat[h-1][r+1][c+1].topleftbelow = R0C0 # mat[h][r][c]
							R0C0.bottomrightabove = mat[h-1][r+1][c+1]
							#mat[h][r][c].bottomrightabove = mat[h-1][r+1][c+1]
					
					
					
					
					
					
				########################
				
					c+= 1
			
			#if c == len(l[r]) :
				#c = 0
				if c == len(l[r]) :
					c = 0
				#print()
				r += 1
			
			
			
			mat.append(dim)# dim2
			
			
			ind += 1
			
			
			
			
		#print(count,"count")	
		#col 9
		def mul(m) :
			mm = 0
			for i in m :
				mm += i
			return mm
			
			#print([[0]*len(dim[i]) for i in range(len(l))])
		#print([len(dim2[i]) for i in range(len(l))],"SEEE",  [len(dim[i]) for i in range(len(l))  ]   , count )
			
		#print( mul( [len(dim2[i]) for i in range(len(l))  ]  ) ,"SEEE", mul( [len(dim[i]) for i in range(len(l))  ]  )   )
		
		#print( count ,"SEEE", mul( [len(dim[i]) for i in range(len(l))  ]  )   )
		
		#self.dim = dim
		
		#print(len([x.value  for z in mat for y in z for x in y]),    [ [x.value  for x in y] for z in mat for y in z ] )
		#print(mat)
		return mat# dim
			
	def printList(self, dim):
		currRow = dim[0][0]
		
		r = 0
		c =  0
		while r<len(dim):
			#if currCol == None :
			currCol = currRow
			while c< len(dim[r]) and currCol != None:
				print(currCol.value, end=" ")
				currCol = currCol.right
				c+= 1
			print()
			if c == len(dim[r]) :
				c = 0
				currRow = currRow.down
			r+= 1
			
	def printList1(self, dim):
		currRow = dim[0][0]
		while currRow:
			currCol = currRow
			while currCol:
				print(currCol.value, "->",end=" ")
				currCol = currCol.right
			print()
			currRow = currRow.down
			
	def printList2(self, dim): # dim == mat
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

Obj = Solution() # Obj.

xyz = [ [[1,2,3],
	[4,5,6]] ,
	
	[[7,8,9],        # <<<
	[10,11,12]]  ,
	
	[[13,14,15], 
	[16,17,18]]  ]


xyz = [ [[1,2,3],
	[4,5,6]] ,
	
	[[7,8,9],        # <<<
	[10,11,12],
	[13,14,15]]  ,
	
	[[13,14,15],
	[16,17,18]]  ]

Obj.ch(xyz)
Obj.printList2(Obj.ch( xyz ) )


"""


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


if  h > 0:
	
	if mat[h-1][r][c] != None and      0 <= r  < len(mat[h-1])  and  0 <= c  < len(mat[h-1][r])   :
		mat[h-1][r][c].below = mat[h][r][c]
		mat[h][r][c].above = mat[h-1][r][c]#
		
		
		
		
		
		
	if mat[h-1][r-1][c] != None and      0 <= r  < len(mat[h-1])  and  0 <= c  < len(mat[h-1][r])   :
		mat[h-1][r-1][c].downbelow = mat[h][r][c]
		mat[h][r][c].upabove = mat[h-1][r-1][c]#
		
	if mat[h-1][r+1][c] != None and      0 <= r  < len(mat[h-1])  and  0 <= c  < len(mat[h-1][r])   :
		mat[h-1][r+1][c].upbelow = mat[h][r][c]
		mat[h][r][c].downabove = mat[h-1][r+1][c]#
		
	
	if mat[h-1][r][c-1] != None and      0 <= r  < len(mat[h-1])  and  0 <= c  < len(mat[h-1][r])   :
		mat[h-1][r][c-1].rightbelow = mat[h][r][c]
		mat[h][r][c].leftabove = mat[h-1][r][c-1]#
		
	if mat[h-1][r][c+1] != None and      0 <= r  < len(mat[h-1])  and  0 <= c  < len(mat[h-1][r])   :
		mat[h-1][r][c+1].leftbelow = mat[h][r][c]
		mat[h][r][c].rightabove = mat[h-1][r][c+1]
		
		
		
		
		
		
	if mat[h-1][r-1][c+1] != None and      0 <= r  < len(mat[h-1])  and  0 <= c  < len(mat[h-1][r])   :
		mat[h-1][r-1][c+1].bottomleftbelow = mat[h][r][c]
		mat[h][r][c].toprightabove = mat[h-1][r-1][c+1]
		
	if mat[h-1][r+1][c-1] != None and      0 <= r  < len(mat[h-1])  and  0 <= c  < len(mat[h-1][r])   :
		mat[h-1][r+1][c-1].toprightbelow = mat[h][r][c]
		mat[h][r][c].bottomleftabove = mat[h-1][r+1][c-1]
		
		
	if mat[h-1][r-1][c-1] != None and      0 <= r  < len(mat[h-1])  and  0 <= c  < len(mat[h-1][r])   :
		mat[h-1][r-1][c-1].bottomrightbelow = mat[h][r][c]
		mat[h][r][c].topleftabove = mat[h-1][r-1][c-1]
		
	if mat[h-1][r+1][c+1] != None and      0 <= r  < len(mat[h-1])  and  0 <= c  < len(mat[h-1][r])   :
		mat[h-1][r+1][c+1].topleftbelow = mat[h][r][c]
		mat[h][r][c].bottomrightabove = mat[h-1][r+1][c+1]
		


"""
		