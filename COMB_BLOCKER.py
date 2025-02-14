

def product(iterables):
	
	u = 5   + 4 # 4 redundants
	repeat = u
	#repeat = [ tuple(iterables[0]) ]
	f = [tuple(pool) for pool in iterables] 
	#print(pools	,'here')
	pools = []
	
	cn = 0
	while u > 0 :
		
		pools.append(f[cn])
		
		if cn + 1 == len(f) : cn = -1
		
		
		
		cn += 1
		u -= 1
		
	
	q = []
	result = [[]]
	cn= 0
	
	ans = []
	for pool in pools:
		
		q = []
		for x in result :
			
			
			#if sum(x) == 5 : ans.append(x)
				
				
			
			for y in pool :
				
				cn += 1
				
				
				if  sum(x + [y]) > 5 : 
					continue
				
				if sum(x+[y]) == 5 and len(x+[y]) == 5 + 4: ans.append(x+[y])
				
				q.append( x+[y]   )
				
		result = q
		
		
		
	return ans # result  # or q 

	





	



_2nd = list( product([ [0,1], [0,1]]   )  ) 		#  my form 

print(  _2nd , len( _2nd )   )




from itertools import combinations


print(len(list(combinations([1,2,3,4,5,6,7,8,9],5))))

#print([4 ** i for i in range(1, 6 + 1)])

"""   >    \
0   0  0  0   0
    1  1  1   1
	   2  2   2
          3   3
              4




0  0
1  1
"""
				