#!/usr/bin/env python3

def product(*iterables, repeat=3):
	# product('ABCD', 'xy') → Ax Ay Bx By Cx Cy Dx Dy
	# product(range(2), repeat=3) → 000 001 010 011 100 101 110 111
	
	if repeat < 0:
		raise ValueError('repeat argument cannot be negative')
	pools = [tuple(pool) for pool in iterables] * repeat
	
	
	#print(pools) # [('A', 'B', 'C', 'D'), ('x', 'y'), ('A', 'B', 'C', 'D'), ('x', 'y'), ('A', 'B', 'C', 'D'), ('x', 'y')]

	
	result = [[]]
	for pool in pools:
		result = [x+[y] for x in result for y in pool]
		
	for prod in result:
		yield tuple(prod)
		
_1st = list( product('ABCD', 'xy')  ) 		  #  python standard library form
print(  _1st , len(_1st )   )  # 512      ----   3 x       4 x 2  x     4 x 2  x       4 x 2


print()
print()

print()
print()

def product(*iterables, repeat=3):
	
	pools = [tuple(pool) for pool in iterables] * repeat
	#print(pools	,'here')
	
	
	q = []
	result = [[]]
	cn= 0
	for pool in pools:
		
		q = []
		for x in result :
			if  len( x ) == (repeat * len(iterables)  ) : break
		
			for y in pool :
		
				cn += 1
				#if  len( x+[y] ) == (repeat * len(iterables)  )  : print(x+[y] , cn) # 365     876
				if  len(  x+[y]  ) == (repeat * len(iterables)  ) : print(x+[y] )
				q.append( x+[y]   )
		
		result = q
		
		
	
	return result  # or q 
	




_2nd = list( product('ABCD', 'xy')  ) 		#  my form 
print(  _2nd , len( _2nd )   )

"""
if one + len(pools[0]) == cn :
	break
"""