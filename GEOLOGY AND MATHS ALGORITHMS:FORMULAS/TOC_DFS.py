

from collections import defaultdict

def combinations(iterable, r):
	# combinations('ABCD', 2) --> AB AC AD BC BD CD
	# combinations(range(4), 3) --> 012 013 023 123
	pool = tuple(iterable)
	n = len(pool)
	if r > n:
		return
	indices = list(range(r))
	yield tuple(pool[i] for i in indices)
	while True:
		for i in reversed(range(r)):
			if indices[i] != i + n - r:
				break
		else:
			return
		indices[i] += 1
		for j in range(i+1, r):
			indices[j] = indices[j-1] + 1
		yield tuple(pool[i] for i in indices)
		
def maxi(well):
	mx = 0
	for o, oo, _, _ in well:
		#print(oo,'OO')
		mx = max(mx, oo)
	return mx

def depthsort(wellz):
	wellcombo = []
	for wel in list(wellz):   # wel each well
		for depth in wel:  #  [2,15]
			wellcombo.append(depth)
	
	#print(wellcombo ,'now')
	
	wellcombo.sort(key=lambda e: e[0])	 # sort by depth
	return wellcombo 
	#return wellcombo
	
	

			
			
			
def printAllPathsUtil(tar , tar2, edges, n):

	graph = defaultdict(list) 
	se = {}
	#print(n,'NN')
	#print()
	print(edges,'EGDES')
	tocgraph = defaultdict(list)
	q = []
	for u, v , t ,tt in edges:
		#se[(u,v)] = w
		if [u, v,t, tt ] not in q:
			se[(u,v)] = t
			q.append( [u, v,t, tt ])
		graph[u].append((v))
		tocgraph[v].append(t)  # TOC
		
	print(graph)
		#print()
		#print(se)
	print()
	
	def printAllPathsUtil(edges, n,   path, par, u, cum ):
	
		visited[u]= True
		path.append(u)
		
		
		if   path[-1] <= tar2 and par != -1 :
			cum += se[(par,u)]
			print(path,'  path', '<=', tar2,'               cummulative TOC:  ', cum,"    Depth: ",path[-1],'         CURRENT TOC     ',tocgraph[u][0]) 
		print("-------------------------------------------------------------------------------------------------------------------------------------------------")
			
		
		for v in graph[u]:
			#print(v)
			#if  par != v and visited[v] == False:
			#cum += se[(u,v)]
			#print(cum)
			printAllPathsUtil(edges, n,   path,u, v, cum)
		print()			
		path.pop()
		visited[u]= False
		
	visited =[False]*(n)
		
	path = []
	
	cum = 0
	printAllPathsUtil(edges, n,   path,  -1, 0, cum)

def add(wells, tar, tar2):
	
	mat = 0
	n = 0
	edges = 0
	
	
	for i in range(2, len(wells)+1):
		#n = 0
		for wellz in list(combinations(wells, i))  :
			#print( depthsort(wellz) ,"HERE BOY" )
			#n = len(depthsort(wellz)  ) + 1
			#n = len(depthsort(wellz)  ) + 2
			n = maxi(depthsort(wellz)) + 1
			#print(n,'NN')
			edges = depthsort(wellz) 
			#print(edges, n,'lll')
			printAllPathsUtil(tar ,tar2, edges, n)
			print()
			print()
			
			#return mat
	
tar = 75
tar2  = 30		

"""
2 0 1 3 
2 0 3 
2 1 3 
"""
#edges = [[-1, 0, 0],     [0, 1, 20],   [0,2,15]   , [1,6,12]  , [2,5,3], [6,9,11], [5,7,21],  ]




#!/usr/bin/env python3
def doe(m):
	cum = 0
#main = []
	q = [0]
	cn = 0
	for u in m:
		if cn == 0:
			u.append(u[1])
			q.append(u[1])
			
			
		else :
			#if u[1]:
			cum += u[1] - q[-1]
			u.append(cum)
			cum = 0
			#print(cum)
			q.append(u[1])
			
		cn += 1
		
	return m

	
	
w1 = [[0, 2,15],[2, 5,3],[5, 7,21],[7, 15,7],[15, 20,3],[20, 28,15],[28, 34,8]] #, [34, None, 0]]

w2 = [[0, 1,20],[1, 8,12],[8, 11,11],[11, 13,16],[13, 21,9],[21, 33,4],[33, 50,17],[50, 53,4],[53, 59,10]] #, [59, None, 0]]

w3 = [[0, 3,11],[3, 6,4],[6, 9,15],[9, 10,5],[10, 22,14],[22, 29,6],[29, 35,7],[35, 39,21], [39, 43,5], [43, 48,25],[48, 51,9],[51, 56,11]] #, [56, None, 0]]

#n = 29
"""
print( doe(w1))
print()
print( doe(w2))
print()
print( doe(w3))
"""

all_ = [ doe(w1) ,doe(w2), doe(w3) ]

add( all_  , tar , tar2)
