def Square(mat):
	R = len(mat)
	C = len(mat[0])
	
	if((len(mat) == 2 and len(mat[0]) == 1) or (len(mat) == 1 and len(mat[0]) == 2) or ( len(mat) == 1 and len(mat[0]) == 1)):
		print("No Sub Sum because of size 1 x 2  or 2 x 1 which is smallest rectangle possible already or it is 1 x 1")
		return mat
	
	max_sum = -99999999
	sum = 0
	for r in range(R):
		for c in range(C):
			
			for r2 in range(R):
				for c2 in range(C):
					if( r <= r2 and c <= c2 and  ( (r2 + 1 - r)!= R or (c2 + 1 - c) !=C) ):
						#sum += mat[r:r2][c:c2] 
						if( (  (r2 + 1 - r) * (c2 + 1 - c)  )/ ( r2 + 1 - r)   !=     ( r2 + 1 - r ) and (  (r2 + 1 - r) * (c2 + 1 - c)  )/ (c2 + 1 - c)   !=     (c2 + 1 - c)  and (c2 + 1 - c) != ( r2 + 1 - r)  and ( r2 + 1 - r ) != ( c2 + 1 - c ) ):
							
						
								# always a rectangle
							aux = [[0 for ii in range(C)] for jj in range(R)]  # N col, M row
							
							preProcess(mat, aux)
							sum = sumQuerymethod1(aux, r, c, r2, c2)     ## METHOD 1
							
							#sum = sumQuerymethod2(mat, r, c, r2, c2)    ## METHOD 2
							if (sum > max_sum):
								max_sum = sum;
							
								q =[[r,c,r2,c2]]

	print("(Top, Left)", "(",q[-1][0],q[-1][1],")")
	print("(Bottom, Right)", "(", q[-1][2],q[-1][3], ")")
	for i in range(q[-1][0],q[-1][2] + 1 ):
		for j in range(q[-1][1],q[-1][3] + 1 ):
			#if(mat[i][j] == 1 ):
			print(mat[i][j],end = ' ')
	
		print()
	
	return max_sum

############################################################################################################################################################################
## METHOD 2

def sumQuerymethod2(mat, r, c, r2, c2):
	R = len(mat)
	C = len(mat[0])
	
	#vis= [0] * (  (r2 + 1) - r ) *  (  (c2 + 1) - c  )   #  or (r2  - (r - 1) ) * (c2  - (c - 1))
	vis = [0] * R * C
	
	sum = 0 # 1 for multiplication, 0 for addition
	for i in range(r , r2 + 1):
		for j in range(c, c2 + 1):
			index = (i * C) +  j; 
			vis[index] = mat[i][j];
			sum += vis[index];
			
	return sum
############################################################################################################################################################################
## METHOD 1

def preProcess(mat, aux):
	R = len(mat)
	C = len(mat[0])
	# Copy first row of mat[][] to aux[][]
	for i in range(0, C, 1):
		aux[0][i] = mat[0][i]
		
	# Do column wise sum
	for i in range(1, R, 1):
		for j in range(0, C, 1):
			aux[i][j] = mat[i][j] + aux[i - 1][j]
			
	# Do row wise sum
	for i in range(0, R, 1):
		for j in range(1, C, 1):
			aux[i][j] += aux[i][j - 1]
			
# A O(1) time function to compute sum of submatrix
# between (tli, tlj) and (rbi, rbj) using aux[][]
# which is built by the preprocess function
def sumQuerymethod1(aux, top, left, bottom, right):
	
	# result is now sum of elements
	# between (0, 0) and (rbi, rbj)
	res = aux[bottom][right]
	
	# Remove elements between (0, 0)
	# and (tli-1, rbj)
	if (top > 0):
		res = res - aux[top - 1][right]
		
	# Remove elements between (0, 0)
	# and (rbi, tlj-1)
	if (left > 0):
		res = res - aux[bottom][left - 1]
		
	# Add aux[tli-1][tlj-1] as elements
	# between (0, 0) and (tli-1, tlj-1)
	# are subtracted twice
	if (top > 0 and left > 0):
		res = res + aux[top - 1][left - 1]
		
	return res
############################################################################################################################################################################

				
			
M = [[1, 2, -1, -4, -20],
     [-8, -3, 4, 2, 1],
     [3, 8, 10, 1, 3],
     [-4, -1, 1, 7, -6]]

print( "sum = ", Square(M) )
print()


matrix = [[1,0,1,0,0],
	      [1,0,1,1,1],
		  [1,1,1,1,1],
		 [1,0,0,1,0]]
	
print("sum = ",  Square(matrix) )
print()



t = [[0, 1, 1],
     [1, 1, 1],
     [0, 1, 1]]
print("sum = ",  Square(t) )
print()

A = [[0, 1, 1, 0],
	[1, 1, 1, 1],
	[1, 1, 1, 1],
	[1, 1, 0, 0]]

print("sum = ",  Square(A) )
print()


""""
h = [[1,1,1,1],
	[0,0,1,0],
	[1,1,1,0],
	[0,1,1,1],
	[0,1,1,0]]

print("sum = ",  Square(h) )
print()
"""






H = [[1,2,3]]

print( "sum =", Square(H)  )
print()


HH = [[1,2]]
print()

print( "sum =", Square(HH)  )
print()

HHH = [[1]]
print()

print( "sum =", Square(HHH)  )
