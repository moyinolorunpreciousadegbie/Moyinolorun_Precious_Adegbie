#!/usr/bin/env python3
from collections import defaultdict
def critic(edges, n):
	
	adj = defaultdict(list)
	#adj = {}
	for u,v in edges:
		
		adj[u].append(v)
		adj[v].append(u)
	
	visited = {}  
	res = []
	
	def dfs(par, x):
		
		if x in seen:
			return x
		
		seen.add(x)	
		
		for xx in adj[x]:
			if xx != par and dfs(x,xx) != None :
				res.append( dfs(x,xx))
			
	for x in adj:
		seen = set()
		dfs(-1, x)
	
	rez = list(set(res))
	#print(rez)
	ls = []
	
	vv = []
	for u,v in edges:
		
		if (u not in rez or v not in rez )and v not in vv :
			
			ls.append([u,v])
			#
		vv.append(v)
	return ls
	
n = 4
connections = [[0,1],[1,2],[2,0],[1,3]]  # G
#Output: [[1,3]]
			
print(critic(connections, n))


n = 2
connections = [[0,1]]  # G
#Output: [[0,1]]

print(critic(connections, n))

n = 6
connections = [[0,1],[0,2],[1,2],[3,4],[3,5],[4,5],[1,3]]    ### I failed this test case
#[1,3]
print(critic(connections, n))

n = 3
connections = [[1,0],[2,0]]  # G
#Expected
#[[0,1]]
print(critic(connections, n))


n = 5
connections = [[0,1],[0,2],[1,2],[3,4]]  # G
# [[3,4]] 
print(critic(connections, n))


n = 8
connections = [[6,1],[1,2],[2,3],[3,4],[4,1],[4,5],[5,6],[1,0],[0,7]]   # 
#Output = [[0,7]]
#Expected = [[0,1],[0,7]]    
print(critic(connections, n))



n = 5
connections = [[1,0],[2,0],[3,2],[4,2],[4,3],[3,0],[4,0]]  # G
# [[0,1]]
print(critic(connections, n))