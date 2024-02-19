from collections import deque
from collections import defaultdict
import heapq
import math


# LEETCODE  2872. Maximum Number of K-Divisible Components, DFS
#  dinesh55

class Solution:
	def maxKDivisibleComponents(self, n: int, edges: list[list[int]], values: list[int], k: int) -> int:
		visited = [False for _ in range(n)]
		self.ans = 0
		graph = [[] for _ in range(n)]
		for u,v in edges:
			graph[u].append(v)
			graph[v].append(u)
			
		def dfs(node)->int:
			visited[node] = True
			sums = values[node]
			# iterate over the neighbours
			for nei in graph[node]:
				# if neighbour was visited continue
				if visited[nei]:
					continue 
				temp = dfs(nei)
				# if the neighbour subtree sum is divisible by k then we cut it hence we don't add it to sums
				if temp % k == 0:
					self.ans += 1
				else:
				# if neighbour subtree sum is not divisible by k then this subtree will have to rely on the parent 
				# to make sum % k == 0 thus we add it to parent.
					sums += temp
			return sums
		dfs(0)
		# if we make x cuts there will be x + 1 trees 
		return self.ans + 1
	
	
n = 5
edges = [[0,2],[1,2],[1,3],[2,4]]
values = [1,8,1,4,4]
k = 6
#Output: 2

Object2 = Solution()

print( Object2.maxKDivisibleComponents(n, edges, values, k)  )


n = 7
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
values = [3,0,6,1,5,2,1]
k = 3
#Output: 3

Object2 = Solution()

print( Object2.maxKDivisibleComponents(n, edges, values, k)  )      


print()#####################################################################################################################################################################


# LEETCODE 2867  Count Valid Paths in a Tree , DFS
# cpcs
class Solution:
	def countPaths(self, n: int, edges: list[list[int]]) -> int:
		def mul(x, y):
			return x * y
		
		def dfs(x, f, con, prime, r):
			v = [1 - prime[x], prime[x]]
			#print(x, v)  # 1 [1, False]
			for y in con[x]:
				if y == f:
					continue
				p = dfs(y, x, con, prime, r)
				#print(  p[0], p[1] , v[0], v[1 ],"     ==   ", mul(p[0], v[1]) + mul(p[1], v[0]), '|||',x,y, "[[",v,'[[',p)   ###############  CLUE  !!!!
				
				#print(p[0], v[1] ,  p[1], v[0],  "== ",mul(p[0], v[1]) + mul(p[1], v[0]))
				r[0] += mul(p[0], v[1]) + mul(p[1], v[0])
				#print(r)
				if prime[x]:
					#print(v[1],  p[0] )
					#print(  p[0], v[1] , p[1], v[0])
					v[1] += p[0] 
					#print(v[1],  p[0] )
					
				else:
					#print(v[0], v[1],  p[0] , p[1])
					v[0] += p[0]
					v[1] += p[1]
			return v
		
		prime = [True] * (n + 1)
		prime[1] = False
		#print(prime)
		
		all_primes = []
		for i in range(2, n + 1):
			#print(i,"i")
			#print(prime[i],"{}")
			if prime[i]:
				
				all_primes.append(i)
				#print(all_primes, prime,i)
				
			for x in all_primes:
				#print(i,x,"kkkk")  
				temp = i * x
				
				if temp > n:
					break
				#print(i,x,'brk')
				prime[temp] = False
				if i % x == 0:
					#print(i,x,'this')
					break
				#print(i,x,'new')
				
		con = [[] for _ in range(n + 1)]
		for e in edges:
			con[e[0]].append(e[1])
			con[e[1]].append(e[0])
			
		r = [0]
		
		#print(prime)
		
		dfs(1, 0, con, prime, r)
		return r[0]
	
	
	
n = 6
edges = [[1,2],[1,3],[2,4],[2,5],[5,6]]
#Output: 5             PRIME NUMBERS   2, 3, 5   MY OWN TEST CASE


#Object2 = Solution()

#print( Object2.countPaths(n, edges)  )


n = 5
edges = [[1,2],[1,3],[2,4],[2,5]]
#Output: 4             PRIME NUMBERS   2, 3, 5


Object2 = Solution()

print( Object2.countPaths(n, edges)  )


n = 6
edges = [[1,2],[1,3],[2,4],[3,5],[3,6]]
#Output: 6

Object2 = Solution()

print( Object2.countPaths(n, edges)  )

print()#####################################################################################################################################################################

