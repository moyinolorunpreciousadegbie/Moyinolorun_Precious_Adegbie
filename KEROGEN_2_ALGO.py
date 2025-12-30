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
		self.cvv = 1
		
	def inorder(self, x):
		if x is None:
			return
		self.inorder(x.left)
		#print(x.val)
		#print([x.val, x.string ] )
		#print( x.string  + [float(x.val)]  , self.cvv)
		#self.cvv += 1
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
def product(iterables, variables):
	
	pools = iterables
	#print(pools	,'here')
	
	pools_vvv = variables
	pools_nnn = variables
	
	q = []
	result = [[]]
	cn= 0
	
	q_vvv = []
	result_vvv = [""]
	
	q_nnn = []
	result_nnn = [[]]
	
	source_num = {}
	
	ind_vvv = 0
	ind_nnn = 0
	Obj = RBTree()
	for pool in pools:############
		pool_vvv = pools_vvv[ind_vvv]
		pool_nnn = pools_nnn[ind_nnn]
		q = []#########
		q_vvv = []
		q_nnn = []
		ind_vvv_vvv = 0
		ind_nnn_nnn = 0
		for x in result :#######
			x_vvv = result_vvv[ind_vvv_vvv]
			x_nnn = result_nnn[ind_nnn_nnn]
			if  len( x ) == (len(iterables)  ) : break############
			if len(x_vvv) == (len(variables)  ) : break
			if len(x_nnn) == (len(variables)  ) : break
			
			ind_vvv_vvv_vvv = 0
			ind_nnn_nnn_nnn = 0
			for y in pool :############# 
				y_vvv = pool_vvv[ind_vvv_vvv_vvv]
				y_nnn = pool_nnn[ind_nnn_nnn_nnn]
				
				#if  len( x+[y] ) == (repeat * len(iterables)  )  : print(x+[y] , cn) # 365     876
				lass = x+[y]
				sum_lass = sum(lass)
				
				if x_vvv == "" :
					lass_vvv = y_vvv  
				if x_vvv != "" :
					lass_vvv = x_vvv+", "+y_vvv 
					
				lass_nnn = x_nnn + [y_nnn]
					
				if  len( lass  ) == ( len(iterables)  ) : ##############
					if sum_lass not in source_num :
						source_num[sum_lass] = []
					source_num[sum_lass].append(lass_vvv)
					#print(lass , sum_lass , lass_vvv)########
					cn += 1
					#print( sum_lass , lass_nnn , cn)
					 
					#print(cn)
				#if ind_vvv  >= len(variables)  :
					Obj.insert(float(sum_lass) , lass_nnn )
					
				q.append( lass   )###########
				
				q_vvv.append(lass_vvv)
				
				q_nnn.append(lass_nnn)
				
				ind_vvv_vvv_vvv +=1
				ind_nnn_nnn_nnn +=1
			ind_vvv_vvv += 1
			ind_nnn_nnn += 1
		
		ind_vvv += 1
		ind_nnn += 1
		
		result = q
		
		result_vvv = q_vvv
		result_nnn = q_nnn
		
		#for k ,v in source_num.items():
			#print(k,v, len(v))
			#print()
	Obj.printInOrder()  # after adding all sort print
	
	AN = Obj.ANS
	#print(AN , len(AN))
		
	return AN  # or q 

all_variables = [ [1,2,3,4] ,       # 4
					[1,2,2.5,3] ,         # 4
					[1,2,2.5,3,4] ,   # 5
					[1,2,2.5,3] ]     # 4
				
				
Kerogen_Conversion_and_Maturity  = [ "Oil zone" , "Condensate wet gas zone" , "Dry gas zone" ,  "Immature" ] # 4
	
Kerogen_Type_and_Maturity = [ "Type I Kerogen" ,  "Type II Kerogen" ,  "Type III Kerogen"  ] # 3
	
Kerogen_Quality_Plot =  [  "Type I Kerogen oil prone usually lacustrine" , 
							"Type II Kerogen oil prone usually marine" , "Mixed Type II/III Kerogen (oil/gas prone)" ,
							"Type III Kerogen (gas prone)" , "Type IV (dry gas prone)" ]  # 5

Pseudo_Van_Krevelen_Plot  = [ "Type I Kerogen (highly oil prone)"  , "Type II Kerogen (oil prone)"  ,
								"Mixed Type II/III Kerogen (oil/gas prone)" , "Type III Kerogen (gas prone)" ] # 4

############## 
Kerogen_Conversion_and_Maturity  = [ "Oil Zone" , "Condensate Wet Gas Zone" , "Dry Gas Zone"  ,  "Immature"  ]   # 4

	
Kerogen_Type_and_Maturity =  ["TYPE I KEROGEN"  ,  "TYPE II KEROGEN" , "TYPE II/III KEROGEN" ,  "TYPE III KEROGEN"  ] # 4
	
	
	
Kerogen_Quality_Plot =  [  "Type I: Oil Prone Usually Lacustrine"  ,      "Type II: Oil Prone Usually Marine"  ,
            "Mixed Type II / III Oil / Gas Prone"  , "Type III: Gas Prone"  ,  "Dry Gas Prone"   ]                   # 5

	
Pseudo_Van_Krevelen_Plot  = [ "TYPE I KEROGEN Oil Prone"  , "TYPE II KEROGEN Oil Prone" , "Mixed Type II/III KEROGEN" , "TYPE III KEROGEN Gas Prone"  ] # 4
	
	
	
	
#variables = [Pseudo_Van_Krevelen_Plot]+[Kerogen_Quality_Plot]+[Kerogen_Type_and_Maturity]+[Kerogen_Conversion_and_Maturity]
variables = [Kerogen_Conversion_and_Maturity]+[Kerogen_Type_and_Maturity]+[Kerogen_Quality_Plot]+[Pseudo_Van_Krevelen_Plot]


#all_variables = [ list(range(1,1+len(lenghts))) for lenghts in variables]
#print( all_variables )

waves_layer_st_num = []
waves_layer_num_st = []
indd = 0
mul = 1
for classifications in variables:
	mul *= len(classifications)
	ind = 0
	string_to_number = {}
	number_to_string = {}
	for types in classifications:
		number_to_string[all_variables[indd][ind]] = types
		string_to_number[types] = all_variables[indd][ind]
		ind += 1
	waves_layer_st_num.append(string_to_number)
	waves_layer_num_st.append(number_to_string)
	indd += 1
		
	#print(waves_layer_st_num)

#print(waves_layer_num_st)
print()
print(mul,"REAL LEN")

iterables= all_variables
mat = product(iterables, variables)
print(mat,len(mat))


