from itertools import combinations
from collections import defaultdict

def closingbranches(n, edges, maxDistance):
    
    def fn(edges): 
    
        graph = {}    
        graph2 = {} # graph as adjacency list 
        for u, v , w in edges:
            graph.setdefault(u, []).append(v) 
            graph.setdefault(v, []).append(u)
            graph2[(u, v)] = w
            graph2[(v, u)] = w
        
            
        def dfs(x, w , par):  # DFS solution fails one test case
            
            seen.add(x)
            lss.append(x)
            
            #print(w,' DFS SOLUTION',(tuple(set(lss))))
            if w <= maxDistance :
                ans[(tuple(set(lss)))] = w
                
             # mark visited 
            for xx  in graph.get(x, []):
                                        
                if xx not in seen and xx != par  : 
                    
                    dfs(xx, w + graph2[(x, xx)], x)
            
            
        def bfs(x, w, par):
            
            q = [(x, w , -1)]
            while q:
                curr, wei, prev = q.pop(0)
                #print(wei, 'wwwwww      ', tuple(set(ls)))
                seen2.add(curr) 
                ls.append(curr)
                for xx in graph.get(x, []):
                    if xx not in seen2 and xx != par:
                        q.append((xx, wei +  graph2[(x, xx)] , curr))
                        
                    
            if wei <= maxDistance :
                ans[(tuple(set(ls)))] = wei
    
    
        for i in range(n): 
            seen = set()
            seen2 = set()
            lss = [i]
            ls = [i]
            #dfs(i, 0, -1)  # DFS solution fails one test case
            bfs(i, 0, -1)
        
        
    ans = defaultdict(set) 
    #ans2 = defaultdict(set) 
    for r in range(len(edges)+1):        
        for x in combinations(edges, r): 
            fn(list(x))
            
            #print(ans, len(ans))
            #print(ans2, len(ans2))  # DFS SOLUTION
    
    final = [[]]
    
    final.append(list(ans))
    return  len(ans) + 1, final
        
            
  
n = 3
maxDistance = 5
roads = [[0,1,2],[1,2,10],[0,2,10]]
#Output: 5
print( closingbranches(n, roads, maxDistance )  )	


print()


n = 3
maxDistance = 5
roads = [[0,1,20],[0,1,10],[1,2,2],[0,2,2]]
#Output: 7



print( closingbranches(n, roads, maxDistance )  )	

print()


n = 1
maxDistance = 10
roads = []
#Output: 2
print( closingbranches(n, roads, maxDistance )  )	

print()

n = 3
maxDistance = 3
roads = [[2,0,14],[1,0,15],[1,0,7]]  # 4
print( closingbranches(n, roads, maxDistance )  )	
print()


n = 5
maxDistance = 20
roads = [[3,2,20],[1,0,10],[0,2,19],[0,3,13],[0,4,19]] # 11    DFS FAILS THIS TESTCASE
print( closingbranches(n, roads, maxDistance )  )	
print()




n = 3
maxDistance = 12
roads = [[1,0,11],[1,0,16],[0,2,13]]
#expected : 5
print( closingbranches(n, roads, maxDistance )  )	
print()



n = 3
maxDistance = 3
roads = [[0,1,14],[0,2,10],[0,2,15]]
#output is 4
print( closingbranches(n, roads, maxDistance )  )	
print()