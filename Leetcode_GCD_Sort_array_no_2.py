#Leetcode1998. GCD Sort of an Array DFS

def is_integer_num(n):
	if isinstance(n, int):
		return True
	if isinstance(n, float):
		return n.is_integer()
	return False


def is_prime(n):
	if n < 2:
		return False
	i = 2
	while i*i <= n:
		if n % i == 0:
			return False
		i += 1
	return True

def do(A):
	
	AA = [A]
	q = []		
	for r1 in range( len(AA[0])):		
		for r2 in range( 2,len(AA[0]) + 1): 
			if r1 < r2-1:
				#print(r1, r-1)
				q.append([r1, r2-1])
	
	q = q[0::2]
	
	for rw in range(len(q)):
		#print(q[rw][0],q[rw][1]) 
		if is_integer_num(AA[0][q[rw][0] ] / AA[0][q[rw][1] ])  or is_integer_num(AA[0][q[rw][1] ] / AA[0][q[rw][0]] ) :
			return True
		if not is_integer_num(AA[0][q[rw][0] ] / AA[0][q[rw][1] ])  or not is_integer_num(AA[0][q[rw][1] ] / AA[0][q[rw][0]] ) or                                      (AA[0][q[rw][0]] % 2 !=0 and AA[0][q[rw][0]] % 2 != 1 ) and (AA[0][q[rw][1]] % 2 != 0 and AA[0][q[rw][1]] % 2 != 1 )   or  AA[0][q[rw][0] ] / AA[0][q[rw][1] ] < 0 or AA[0][q[rw][1] ] / AA[0][q[rw][0] ]   < 0  or is_prime(AA[0][q[rw][0]]) or is_prime(AA[0][q[rw][1]]):
			return False
			
			
A = [7,21,3]


AA = [5,2,6,2]


AAA = [10,5,9,3,15]


print(do(A)  )    # true
print()

print(do(AA)  )   #  false
print()

print(do(AAA)  )   #  true
print()


AB = [10,5,9,3,15,99989,123] # true

print(do(AB)  ) 
print()


AC = [3,2] # false
AD = [5,2] # false
AE = [9, 3, 13, 12] # false     SHOULD RETURN FALSE not TRUE !!! STILL WORKING ON THIS TEST CASE

print(do(AC)  ) 
print()

print(do(AD)  ) 
print()

print(do(AE)  ) 
print()


