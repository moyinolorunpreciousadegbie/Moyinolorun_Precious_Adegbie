def serch(mat):
	
	l = set(  len(i)  for i in mat )
	
	mp = {ll : [] for ll in l }
	
	for i in mat :
		mp[ len(i) ].append(i)
		
	
		
		
	
		#candidates = mat
	res = []
	target = list(mat[0] )
	#print(type(target))
	#print(target,"targ")
	def dfs(i, cur, total  ):
		
				
		if sorted(total) == target:
			#print(sorted(total) ,'here')
			res.append(  cur.copy() ) 
		
			return
	
	
		if i >= len(candidates) or len(total) > len(target)   :
			#cur, total =  [], () 
			return
				
			
		cur.append(candidates[i])
		#print( total, target, sorted(total) == target)  # ,  type(total)==type(target))
	
		dfs(i+1, cur,  total + list(candidates[i])  ) 
	
		cur.pop()
	
		dfs(i + 1, cur, total)
	
	for i in l:
		if i == 1 :
			continue
		candidates = mp[i]
		#print(candidates,"{{{{{{{")
		dfs(0, [], []  )
	return res


					
def combinations(iterable):
	# combinations('ABCD', 2) → AB AC AD BC BD CD
	# combinations(range(4), 3) → 012 013 023 123
	
	pool = tuple(iterable)
	n = len(pool)
	#if r > n:
		#return
	#indices = list(range(r))
	
	for r in range(n, 0, -1):
		indices = list(range(r))
		if len(iterable) % len(indices) == 0 :
			
			yield tuple(pool[i] for i in indices)
			while True:
				for i in reversed(range(r)):
					if indices[i] != i + n - r:
						break
				else:
					break
				indices[i] += 1
				for j in range(i+1, r):
					indices[j] = indices[j-1] + 1
				yield tuple(pool[i] for i in indices)
				
				
l = [1,2,3,4,5,6]		# 3,,,,4
print(list(combinations(l)) , len(list(combinations(l)) ))  

mat = [(1, 2, 3, 4, 5, 6), (1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 2, 6), (1, 3, 4), (1, 3, 5), (1, 3, 6), (1, 4, 5), (1, 4, 6), (1, 5, 6), (2, 3, 4), (2, 3, 5), (2, 3, 6), (2, 4, 5), (2, 4, 6), (2, 5, 6), (3, 4, 5), (3, 4, 6), (3, 5, 6), (4, 5, 6), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 3), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6), (4, 5), (4, 6), (5, 6), (1,), (2,), (3,), (4,), (5,), (6,)] 



print( serch(mat) )



from itertools import combinations_with_replacement
from itertools import permutations

an = set()


for i in list(combinations_with_replacement(["0","-1","1"],2))      :
	for g in permutations(i)  :
		
		an.add(  tuple(    g      )      )
		
	
	
print(an , len(an ) )
	