# LEETCODE 2846 Minimum Edge Weight Equilibrium Queries in a Tree
# cpcs
class Solution:
	def minOperationsQueries(self, n: int, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
		def dfs(p, x, t, b, e, w, f,  all):
			all[x] = w[:]
			#print(all)
			f[x][0] = p
			b[x] = t[0] = t[0] + 1
			for y in adj[x]:
				if y[0] != p:
					w[y[1]] += 1
					#print(y[0], y[1],"top",  w[y[1]], w)
					#print(p,x,  w)
					dfs(x, y[0],t, b, e, w, f,  all)
					w[y[1]] -= 1
					#print(y[0], y[1],"bottom", w[y[1]],w)
					#print()
					#print(p,x, w, "minus")
			e[x] = t[0]
			
		def isAncestor( x, y, b, e):
			return b[x] <= b[y] and e[x] >= e[y]
		
		def lca(x, y, b, e, f):
			if isAncestor(x, y, b, e):
				#print('here')
				return x
			if isAncestor(y, x, b, e):
				#print('here22')
				return y
			r = 0
			for i in range(19, -1, -1):
				temp = f[x][i]
				if isAncestor(temp, y, b, e):
					r = temp
				else:
					x = temp
			return r
		
		adj = [[] for _ in range(n)]
		for e in edges:
			adj[e[0]].append((e[1], e[2] - 1))
			adj[e[1]].append((e[0], e[2] - 1))
			
		all = [[0] * 26 for _ in range(n)]
		f = [[0] * 20 for _ in range(n)]
		b = [0] * n
		e = [0] * n
		w = [0] * 26
		
		t = [0]
		dfs(-1, 0, t, b, e, w, f,  all)
		f[0][0] = 0
		#g= set()
		for i in range(1, 20):
			#print()
			for j in range(n):
				#print(f[j][i],j,i,'     ', f[f[j][i - 1]][i - 1], f[j][i - 1], "      ",j, i - 1 )
				f[j][i] = f[f[j][i - 1]][i - 1]
				#print()
				
				#print(f)
				
		cn = 0
		result = []
		for q in queries:
			if q[0] == q[1]:
				result.append(0)
				continue
			tLca = lca( q[0], q[1],  b, e, f)
			_sum, m = 0, 0
			for i in range(26):
				
				temp = all[q[0]][i] + all[q[1]][i] - (all[tLca][i] << 1)
				#print( temp, all[q[0]][i],'+', all[q[1]][i] ,'-' ,(all[tLca][i] << 1)  ,"|||||", all[tLca][i],'     ',q[0],'   ',q[1]) 
				_sum += temp
				m = max(m, temp)
				#cn+=1
				#print(all)
				#print(_sum, m,cn)
			result.append(_sum - m)
		return result
	
	
	
n = 7
edges = [[0,1,1],[1,2,1],[2,3,1],[3,4,2],[4,5,2],[5,6,2]]   # 
queries = [[0,3],[3,6],[2,6],[0,6]]#,[4,2]]
#Output: [0,0,1,3]


Object2 = Solution()

print( Object2.minOperationsQueries(n, edges, queries)  )	

n = 8
edges = [[1,2,6],[1,3,4],[2,4,6],[2,5,3],[3,6,6],[3,0,8],[7,0,2]]
queries = [[4,6],[0,4],[6,5],[7,4]]
#Output: [1,2,2,3]
Object2 = Solution()

print( Object2.minOperationsQueries(n, edges, queries)  )	

print()#####################################################################################################################################################################

# LEETCODE 2646. Minimize the Total Price of the Trips
# rukt and ME

class Solution:
	def minimumTotalPrice(self, n: int, e: list[list[int]], price: list[int], trips: list[list[int]]) -> int:
		edges = [[] for _ in range(n)]
		save = {}
		
		def dfs(start, start2, path):
			
			save[(start, start2)]  = path+[start2]
			seen.add(start2)
			path = path+[start2] # adding the paths up
			
			for next in edges[start2]:
				if next  not in seen:
					dfs( start, next,path)
					
		def bfs(start):
					q = [(start, [start], -1)]
					while q:
						curr, path, prev = q.pop(0)
						save[(start, curr)] = path
						for i in edges[curr]:
							if i != prev:
								q.append((i, path + [i], curr))
					
		for u, v in e:
			edges[u].append(v)
			edges[v].append(u)
		for i in range(n):
			
			path = []   #
			seen = set()  #
			dfs(i, i , path)  # 
			#bfs(i)
			
			
			
			

		impacts = [0] * n
		for u, v in trips:
			for i in save[(u, v)]:
				impacts[i] += price[i]
				
		def dfs(loc, prev, can):
			#print(loc, can, 'can1') # 0  1   2,3    2,3   1    2,3
			res = impacts[loc] + sum(dfs(i, loc, True) for i in edges[loc] if i != prev)  # can, true   1t   2t   3t    (x dfs(0, -1, True), y dfs(y, x, True) always maked True at 1st)     #  1  True  
			#print(loc, can, 'can2')  #  2,3    1    2,3    0    2,3   1              9
			if can:
				#print(loc, can, 'can') # 2,3   1    0    2,3                  6
				res = min(res,      # if 1  True     1//2    then 1 False    
			impacts[loc] // 2 + sum(dfs(i, loc, False) for i in edges[loc] if i != prev)  # can is now true   1t   2t   3t
				)   
				#print(loc, can, 'can') #     2,3       1        2,3          0          6     1t//2    2t//2    3t//2 
			return res
		return dfs(0, -1, True)    #  0 True       -1 parent is useless for calculation
	
	
	
n = 4
edges = [[0,1],[1,2],[1,3]]
price = [2,2,10,6]
trips = [[0,3],[2,1],[2,3]]
#Output: 23

Object2 = Solution()

print( Object2.minimumTotalPrice(n, edges, price, trips)  )	

n = 2
edges = [[0,1]]
price = [2,2]
trips = [[0,0]]
#Output: 1


Object2 = Solution()

print( Object2.minimumTotalPrice(n, edges, price, trips)  )	

print()#####################################################################################################################################################################


# LEETCODE 2603. Collect Coins in a Tree
# rnotappl

class Solution:
	def collectTheCoins(self, coins, edges):
		if not edges:
			return 0
		
		n, dict1 = len(coins), defaultdict(set)
		
		for i,j in edges:
			dict1[i].add(j)
			dict1[j].add(i)
			
		leaves = [i for i in dict1 if len(dict1[i]) == 1]
		
		for u in leaves:
			while len(dict1[u]) == 1 and coins[u] == 0:
				p = dict1[u].pop()
				del dict1[u]
				dict1[p].remove(u)
				u = p
				
		for _ in range(2):
			leaves = [i for i in dict1 if len(dict1[i]) == 1]
			for u in leaves:
				p = dict1[u].pop()
				del dict1[u]
				dict1[p].remove(u)
				if len(dict1) < 2:
					return 0
				
		return 2*(len(dict1)-1)
	
	
	
	


coins = [1,0,0,0,0,1]
edges = [[0,1],[1,2],[2,3],[3,4],[4,5]]
#Output: 2
Object2 = Solution()

print( Object2.collectTheCoins(coins, edges)  )	


coins = [0,0,0,1,1,0,0,1]
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[5,6],[5,7]]
#Output: 2
Object2 = Solution()

print( Object2.collectTheCoins(coins, edges)  )	

print()#####################################################################################################################################################################

# LEETCODE 2581. Count Number of Possible Root Nodes , DFS
# penolove

class Solution:
	def rootCount(self, edges: list[list[int]], guesses: list[list[int]], k: int) -> int:
		# n memory
		# build graph
		graph = defaultdict(list)
		for i, j in edges:
			graph[i].append(j)
			graph[j].append(i)
			
		gt = set((i, j) for i, j in guesses)
		
		# dfs traverse from parent -> i
		#@cache
		def get_correct_pairs(i, parent):
			next_nodes = graph[i]
			n_correct = 0
			for next_node in next_nodes:
				if next_node == parent:
					continue
				if (i, next_node) in gt:
					n_correct += 1
				n_correct += get_correct_pairs(next_node, i)
			return n_correct
		
		ans = 0
		for i in graph:
			if get_correct_pairs(i, None) >= k:
				ans += 1
		return ans
	
	
edges = [[0,1],[1,2],[1,3],[4,2]]
guesses = [[1,3],[0,1],[1,0],[2,4]]
k = 3
#Output: 3
Object2 = Solution()

print( Object2.rootCount(edges, guesses, k)  )


edges = [[0,1],[1,2],[2,3],[3,4]]
guesses = [[1,0],[3,4],[2,1],[3,2]]
k = 1
#Output: 5
Object2 = Solution()

print( Object2.rootCount(edges, guesses, k)  )

print()#####################################################################################################################################################################

# LEETCODE 2538. Difference Between Maximum and Minimum Price Sum, DFS

#vergil0327

class Solution:
	def maxOutput(self, n: int, edges: list[list[int]], price: list[int]) -> int:
		graph = defaultdict(list)
		indegree = [0] * n
		for u, v in edges:
			graph[u].append(v)
			graph[v].append(u)
			indegree[u] += 1
			indegree[v] += 1
			
		leaves = [node for node, deg in enumerate(indegree) if deg == 1]
		
		
		cache = {}
		def dfs(node, prev):
			if (node, prev) in cache:
				#print(cache)
				return cache[(node, prev)]
			
			pathsum = 0
			for nei in graph[node]:
				#print(nei, prev)
				if nei == prev: continue
				pathsum = max(pathsum, dfs(nei, node))
				
				
				#print( pathsum ,'+' ,price[node])
			cache[(node, prev)] = pathsum + price[node]
			
			return cache[(node, prev)]
		
		res = 0
		for node in leaves:
			#print(dfs(node, node) ,'-', price[node])
			res = max(res, dfs(node, node) - price[node])
			
		return res
	
	
n = 6
edges = [[0,1],[1,2],[1,3],[3,4],[3,5]]
price = [9,8,7,6,10,5]
#Output: 24

