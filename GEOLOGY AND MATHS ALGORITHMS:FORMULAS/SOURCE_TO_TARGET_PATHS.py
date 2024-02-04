

from collections import defaultdict

def printAllPathsUtil(edges, n,  s, d):

	graph = defaultdict(list) 
		
	for u, v in edges:
		graph[u].append(v)
		
	
	def printAllPathsUtil(edges,visited, n,  s, d, path, u):
	
		visited[u]= True
		path.append(u)
		
		if u == d:
			print(path) 
		else:
			
			for v in graph[u]:
				if  visited[v]== False:
					printAllPathsUtil(edges,visited, n,  s, d, path, v)
					
		path.pop()
		visited[u]= False
		
	visited =[False]*(n)
		
	path = []
		
	printAllPathsUtil(edges,visited, n,  s, d, path,  s)
		
		
n = 4
"""
2 0 1 3 
2 0 3 
2 1 3 
"""
edges = [[0, 1], [0, 2], [0, 3], [2, 0],  [2, 1], [1, 3]]

s = 2 ; d = 3

printAllPathsUtil(edges, n,  s, d)