#!/usr/bin/env python3
import queue
from collections import defaultdict




def cumul(mat):
	q = []
	cum = 0
	for u in mat:
		cum += u
		q.append(cum)
	return q
		

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
		
		
def depthsort(wellz):
	wellcombo = []
	for wel in list(wellz):   # wel each well
		for depth in wel:  #  [2,15]
			wellcombo.append(depth)
	
	#print(wellcombo ,'now')
	
	wellcombo.sort(key=lambda e: e[0])	 # sort by depth
	return wellcombo 
	#return wellcombo
	

	
def add(wells, tar, tar2):
	
	mat = 0
	n = 0
	edges = 0
	
	grph = defaultdict(list)
		
	cnt = 0
	
	ser = set()
	for  i in wells:
		cnt += 1
		temp = cnt
		for j in i:
			
			
			if j[1] in ser :
				#cnt +=1
				grph[ j[1]  ].append((' and ')  )
				grph[ j[1]  ].append(('WELL',cnt))
				#cnt -=1
				continue
			grph[ j[1]  ].append(('WELL',cnt))
			ser.add(j[1]  )
			
			#print(grph,'grph')
			 
	for i in range(2, len(wells)+1):
		#n = 0
		for wellz in list(combinations(wells, i))  :
			
			n = maxi(depthsort(wellz)) + 1
		
			edges = depthsort(wellz) 
			
			#grph.tuple()
	
			#print(edges)
			findShortestCycle(n, edges, tar, tar2,     grph) 
			print("-------------------------------------------------------------------------------------------------------------------------------------------------")
			
			print()
			print()
			print()
			print()
			
			
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


def maxi(well):
	mx = 0

	for o, oo , _ , _ in well:
		#print(oo,'OO')
		
		mx = max(mx, oo)
	return mx

def findShortestCycle(n, edges, tar, tar2,  grph) :
	
	
		
		graph = [[] for _ in range(n)]
		
		#  from   to  TOC   gape  
	
		graph2 = defaultdict(list)
	
	
	
		#graph2[n[1]].append(n[3])
		
		for   u,   v , toc, gape in edges: 
			graph[u].append((v,gape))
			graph[v].append((u,gape))
			graph2[v].append(toc)
		
		visited=[False]*(n)
		path = []
		tooc = []
		for u , vv ,tocc, gap in edges: 
			dist = {}
			queue1 = queue.deque([(u, -1, gap   )])
			while queue1: 
				u, p, d = queue1.popleft()
				if tar <= sum(path) <= tar2 : 
					ln = len(path)
					print(path[1:],'     path in range          ',tar,'<=',sum(path),'<=',tar2,'      DEPTH: ',path[-1],'   ',grph[  path[-1]   ])
					
					print(tooc[:ln-1],'     TOC so far            total TOC value',sum(tooc[:ln-1]), '    Current TOC:',tooc[:ln-1][-1])
					print(cumul(tooc[:ln-1] ),'   Cumulative TOC')
					print()
					print()
					
					
					#break 
					#visited[u]=True
				path.append(u)
				
				for v , gapp in graph[u]: # or visited[v] == False
					
					if v != p:
						if graph2[v] :
							
							tooc.append(graph2[v][0])
							#print(tooc)
						queue1.append((v, u, d + gapp))
				#if queue1:
			#	queue1.popleft()
				#visited[u]=False
		return path

def each(w, tar):
	
	path = [ ]
	tooc = []
	toocc = []
	cum = 0
	tc = 0
	for   u in w : 
				
        #   depth
		if u[1] > tar :
			break
		
		cum += u[3]   # gape
		tc+= u[2]     # toc
		path.append(cum)
		tooc.append(tc)
		toocc.append(u[2])
		print(path,path[-1],'depth <',tar )
		print(toocc,toocc[-1],' current toc')
		print(tooc,tooc[-1],'toc seen so far')
		print()

tar2 = 55
tar  = 14	

w1 = [[0, 1,15],[1, 5,3],[5, 7,21],[7, 15,7],[15, 20,3],[20, 28,15],[28, 34,8]] #, [34, None, 0]]

w2 = [[0, 2,20],[2, 8,12],[8, 11,11],[11, 13,16],[13, 21,9],[21, 33,4],[33, 50,17],[50, 53,4],[53, 59,10]] #, [59, None, 0]]

w3 = [[0, 3,11],[3, 6,4],[6, 9,15],[9, 10,5],[10, 22,14],[22, 29,6],[29, 35,7],[35, 39,21], [39, 43,5], [43, 48,25],[48, 51,9],[51, 56,11]] #, [56, None, 0]]



all_ = [ doe(w1) ,doe(w2), doe(w3) ]

add( all_  , tar , tar2)


print("#################################################################################################################################################################")

print()
tarr = 23


print()
print('SINGULAR WELLS :')
print()
for wel in all_  :
	each(  doe(wel)   , tarr)
	print("-------------------------------------------------------------------------------------------------------------------------------------------------")
	
	print()
print()








