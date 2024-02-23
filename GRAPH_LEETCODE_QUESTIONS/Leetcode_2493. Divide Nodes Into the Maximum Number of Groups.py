#LEETCDOE 2493 Divide Nodes Into the Maximum Number of Groups ,BFS

from collections import defaultdict

class Solution:
	def magnificentSets(self, n: int, edges: list[list[int]]) -> int:
		g = defaultdict(set)
		for u,v in edges:
			u, v = u-1, v-1
			g[u].add(v)
			g[v].add(u)
			
		ans = defaultdict(lambda: float('-inf'))
		
		for u in range(n):
			dist=[0]*n  # current distribution
			dist2=[0]*n  # next distribution
			q, visited, steps = [u], set([u]), 0
			
			ls = []
			while q:
				steps += 1
				qw = set()
				for u in q:
					dist[u] += 1
					ls.append(u)
					for v in g[u]:
						dist2[v] += 1
						if dist[v] >= dist2[v] :  # if the  v from the previous distribution, dist   is >= the v from the next distribution it means v has been seen before 
							return -1
						if dist[v] < dist2[v] and v not in ls : 
							
							qw.add(v)
							visited.add(v)
						
							
				dist = dist2
				dist2=[0]*n
				q = list(qw)
				
				
				
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



n = 10
edges = [[3,5],[4,2],[4,7],[6,8],[2,6],[6,3],[6,1],[1,5],[6,7],[5,9],[9,6],[6,10],[10,4]]
Object2 = Solution()  # Not sure of this test case !!!

print( Object2.magnificentSets(n, edges)  )



n = 92
edges = [[67,29],[13,29],[77,29],[36,29],[82,29],[54,29],[57,29],[53,29],[68,29],[26,29],[21,29],[46,29],[41,29],[45,29],[56,29],[88,29],[2,29],[7,29],[5,29],[16,29],[37,29],[50,29],[79,29],[91,29],[48,29],[87,29],[25,29],[80,29],[71,29],[9,29],[78,29],[33,29],[4,29],[44,29],[72,29],[65,29],[61,29]]
# 57
Object2 = Solution()

print( Object2.magnificentSets(n, edges)  )


n = 5 
edges = [[1,2],[1,3],[1,4],[1,5]]
# 3
Object2 = Solution()

print( Object2.magnificentSets(n, edges)  )
