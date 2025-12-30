
############################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
class Node:
	def __init__(self, val , strrrrr):
		# Initialize node attributes
		self.val = val
		self.left = None
		self.right = None
		self.parent = None
		self.string = strrrrr
		
		
		
	def isOnLeft(self):
			# Checks if the node is the left child of its parent
		return self == self.parent.left
	
	def isOnRight(self):
				# Checks if the node is the left child of its parent
		return self == self.parent.right	
	
	def moveDown_l(self, new_parent):
		
		           #       self.parent                               |          x
		        #          /  /     \ \                              |          /\
		#x, self.parent.left /       \ self.parent.right,x      self,|     x.left  x.right
		#          new_parent         new_parent                     |
		#
		#             x                   x
		#             /\                  /\ 
		#      new_parent.left
		#         or
			# Moves the node down by changing its parent
		if self.parent is not None:
			if self.isOnLeft():
				self.parent.left = new_parent
				#else: # 
			if  self.isOnRight():
				self.parent.right = new_parent
		new_parent.parent = self.parent
		self.parent = new_parent
		
		new_parent.left = self #
		#new_parent.right = self #
		#print("LL")
		
	def moveDown_r(self, new_parent):
		
		           #       self.parent                               |          x
		        #          /  /     \ \                              |          /\
		#x, self.parent.left /       \ self.parent.right,x      self,|     x.left  x.right
		#          new_parent         new_parent                     |
		#
		#             x                   x
		#             /\                  /\ 
		#      new_parent.left
		#         or
			# Moves the node down by changing its parent
		if self.parent is not None:
			if self.isOnLeft():
				self.parent.left = new_parent
				#else: # 
			if  self.isOnRight():
				self.parent.right = new_parent
		new_parent.parent = self.parent
		self.parent = new_parent
		
		#new_parent.left = self #
		new_parent.right = self #
		#print("RR")
		
		
class RBTree:
	def __init__(self):
		self.root = None
		self.ANS = []
		self.BIN = ["L"]
		
	def inorder(self, x):
		if x is None:
			return
		self.inorder(x.left)
		#print(x.val)
		#print([x.val, x.string ] )
		self.ANS.append(   x.string  + [float(x.val)]    )
		self.inorder(x.right)
		
		
	def search(self, n):
		##print(n)
		temp = self.root
		while temp is not None:
			if n < temp.val:
				if temp.left is None:
					break
				else:
					temp = temp.left
					
			if temp.val < n:
				if temp.right is None:
					break
				else:
					temp = temp.right
					
			if n == temp.val:
				#return temp
				#print(n)
				break
			
			#print(n,temp.val)
		return temp
	
	def insert(self, n , strrrrr ):
		newNode = Node(n , strrrrr )
		
		
		
		
		# When the tree is empty
		if self.root is None:
			
			self.root = newNode
		else:
			
			temp = self.search(n)
			#print(n,temp.val)
			
				# Value already exists, return
			#if temp.val == n:
				#return
			
				# Connect the new node to the correct node
			
			
			
			if n < temp.val:
				newNode.parent = temp
				temp.left = newNode
				return
			if temp.val < n:					
				newNode.parent = temp
				temp.right = newNode
				return
			
			#############
			if True :
				
				#if temp.val == n:
					#print(temp.val , n,"||")
				if temp.left is None and temp.val == n:
					
					temp.left = newNode
					newNode.parent = temp
					return
				
				if temp.right is None  and temp.val == n:
					
					temp.right = newNode
					newNode.parent = temp
					return
				
				
				
				
				if temp.left is not None    and temp.val == n : # and self.BIN[0] == "L":
					temp.left.moveDown_l( newNode)
					#self.left_successor(temp , newNode )
					#self.BIN[0] = "R"
					return
			
				if temp.right is not None   and temp.val == n : # and self.BIN[0] == "R":
					temp.right.moveDown_r( newNode)
					#self.right_successor(temp , newNode )
					#self.BIN[0] = "L"
					return
		
		
		
		
		
		
	# Prints the in-order traversal of the tree
	def printInOrder(self):
		#print("Inorder:")
		if self.root is None:
			print("Tree is empty")
		else:
			self.inorder(self.root)
			#print() #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
			
			
			
			
			
			
	def leftRotate_(self, z):
						# a
		y = z.right# b
		T2 = y.left
		
		# Perform rotation
		y.left = z
		z.right = T2
		
		z.parent = y
		if T2 != None :
			T2.parent = z
			
			
	def rightRotate_(self, z):
		               #   b
		
		
		y = z.left# a
		T3 = y.right
		
		# Perform rotation
		y.right = z
		z.left = T3
		
		
		z.parent = y
		if T3 != None :
			T3.parent = z
			
			
	def left_successor(self, x , newNode):
			# Finds the in-order successor of the given node
		
		newNode.parent = x#<<<<
		
		
		temp = x.left
		
		while temp.right is not None:
			temp = temp.right#b
			
			
			
		print(newNode.val,temp.val,">>ls")
		newNode.parent = temp
		temp.right = newNode
		#self.leftRotate_(temp.parent)
		
		y = temp.parent.right#z.right# b
		T2 = temp.parent.right.left#y.left
		
		# Perform rotation
		#y.left = temp.parent#z
		temp.parent.right.left = temp.parent#z
		#z.right = T2
		temp.parent.right = T2
		
		#z.parent = y
		temp.parent.parent = y
		if T2 != None :
			T2.parent = temp.parent # z
			
			
	def right_successor(self, x, newNode):
			# Finds the in-order successor of the given node
		
		
		
		
		temp = x.right
		
		while temp.left is not None:
			temp = temp.left#a
			
		print(newNode.val,temp.val,">>rs")
		
		newNode.parent = temp
		temp.left = newNode
		
		#self.rightRotate_(temp.parent)
		
		
		
		y = temp.parent.left#z.left# a
		T3 = temp.parent.left.right#y.right
		
		# Perform rotation
		#y.right = z
		temp.parent.left.right = temp.parent
		#z.left = T3
		temp.parent.left = T3
		
		#z.parent = y
		temp.parent.parent = y
		if T3 != None :
			T3.parent = temp.parent # z
			
			
