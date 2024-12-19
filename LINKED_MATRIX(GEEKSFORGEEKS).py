# Python implementation of construction
# of a Doubly linked linked list from 2D Matrix


class Node:
	def __init__(self, data):
		self.data = data # To hold the value of matrix

		# 4 pointers for left, right, up, down for markings.
		self.left = None
		self.right = None
		self.up = None
		self.down = None


def printList(head):
	# 4 pointers for left, right, up, down for markings.
	downptr = head
	rightptr = None
	while downptr != None:
		rightptr = downptr
		while rightptr != None and rightptr.data != -1:
			print(rightptr.data,"->" ,end=" ")
			rightptr = rightptr.right
		print()
		downptr = downptr.down


if __name__ == "__main__":
	mat = [
		[1, 2, 3],
		[4, 5, 6, 66],
		[7, 8, 9]
	]
	n = len(mat)
	#m = 3
	# head of our final modified doubly linked list from 2d matrix.
	head_main = None
	prev = None
	upper = Node(-1) # dummy node to mark start of up pointer.
	for i in range(n):
		head_row = None # row-wise head of list.
		prev = Node(-1) # dummy node to mark start of left pointer.
		for j in range(len(mat[i])):
			temp = Node(mat[i][j])
			if j == 0:
				head_row = temp
			if i == 0 and j == 0:
				head_main = temp
			temp.left = prev
			prev.right = temp
			if i == n-1:
				temp.down = None

			# This is only used for 1st row.
			if upper.right == None:
				upper.right = Node(-1)
			upper = upper.right
			temp.up = upper
			upper.down = temp
			prev = temp

			if j == len(mat[i])-1:
				prev.right = None
		upper = head_row.left
	printList(head_main)

# This code is contributed by Tapesh (tapeshdua420)


print("####################################################################################")
print("####################################################################################")

# Python3 program to construct 
# a Doubly linked linked list 
# from 2D Matrix

# define dimension of matrix


# struct node of doubly linked
# list with four pointer
# next, prev, up, down
class Node:
	
	def __init__(self, data):
		
		self.data = data
		self.prev = None
		self.up = None
		self.down = None
		self.next = None	
		
# function to create a 
# new node
def createNode(data):
	
	temp = Node(data); 
	return temp;

# function to construct the
# doubly linked list
def constructDoublyListUtil(mtrx, i, 
							j, curr):
	
	if (i >= len(mtrx) or
		j >=len(mtrx[i])):
		return None;

	# Create Node with value 
	# contain in matrix at 
	# index (i, j)
	temp = createNode(mtrx[i][j]);
	
	# Assign address of curr into
	# the prev pointer of temp
	temp.prev = curr;
	
	# Assign address of curr into
	# the up pointer of temp
	temp.up = curr;
	
	# Recursive call for next 
	# pointer
	temp.next= constructDoublyListUtil(mtrx, i, 
									j + 1, 
									temp);

	# Recursive call for down pointer
	temp.down= constructDoublyListUtil(mtrx, 
									i + 1, 
									j, temp);

	# Return newly constructed node
	# whose all four node connected
	# at it's appropriate position
	return temp;
	
# Function to construct the
# doubly linked list
def constructDoublyList(mtrx):
	
	# function call for construct
	# the doubly linked list
	return constructDoublyListUtil(mtrx,
								0, 0, 
								None);
								
# function for displaying
# doubly linked list data
def display(head):
	
	# pointer to move right
	rPtr = None
	
	# pointer to move down
	dPtr = head;
	
	# loop till node->down 
	# is not NULL
	while (dPtr != None):
		
		rPtr = dPtr;
		
		# loop till node->right 
		# is not NULL
		while (rPtr != None):
			print(rPtr.data, "->", 
				end = ' ')
			rPtr = rPtr.next;
			
		print()
		dPtr = dPtr.down;
		
# Driver code
if __name__=="__main__":
	
	# initialise matrix
	mtrx =[[1, 2, 3], 
		[4, 5, 6, 66], 
		[7, 8, 9]]
	
	list = constructDoublyList(mtrx); 
	display(list);
	
# This code is contributed by Rutvik_56
	