Object2 = Solution()

print( Object2.maxOutput(n, edges, price)  )

	
n = 3
edges = [[0,1],[1,2]]
price = [1,1,1]
#Output: 2
Object2 = Solution()

print( Object2.maxOutput(n, edges, price)  )

print()#####################################################################################################################################################################

#LEETCDOE 2440. Create Components With Same Value , DFS
#  rnotappl


class Solution:
	def componentValue(self, nums, edges):
		if not edges:
			return 0
		
		dict1, result = defaultdict(list), sum(nums)
		
		for i,j in edges:
			dict1[i].append(j)
			dict1[j].append(i)
			
		def dfs(a,b):
			total = nums[a]
			
			for neighbor in dict1[a]:
				if neighbor != b:
					total += dfs(neighbor,a)
					
			return total if total != i else 0
		
		for i in range(max(nums),result//min(nums)):
			if result%i == 0 and dfs(0,len(nums)-1) == 0:
				return result//i - 1
			
		return 0
	
	
	
nums = [6,2,2,2,6]
edges = [[0,1],[1,2],[1,3],[3,4]] 
#Output: 2 
Object2 = Solution()

print( Object2.componentValue(nums, edges)  )

nums = [2]
edges = []
#Output: 0
Object2 = Solution()

print( Object2.componentValue(nums, edges)  )


print()#####################################################################################################################################################################


# LEETCODE 2421. Number of Good Paths
# neetcodeio

from collections import deque


class UnionFind:
	def __init__(self, n):
		self.par = [i for i in range(n)]
		self.rank = [1] * n
		
	def find(self, x):
		while x != self.par[x]:
			self.par[x] = self.par[self.par[x]]
			x = self.par[x]
		return x
	
	def union(self, x1, x2):
		p1, p2 = self.find(x1), self.find(x2)
		if p1 == p2:
			return False
		if self.rank[p1] > self.rank[p2]:
			self.par[p2] = p1
			self.rank[p1] += self.rank[p2]
		else:
			self.par[p1] = p2
			self.rank[p2] += self.rank[p1]
		return True
	
	
class Solution:
	def numberOfGoodPaths(self, vals: list[int], edges: list[list[int]]) ->int:
		
		adj = defaultdict(list)
		
		for a, b in edges:
			adj[a].append(b)
			adj[b].append(a)
			
		valtoindex = defaultdict(list)
		
		for i, val in enumerate(vals):
			valtoindex[val].append(i)
			
		uf = UnionFind( len(vals) )
		res = 0
		for val in sorted( valtoindex.keys() ):
			for i in 	valtoindex[val]:
				for nei in adj[i]:
					if vals[nei] <= vals[i]:
						#print(  uf.par, uf.rank)
						uf.union( nei, i)
						#print(  uf.par, uf.rank)
						
			count = defaultdict(int)  
			
			for i in 	valtoindex[val]:
				count[(uf.find(i))] += 1
				#print(count[(uf.find(i))] ,'count[(uf.find(i))] ', i,nei, uf.par, uf.rank, val)
				res	+= count[(uf.find(i))] 
		return res
	
edges= [[0,1], [0,2], [2,3],[2,4]] 
vals = [1,3,2,1,3]
# OUTPUT  6

vals = [1,3,2,1,3]


Object2 = Solution()

print( Object2.numberOfGoodPaths(vals, edges)  )	

vals = [1,1,2,2,3]
edges = [[0,1],[1,2],[2,3],[2,4]]
#Output: 7
Object2 = Solution()

print( Object2.numberOfGoodPaths(vals, edges)  )	

vals = [1]
edges = []
#Output: 1
Object2 = Solution()

print( Object2.numberOfGoodPaths(vals, edges)  )	

print()#####################################################################################################################################################################

# LEETCODE 1617. Count Subtrees With Max Distance Between Cities
# ye15

from itertools import combinations


def countSubgraphsForEachDiameter(n, edges):
	def fn(edges): 
		#print("________________________________")
		
		""" """
		graph = {} # graph as adjacency list 
		for u, v in edges:
			graph.setdefault(u-1, []).append(v-1) # 0-indexed 
			graph.setdefault(v-1, []).append(u-1)
		group = [None]*n
		dist = [0]*n
		
		def dfs(x, d=0): 
				#print()
			""" """
			seen.add(x) # mark visited 
			for xx in graph.get(x, []): 
				dist[x] = max(dist[x], d)
				if group[xx] is None:
						#print(  x,  xx, '||', group[xx] ,'=', group[x],"    ", dist)
					
					group[xx] = group[x]
					#print(  x,  xx, '||', group[xx] ,'=', group[x],"    ", dist)
				if xx not in seen: dfs(xx, d+1)
					#print(  x,  xx, '||', group[xx] ,'=', group[x],"    ", dist)
					#print()
		for i in range(n): 
			seen = set()
			if group[i] is None: group[i] = i
			dfs(i)
		return group, dist 
	
	ans = {} # answer 
	for r in range(1,len(edges)+1):        
		for x in combinations(edges, r): 
				#print(x)
			temp = {}
			d = {}
			seen, dist = fn(x)
			#print(seen, dist)
				#print("______________________________")
			#print()
			for i in range(n): 
				temp.setdefault(seen[i], []).append(i)
				#print(temp)
					#print(  seen[i] ,  i)
					#print()
				if seen[i] not in d: d[seen[i]] = dist[i]
				else: d[seen[i]] = max(d[seen[i]], dist[i])
				#print(d,"d")
			for k, v in temp.items(): 
				if len(v) > 1: 
					ans.setdefault(d[k], set()).add(tuple(sorted(v)))
					#print(ans)
					
						#print()
	return [len(ans.get(x, set())) for x in range(1, n)]

	
	
	
n = 4
edges = [[1,2],[2,3],[2,4]]
#Output: [3,4,0]

print( countSubgraphsForEachDiameter(n, edges)  )	

n = 2
edges = [[1,2]]
#Output: [1]
print( countSubgraphsForEachDiameter(n, edges)  )	

n = 3
edges = [[1,2],[2,3]]
#Output: [2,1]
print( countSubgraphsForEachDiameter(n, edges)  )	

print()#####################################################################################################################################################################

# LEETCODE 1377 Frog Position After T Seconds
#yanrucheng

class Solution:
	def frogPosition(self, n: int, edges: list[list[int]], t: int, target: int) -> float:
		nei = defaultdict(set)
		for a, b in edges:
			nei[a].add(b)
			nei[b].add(a)
			
		visited, res = set(), 0.
		def dfs(leaf_id, p, time):
			nonlocal res
			if time >= t:
				if leaf_id == target: res = p
				return
			visited.add(leaf_id)
			neighbors = nei[leaf_id] - visited
			for n in neighbors or [leaf_id]:
				dfs(n, p / (len(neighbors) or 1), time + 1)
		dfs(1, 1, 0)
		return res
	
	
n = 7
edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
t = 2
target = 4
#Output: 0.16666666666666666 
Object2 = Solution()

print( Object2.frogPosition(n, edges, t, target)  )


n = 7
edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
t = 1
target = 7
#Output: 0.3333333333333333
Object2 = Solution()

print( Object2.frogPosition(n, edges, t, target)  )

print()#####################################################################################################################################################################


#LEETCODE 834 Sum of Distances in Tree ,DFS
#sanial2001	

class Solution:
	def sumOfDistancesInTree(self, n: int, edges: list[list[int]]) -> list[int]:
		g = defaultdict(list)
		for u, v in edges:
			g[u].append(v)
			g[v].append(u)
			
		d = {i:[1, 0] for i in range(n)}
		
		def dfs(root, prev):
			for nei in g[root]:
				if nei != prev:
					dfs(nei, root)
					d[root][0] += d[nei][0]
					d[root][1] += (d[nei][0] + d[nei][1])
					
		def dfs2(root, prev):
			for nei in g[root]:
				if nei != prev:
					d[nei][1] = d[root][1] - d[nei][0] + (n-d[nei][0])
					dfs2(nei, root)
					
		dfs(0, -1)
		dfs2(0, -1)
		res = []
		for key in d:
			res.append(d[key][1])
		return res	
	
	
n = 6
edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
#Output: [8,12,6,10,10,10]
Object2 = Solution()

print( Object2.sumOfDistancesInTree(n, edges)  )	

n = 1
edges = []
#Output: [0]
Object2 = Solution()

print( Object2.sumOfDistancesInTree(n, edges)  )

n = 2
edges = [[1,0]]
#Output: [1,1]
Object2 = Solution()

print( Object2.sumOfDistancesInTree(n, edges)  )

print()#####################################################################################################################################################################

#LEETCODE 2858 Minimum Edge Reversals So Every Node Is Reachable  ,BFS    or DFS
#Spaulding_

class Solution:
	def minEdgeReversals(self, n: int, edges: list[list[int]]) -> list[int]:
		
		g, ans, zeroCnt = defaultdict(list), defaultdict(int), 0
		
		for u, v in edges:
			g[u].append((v, 1))
			g[v].append((u,-1))
			
		queue = deque([(0,0)])
		
		while queue:
			par, parCnt = queue.pop()
			ans[par] = parCnt
			
			for chd,cnt in g[par]:
				if chd in ans: continue
				zeroCnt+= cnt
				queue.append((chd,cnt+parCnt))
				
		ans0 = (n-1-zeroCnt)//2
		return [ans[i] + ans0 for i in range(n)] 
	
	
n = 4
edges = [[2,0],[2,1],[1,3]]
#Output: [1,1,0,2]
Object2 = Solution()

print( Object2.minEdgeReversals(n, edges)  )	

n = 3
edges = [[1,2],[2,0]]
#Output: [2,0,1]
Object2 = Solution()

print( Object2.minEdgeReversals(n, edges)  )

print()#####################################################################################################################################################################

#LEETCDOE 2097.  Valid Arrangement of Pairs , BFS

#  brianchiang_tw  , brianchiang_tw

class Solution:
	def validArrangement(self, pairs: list[list[int]]) -> list[list[int]]:
		
		# in degree table for each node
		in_degree = defaultdict(int)
		
		# out degree table for each node
		out_degree = defaultdict(int)
		
		# adjacency matrix for each node
		adj_matrix = defaultdict(list)
		
		
		# update table with input edge pairs
		for src, dst in pairs:
			
			in_degree[dst] += 1
			out_degree[src] += 1
			adj_matrix[src].append(dst)
			
			
		## Case_#1:
		# There is eular circuit in graph, any arbitrary node can be start point, here we use source node of first edge just for convenience
		start_node_idx = pairs[0][0]
		
		
		## Case_#2
		# There is no eular circuit. But there is eular path, find the start node by indegree and outdegree relation
		for node in adj_matrix:
			
			# find the node whose outdegree is one more than indegree
			if out_degree[node] - in_degree[node] == 1:
				start_node_idx = node
				break
			
		# ------------------------------------------------
		def eular_path( adjMatrix, path, cur_node):
			
			# Keep traverse to next node in DFS until all edges of current node are visited
			while adjMatrix[cur_node]:
				
				# pop one edge and get next visit node
				next_visit_node = adjMatrix[cur_node].pop()
				
				eular_path( adjMatrix, path, next_visit_node )
				
				# post-order style
				# current explorer is finished, record current edge pair 
				path.append([cur_node, next_visit_node])
				
				
		# ------------------------------------------------
		record = []
		eular_path(adj_matrix, record, start_node_idx)
		
		# reversed of post-order record is the answer of eular path        
		return record[::-1]
	
	
pairs = [[5,1],[4,5],[11,9],[9,4]]
#Output: [[11,9],[9,4],[4,5],[5,1]]
Object2 = Solution()

print( Object2.validArrangement(pairs)  )

pairs = [[1,3],[3,2],[2,1]]
#Output: [[1,3],[3,2],[2,1]]
Object2 = Solution()

print( Object2.validArrangement(pairs)  )
pairs = [[1,2],[1,3],[2,1]]
#Output: [[1,2],[2,1],[1,3]]
Object2 = Solution()

print( Object2.validArrangement(pairs)  )

print()#####################################################################################################################################################################

#LEETCDOE 2092. Find All People With Secret ,BFS
# ye15  yegao

from itertools import groupby
class Solution:
	def findAllPeople(self, n: int, meetings: list[list[int]], firstPerson: int) -> list[int]:
		can = {0, firstPerson}
		for _, grp in groupby(sorted(meetings, key=lambda x: x[2]), key=lambda x: x[2]): 
			queue = set()
			graph = defaultdict(list)
			for x, y, _ in grp: 
				graph[x].append(y)
				graph[y].append(x)
				if x in can: queue.add(x)
				if y in can: queue.add(y)
				
			queue = deque(queue)
			while queue: 
				x = queue.popleft()
				for y in graph[x]: 
					if y not in can: 
						can.add(y)
						queue.append(y)
		return can
	
n = 6
meetings = [[1,2,5],[2,3,8],[1,5,10]]
firstPerson = 1
#Output: [0,1,2,3,5]	
Object2 = Solution()
print( Object2.findAllPeople(n, meetings, firstPerson)  )

n = 4
meetings = [[3,1,3],[1,2,2],[0,3,3]]
firstPerson = 3
#Output: [0,1,3]
Object2 = Solution()
print( Object2.findAllPeople(n, meetings, firstPerson)  )

n = 5 
meetings = [[3,4,2],[1,2,1],[2,3,1]]
firstPerson = 1
#Output: [0,1,2,3,4]
Object2 = Solution()
print( Object2.findAllPeople(n, meetings, firstPerson)  )

print()#####################################################################################################################################################################

# LEETCODE 1192. Critical Connections in a Network
##  ye15

class Solution:
	def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
		graph = {} # graph as adjacency list 
		for u, v in connections: 
			graph.setdefault(u, []).append(v)
			graph.setdefault(v, []).append(u)
			
		def dfs(x, p, step): 
			"""Traverse the graph and collect bridges using Tarjan's algo."""
			disc[x] = low[x] = step
			for xx in graph.get(x, []): 
				if disc[xx] == inf: 
					step += 1
					dfs(xx, x, step)
					low[x] = min(low[x], low[xx])
					if  disc[x] < low[xx] : ans.append([x, xx]) # bridge
				elif xx != p: low[x] = min(low[x], disc[xx])
				
		inf = 9999999		
		ans = []
		low = [inf]*n
		disc = [inf]*n
		
		dfs(0, -1, 0)
		return ans 
	
n = 4
connections = [[0,1],[1,2],[2,0],[1,3]]
#Output: [[1,3]]
#Explanation: [[3,1]] is also accepted.
Object2 = Solution()

print( Object2.criticalConnections(n, connections) )   #,"THIS" )	

n = 2
connections = [[0,1]]
#Output: [[0,1]]	
Object2 = Solution()

print( Object2.criticalConnections(n, connections)  )	


print()#####################################################################################################################################################################

####   LEETCODE 685. Redundant Connection II
# me

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

print()#####################################################################################################################################################################

# LEETCODE 332. Reconstruct Itinerary
# neetcodeio

class Solution:
	def findItinerary(self, tickets: list[list[str]]) -> list[str]:
		adj = {src: [] for src, dst in tickets}
		res = []
		
		for src, dst in tickets:
			adj[src].append(dst)
			
		for key in adj:
			adj[key].sort()
			
		def dfs(adj, result, src):
			if src in adj:
				destinations = adj[src][:]
				while destinations:
					dest = destinations[0]
					adj[src].pop(0)
					dfs(adj, res, dest)
					destinations = adj[src][:]
			res.append(src)
			
		dfs(adj, res, "JFK")
		res.reverse()
		
		if len(res) != len(tickets) + 1:
			return []
		
		return res
	
	
	
tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
#Output: ["JFK","MUC","LHR","SFO","SJC"]
Object2 = Solution()
print( Object2.findItinerary(tickets) ) 


tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
#Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Object2 = Solution()
print( Object2.findItinerary(tickets) ) 	
	
print()#####################################################################################################################################################################
	
##  LEETCODE 2608. Shortest Cycle in a Graph  ,BFS
##  rnotappl

def findShortestCycle(n, edges):
	dict1, min_val = defaultdict(list), float("inf")
	
	
	for i,j in edges:
		dict1[i].append(j)
		dict1[j].append(i)
		
	for i in range(n):
		dis, stack = [-1]*n, [i]
		
		dis[i] = 0
		
		while stack:
			node = stack.pop(0)
			
			for neighbor in dict1[node]:
				#if dis[node] > dis[neighbor] :
				if dis[neighbor] == -1:
					dis[neighbor] = dis[node] + 1
					stack.append(neighbor)
				elif dis[neighbor] >= dis[node]:
					min_val = min(min_val,dis[neighbor]+dis[node]+1)
					
	return min_val if min_val != float("inf") else -1


n = 7

edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]]
#Output: 3
print( findShortestCycle(n, edges))

