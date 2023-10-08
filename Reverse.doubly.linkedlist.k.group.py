class Node: 
	def __init__(self):
		self.data = 0; 
		self.next = None;
		self.next = None;

# Function to add Node at the end of a
# Doubly LinkedList
def insertAtEnd(head, data):
	new_Node = Node();
	new_Node.data = data;
	new_Node.next = None;
	temp = head;

	if (head == None):
		new_Node.prev = None;
		head = new_Node;
		return head;
	

	while (temp.next != None):
		temp = temp.next;
	
	temp.next = new_Node;
	new_Node.prev = temp;
	return head;


# Function to print Doubly LinkedList
def printDLL(head):
	while (head != None):
		print(head.data, end=" ");
		head = head.next;
	
	print();


# Function to Reverse a doubly linked list
# in groups of given size
def reverseByN(head, k):
	if (head == None):
		return None;

	head.prev = None;
	temp=None;
	curr = head;
	newHead = None;
	count = 0;

	while (curr != None and count < k):
		
		""""
		## umadevi9616 version via Geeksforgeeks
		newHead = curr;
		temp = curr.prev;
		curr.prev = curr.next;
		curr.next = temp;
		curr = curr.prev;
		count += 1;
		
		"""
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
		rest = reverseByN(curr, k);
		head.next = rest;
		if (rest != None):
		
			# it is required for prev link otherwise u
			# wont be backtrack list due to broken
			# links
			rest.prev = head;
	
	return newHead;


# Driver code
if __name__ == '__main__':
	head = None;
	for i in range(1,11):                 #  1 2 3 4 5 6 7 8 9 10 - values 
		head = insertAtEnd(head, i);
	
	printDLL(head);
	n = 4;

	head = reverseByN(head, n);
	printDLL(head);

# This code contributed by umadevi9616 via Geeksforgeeks https://www.geeksforgeeks.org/reverse-doubly-linked-list-groups-given-size/ I edited my own version from it using reverse thinking. Please give umadevi9616 a thumbs up.

	
	#  4 3 2 1 8 7 6 5 10 9 - Expected answer 
	
	