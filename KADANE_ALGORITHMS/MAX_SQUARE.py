def Square(mat):
	R = len(mat)
	C = len(mat[0])
	
	if(   len(mat) == 1 and len(mat[0]) == 1 ):
		print("No Sub Sum because of size 1 x 1")
		return mat
                 
	max_sum = -99999999
	sum = 0
	for r in range(R):
		for c in range(C):
			for r2 in range(R):
				for c2 in range(C):                                                    ########
					if( r <= r2 and c <= c2  and  ( (r2 + 1 - r)!= R or (c2 + 1 - c) !=C ) ): 
						if( (  (r2 + 1 - r) * (c2 + 1 - c)  )/ ( r2 + 1 - r)   ==     ( r2 + 1 - r )    or   (  (r2 + 1 - r) * (c2 + 1 - c)  )/ ( r2 + 1 - r)   !=      (c2 + 1 - c)  
							
							and (  (r2 + 1 - r) * (c2 + 1 - c)  )/ (c2 + 1 - c)   ==    (c2 + 1 - c)     or    (  (r2 + 1 - r) * (c2 + 1 - c)  )/ (c2 + 1 - c)   !=   ( r2 + 1 - r )   and ( r2 + 1 - r)  == ( c2 + 1 - c)  ):
					## always a square
							
							sum = sumQuery(mat, r, c, r2, c2)
							if (sum > max_sum):
								max_sum = sum;
								q =[[r,c,r2,c2]]
							
									
	print("(Top, Left)", "(",q[-1][0],q[-1][1],")")
	print("(Bottom, Right)", "(", q[-1][2],q[-1][3], ")")
	for i in range(q[-1][0],q[-1][2] + 1 ):
		for j in range(q[-1][1],q[-1][3] + 1 ):
			print(mat[i][j],end = ' ')
		print()
		
	return max_sum
def sumQuery(mat, r, c, r2, c2):
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

# 35 lines
				
M = [[1, 2, -1, -4, -20],
     [-8, -3, 4, 2, 1], 
     [3, 8, 10, 1, 3],
     [-4, -1, 1, 7, -6]]

print("sum =", Square(M) )
print()

""""

MM = [[0, 1, 1, 0, 1],
     [1, 1, 0, 1, 0],
     [0, 1, 1, 1, 0],
     [1, 1, 1, 1, 0],
     [1, 1, 1, 1, 1],
     [0, 0, 0, 0, 0]]

print("sum =",Square(MM) )
print()

Mn=[[-1,-2],[-3,-4]]

print("sum =",Square(Mn) )
print()

b = [[1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0]]

print("sum =",Square(b) )
print()

"""


matrix1 = [[  1, -2, -6, 0 ],
		   [  9,  3, -5, 3 ],
		   [ -5,  1, -4, 1 ],
		   [ -3,  7,  0,-3 ]]
		
print( "sum =",Square(matrix1) )

matrix2 = [[ 8, -2, -6, 11 ],
		   [ 9, -4, -5, -3 ],
		   [-5, -16, 14,-1 ],
		   [-3, -7, -1, 13 ]]

print( "sum =", Square(matrix2)  )
print()



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
print()

MB = [[-1,-2],[-3,-4]] #  -1
print()

print( "sum =", Square(MB)  )
print()

## MAXIMUM PRODUCT SUB ARRAY : LEETCODE 152 MEDIUM

""""
num = [[2,3,-2,4]]   # 6

print( "sum =", Square(num)  )

nums = [[-2,0,-1]]  # 0
print()
print( "sum =", Square(nums)  )"""