n = 4
edges = [[0,1],[0,2]]
#Output: -1
print( findShortestCycle(n, edges))	

print()#####################################################################################################################################################################

#LEETCDOE 2493 Divide Nodes Into the Maximum Number of Groups ,BFS
#user4203yE

class Solution:
	def magnificentSets(self, n: int, edges: list[list[int]]) -> int:
		g = defaultdict(set)
		for u,v in edges:
			u, v = u-1, v-1
			g[u].add(v)
			g[v].add(u)
			
		ans = defaultdict(lambda: float('-inf'))
		for u in range(n):
			q, visited, steps = [u], set([u]), 0
			while q:
				steps += 1
				q1 = set()
				for u in q:
					for v in g[u]:
						if v in q: return -1
						if v not in visited:
							q1.add(v)
							visited.add(v)
				q = q1
				
			k = min(visited)
			ans[k] = max(ans[k], steps)
			
		return sum(ans.values())
	
	
	
n = 6
edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]
#Output: 4
Object2 = Solution()

print( Object2.magnificentSets(n, edges)  )

n = 3
edges = [[1,2],[2,3],[3,1]]
#Output: -1
Object2 = Solution()

print( Object2.magnificentSets(n, edges)  )

print()#####################################################################################################################################################################

#LEETCDOE 2045. Second Minimum Time to Reach Destination ,BFS
#DBabichev

