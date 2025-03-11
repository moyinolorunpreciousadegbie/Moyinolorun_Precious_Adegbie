#!/usr/bin/env python3
class Listnode:
	def __init__(self, path=None, steps=None, rk = None, prev=None, next = None):
		self.path = path
		self.steps = steps
		self.rk = rk
		
class MyCircularDeque:
	def __init__(self, k):
			self.max_size = k
			self.cnt = 0
			self.all = [0]
		
		
		
	def insertFront(self, path, steps, rk):
		
		
		if  self.cnt == self.max_size :
			return False
		
		if  self.cnt == 0 :
			head = Listnode()
			tail = Listnode()
			head.next = tail
			tail.prev = head
			self.all[0] = [head,tail]
			
			
		if  self.cnt < self.max_size :
			node =  Listnode(path, steps, rk)
			head = self.all[0][0]
			node.prev = head
			node.next = head.next
			head.next.prev = head.next = node
			self.cnt += 1
			return True
		
		
		
		
	def insertLast(self, path, steps, rk):
		
		
		if  self.cnt == self.max_size :
			return False
		
		if  self.cnt == 0 :
			head = Listnode()
			tail = Listnode()
			head.next = tail
			tail.prev = head
			self.all[0] = [head,tail]
			
			
		if  self.cnt < self.max_size :
			node =  Listnode(path, steps, rk)
			tail = self.all[0][1]  ####
			node.next = tail
			node.prev = tail.prev
			tail.prev.next = tail.prev  = node
			self.cnt += 1
			return True
		
		
		
		
	########################################	
		
		
	def deleteFront(self) :
		if self.cnt == 0 :
			return False
		front = self.all[0][0].next
		
		node = front
		node.prev.next = node.next
		node.next.prev = node.prev
		self.cnt -=1 
		return True
	
	
	
	def deleteLast(self):
		if self.cnt == 0 :
			return False
		back = self.all[0][1].prev
		
		node = back
		node.prev.next = node.next
		node.next.prev = node.prev
		self.cnt -=1 
		return True
	
	
	##########
	
	
	def getFront(self) :
		if self.cnt == 0 :
			return -1
		front = self.all[0][0].next
		node_path = front.path
		node_steps = front.steps
		node_rk = front.rk
		return front#node_path ,  node_steps ,  node_rk
	
	
	def getRear(self):
		if self.cnt == 0 :
			return -1
		back = self.all[0][1].prev
		node_path = back.path
		node_steps = back.steps
		node_rk = back.rk
		return back#node_path ,  node_steps ,  node_rk
	
	
	
	##########
	
	
	def isEmpty(self) :
		if self.cnt == 0 :
			return True
		return False
	
	def isFull(self) :
		if self.cnt == self.max_size :
			return True
		return False
	
	
	
	###############
	
	def getatIndex(self, index: int) -> int:
			head = self.all[0][0] # head
			while head and index > 0:
				head = head.next
				index -= 1
				
			if head and head != self.all[0][1] and index == 0:
				node = head.next
				return node  #node.path , node.steps ,  node.rk
			return -1
	
	###############
	
	def addmanyAtIndex( self, index_three , path_steps_rk) :
		for path, steps, rk in path_steps_rk :
			self.addAtIndex( index_three ,             path, steps, rk)
			index_three+=1
			
	def addAtIndex(self, index, path, steps, rk):
		head = self.all[0][0]  # head
		while head and index > 0:
			head = head.next
			index -= 1
			
		if head and index == 0:
			node = Listnode(path, steps, rk)
			node.prev = head
			node.next = head.next
			head.next.prev = head.next = node
			
			
			#node.next = head
			#node.prev = head.prev
			#head.prev.next = head.prev = node
			self.cnt += 1
################################################################################################				
			
	def deleteAtIndex(self, index: int) :
		head = self.all[0][0] # head
		while head and index > 0:
			head = head.next 
			index -= 1
			
		if head and head != self.all[0][1] and index == 0:
			node = head.next
			node.prev.next = node.next
			node.next.prev = node.prev
			self.cnt -= 1
			
################################################################################################
			

####################################################################################
	
	def printList(self):
		head = self.all[0][0] # head
		head = head.next
		while head != None and head.path != None : #  head.steps!=None and  head.rk != None
			print(head.path,"->",end=" ")
			head = head.next
			
			
