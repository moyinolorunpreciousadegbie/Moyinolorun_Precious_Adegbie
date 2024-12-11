#!/usr/bin/env python3

def combinations_with_replacement(iterable, r):
	# combinations_with_replacement('ABC', 2) → AA AB AC BB BC CC
	
	pool = tuple(iterable)
	n = len(pool)
	if not n and r:
		return
	indices = [0] * r
	
	yield tuple(pool[i] for i in indices)
	while True:
		for i in reversed(range(r)):
			if indices[i] != n - 1:
				break
		else:
			return
		indices[i:] = [indices[i] + 1] * (r - i)
		yield tuple(pool[i] for i in indices)
		
		
def combinations_with_replacement2(iterable, r):
	# combinations_with_replacement('ABC', 2) → AA AB AC BB BC CC
	
	pool = tuple(iterable)
	n = len(pool)
	if not n and r:
		return
	indices = [n-1] * r
	
	yield tuple(pool[i] for i in indices)
	while True:
		for i in range(r):
			if indices[i] != 0 :
				break
		else:
			return
		#indices[:i+1] = [indices[i] - 1] * (i+1)
		indices[:i+1] = [indices[i] - 1] * (i+1)
		yield tuple(pool[i] for i in indices)
		
##############################################################################################		
def combinations(iterable, r):
	# combinations('ABCD', 2) → AB AC AD BC BD CD
	# combinations(range(4), 3) → 012 013 023 123
	
	pool = tuple(iterable)
	n = len(pool)
	if r > n:
		return
	indices = list(range(r))
	
	yield tuple(pool[i] for i in indices)
	while True:
		for i in reversed(range(r)):
			if indices[i] < i + n - r:    #   012345     :3    012  + 6-3=3      345   i + n - r   || i + 3   
				break												# n-r        012   i <<
		else:																	#+++3
			return
		indices[i] += 1
		for j in range(i+1, r):
			indices[j] = indices[j-1] + 1
		yield tuple(pool[i] for i in indices)
		
def combinations2(iterable, r):
	# combinations('ABCD', 2) → AB AC AD BC BD CD
	# combinations(range(4), 3) → 012 013 023 123
	
	pool = tuple(iterable)
	n = len(pool)
	if r > n:
		return
	#indices = list(range(r))
	#indices = list(range(r))[::-1]
	#indices =   list(range( n -1, n -r-1, -1))   # 543     210      3
	
												#  345
	                                            #  012  i
												#  210 <<<
												
	indices =  list(range( n-r , n  )) 
	yield tuple(pool[i] for i in indices)
	while True:
		for i in range(r):
			if indices[i] >  i:  # n - i -1 :  #  n - r + i
				break
		else:
			return
		indices[i] -= 1
		for j in range(i-1, -1, -1):
			indices[j] = indices[j+1] - 1
		yield tuple(pool[i] for i in indices)
		
		
		
	
	
r = 3

m = [0,1,2,3,4,5]

print(list(range(r)),  list(range(len(m)-1, len(m)-r-1, -1))    , list(range( len(m)-r , len(m)  )) )
		
print(   list(combinations_with_replacement([1,2,3,4,5], 3)))

print()

print(   list(combinations_with_replacement2([1,2,3,4,5], 3)))

print()

print(   list(combinations([1,2,3,4,5,6], 3))  )

print()

print(   list(combinations2([1,2,3,4,5,6], 3)))



"""
print()

print(   list(combinations([1,2,3,4,5,6], 3))[len(list(combinations([1,2,3,4,5,6], 3)))//2:] )

print()

print(   list(combinations2([1,2,3,4,5,6], 3))[len(list(combinations([1,2,3,4,5,6], 3)))//2:] )
"""