#!/usr/bin/env python3
from itertools import combinations
from collections import defaultdict

def sumofdistances(n, edges):
	#graph = {} 
	graph = defaultdict(list)
	graph2 = {} # graph as adjacency list 
	for u, v in edges:
		graph.setdefault(u, []).append(v) 
		graph.setdefault(v, []).append(u)
		
		
	def dfs(x, par, cnt): 
		seen.add(x)
		path.append(cnt) 
		#print(path,'    ', sum(path)  )
		for xx in graph.get(x, []) :
			if xx != par:
				dfs(xx, x, cnt + 1)
				
	def bfs(x, par, cnt):
		q = [(x, par, cnt)]
		while q:
			curr, prev , count = q.pop(0)
		#print(wei, 'wwwwww      ', tuple(set(ls)))
			seen.add(curr) 
			path.append(count) 
			for xx in graph.get(curr, []):
				
				if xx not in seen and xx != prev:
					q.append((xx,x, count+1))
		
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
edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
#Output: [8,12,6,10,10,10]
print( sumofdistances(n, edges) )
print()

n = 1
edges = []
#Output: [0]
print( sumofdistances(n, edges) )
print()


n = 2
edges = [[1,0]]
#Output: [1,1]
print( sumofdistances(n, edges) )
print()