###############################################################################################################################################################
class Solution:
	def shortestPath(self, grid: list[list[int]], k: int) -> int:
		rows = len(grid)
		cols = len(grid[0])
		# Directions we'll use to change our location (down, up, right, left).
		directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
		# We'll use a deque for our BFS traversal.
		#q = collections.deque([])
		q  = MyCircularDeque(float('inf'))
		#head = q.all[0][0] # head
		#tail = q.all[0][1] # tail
		# Append our starting details to the q.
		# (row, col, steps, k)
		
		
		
		#q.append((0, 0, 0, k))
		q.insertLast( [[0, 0]], 0, k )
		
		w = MyCircularDeque(float('inf'))
		w.insertLast( [0, 0] , None, None )
		# q.insertLast( w , 0, k )
		#print(q.getRear().path)
		# Use a set (O(1) lookup) to track the locations we've visited to avoid revisiting.
		# We track (r, c, k) - k: is tracked because there might be multiple ways to get to
		# a give (r, c) on the grid. With the addition of k, it ensures that multiple path
		# options can be explored, instead of simply eliminating a (r, c) after the first visit.        .next       .prev
		seen = set()
		mn = float('inf')
		PP = []
		mp = {}
		#q.getRear()  
		#q.getFront()  
		#q.insertFront(path, steps, rk)
		#q.insertLast(path, steps, rk)
		#q.deleteFront() 
		#q.deleteLast()
		#while       head.next.path != None         and          head.next.steps!=None           and              head.next.rk != None:
		while       q.all[0][1].prev.path != None       and       q.all[0][1].prev.steps!=None        and          q.all[0][1].prev.rk != None and q.getRear() != -1:
		#while       q.getFront() != -1:
			# Pop the next location from the q.
			NODE = q.getRear()
			#NODE = q.deleteLast()
			path, steps, rk = NODE.path , NODE.steps , NODE.rk 
			
			r , c = path[-1]  # path[-1][0]  ,   path[-1][1]
			# If we're at the finish location return the steps, given BFS this will be
			# guaranteed to be the first to hit this condition.
			q.deleteLast()           #  00      01 10       20    02 good 
									 #  00      -11 -10       50    03 bad (out of bounds)    R_5   C_3  wont be appended
									# 00 deleted forever never to be re-used
			if r == rows-1 and c == cols - 1:
				print(path) # [[0, 0]]
				PP.append(path)
				if NODE.rk == 0 :
					
					mn = min(mn, len(path)-1)
					
				#return steps
			# Otherwise we'll keep travelling throught the grid in our 4 directions.
				#else:
					#QQ  = MyCircularDeque(float('inf'))
			for y, x in directions:
				nr = r + y
				nc = c + x
					# If the new location is on the board and has not been visited.
				if 0 <= nr < rows and 0 <= nc < cols :#and (nr, nc, rk) not in seen:
						# If it's a blocker but we still have k left, we'll go there and k -= 1.
					if grid[nr][nc] == 1 and rk > 0 and [nr, nc] not in path:
							#seen.add((nr, nc, rk))
						#q.append((nr, nc, steps + 1, rk - 1))
						q.insertLast(path + [[nr, nc]], steps+1, rk-1)
						
						# Otherwise continue on  if it's a 0 - free location.
					elif grid[nr][nc] == 0 and [nr, nc] not in path:
							#seen.add((nr, nc, rk))
						#q.append((nr, nc, steps + 1, rk))
						q.insertLast(path + [[nr, nc]], steps+1, rk)
						
						#if  nr < 0 or  rows <= nr        or     nc < 0 or  cols <= nc :
						#NODE.prev.next = NODE.next
						#NODE.next.prev = NODE.prev
						#q  = QQ
			#head = q.all[0][0] # head
			#tail = q.all[0][1] # tail
			#QQ = MyCircularDeque(float('inf'))
			
			#head = head.next
		li = []
		for i in PP:
			if len(i) - 1 == mn :
				li.append(i)
				
		print(mn, li)	
		# If we don't hit the end in our traversal we know it's not possible.
		return -1
	
	
	
Obj = Solution()

grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]
k = 1
#Output: 6
print( Obj.shortestPath(grid, k) )
print()
































