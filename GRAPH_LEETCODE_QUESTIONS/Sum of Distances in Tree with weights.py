#!/usr/bin/env python3
from itertools import combinations
from collections import defaultdict

def sumofdistances(n, edges):
	#graph = {} 
	graph = defaultdict(list)
	graph1 = {}
	graph2 = {} # graph as adjacency list 
	for u, v , w in edges:
		graph.setdefault(u, []).append(v) 
		graph.setdefault(v, []).append(u)
		graph1[(u, v)] = w
		graph1[(v, u)] = w
		
		
	def dfs(x, par, cnt): 
		seen.add(x)
		path.append(cnt) 
		#print(path,'    ', sum(path)  )
		for xx in graph.get(x, []) :
			if xx != par:
				dfs(xx, x, cnt + graph1[(x, xx)])
				
	def bfs(x, par, cnt):
		q = [(x, par, cnt)]
		while q:
			curr, prev , count = q.pop(0)
		#print(wei, 'wwwwww      ', tuple(set(ls)))
			seen.add(curr) 
			path.append(count) 
			for xx in graph.get(curr, []):
				
				if xx not in seen and xx != prev:
					q.append((xx,x, count+ graph1[(curr, xx)]))
		
	for i in range(n):
		seen = set()
		cnt=0
		path = []
		dfs(i, -1, cnt) # DFS WORKS
		#bfs(i, -1, cnt)  # BFS WORKS
		graph2[i] = sum(path)
		path = []
		
	print(graph2)
	
	lss = [0] * n
	for i, v in graph2.items():
		#print(i, v)
		lss[i] = v

	return lss
		
n = 6
edges = [[0,1, 4],[0,2, 3],[2,3, 5],[2,4, 7],[2,5, 2]]
#Output: [8,12,6,10,10,10]
print( sumofdistances(n, edges) )
print()

"""
print(3+    4+       3+5+     3+7+   3+2     )
print(4+    4+3+       4+3+5+     4+3+7+   4+3+2     )
print(3+    3+4+       5+     7+   2     )

print(5+    5+7+       5+2+     5+3+   5+3+4     )
print(7+    7+5+       7+2+     7+3+   7+3+4     )
print(2+    2+5+       2+7+     2+3+   2+3+4     )
"""