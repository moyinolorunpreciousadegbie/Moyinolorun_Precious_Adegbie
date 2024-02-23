from collections import defaultdict

def check(ans):
	q = [0] * (max(ans)+1)
	for i in ans:
		q[i]+=1
	qq = []
	for i in ans:
		if q[i] == 1:
			qq.append(i)
	return qq
			
class Solution:
	def RedundantConnections(self, edges: list[list[int]]) -> int:
		n = len(edges)
		g = defaultdict(set)
		for u,v in edges:
			u, v = u, v
			g[u].add(v)
			
			
		ans = []
		for u in range(n):
			q, visited, steps = [u], set([u]), 0
			while q:
				steps += 1
				q1 = set()
				for u in q:
					for v in g[u]:
						if v in q : 
							ans.append(u)
							ans.append(v) 
													
							
						if v not in visited: 
							q1.add(v)
							visited.add(v)
				q = q1
			
		q = set()
		for u, v in edges:
			q.add(u)
			if v in q:
				ans.append(u)
				ans.append(v)
			
		
		return check(ans)
	
	
	
edges = [[1,2],[1,3],[2,3]]
#Output: [2,3]

Object2 = Solution()

print( Object2.RedundantConnections(edges)  )

edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
#Output: [4,1]


Object2 = Solution()

print( Object2.RedundantConnections(edges)  )
 


edges = [[2,1],[3,1],[4,2],[1,4]]
#Output: [2,1]

Object2 = Solution()

print( Object2.RedundantConnections(edges)  )

