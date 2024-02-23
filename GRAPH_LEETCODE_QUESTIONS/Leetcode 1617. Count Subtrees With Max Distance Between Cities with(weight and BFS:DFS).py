from itertools import combinations
from collections import defaultdict

def closingbranches(n, edges):
    
    def fn(edges): 
    
        graph = {}    
        graph2 = {} # graph as adjacency list 
        for u, v , w in edges:
            graph.setdefault(u-1, []).append(v-1) 
            graph.setdefault(v-1, []).append(u-1)
            graph2[(u-1, v-1)] = w
            graph2[(v-1, u-1)] = w
        
        group = [None]*n
        dist = [0]*n 
        
        def dfs(x, w , par):  # DFS solution fails one test case
            
            seen.add(x)
            #print(w,' DFS SOLUTION',(tuple(set(lss))))
             # mark visited 
            for xx  in graph.get(x, []):
                dist[x] = max(dist[x], w)
                if group[xx] is None:
                    group[xx] = group[x]
                if xx not in seen and xx != par  : 
                
                    dfs(xx, w + graph2[(x, xx)], x)
            
            
        def bfs(x, w, par):
            
            q = [(x, w , -1)]
            while q:
                curr, wei, prev = q.pop(0)
                #print(wei, 'wwwwww      ', tuple(set(ls)))
                seen2.add(curr) 
                
                for xx in graph.get(curr, []):
                    dist[curr] = max(dist[curr], wei)
                    if group[xx] is None:
                        group[xx] = group[curr]
                    if xx not in seen2 and xx != prev:
                        q.append((xx, wei +  graph2[(curr, xx)] , curr))
                        
                    
            
    
    
        for i in range(n): 
            seen = set()
            seen2 = set()
            if group[i] is None: group[i] = i
            
            #dfs(i, 0, -1) #  DFS ALSO WORKS
            bfs(i, 0, -1)  #  BFS ALSO WORKS
        return group, dist 
        
    mx_wei = 0    
    
    ans = {}
    for r in range(1,len(edges)+1):        
        for x in combinations(edges, r): 
            temp = {}
            d = {}
            seen, dist = fn(x)
            mx_wei = max(  dist )
            
            for i in range(n): 
                temp.setdefault(seen[i], []).append(i)
                
                if seen[i] not in d: d[seen[i]] = dist[i]
                else: d[seen[i]] = max(d[seen[i]], dist[i])
                
            for k, v in temp.items(): 
                if len(v) > 1: 
                    ans.setdefault(d[k], set()).add(tuple(sorted(v)))
    print(ans, 'ans')
    
    

    return [len(ans.get(x, set())) for x in range(1, mx_wei+1)]
            
        
    
            
n = 4
edges = [[1,2,     1],[2,3,   1],[2,4,    1]]
#Output: [3,4,0]

print(  closingbranches(n, edges)   )
print()


n = 2
edges = [[1,2,   1]]
#Output: [1]
print(  closingbranches(n, edges)   )
print()


n = 3
edges = [[1,2,     1],[2,3,    1]]
#Output: [2,1]
print(  closingbranches(n, edges)   )
print()



n = 4
edges = [[1,2,     53],[2,3,   100],[2,4,    78]]
#Output: [3,4,0]

print(  closingbranches(n, edges)   )
print()