class Solution:
	def secondMinimum(self, n, edges, time, change):
		D = [[] for _ in range(n + 1)]
		
		D[1] = [0]
		G, heap = defaultdict(list), [(0, 1)]
		
		for a, b in edges:
			G[a] += [b]
			G[b] += [a]
			
		while heap:
			min_dist, idx = heapq.heappop(heap)
			if idx == n and len(D[n]) == 2: return max(D[n])
			
			for neib in G[idx]:
				if (min_dist // change) % 2 == 0:
					cand = min_dist + time
					#print(cand)
				else:
					cand = math.ceil(min_dist/(change)) * (change) + time
					#print('(',min_dist,'/',change,')) * (',change,') + ',time,')')
					#print(cand)
					
				if not D[neib] or (len(D[neib]) == 1 and D[neib] != [cand]):
					D[neib] += [cand]
					heapq.heappush(heap, (cand, neib))
					#print(D)
					
					
n = 5
edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]
time = 3
change = 5
#Output: 13
Object2 = Solution()

print( Object2.secondMinimum(n, edges, time, change)  )


n = 2
edges = [[1,2]]
time = 3
change = 2
#Output: 11
Object2 = Solution()

print( Object2.secondMinimum(n, edges, time, change)  )

print()#####################################################################################################################################################################

#LEETCDOE 815 Bus Routes ,BFS
#yegao ye15

class Solution:
	def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
		mp = {}
		for i, route in enumerate(routes): 
			for x in route: 
				mp.setdefault(x, []).append(i)
				
		ans = 0 
		seen = {source}
		queue = [source]
		while queue: 
			newq = []
			for x in queue: 
				if x == target: return ans 
				for i in mp[x]: 
					for xx in routes[i]: 
						if xx not in seen: 
							seen.add(xx)
							newq.append(xx)
					routes[i] = []
			ans += 1
			queue = newq
		return -1 
	
	
	
routes = [[1,2,7],[3,6,7]]
source = 1
target = 6
#Output: 2	
Object2 = Solution()

print( Object2.numBusesToDestination(routes, source, target)  )

routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]]
source = 15
target = 12
#Output: -1
Object2 = Solution()

print( Object2.numBusesToDestination(routes, source, target)  )

print()#####################################################################################################################################################################

# LEETCODE 1697. Checking Existence of Edge Length Limited Paths
#  ye15

class UnionFind:
	def __init__(self, N: int):
		self.parent = list(range(N))
		self.rank = [1] * N
		
	def find(self, p: int) -> int:
		if p != self.parent[p]:
			self.parent[p] = self.find(self.parent[p])
		return self.parent[p]
	
	def union(self, p: int, q: int) -> bool:
		prt, qrt = self.find(p), self.find(q)
		if prt == qrt: return False 
		if self.rank[prt] > self.rank[qrt]: 
			prt, qrt = qrt, prt 
		self.parent[prt] = qrt 
		self.rank[qrt] += self.rank[prt] 
		return True 
	
	
