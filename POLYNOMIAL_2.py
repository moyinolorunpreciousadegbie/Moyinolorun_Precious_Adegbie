#!/usr/bin/env python3

#  EXPAND ((100a+10b+c)^4)


# https://www.google.com/search?q=expand+%28100a+%2B+10b+%2B+c%29%5E4&sca_esv=1052824479652a46&sxsrf=ADLYWIIUS6XduOrcwXeLJlH45RltJM1OKA%3A1727982824006&ei=6Oz-Zq0Hq7fA3g-JiI3YAg&ved=0ahUKEwitm5zT9fKIAxWrG9AFHQlEAysQ4dUDCA8&uact=5&oq=expand+%28100a+%2B+10b+%2B+c%29%5E4&gs_lp=Egxnd3Mtd2l6LXNlcnAiGWV4cGFuZCAoMTAwYSArIDEwYiArIGMpXjQyBRAhGKABMgUQIRigATIFECEYoAFIuAtQxgRY1whwAXgAkAEAmAGBAaAB7gGqAQMwLjK4AQPIAQD4AQGYAgOgAvwBwgIOEAAYgAQYsAMYhgMYigXCAgsQABiwAxiiBBiJBcICCxAAGIAEGLADGKIEwgIFECEYnwWYAwCIBgGQBgeSBwMxLjKgB8gK&sclient=gws-wiz-serp


# expand (100a + 10b + c)^8


def product(iterables, square):
	# product('ABCD', 'xy') → Ax Ay Bx By Cx Cy Dx Dy
	# product(range(2), repeat=3) → 000 001 010 011 100 101 110 111
	
	
	
	
	pools = [tuple(iterables) for i in range(square)]
	
	
	#print( iterables[ 0 ] ** square )
	#print( iterables[ -1 ] ** square )  # 1
	
	#print(pools,"here") # (100,10,1)
	
	def mul(l):
		one = 1
		for i in l:
			one *= i
		return one
	
	
	# len(iterables) ** square
	
	
	q = []
	result = [() ]
	cn= 0
	
	cnn = {}
	for pool in pools:
		
		q = []
		for x in result :
			if  len(result)  == len(iterables) ** square : break
			
			for y in pool :
				
				cn += 1
				#if  len(result)     == len(iterables) ** square : #iterables[-1] ** square  : 
				if mul(x)*mul([y])  == iterables[ -1 ] ** square  :
					i = mul(x)*mul([y])
					#print(i)
					if i not in cnn :
						cnn[ i ] = 0
					cnn[ i ] += 1
				q.append( [ mul(x)*mul([y]) ]  )
				
				
		result = q
		
		
	return result
		
def product_str(iterables, square):
	# product('ABCD', 'xy') → Ax Ay Bx By Cx Cy Dx Dy
	# product(range(2), repeat=3) → 000 001 010 011 100 101 110 111
	
	
	repeat = 1
	
	pools = [tuple(iterables) for i in range(square)]  
	
	#print(pools,"here")
	
	
	
		
	q = []
	result = [[]]
	cn= 0
	
	qu = []
	cnt = {}
	for pool in pools:
		
		q = []
		for x in result :
			if  len( x ) == square  :  break #len( x ) == (repeat * len(iterables)  ) : break
			
			for y in pool :
				
				cn += 1
				#if  len( x+[y] ) == (repeat * len(iterables)  )  : print(x+[y] , cn) # 365     876
				if  len(  x+[y]  ) == square  :   #   (repeat * len(iterables)  ) : #print(x+[y] )
					i = x+[y]
					#print(i," <<<")
					for ii in i :
						if ii not in cnt:
							cnt[ii] = 0
							
						cnt[ii] += 1
					mykeys = list(cnt.keys())
					mykeys.sort()
					cnt = {i:cnt[i] for i in mykeys}
					qu.append( cnt )
					cnt = {}
				
				q.append( x+[y]   )
				
		result = q
		

		
		#print(q,"qq")
	return qu
	#return result
	
	
	
	
	


#iterables = ['100 A', '10 B',  'C']

#one = 10 ** (len(iterables )  - 1  )

#cn = 0
#iterables_let = []
#iterables_num = []

#for i in  iterables :
	#iterables_let.append(i[-1])
	#iterables_num.append(int(one)   )
	#one/= 10
	#cn += 1
	
	
	