def rad1(nums):
	Obj = RBTree() 
	
	for i in nums :
		Obj.insert(i)
		#print("*********")	
	Obj.printInOrder()  # after adding all sort print
	
	AN = Obj.ANS
	print(len(AN))
	return AN


############################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

#AL910


def combinations(rang):
	
	from collections import defaultdict
	
	adj = defaultdict(int)
	adj2 = defaultdict(int)
	
	lss = set()
#rangr = tuple(range(1,rang + 1))
	pool = tuple(rang)
	n = len(pool)      
	r = n 
	indices = [n]  * (n)
	cycles = [0] * (n)
	
    #matrix = []   #  <<<<<<<<<<<<<<<<<<<<<
	
    #lisd = ['Kerogen Conversion and Maturity',
       #  'Kerogen Type and Maturity',
       #  'Kerogen Quality Plot',
       #  'Pseudo Van Krevelen Plot']
	
	all_variables = [ [1,2,3,4] ,       # 4
		              [1,2,2.5,3] ,         # 3
					  [1,2,2.5,3,4] ,   # 5
					  [1,2,2.5,3] ]     # 4
	########################################################
	Kerogen_Conversion_and_Maturity  = [ "Oil zone" , "Condensate wet gas zone" , "Dry gas zone" ,  "Immature" ] # 4
	
	Kerogen_Type_and_Maturity = [ "Type I Kerogen" ,  "Type II Kerogen" ,  "Type III Kerogen"  ] # 3
	
	Kerogen_Quality_Plot =  [  "Type I Kerogen oil prone usually lacustrine" , 
							"Type II Kerogen oil prone usually marine" , "Mixed Type II/III Kerogen (oil/gas prone)" ,
							"Type III Kerogen (gas prone)" , "Type IV (dry gas prone)" ]  # 5
	
	Pseudo_Van_Krevelen_Plot  = [ "Type I Kerogen (highly oil prone)"  , "Type II Kerogen (oil prone)"  ,
								"Mixed Type II/III Kerogen (oil/gas prone)" , "Type III Kerogen (gas prone)" ] # 4
	
