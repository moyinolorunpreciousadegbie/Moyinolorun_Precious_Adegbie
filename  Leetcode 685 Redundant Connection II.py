####   LEETCODE 685. Redundant Connection II
def findRedundantDirectedConnection2(edges):      
	
	n = len(edges)
	mult = False
	cycle = False 
	parent = [0]*(n)
	
	q = set()
	for u, v in edges: 
		
		q.add(u)  ## Store the sources 
		if parent[v-1]:  
			mult = True # seeing multiple parents
			cand0 = [parent[v-1], v]  #  [parent[v-u], v]
			cand1 = [u, v]
			
		else: 
			parent[v-1] = u  
			
			if v in q:  ## check if q (sources) are being revisited
				cycle = True # seeing cycle
				cand2 = [u, v]
					
	return cand0 if mult and cycle else cand1 if mult else cand2
	
edges = [[1,2],[1,3],[2,3]]

n = len(edges)
print( findRedundantDirectedConnection2(edges)  )

edge = [[1,2],[2,3],[3,4],[4,1],[1,5]]

nn = len(edge)
print( findRedundantDirectedConnection2(edge)  )