num = 100   ##################
race_to_power = 8    # 8 you are pushing it

alphabet = [    "A", "B", "C" , "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"    ]
len( str(   num)    )		

#cn = 0
iterables_let = []
iterables_num = []
number = 1

one = 10 ** (len( str(   num)    ) - 1  )
for i in  range(  len( str(   num)    )	 ) :
	#iterables_let.append(alphabet[i])
	A = chr(number + 64) 
	iterables_let.append(A)
	iterables_num.append(int(one)   )
	one/= 10
	number+=1
	
	
	
	
	
	
print()
print()




q = {}


ccc = 0
for j in list(product_str(iterables_let, race_to_power)) :
	
	if tuple(    [k+str(v) for k, v in j.items()]    ) not in q :
		q[ tuple(    [k+str(v) for k, v in j.items()]    ) ] = 0
		
		
	q[tuple(    [k+str(v) for k, v in j.items()]    ) ] +=    list(product(iterables_num, race_to_power))[ccc][0]
	
	#print(j  , list(product(iterables_num, 4))[ccc])
	ccc+=1
	
	
	#print(q,"QQQ" , )
	
	
	
print([[v,k]  for k, v in q.items()])


#print( [k+str(v) for k, v in {'A': 1, 'B': 1, 'C': 2}.items()]  )




"""
# Function to get cofactor of mat[p][q] in cof[][]
def get_cof(mat, cof, p, q, n):
	i = 0
	j = 0
	for row in range(n):
		for col in range(n):
			if row != p and col != q:
				cof[i][j] = mat[row][col]
				j += 1
				if j == n - 1:
					j = 0
					i += 1

# Recursive function for finding determinant
# of matrix mat of dimension n
def get_det(mat, n):
	if n == 1:
		return mat[0][0]
	det = 0
	cof = [[0] * n for _ in range(n)]  # To store cofactors
	sign = 1
	for f in range(n):
		get_cof(mat, cof, 0, f, n)
		det += sign * mat[0][f] * get_det(cof, n - 1)
		sign = -sign
	return det

# Function to get adjoint of mat in adj
def adjoint(mat, adj):
	n = len(mat)
	if n == 1:
		adj[0][0] = 1
		return
	sign = 1
	cof = [[0] * n for _ in range(n)]
	for i in range(n):
		for j in range(n):
			get_cof(mat, cof, i, j, n)
			sign = 1 if (i + j) % 2 == 0 else -1
			adj[j][i] = sign * get_det(cof, n - 1)

# Function to calculate and store inverse, returns 
# false if matrix is singular
def inverse(mat):
	n = len(mat)
	det = get_det(mat, n)
	if det == 0:
		print("Singular matrix, can't find its inverse")
		return None
	adj = [[0] * n for _ in range(n)]
	adjoint(mat, adj)
	inv = [[adj[i][j] / det for j in range(n)] for i in range(n)]
	return inv

if __name__ == '__main__':
	mat = [[5, -2, 2, 7], [1, 0, 0, 3], [-3, 1, 5, 0], [3, -1, -9, 4]]
	n = len(mat)
	adj = [[0] * n for _ in range(n)]  # To store adjoint

	# Print the input matrix
	print("Input matrix is:")
	for row in mat:
		print(row)

	# Print the adjoint matrix
	print("\nThe Adjoint is:")
	adjoint(mat, adj)
	for row in adj:
		print(row)

	# Print the inverse matrix if it exists
	print("\nThe Inverse is:")
	inv = inverse(mat)
	if inv:
		for row in inv:
			print(row)


###########################################################################################################################################################

def mulMat(m1, m2):
	r1 = len(m1)
	c1 = len(m1[0])
	r2 = len(m2)
	c2 = len(m2[0])

	if c1 != r2:
		print("Invalid Input")
		return None

	# Initialize the result matrix with zeros
	res = [[0] * c2 for _ in range(r1)]

	# Perform matrix multiplication
	for i in range(r1):
		for j in range(c2):
			for k in range(c1):
				res[i][j] += m1[i][k] * m2[k][j]

	return res

# Driver code
if __name__ == "__main__":
	m1 = [
		[1, 1],
		[2, 2]
	]

	m2 = [
		[1, 1],
		[2, 2]
	]

	result = mulMat(m1, m2)

	print("Multiplication of given two matrices is:")
	for row in result:
		print(" ".join(map(str, row)))
"""
