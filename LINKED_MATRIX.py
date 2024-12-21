class LinkedList:
	def __init__(self, value=None, up=None, down = None, left=None, right=None ,  topleft=None  , topright=None , bottomleft=None , bottomright=None ):
		self.value = value
		self.up = up
		self.down = down
		self.left = left
		self.right = right 
		
		
		self.topleft = topleft
		self.topright = topright
		
		self.bottomleft = bottomleft
		self.bottomright = bottomright
		
		#  LinkedList(value)
class Solution:	
	def __init__(self):
		self.dim = []
	def ch(self, l):
		r=0
		c=0
		dim = [  [] for _ in range( len(l) )   ] 
		
		dim2 = [  [] for _ in range( len(l) )   ] 
		
		dim3 = [  [] for _ in range( len(l) )   ] 
		
		NONE = LinkedList( "None") 
		
		count = 0 # row,col both == 0
		
		
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
				
					print("0 R, 0 C, HERE",l[r][c])
					R0C0.topleft = NONE  # v
					R0C0.topright = NONE
				
					NONE.bottomright = R0C0 # ^
					NONE.bottomleft = R0C0
					dim2[r].append(R0C0) 
					count += 1
				
				
				
				if (r == 0 ) and (1 <=  c  and len(dim2[r])>=1) :
					
					print("0 R HERE",l[r][c])
					R0C0.topleft = NONE  # v
					R0C0.topright = NONE
					
					NONE.bottomright = R0C0 # ^
					NONE.bottomleft = R0C0
					dim2[r].append(R0C0) 
					count += 1
					
				if (c == 0 and dim2[r]==[])  and len(dim2[r]) == 0 and          dim2[r-1] != [] and len(dim2[r-1])>0:
					print("0 C HERE",l[r][c])
					R0C0.topleft = NONE
					R0C0.bottomleft = NONE # >
					
					
					NONE.bottomright = R0C0 # <
					NONE.topright = R0C0 
					dim2[r].append(R0C0) 
					count += 1
				
				if len(dim2[r]) + 1 == len(dim2[r-1]) and  1<=r<=len(l)-1 and 1<=c<=len(l[r])-1  and   dim2[r-1] != []   and len(dim2[r-1]) >=1 and c+1 == len(dim2[r-1])  and c == len(dim2[r]) :
					print("> 1 HERE",l[r][c])
					R0C0.topleft = dim2[r-1][c-1] 
					dim2[r-1][c-1].bottomright = R0C0
					dim2[r].append(R0C0) 
					count += 1
					
				if  len(dim2[r])  == len(dim2[r-1])  and   1<=r<=len(l)-1 and 1<=c<=len(l[r])-1 and   dim2[r-1] != []   and len(dim2[r-1]) >=1 and c==len(dim2[r-1])  and c == len(dim2[r]):
					print("> 2 HERE",l[r][c])
					R0C0.topleft = dim2[r-1][c-1] 
					dim2[r-1][c-1].bottomright = R0C0
					dim2[r].append(R0C0) 
					count += 1
					
				if len(dim2[r]) + 2 <= len(dim2[r-1]) and  1<=r<=len(l)-1 and 1<=c<=len(l[r])-1  and   dim2[r-1] != []   and len(dim2[r-1]) >=1 and c+1<=len(dim2[r-1]) and c == len(dim2[r]):
					print("> 3 HERE",l[r][c])
					R0C0.topleft = dim2[r-1][c-1] 
					R0C0.topright = dim2[r-1][c+1] 
					
					dim2[r-1][c-1].bottomright = R0C0
					dim2[r-1][c+1].bottomleft = R0C0
					
					dim2[r].append(R0C0) 
					count += 1
					
				if len(dim2[r]) > len(dim2[r-1]) and  1<=r<=len(l)-1 and len(l[r-1])<=c<=len(l[r])-1 and  len(dim2[r-1])>=1   and dim2[r-1] != [] and c > len(dim2[r-1])        and c == len(dim2[r]):
					print("> 4 HERE",l[r][c])
					R0C0.topleft = NONE
					R0C0.topright = NONE
					NONE.bottomright = R0C0
					NONE.bottomleft = R0C0
					dim2[r].append(R0C0) 
					count += 1
					
				########################
				
				c+= 1
			
			#if c == len(l[r]) :
				#c = 0
			if c == len(l[r]) :
				c = 0
			print()
			r += 1
		#print(count,"count")	
		#col 9
		def mul(m) :
			mm = 0
			for i in m :
				mm += i
			return mm
			
			#print([[0]*len(dim[i]) for i in range(len(l))])
		print([len(dim2[i]) for i in range(len(l))],"SEEE",  [len(dim[i]) for i in range(len(l))  ]   , count )
			
		#print( mul( [len(dim2[i]) for i in range(len(l))  ]  ) ,"SEEE", mul( [len(dim[i]) for i in range(len(l))  ]  )   )
		
		#print( count ,"SEEE", mul( [len(dim[i]) for i in range(len(l))  ]  )   )
		
		#self.dim = dim
		return dim
			
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
			
	def printList2(self, dim):
		currRow = dim[0][0]
		while currRow:
			currCol = currRow
			while currCol:
				
					
				if currCol.left != None and currCol.right != None :
					
					
					space = ' '* (  len(str(currCol.left.value)) +  len("<-") + len(str(currCol.value))  )
					
					if currCol.up!= None :
						print(space, currCol.up.value)
						print(space+" ^")
					print(currCol.left.value, "<-",currCol.value,"->",currCol.right.value,end=" ")
					
					
					if currCol.down!= None :
						print()
						print(space+" V")
						print(space,currCol.down.value)
						
				
				#print(end=" ")
				#print()
				currCol = currCol.right
			#print(end=" ")
			print("------------------")
			print()
			currRow = currRow.down

