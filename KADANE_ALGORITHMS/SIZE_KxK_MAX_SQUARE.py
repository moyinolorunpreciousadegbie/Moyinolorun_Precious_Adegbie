# An efficient Python3 program to find maximum sum
# sub-square matrix

# Size of given matrix
# ROW = 1
# COL = 3


# A O(n^2) function to the maximum sum sub-
# squares of size k x k in a given square
# matrix of size n x n
def printMaxSumSub(mat, rw, cl):         

	# k must be smaller than or equal to n
	
	ROW = len(mat)    
	COL = len(mat[0])
	
	if(rw > ROW):
		kk = ROW
	else:
		kk = rw
	##############
	if(cl > COL):
		kkk = COL
	else:
		kkk = cl
		
		
	# 1: PREPROCESSING
	# To store sums of all strips of size k x 1
	stripSum = [[0 for j in range(COL)] for i in range(ROW)];
	#if (k > ROW or k > COL):
		#kk=ROW
		#kkk=COL
		#return;

	# Go column by column
	for j in range(COL):
		
		# Calculate sum of first k x 1 rectangle
		# in this column
		sum = 0;
		for i in range(kk):  ######################## ROW
			sum += mat[i][j];
		stripSum[0][j] = sum;

		# Calculate sum of remaining rectangles
		for i in range(1,ROW- rw +1):
			sum += (mat[i+ rw -1][j] - mat[i-1][j]);
			stripSum[i][j] = sum;

	# max_sum stores maximum sum and its
	# position in matrix
	max_sum = -1000000000
	i_ind = 0
	j_ind = 0

	# 2: CALCULATE SUM of Sub-Squares using stripSum[][]
	for i in range(ROW- cl +1):  #  ROW OR COL
		
		# Calculate and print sum of first subsquare
		# in this row
		sum = 0;
		for j in range(kkk):    ######################## COL
			sum += stripSum[i][j];

		# Update max_sum and position of result
		if (sum > max_sum):
			max_sum = sum;
			i_ind = i
			j_ind = 0


		# Calculate sum of remaining squares in
		# current row by removing the leftmost
		# strip of previous sub-square and adding
		# a new strip
		for j in range(1,COL- cl +1):
			sum += (stripSum[i][j+ cl -1] - stripSum[i][j-1]);

			# Update max_sum and position of result
			if (sum > max_sum):
				max_sum = sum;
				i_ind = i
				j_ind = j

	# Print the result matrix
	for i in range(kk): # ROW
		for j in range(kkk): # COL
			print(mat[i+i_ind][j+j_ind], end = ' ')
		print()
	
	
		
	print('(Top, Left)', (i_ind,j_ind ))
	print('(Bottom, Right)', (i_ind+kk-1,j_ind+kkk-1 ))
	
	sum=0
	for i in range(kk): # ROW
		for j in range(kkk): # COL
			sum+= mat[i+i_ind][j+j_ind]
			#if(i ==k-1 and j ==k-1):
			#if(j ==k-1):
			if(i ==kk -1 and j ==kkk-1):
				print("Max sum is:", sum) 
# Driver program to test above function
				
matrix1 = [[0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
		   [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
		   [0, 0, 2, 1, 1, 1, 1, 1, 0, 0],
		   [0, 0, 2, 1, 1, 1, 1, 1, 0, 0],
		   [0, 0, 2, 1, 1, 1, 1, 1, 0, 0],
		   [0, 0, 2, 1, 1, 1, 1, 1, 0, 0],
	       [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
		   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 8 , 10
	];
row = 7;
col = 3;

row2 = 4;
col2 = 6;

matrix2 = [[1,0,1],[0,-2,3]]  # = 2
row3 = 2;
col3 = 2;

matrix3 = [[2,2,-1]]  # = 3
row4 = 1;
col4 = 3;



printMaxSumSub(matrix1, row, col);
print()
printMaxSumSub(matrix1, row2, col2);

print()
printMaxSumSub(matrix2, row3, col3);

print()
printMaxSumSub(matrix3, row4, col4);

#print(len(matrix2), len(matrix2[0]))
#       2                3
#print(len(matrix3), len(matrix3[0]))
#       1                3
M = [[1, 2, -1, -4, -20],
     [-8, -3, 4, 2, 1],
     [3, 8, 10, 1, 3],
     [-4, -1, 1, 7, -6]]

# This code is contributed by rutvik_56.
