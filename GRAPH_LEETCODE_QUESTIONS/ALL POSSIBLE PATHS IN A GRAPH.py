

from collections import defaultdict

def printAllPathsUtil(edges, n,  s, d):

	graph = defaultdict(list) 
		
	for u, v in edges:
		graph[u].append(v)
		graph[v].append(u)
	cn  = 0
	
	q= []
	
	def printAllPathsUtil(edges,visited, n,  s, d, path, u):
		
		visited[u]= True
		path.append(u)
		
		if u == d:
			
			#print(path) 
			counter.append(path)
			SSET.add(  tuple(path) )
			
		else:
			
			for v in graph[u]:
				
				if  visited[v]== False:
					printAllPathsUtil(edges,visited, n,  s, d, path, v)
					
				
		path.pop()
		visited[u]= False
			
		
	visited =[False]*(n)
		
	path = []
	SSET = set()
	counter = []
	
	for s in range(n):
		for d in range(n):
			if s != d :
				printAllPathsUtil(edges,visited, n,  s, d, path,  s)  
				cn+= 1
		  
	return SSET
n = 4
"""
2 0 1 3 
2 0 3 
2 1 3 
"""
edges = [[0, 1], [0, 2], [0, 3], [2, 0],  [2, 1], [1, 3]]

s = 2 ; d = 3

print( printAllPathsUtil(edges, n,  s, d)  )  # ALL POSSIBLE PATHS IN A GRAPH