Obj = Solution() # Obj.


l = [[1,2],  # 1
	 [1,2],  # 1
	 [1,2]]  # 1

Obj.ch(l)
Obj.printList1(Obj.ch(l) )
#Obj.printList2(Obj.ch(l) )
print("#############################################")



##################
l = [[1,2],    # 1
	 [1,2],    # 1
	 [1,2,3]]  # 2

Obj.ch(l)
Obj.printList1(Obj.ch(l) )
#Obj.printList2(Obj.ch(l) )
print("#############################################")

l = [[1,2],   # 1
	 [1,2,3], # 2
	 [1,2]]   # 1

Obj.ch(l)
Obj.printList1(Obj.ch(l) )
#Obj.printList2(Obj.ch(l) )
print("#############################################")

l = [[1,2,3],  # 2
	 [1,2],    # 1
	 [1,2]]    # 1

Obj.ch(l)
Obj.printList1(Obj.ch(l) )
#Obj.printList2(Obj.ch(l) )
print("#############################################")
#################



#################
l = [[1,2],    # 1
	 [1,2,3],  # 2
	 [1,2,3]]  # 2

Obj.ch(l)
Obj.printList1(Obj.ch(l) )
#Obj.printList2(Obj.ch(l) )
print("#############################################")

l = [[1,2,3],  # 2
	 [1,2],    # 1
	 [1,2,3]]  # 2

Obj.ch(l)
Obj.printList1(Obj.ch(l) )
#Obj.printList2(Obj.ch(l) )
print("#############################################")

l = [[1,2,3],  # 2
	 [1,2,3],  # 2
	 [1,2]]    # 1

Obj.ch(l)
Obj.printList1(Obj.ch(l) )
#Obj.printList2(Obj.ch(l) )
print("#############################################")
#################



################
l = [[1,2],      # 1
	 [1,2,3],    # 2
	 [1,2,3,4]]  # 3

Obj.ch(l)
Obj.printList1(Obj.ch(l) )
#Obj.printList2(Obj.ch(l) )
print("#############################################")

l = [[1,2],      # 1
	 [1,2,3,4],  # 3
	 [1,2,3]]    # 2

Obj.ch(l)
Obj.printList1(Obj.ch(l) )
#Obj.printList2(Obj.ch(l) )
print("#############################################")