class Solution:
	def distanceLimitedPathsExist(self, n: int, edgeList: list[list[int]], queries: list[list[int]]) -> list[bool]:
		queries = sorted((w, p, q, i) for i, (p, q, w) in enumerate(queries))
		edgeList = sorted((w, u, v) for u, v, w in edgeList)
		
		uf = UnionFind(n)
		
		ans = [None] * len(queries)
		ii = 0
		for w, p, q, i in queries: 
			while ii < len(edgeList) and edgeList[ii][0] < w: 
				_, u, v = edgeList[ii]
				uf.union(u, v)
				ii += 1
			ans[i] = uf.find(p) == uf.find(q)
		return ans 

n = 3
edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]]
queries = [[0,1,2],[0,2,5]]
#Output: [false,true]
Object2 = Solution()

print( Object2.distanceLimitedPathsExist(n, edgeList, queries)  )

n = 5
edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]]
queries = [[0,4,14],[1,4,13]]
#Output: [true,false]
Object2 = Solution()
	
print( Object2.distanceLimitedPathsExist(n, edgeList, queries)  )


print()#####################################################################################################################################################################

# LEEICODE 1579. Remove Max Number of Edges to Keep Graph Fully Traversable
#  ye15

class UnionFind:
	"""A minimalist standalone union-find implementation."""
	def __init__(self, n):
		self.count = n               # number of disjoint sets 
		self.parent = list(range(n)) # parent of given nodes
		self.rank = [1]*n            # rank (aka size) of sub-tree 
		
	def find(self, p):
		"""Find with path compression."""
		if p != self.parent[p]: 
			self.parent[p] = self.find(self.parent[p]) # path compression 
		return self.parent[p]
	
	def union(self, p, q):
		"""Union with ranking."""
		prt, qrt = self.find(p), self.find(q)
		if prt == qrt: return False
		self.count -= 1 # one more connection => one less disjoint 
		if self.rank[prt] > self.rank[qrt]: prt, qrt = qrt, prt # add small sub-tree to large sub-tree for balancing
		self.parent[prt] = qrt
		self.rank[qrt] += self.rank[prt] # ranking 
		return True
	
	
class Solution:
	def maxNumEdgesToRemove(self, n: int, edges: list[list[int]]) -> int:
		ufa = UnionFind(n) # for Alice
		ufb = UnionFind(n) # for Bob
		
		ans = 0
		edges.sort(reverse=True) 
		for t, u, v in edges: 
			u, v = u-1, v-1
			if t == 3: ans += not (ufa.union(u, v) and ufb.union(u, v)) # Alice & Bob
			elif t == 2: ans += not ufb.union(u, v)                     # Bob only
			else: ans += not ufa.union(u, v)                            # Alice only
		return ans if ufa.count == 1 and ufb.count == 1 else -1 # check if uf is connected 
	
	
n = 4
edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
#Output: 2
Object2 = Solution()

print( Object2.maxNumEdgesToRemove(n, edges)  )

n = 4
edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
#Output: 0
Object2 = Solution()

print( Object2.maxNumEdgesToRemove(n, edges)  )


n = 4
edges = [[3,2,3],[1,1,2],[2,3,4]]
#Output: -1
Object2 = Solution()

print( Object2.maxNumEdgesToRemove(n, edges)  )

print()#####################################################################################################################################################################

# LEETCODE 1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
# neetcodeio

class UnionFind:
	def __init__(self, n):
		self.par = [i for i in range(n)]
		self.rank = [1] * n
		
	def find(self, v1):
		while v1 != self.par[v1]:
			self.par[v1] = self.par[self.par[v1]]
			v1 = self.par[v1]
		return v1
	
	def union(self, v1, v2):
		p1, p2 = self.find(v1), self.find(v2)
		if p1 == p2:
			return False
		if self.rank[p1] > self.rank[p2]:
			self.par[p2] = p1
			self.rank[p1] += self.rank[p2]
		else:
			self.par[p1] = p2
			self.rank[p2] += self.rank[p1]
		return True
	
class Solution:
	def findCriticalAndPseudoCriticalEdges(self, n: int, edges: list[list[int]]) -> list[list[int]]:
		# Time: O(E^2) - UF operations are assumed to be approx O(1)
		for i, e in enumerate(edges):                          # 1
			e.append(i) # [v1, v2, weight, original_index]
		
		edges.sort(key=lambda e: e[2])             # 2
		#cnt = 0                                   #  3
		mst_weight = 0                          # 4
		uf = UnionFind(n)                       # 5
		for v1, v2, w, i in edges:               # 6
			#cnt+=1
			if uf.union(v1, v2):               # 7
				#cnt+=1
				mst_weight += w                # 8
		
		critical, pseudo = [], []             #  9
		for n1, n2, e_weight, i in edges:     # 10
			# Try without curr edge
			weight = 0                        #  11
			uf = UnionFind(n)                 #  12
			#cnt+=1
			for v1, v2, w, j in edges:        #   13
				#cnt+=1
				if i != j and uf.union(v1, v2):       #   14
					#cnt+=1
					weight += w                       #     15
			if max(uf.rank) != n or weight > mst_weight:      #          > , = ,  <            5    5     1         2     ||||   3, 2, 6, 2                     #   16
				#cnt+=1
				critical.append(i)                     #   17
				continue                              #    18
			#cnt+=1
		
			# Try with curr edge
			uf = UnionFind(n)                          #    19
			uf.union(n1, n2)                           #    20
			weight = e_weight                          #    21
			for v1, v2, w, j in edges:
				#cnt+=1######### THIS    35     11       24  or 46
				#print(v1,v2,w,cnt)
				if uf.union(v1, v2):                     #    22
					#cnt+=1
					weight += w                          #  23
			if weight == mst_weight:                    #  24
				#cnt+=1
				pseudo.append(i)                       #  25
		
		#print(cnt,"cnt")
		return [critical, pseudo]
	

n = 5
edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
Object = Solution()

print( Object.findCriticalAndPseudoCriticalEdges(n, edges)  )

n = 4
edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
#Output: [[],[0,1,2,3]]
Object = Solution()

print( Object.findCriticalAndPseudoCriticalEdges(n, edges)  )

print()#####################################################################################################################################################################

# LEETCODE 2050. Parallel Courses III
# leetcode solution

class Solution:
	def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
		graph = defaultdict(list)
		indegree = [0] * n
		
		for (x, y) in relations:
			graph[x - 1].append(y - 1)
			indegree[y - 1] += 1
			
		queue = deque()
		max_time = [0] * n
		for node in range(n):
			if indegree[node] == 0:
				queue.append(node)
				max_time[node] = time[node]
				
		while queue:
			node = queue.popleft()
			for neighbor in graph[node]:
				#print(max_time[neighbor], max_time[node] ,'+', time[neighbor],'=',max(max_time[neighbor], max_time[node] + time[neighbor]),'    ',node+1,'->',neighbor+1)
				max_time[neighbor] = max(max_time[neighbor], max_time[node] + time[neighbor])  # 3,4 added prior to 5
				indegree[neighbor] -= 1
				if indegree[neighbor] == 0:
					queue.append(neighbor)
					
		return max(max_time)
	
	
n = 3
relations = [[1,3],[2,3]]
time = [3,2,5]
#Output: 8
Object = Solution()

print( Object.minimumTime(n, relations, time)  )

n = 5
relations = [[1,5],[2,5],[3,5],[3,4],[4,5]]
time = [1,2,3,4,5]
#Output: 12
Object = Solution()

