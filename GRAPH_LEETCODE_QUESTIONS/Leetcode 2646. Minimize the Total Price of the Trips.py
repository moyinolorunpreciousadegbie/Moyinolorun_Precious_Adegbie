#!/usr/bin/env python3

class Solution:
	def minimumTotalPrice(self, n: int, e: list[list[int]], price: list[int], trips: list[list[int]]) -> int:
		edges = [[] for _ in range(n)]
		save = {}
		
		def dfs(start, start2, path, par):
			
			save[(start, start2)]  = path+[start2]
			seen.add(start2)
			path = path+[start2] # adding the paths up
			
			for next in edges[start2]:
				if next != par and next not in seen:
					#  not in seen:
					dfs( start, next,path, start2)
					
		for u, v in e:
			edges[u].append(v)
			edges[v].append(u)
		for i in range(n):
		      
			path = []
			seen = set()
			dfs(i, i , path, -1)
			
		print(save)		   
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

#3  {(0, 0): [0], (0, 1): [0, 1], (0, 2): [0, 1, 2], (0, 3): [0, 1, 3], (1, 1): [1], (1, 0): [1, 0], (1, 2): [1, 2], (1, 3): [1, 3], (2, 2): [2], (2, 1): [2, 1], (2, 0): [2, 1, 0], (2, 3): [2, 1, 3], (3, 3): [3], (3, 1): [3, 1], (3, 0): [3, 1, 0], (3, 2): [3, 1, 2]} save
