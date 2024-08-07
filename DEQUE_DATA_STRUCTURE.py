
class Listnode:
	def __init__(self, value=None, prev=None, next = None):
		self.value = value
		
class MyCircularDeque:
	def __init__(self, k):
			self.max_size = k
			self.cnt = 0
			self.all = [0]
			
			
	def insertFront(self, value):
		
		
		if  self.cnt == self.max_size :
			return False
		
		if  self.cnt == 0 :
			head = Listnode()
			tail = Listnode()
			head.next = tail
			tail.prev = head
			self.all[0] = [head,tail]
			
		
		if  self.cnt < self.max_size :
			node =  Listnode(value)
			head = self.all[0][0]
			node.prev = head
			node.next = head.next
			head.next.prev = head.next = node
			self.cnt += 1
			return True
		
		
		
		
	def insertLast(self, value):
		
		
		if  self.cnt == self.max_size :
			return False
		
		if  self.cnt == 0 :
			head = Listnode()
			tail = Listnode()
			head.next = tail
			tail.prev = head
			self.all[0] = [head,tail]
			
			
		if  self.cnt < self.max_size :
			node =  Listnode(value)
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
		node = front.value
		return node
		
	
	def getRear(self):
		if self.cnt == 0 :
			return -1
		back = self.all[0][1].prev
		node = back.value
		return node
		
	
	
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
				return node.value
			return -1
		
	###############
		
	def addmanyAtIndex( self, index_three , values) :
		for val in values :
			Obj.addAtIndex( index_three , val)
			index_three+=1
		
	def addAtIndex(self, index, value):
		head = self.all[0][0]  # head
		while head and index > 0:
			head = head.next
			index -= 1
				
		if head and index == 0:
			node = Listnode(value)
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
			
			
			
# Function to Reverse a doubly linked list
# in groups of given size
	def reverseByN(self, k):
	
		#if self.all != [0] :
		head = self.all[0][0].next 
		
		self.all[0][0].next  = self.reverseByNN( head, k)
			
	def reverseByNN(self, head, k):
		
		currr = head
		for _ in range(k):
			if  currr == self.all[0][1]  : return head
			currr = currr.next
		
		if head == self.all[0][1] :
			return head
		
		
	
		if (head == None):
			return head;
			
		#print("done",head.value)
		head.prev = None;# self.all[0][0];
		temp=None;
		curr = head;
		newHead = None;
		count = 0;
		
		
				
				
		while (curr != self.all[0][1] and count < k ):
		

		## umadevi9616 version via Geeksforgeeks
			#newHead = curr;
			#temp = curr.prev;
			#curr.prev = curr.next;
			#curr.next = temp;
			#curr = curr.prev # newHead.next;
			#count += 1;
		

		## My own version using umadevi9616 thinking but in reverse.
			newHead = curr;
			temp = curr.next;
			curr.next = curr.prev;
			curr.prev = temp;
			curr = temp #      curr = curr.prev  will also work. 
			count += 1;
		
		
		
	# Checking if the reversed LinkedList size is
	# equal to K or not. If it is not equal to k
	# that means we have reversed the last set of
	# size K and we don't need to call the
	# recursive function
		if (count >= k):
			rest = self.reverseByNN(curr, k);
			head.next = rest;
			if (rest != None ):
			
			# it is required for prev link otherwise u
			# wont be backtrack list due to broken
			# links
				rest.prev = head;
			
		return newHead;

####################################################################################
			
	def printList(self):
		head = self.all[0][0] # head
		head = head.next
		while head != None and head.value != None :
			print(head.value,"->",end=" ")
			head = head.next
		
		
		
		
Obj = MyCircularDeque(10)

lis = [0,1,2,3,4,5]


for l in lis :
	Obj.insertLast(l )
	
Obj.printList()	


print()
print()

t = [33,333,3333]


index_three = 3


	
Obj.addmanyAtIndex( index_three , t) 
	
Obj.printList()	


print()
print()

Obj.deleteAtIndex(4) 

Obj.printList()	


print()
print()

print( Obj.getatIndex(6)  ) 
	
print()
print()
	
Obj.addAtIndex( 6 , "HHH") 

Obj.printList()	

print()
print()


Obj.insertLast("END" )
Obj.printList()	

print()
print()

Obj.reverseByN( 4)  

Obj.printList()	
"""
	
class MyCircularDeque:
	def __init__(self, k):
			self.queue = [None] * k
			self.max_size = k
			self.head = 0
			self.tail = 0
			self.size = 0
		
	def insertFront(self, value) :
		if self.isFull():
			return False
		self.head = (self.head - 1) % self.max_size
		self.queue[self.head] = value
		self.size += 1
		return True
	
	def insertLast(self, value):
		if self.isFull():
			return False
		self.queue[self.tail] = value
		self.tail = (self.tail + 1) % self.max_size
		self.size += 1
		return True
	
	def deleteFront(self) :
		if self.isEmpty():
			return False
		self.head = (self.head + 1) % self.max_size
		self.size -= 1
		return True
	
	def deleteLast(self):
		if self.isEmpty():
			return False
		self.tail = (self.tail - 1) % self.max_size
		self.size -= 1
		return True
	
	def getFront(self):
		if self.isEmpty():
			return -1
		return self.queue[self.head]
	
	def getRear(self) :
		if self.isEmpty():
			return -1
		return self.queue[(self.tail - 1) % self.max_size]
	
	def isEmpty(self) :
		return self.size == 0
	
	def isFull(self) :
		return self.size == self.max_size


"""
	
	
	

	