print( Object.minimumTime(n, relations, time)  )

print()#####################################################################################################################################################################

# LEETCODE 1857. Largest Color Value in a Directed Graph
#  https://walkccc.me/LeetCode/problems/1857/#__tabbed_1_3

def largestPathValue(colors, edges):
	n = len(colors)
	ans = 0
	processed = 0
	graph = [[] for _ in range(n)]
	inDegree = [0] * n
	q = deque()
	count = [[0] * 26 for _ in range(n)]
	
	# Build graph.
	for u, v in edges:
		graph[u].append(v)
		#print(graph)
		inDegree[v] += 1
	#print(inDegree)
	#print(graph)
		
		
	# Vpology
	for i, degree in enumerate(inDegree):
		if degree == 0:
			q.append(i)
			#print(q,"Q") # 0
			
	while q:
		u = q.popleft()
		processed += 1
		count[u][ord(colors[u]) - ord('a')] += 1
		#print(count, end=" ")
		#print()
		#print()
		ans = max(ans, count[u][ord(colors[u]) - ord('a')])
		for v in graph[u]:
			for i in range(26):
				count[v][i] = max(count[v][i], count[u][i])
			inDegree[v] -= 1
			if inDegree[v] == 0:
				q.append(v)
				
	return ans if processed == n else -1

colors = "abaca"
edges = [[0,1],[0,2],[2,3],[3,4]]
# 3
print(largestPathValue(colors, edges))

colors = "a"
edges = [[0,0]]
#Output: -1
print(largestPathValue(colors, edges))

print()#####################################################################################################################################################################

# LEETCODE 2065. Maximum Path Quality of a Graph
# harrychen1995

class Solution:
	def maximalPathQuality(self, values: list[int], edges: list[list[int]], maxTime: int) -> int:
		
		
		graph = defaultdict(set)
		time = {}
		for a, b, t in edges:
			time[(a,b)] = t
			time[(b,a)] = t
			graph[a].add(b)
			graph[b].add(a)
		ans  = 0
		def dfs(root, t, visit, s):
			if t > maxTime:
				return
			if root == 0:
				nonlocal ans
				ans = max(ans, s)
				
			visit.add(root)
			for v in graph[root]:
				if v not in visit:
					dfs(v, t+time[(root,v)], set(visit), s+values[v])
				else:
					dfs(v,t+time[(root,v)], set(visit), s)
					
					
		dfs(0,  0, set(), values[0])
		return ans
	
	
values = [0,32,10,43]
edges = [[0,1,10],[1,2,15],[0,3,10]]
maxTime = 49
#Output: 75
Object = Solution()

print( Object.maximalPathQuality(values, edges, maxTime)  )

values = [5,10,15,20]
edges = [[0,1,10],[1,2,10],[0,3,10]]
maxTime = 30
#Output: 25
Object = Solution()

print( Object.maximalPathQuality(values, edges, maxTime)  )

values = [1,2,3,4]
edges = [[0,1,10],[1,2,11],[2,3,12],[1,3,13]]
maxTime = 50
#Output: 7
Object = Solution()

print( Object.maximalPathQuality(values, edges, maxTime)  )
	
print()#####################################################################################################################################################################

# LEETCODE 1601. Maximum Number of Achievable Transfer Requests
# uds5501


class Solution:
	def maximumRequests(self, n: int, req: list[list[int]]) -> int:
		tot = len(req)
		for i in range(tot, 0, -1):
			comb = list(combinations([j for j in range(tot)], i))
			for c in comb:
				net = [0 for j in range(n)]
				for idx in c:
					net[req[idx][0]] -= 1
					net[req[idx][1]] += 1
				if net == [0 for j in range(n)]:
					return i
		return 0
	
n = 5
requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
#Output: 5
Object = Solution()

print( Object.maximumRequests(n, requests)  )

n = 3
requests = [[0,0],[1,2],[2,1]]
#Output: 3
Object = Solution()

print( Object.maximumRequests(n, requests)  )


n = 4
requests = [[0,3],[3,1],[1,2],[2,0]]
#Output: 4
Object = Solution()

print( Object.maximumRequests(n, requests)  )

print()#####################################################################################################################################################################

# LEETCODE 2959. Number of Possible Sets of Closing Branches
# xil899

class Solution:
	def numberOfSets(self, n: int, maxDistance: int, roads: list[list[int]]) -> int:
		def check(subset, n, maxDistance, roads):
			dist = [[float('inf')] * n for _ in range(n)]
			for i in range(n):
				dist[i][i] = 0
			for u, v, w in roads:
				#print('u',u,'  v',v, '  w',w ,'   ',dist,'old dist')
				if u in subset and v in subset:
					#print(dist,'{{{{',subset)
					dist[u][v] = min(dist[u][v], w)
					dist[v][u] = min(dist[v][u], w)
					#print(dist,'+++++',subset)
					#print()
			q = []
			cn = 0
			for k in subset:
				#cn = 0
				for i in subset:
					#cn=0
					for j in subset:
						#print(dist,'before   ',min(dist[i][j], dist[i][k] + dist[k][j]),'     ',i,j,  '        ', i,k,  k,j,'                     ',dist[i][j],"   ",subset)
						dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
						#print(dist,'after  ',min(dist[i][j],dist[i][k] + dist[k][j]),'      ',i,j, '         ',i,k,  k,j,'                       ', dist[i][j],"   ",subset)
						#cn +=1
						#if [i,k,k,j] not in q:
							#q.append([i,k,k,j])
						#print(cn,'CN')
					
						#print(q,'Q', len(q))
			for i in subset:
				for j in subset:
					#if dist[i][j] <= maxDistance:
						#print(subset,'pppp')
					if dist[i][j] > maxDistance:
						#print(dist,'maxDistance',i,j,subset)  28    57      48
						
						return False
					
			return True
		
		ans = 0
		for r in range(n + 1):
			for subset in combinations(range(n), r):
				#print(subset,'subset')
				if check(subset, n, maxDistance, roads):
					ans += 1
		return ans
	
n = 3
maxDistance = 5
roads = [[0,1,2],[1,2,10],[0,2,10]]
#Output: 5
Object = Solution()
	
print( Object.numberOfSets(n, maxDistance, roads)  )
	
n = 3 
maxDistance = 5
roads = [[0,1,20],[0,1,10],[1,2,2],[0,2,2]]
#  Output: 7    
Object = Solution()

print( Object.numberOfSets(n, maxDistance, roads)  )


n = 1
maxDistance = 10
roads = []
#Output: 2
Object = Solution()

print( Object.numberOfSets(n, maxDistance, roads)  )

print()#####################################################################################################################################################################

# LEETCODE 2699. Modify Graph Edge Weights
# yuanzhi247012

import heapq