l = [[1,2,3],    # 2
	 [1,2],      # 1
	 [1,2,3,4]]  # 3

Obj.ch(l)
Obj.printList1(Obj.ch(l) )
#Obj.printList2(Obj.ch(l) )
print("#############################################")

l = [[1,2,3],    # 2
	 [1,2,3,4],  # 3
	 [1,2]]      # 1

Obj.ch(l)
Obj.printList1(Obj.ch(l) )
#Obj.printList2(Obj.ch(l) )
print("#############################################")

l = [[1,2,3,4],  # 3
	 [1,2],      # 1
	 [1,2,3]]    # 2

Obj.ch(l)
Obj.printList1(Obj.ch(l) )
#Obj.printList2(Obj.ch(l) )
print("#############################################")

l = [[1,2,3,4],  # 3
	 [1,2,3],    # 2
	 [1,2]]      # 1

Obj.ch(l)
Obj.printList1(Obj.ch(l) )
#Obj.printList2(Obj.ch(l) )
print("#############################################")

"""
len(l)

dim = [  [] for _ in range( len(r) )   ]  # add

#dim = [  [0]*len(l[r]) for _ in range( len(r) )   ]  # change

													#  add                              change
while R0C0 = LinkedList( l[r][c] )  while here.....  dim[r].append(R0C0)    #### dim[r][c] == R0C0





# add
###########################################################
if len(dim[r]) == r and   len(dim[r]) == c  and r-1== -1 and c-1== -1        and  r == 0 and c == 0:
R0C0.up = None
R0C0.down = None

R0C0.left = None
R0C0.right = None

dim[r].append(R0C0)  

if len(dim[r]) == c    and r-1==-1 and 0<=c-1<len(l[r]) :
R0C0.up = None
R0C0.down = None

R0C0.left = dim[r][c-1]  #
dim[r][c-1].right = R0C0 #
R0C0.right = None

dim[r].append(R0C0) 


if dim[r-1] != []    and 0<=r-1<len(r) and c-1==-1  :
R0C0.up = dim[r-1][c]  #
dim[r-1][c].down = R0C0 #
R0C0.down = None

R0C0.left = None
R0C0.right = None

dim[r].append(R0C0) 


if len(dim[r]) == c  and  dim[r-1] != []        and 0<=r-1<len(r) and 0<=c-1<len(l[r])  :
R0C0.up = dim[r-1][c]  #
dim[r-1][c].down = R0C0 #
R0C0.down = None

R0C0.left = dim[r][c-1]  #
dim[r][c-1].right = R0C0 #
R0C0.right = None

dim[r].append(R0C0) 
#################################################################


# change


if dim[r][c] == 0   and r-1== -1 and c-1== -1        and  r == 0 and c == 0:
R0C0.up = None
R0C0.down = None

R0C0.left = None
R0C0.right = None

dim[r][c] == R0C0


if dim[r][c] == 0  and dim[r][c-1] != 0   and r-1==-1 and 0<=c-1<len(l[r]) :
R0C0.up = None
R0C0.down = None

R0C0.left = dim[r][c-1]  #
dim[r][c-1].right = R0C0 #
R0C0.right = None

dim[r][c] == R0C0


if dim[r][c] == 0 and dim[r-1][c] != 0     and 0<=r-1<len(r) and c-1==-1  :
R0C0.up = dim[r-1][c]  #
dim[r-1][c].down = R0C0 #
R0C0.down = None

R0C0.left = None
R0C0.right = None

dim[r][c] == R0C0 


if dim[r][c] == 0  and      dim[r][c-1] != 0 and dim[r-1][c] != 0        and 0<=r-1<len(r) and 0<=c-1<len(l[r])  :
R0C0.up = dim[r-1][c]  #
dim[r-1][c].down = R0C0 #
R0C0.down = None

R0C0.left = dim[r][c-1]  #
dim[r][c-1].right = R0C0 #
R0C0.right = None

dim[r][c] == R0C0

#####################################################################################################


len(r) # r

len(l[r]) # c
"""