############## 
	Kerogen_Conversion_and_Maturity  = [ "Oil Zone" , "Condensate Wet Gas Zone" ,
        "Dry Gas Zone"  ,  "Immature"  ]   # 4
	
	
	Kerogen_Type_and_Maturity =  ["TYPE I KEROGEN"  ,  "TYPE II KEROGEN" , "TYPE II/III KEROGEN" ,  "TYPE III KEROGEN"  ] # 4
	
	
	
	Kerogen_Quality_Plot =  [  "Type I: Oil Prone Usually Lacustrine"  ,      "Type II: Oil Prone Usually Marine"  ,
            "Mixed Type II / III Oil / Gas Prone"  , "Type III: Gas Prone"  ,  "Dry Gas Prone"   ] # 5
	
	
	Pseudo_Van_Krevelen_Plot  = [  "TYPE I KEROGEN Oil Prone"  ,    "TYPE II KEROGEN Oil Prone"  , "Mixed Type II/III KEROGEN"   , "TYPE III KEROGEN Gas Prone"  ] # 4
	
	
	
	
	
	#variables = [Pseudo_Van_Krevelen_Plot]+[Kerogen_Quality_Plot]+[Kerogen_Type_and_Maturity]+[Kerogen_Conversion_and_Maturity]
	variables = [Kerogen_Conversion_and_Maturity]+[Kerogen_Type_and_Maturity]+[Kerogen_Quality_Plot]+[Pseudo_Van_Krevelen_Plot]
	#print(variables)
	
	##########################################
	
	lin=[len(i) for i in all_variables]
	mx = max(lin)  ## 5
	
	mat = [[0]* len(all_variables) for _ in range(mx)]
	mat2 = [[0]* len(all_variables) for _ in range(mx)]
	
	cn = 0
	for row in lin:
		
		
		for col in range(row):   # 0-4
			mat[col][cn] = 	all_variables[cn][col]				   # 0-3
			mat2[col][cn]	= 	variables[cn][col]						# 0-5
											# 0-4
			#if row < all_variables
		
		cn += 1
		"""
		[1, 1, 1,  1]
		[2, 2, 2,  2]
		[3, 3, 2.5,2.5]
		[4, 0, 3,  3]
		[0, 0, 4,  0]
		
    #    4  3  5   4
		"""
		
		##########################################
		
		#print(mat2)
	#cyc = [ sum(i) for i in all_variables ]
	cyc = rang
	
	#rang = [i+1 for i in rang ]
	source_num = {}
	Obj = RBTree()
	cgcn = 1
	vish = []
	while n:
		for i in reversed(range(r )):
			
			lss.add( tuple(cycles)  )
			temp = []
			cn=0
			q = []
			
			qw = []
			
			sm = 0
			stringg_joined = ""
			string_list = [] # seperated
			for c in cycles:
				temp.append(  mat[c][cn] )
				
				#temp.append(  [] )
				q.append( mat2[c][cn] +" :"+str( mat[c][cn]))
				qw.append( mat2[c][cn])
				stringg_joined += mat2[c][cn] 
				if cn < len(cycles)-1 :
					stringg_joined += ", " # JOINT STRING !!!
				string_list.append( mat2[c][cn] )
				cn+=1
				
			#temp.append(  [ sum( temp )  ])
			sm = sum( temp ) 
			
				
			Obj.insert(float(sm) , string_list )
			if string_list in vish :
				
				print(cgcn , string_list , float(sm) ,"        <<<<<<<<< DUPL")
				
			else :
				print(cgcn , string_list , float(sm) )
				vish.append( string_list )
			
            #matrixx = qw.append(sm) ##. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
			#print()
			cn = 0
			##print(q,temp, '       ', sm)  # <<<<<<<
			
			adj[  tuple(q) ] = float(sm)
			
			adj2[  tuple(qw) ] = float(sm)
			
			if float(sm) not in source_num :
				source_num[ float(sm) ] = []
			
			source_num[ float(sm) ].append(q)
			
			
			
			#print( float(sm) , stringg_joined )
			
			cycles[i] += 1
			if cycles[i] == rang[i]:
				cycles[i] = 0
			else:
				break 
			
		else:
			break
		cgcn += 1
	
	#print(adj)
	#sorted_dict = dict(sorted(adj.items(), key=lambda x: x[1]))
	
	#sorted_dict2 = dict(sorted(adj2.items(), key=lambda x: x[1]))
	#print(sorted_dict2)
	#print(sorted_dict)
	#return sorted( lss  ,key=sum)
	#return sorted_dict,  sorted_dict2
	Obj.printInOrder()  # after adding all sort print
	
	AN = Obj.ANS
	#print(AN , len(AN))
	
	return AN  # or q 

rang = [ 4 , 4 , 5 , 4 ]

mat = combinations(rang)

#mat = []
print( mat , len(mat) )

#lop = combinations(rang)[0]

#lloopp = combinations(rang)[1]

mat
	

#print(lloopp)
#print()
#print("############################################################################################################################################")
#print()
#print(lop)

"""
for k, v in lloopp.items():
	tem = []
	for kk in k :
		tem.append(kk)
	
	tem.append(v)
	mat.append(tem)
	
print(mat,">>>>:::::")
"""