"""
###############################################################################################################################################################
class Solution:
	def shortestPath(self, grid: list[list[int]], k: int) -> int:
		rows = len(grid)
		cols = len(grid[0])
		# Directions we'll use to change our location (down, up, right, left).
		directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
		# We'll use a deque for our BFS traversal.
		#q = collections.deque([])
		q  = MyCircularDeque(float('inf'))
		#head = q.all[0][0] # head
		#tail = q.all[0][1] # tail
		# Append our starting details to the q.
		# (row, col, steps, k)
		
				
		#q.append((0, 0, 0, k))
		#q.insertLast( [[0, 0]], 0, k )
		
		w = MyCircularDeque(float('inf'))
		w.insertLast( [0, 0] , None, None )
		q.insertLast( w , 0, k )
		#print(q.getRear().path)
		# Use a set (O(1) lookup) to track the locations we've visited to avoid revisiting.
		# We track (r, c, k) - k: is tracked because there might be multiple ways to get to
		# a give (r, c) on the grid. With the addition of k, it ensures that multiple path
		# options can be explored, instead of simply eliminating a (r, c) after the first visit.        .next       .prev
		seen = set()
		mn = float('inf')
		PP = []
		mp = {}
		#q.getRear()  
		#q.getFront()  
		#q.insertFront(path, steps, rk)
		#q.insertLast(path, steps, rk)
		#q.deleteFront() 
		#q.deleteLast()
		#while       head.next.path != None         and          head.next.steps!=None           and              head.next.rk != None:
		while       q.all[0][1].prev.path != None       and       q.all[0][1].prev.steps!=None        and          q.all[0][1].prev.rk != None and q.getRear() != -1  :
		#while       q.getFront() != -1:
			# Pop the next location from the q.
			NODE = q.getRear()
			#NODE = q.deleteLast()
			path, steps, rk = NODE.path , NODE.steps , NODE.rk 
			path_temp = path
			
			r , c = path.all[0][1].prev.path   # path[-1][0]  ,   path[-1][1]
			#print([r,c])
			# If we're at the finish location return the steps, given BFS this will be
			# guaranteed to be the first to hit this condition.
			q.deleteLast()           #  00      01 10       20    02 good 
									 #  00      -11 -10       50    03 bad (out of bounds)    R_5   C_3  wont be appended
									# 00 deleted forever never to be re-used
			if r == rows-1 and c == cols - 1:
				path.printList() # [[0, 0]]
				print()
				print(lenn( path.all[0][0] ))
				PP.append(path)
				if NODE.rk == 0 :
					
					mn = min(mn, lenn( path.all[0][0] ))
					
				#return steps
			# Otherwise we'll keep travelling throught the grid in our 4 directions.
				#else:
					#QQ  = MyCircularDeque(float('inf'))
					#path_temp = path
			for y, x in directions:
				nr = r + y
				nc = c + x
					# If the new location is on the board and has not been visited.
				if 0 <= nr < rows and 0 <= nc < cols :#and (nr, nc, rk) not in seen:
						# If it's a blocker but we still have k left, we'll go there and k -= 1.
					if grid[nr][nc] == 1 and rk > 0 and find( path.all[0][1], [nr, nc] ) == False:
							#seen.add((nr, nc, rk))
						#q.append((nr, nc, steps + 1, rk - 1))
						
						
						node =  Listnode([nr,nc], None, None)
						#    tail = NODE.path.all[0][1]  ####
						node.next = path_temp.all[0][1]
						node.prev = path_temp.all[0][1].prev
						path_temp.all[0][1].prev.next = path_temp.all[0][1].prev  = node
						q.insertLast(path_temp, steps+1, rk-1)
						
						#path.deleteLast()
						#deleteLast_(path.all[0][1])
						#path = path_temp
						#print("yes")
						
						# Otherwise continue on  if it's a 0 - free location.
					elif grid[nr][nc] == 0 and  find( path.all[0][1], [nr, nc] ) == False:
							#seen.add((nr, nc, rk))
						#q.append((nr, nc, steps + 1, rk))
						node =  Listnode([nr,nc], None, None)
						#    tail = NODE.path.all[0][1]  ####
						node.next = path_temp.all[0][1]
						node.prev = path_temp.all[0][1].prev
						path_temp.all[0][1].prev.next = path_temp.all[0][1].prev  = node
						q.insertLast(path_temp, steps+1, rk)
						
						#path.deleteLast()
						#deleteLast_(path.all[0][1])
						#path = path_temp
						#print("yes_")
						
						#if  nr < 0 or  rows <= nr        or     nc < 0 or  cols <= nc :
						#NODE.prev.next = NODE.next
						#NODE.next.prev = NODE.prev
						#q  = QQ
			#head = q.all[0][0] # head
			#tail = q.all[0][1] # tail
			#QQ = MyCircularDeque(float('inf'))
						#path = path_temp
			#head = head.next
		li = []
		for i in PP:
			if lenn( i.all[0][0] ) - 1 == mn :
				li.append(i)
				
		print(mn, li)	
		# If we don't hit the end in our traversal we know it's not possible.
		return -1
	
	
	
Obj = Solution()

grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]
k = 1
#Output: 6
print( Obj.shortestPath(grid, k) )
print()


###############################################################################################################################################################
###############################################################################################################################################################
###############################################################################################################################################################
###############################################################################################################################################################


class LinkedList:
	def __init__(self, value=None, path = [] , up=None, down = None, left=None, right=None ):
		self.value = value
		self.path = path
		self.up = up
		self.down = down
		self.left = left
		self.right = right 
#!/usr/bin/env python3
import collections
class Solution:
	def shortestPath(self, grid: list[list[int]], k: int) -> int:
		rows = len(grid)
		cols = len(grid[0])
		# Directions we'll use to change our location (down, up, right, left).
		directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
		# We'll use a deque for our BFS traversal.
		q = collections.deque([])
		# Append our starting details to the q.
		# (row, col, steps, k)
		RC = LinkedList( [0,0] )
		q.append((0, 0, 0, k, RC, [[0,0]]  ))
		# Use a set (O(1) lookup) to track the locations we've visited to avoid revisiting.
		# We track (r, c, k) - k: is tracked because there might be multiple ways to get to
		# a give (r, c) on the grid. With the addition of k, it ensures that multiple path
		# options can be explored, instead of simply eliminating a (r, c) after the first visit.
		seen = set()
		
		
		stt = [   [[0,0]]    ]
		
		steps2 = 0
		MAT = []
		CCC  =  0
		R_C = []
		while q:
			# Pop the next location from the q.
			
			
			r, c, steps, rk , R0C0 , pathh = q.popleft()
			#R0C0 = LinkedList( [r,c] )
			# If we're at the finish location return the steps, given BFS this will be
			# guaranteed to be the first to hit this condition.
			if r == rows-1 and c == cols - 1:
				CCC += 1
				steps2 = steps
				print(len(q),  R0C0.path[::-1], CCC)     
				MAT.append(pathh)
				R_C.append(R0C0)  
				
				 #steps
				#break #or return 
			# Otherwise we'll keep travelling throught the grid in our 4 directions.
			else:
				for y, x in directions:
					nr = r + y
					nc = c + x
					# If the new location is on the board and has not been visited.
					if 0 <= nr < rows and 0 <= nc < cols and (nr, nc, rk) not in seen:
						# If it's a blocker but we still have k left, we'll go there and k -= 1.
						
						if grid[nr][nc] == 1 and rk > 0:
							print([nr, nc], "UP")
							seen.add((nr, nc, rk))
							
							R0C0_ = LinkedList( [nr,nc] )
							if (1, 0) == (y,x) : 
								R0C0.down = R0C0_
								R0C0_.up = R0C0
								R0C0_.path =  R0C0.path
								R0C0_.path.append("DOWN")
							if (-1, 0) == (y,x) : 
								R0C0.up = R0C0_
								R0C0_.down = R0C0
								R0C0_.path =  R0C0.path
								R0C0_.path.append("UP")
							if (0, 1) == (y,x) : 
								R0C0.right = R0C0_
								R0C0_.left = R0C0
								R0C0_.path =  R0C0.path
								R0C0_.path.append("RIGHT")
							if (0, -1) == (y,x) : 
								R0C0.left = R0C0_
								R0C0_.right = R0C0
								R0C0_.path =  R0C0.path
								R0C0_.path.append("LEFT")
								
							pathh_ = pathh + [[nr,nc]]
							
							q.append((nr, nc, steps + 1, rk - 1,      R0C0_, pathh_))
						# Otherwise continue on  if it's a 0 - free location.
						elif grid[nr][nc] == 0:
							print([nr, nc], "DOWN")
							seen.add((nr, nc, rk))
							
							R0C0_ = LinkedList( [nr,nc] )
							if (1, 0) == (y,x) : 
								R0C0.down = R0C0_
								R0C0_.up = R0C0
								R0C0_.path =  R0C0.path
								R0C0_.path.append("DOWN")
							if (-1, 0) == (y,x) : 
								R0C0.up = R0C0_
								R0C0_.down = R0C0
								R0C0_.path =  R0C0.path
								R0C0_.path.append("UP")
							if (0, 1) == (y,x) : 
								R0C0.right = R0C0_
								R0C0_.left = R0C0
								R0C0_.path =  R0C0.path
								R0C0_.path.append("RIGHT")
							if (0, -1) == (y,x) : 
								R0C0.left = R0C0_
								R0C0_.right = R0C0
								R0C0_.path =  R0C0.path
								R0C0_.path.append("LEFT")
							
							pathh_ = pathh + [[nr,nc]]
							
							q.append((nr, nc, steps + 1, rk,       R0C0_ , pathh_))
		# If we don't hit the end in our traversal we know it's not possible.
		print(MAT, ">>>",len(R_C))
		
		
		return -1



"""