#  >    =     <           <     =   <=    =
class Solution:
	def modifiedGraphEdges(self, n: int, edges: list[list[int]], source: int, destination: int, target: int) -> list[list[int]]:
		dynamicEdges = set()
		d = defaultdict(lambda: defaultdict(int))
		for a, b,  w in edges:
			if w == -1:
				dynamicEdges.add((a,b))
				w = 2*10**9
			d[a][b] = d[b][a] = w
		def djistr():
			q = [(0,source)]
			visited = set()
			while q:
				cost, node = heapq.heappop(q)
				if node == destination:
					return cost
				if node in visited:
					continue
				visited.add(node)
				for next, cost2 in d[node].items() :
					heapq.heappush(q, (cost+cost2,  next))
		def retrn():
			return [[a,b,w] for a, d2 in d.items() for b, w in d2.items() if a<b]
		cost = djistr()
		if cost < target :
			return []
		if cost == target :
			return retrn()
		cost = djistr()
		for a, b in dynamicEdges:
			d[a][b] = d[b][a] = 1
			cost = djistr()
			if cost <= target :
				d[a][b] = d[b][a] = target - cost + 1
				cost = djistr()
				if cost == target :
					return retrn()
		return []
	
n = 5,
edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]]   # 36
source = 0
destination = 1
target = 5
#Output: [[4,1,1],[2,0,1],[0,3,3],[4,3,1]]



Object = Solution()

print( Object.modifiedGraphEdges(n, edges, source, destination, target))  #, 'ANS')

n = 3
edges = [[0,1,-1],[0,2,5]]
source = 0
destination = 2
target = 6
#Output: []
Object = Solution()

print( Object.modifiedGraphEdges(n, edges, source, destination, target)) 

n = 4
edges = [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]]
source = 0
destination = 2
target = 6
#Output: [[1,0,4],[1,2,3],[2,3,5],[0,3,1]]
Object = Solution()

print( Object.modifiedGraphEdges(n, edges, source, destination, target)) 

print()#####################################################################################################################################################################

# LEETCODE  2642. Design Graph With Shortest Path Calculator
# leetcode solution

class Graph:
	
	def __init__(self, n: int, edges: list[list[int]]):
		self.adj_list = [[] for _ in range(n)]
		for from_node, to_node, cost in edges:
			self.adj_list[from_node].append((to_node, cost))
			
	def addEdge(self, edge: list[int]) -> None:
		from_node, to_node, cost = edge
		self.adj_list[from_node].append((to_node, cost))
		
	def shortestPath(self, node1: int, node2: int) -> int:
		n = len(self.adj_list)
		pq = [(0, node1)]
		cost_for_node = [inf] * (n)
		cost_for_node[node1] = 0
		
		while pq:
			curr_cost, curr_node = heapq.heappop(pq)
			if curr_cost > cost_for_node[curr_node]:
				continue
			if curr_node == node2:
				return curr_cost
			for neighbor, cost in self.adj_list[curr_node]:
				new_cost = curr_cost + cost
				if new_cost < cost_for_node[neighbor]:
					cost_for_node[neighbor] = new_cost
					heapq.heappush(pq, (new_cost, neighbor))
		return -1
	
	
	
class Graph:
	
	def __init__(self, n, edges):
		inf = 9999999
		self.adj_matrix = [[inf] * n for _ in range(n)]
		for from_node, to_node, cost in edges:
			self.adj_matrix[from_node][to_node] = cost
		for i in range(n):
			self.adj_matrix[i][i] = 0
		for i in range(n):
			for j in range(n):
				for k in range(n):
					self.adj_matrix[j][k] = min(self.adj_matrix[j][k],
												self.adj_matrix[j][i] + 
												self.adj_matrix[i][k])
					
	def addEdge(self, edge: list[int]) -> None:
		from_node, to_node, cost = edge
		n = len(self.adj_matrix)
		for i in range(n):
			for j in range(n):
				self.adj_matrix[i][j] = min(self.adj_matrix[i][j],
											self.adj_matrix[i][from_node] + 
											self.adj_matrix[to_node][j] +
											cost)
				
	def shortestPath(self, node1, node2):
		inf = 9999999
		if self.adj_matrix[node1][node2] == inf: return -1
		return self.adj_matrix[node1][node2]
	
	
	
["Graph", "shortestPath", "shortestPath", "addEdge", "shortestPath"]
[[4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]], [3, 2], [0, 3], [[1, 3, 4]], [0, 3]]
#Output [null, 6, -1, null, 6]

#obj = Graph(n, edges)
#obj.addEdge(edge)
#param_2 = obj.shortestPath(node1,node2)

#print(param_2)


print()#####################################################################################################################################################################

# LEETCODE  2203. Minimum Weighted Subgraph With the Required Paths
#  DBabichev

class Solution:
	def minimumWeight(self, n, edges, s1, s2, dest):
		G1 = defaultdict(list)
		G2 = defaultdict(list)
		for a, b, w in edges:
			G1[a].append((b, w))
			G2[b].append((a, w))
			
		def Dijkstra(graph, K):
			q, t = [(0, K)], {}
			while q:
				time, node = 	heapq.heappop(q)
				if node not in t:
					t[node] = time
					for v, w in graph[node]:
						heapq.heappush(q, (time + w, v))
			return [t.get(i, float("inf")) for i in range(n)]
		
		arr1 = Dijkstra(G1, s1)
		arr2 = Dijkstra(G1, s2)
		arr3 = Dijkstra(G2, dest)
		
		ans = float("inf")
		for i in range(n):
			ans = min(ans, arr1[i] + arr2[i] + arr3[i])
			
		return ans if ans != float("inf") else -1
	
	
n = 6
edges = [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]]
src1 = 0
src2 = 1
dest = 5
#Output: 9
Object = Solution()

print( Object.minimumWeight(n, edges, src1, src2, dest)) 

n = 3
edges = [[0,1,1],[2,1,1]]
src1 = 0
src2 = 1
dest = 2
#Output: -1
Object = Solution()

print( Object.minimumWeight(n, edges, src1, src2, dest)) 


print()#####################################################################################################################################################################

# LEETCODE 882. Reachable Nodes In Subdivided Graph
# ye15

class Solution:
	def reachableNodes(self, edges: list[list[int]], maxMoves: int, n: int) -> int:
		graph = defaultdict(dict)
		for u, v, w in edges: graph[u][v] = graph[v][u] = w
		
		ans = 0
		pq = [(0, 0)] # min-heap 
		
		seen = [False] * n
		used = defaultdict(int)
		
		while pq: 
			x, u = heapq.heappop(pq)
			if not seen[u]: 
				ans += 1
				seen[u] = True 
				for v, c in graph[u].items(): 
					if not used[u, v]: 
						#print(used[u, v],used[v, u],graph[v][u],'used[u, v]')
						if used[v, u] < graph[v][u]: 
							used[u, v] = min(maxMoves - x, graph[v][u] - used[v, u])
							ans += used[u, v]
						if x + c + 1 <= maxMoves and not seen[v]: heapq.heappush(pq, (x + c + 1, v))
		return ans 
	
	
edges = [[0,1,10],[0,2,1],[1,2,2]]
maxMoves = 6
n = 3
#Output: 13
Object = Solution()

print( Object.reachableNodes(edges, maxMoves, n)) 


edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]]
maxMoves = 10
n = 4
#Output: 23
Object = Solution()

print( Object.reachableNodes(edges, maxMoves, n)) 

edges = [[1,2,4],[1,4,5],[1,3,1],[2,3,4],[3,4,5]]
maxMoves = 17
n = 5
#Output: 1
Object = Solution()

print( Object.reachableNodes(edges, maxMoves, n)) 