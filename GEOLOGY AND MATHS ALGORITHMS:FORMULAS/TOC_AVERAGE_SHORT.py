from collections import defaultdict
def quary(FEE_AL_910, quaries):
    
    graph = defaultdict(list)
    graphtoc = {}
    graphcarbonate = {}
    for u, v , toc , carbonate in FEE_AL_910 :
        graph[u].append(v)
        graphtoc[v] = toc
        graphcarbonate[v] = carbonate
 
    # or graph2[v][u] to get the reverse one 
        
    def dfs(start, stop, sumtoc,sumcarbonate , cnt):
    
        seen.add(start)
        #temp = start
        sumtoc += graphtoc[start]
        sumcarbonate += graphcarbonate[start]
        cnt += 1
        
        for v in graph[start]:
            if v not in seen and start < v   :
                if v == stop:
                    sumtoc += graphtoc[v]
                    sumcarbonate += graphcarbonate[v]
                    cnt += 1
                    #print( sumtoc / cnt , sumcarbonate / cnt,'     sumtoc / cnt , sumcarbonate / cnt     ' ,sumtoc,sumcarbonate, cnt)
                    ans.append([sumtoc / cnt , sumcarbonate / cnt])
                
                dfs(v , stop, sumtoc,sumcarbonate , cnt )
        
    ans = []
    for start, stop in quaries:  ## ([29, 54, 13], [63, 205, 40])
        sumtoc = 0
        sumcarbonate = 0
        cnt = 0
        seen = set()
        dfs(start, stop, sumtoc, sumcarbonate, cnt)
        #print()
        #print()
    return ans
        
        
        
FEE_AL_910  = [[0, 8040, 3, 0], [8040, 8055, 6, 0], [8055, 8072, 5, 0], [8072, 8083, 12, 0], [8083, 9341, 2, 0], [9341, 9350, 2, 0], [9350, 9360, 3, 24], [9360, 9370, 3, 5], [9370, 9861, 2, 34], [9861, 9869, 4, 5], [9869, 9881, 2, 26], [9881, 9903, 4, 3], [9903, 9918, 1, 0], [9918, 9974, 1, 0], [9974, 9984, 3, 0], [9984, 9995, 4, 0], [9995, 10009, 1, 0], [10009, 10020, 2, 0], [10020, 10590, 4, 5], [10590, 10600, 1, 14], [10600, 10610, 2, 21], [10610, 10622, 3, 10], [10622, 10632, 2, 13], [10632, 10641, 8, 10], [10641, 10652, 2, 7], [10652, 10673, 1, 27], [10673, 10692, 4, 46], [10692, 10702, 3, 0], [10702, 10740, 2, 18], [10740, 10750, 1, 8], [10750, 10760, 5, 7], [10760, 10778, 2, 2], [10778, 10787, 3, 3], [10787, 10795, 6, 4], [10795, 10805, 2, 2], [10805, 10815, 0, 2], [10815, 10825, 3, 0], [10825, 10839, 7, 4], [10839, 10850, 1, 32]]

quaries = [[8055, 9861],[9861,10740],[10795, 10850]]

quaries2 = [[8040, 9861],[9861,10740],[10795, 10850]]

print( quary( FEE_AL_910  , quaries) )  
print()

print( quary( FEE_AL_910  , quaries2) ) 


















"""

adj = [[]for _ in range(len(FEE_AL_910))]

graph = {}
cnnn = 0
last = 0
for e in FEE_AL_910:
    #                depth e[1]
    adj[cnnn].append((cnnn+1, e[2],e[3]))
    graph[e[1] ] = cnnn+1
    cnnn += 1

    #  [[4.375, 7.875], [2.6666666666666665, 11.380952380952381], [3.1666666666666665, 7.333333333333333]]
    
    #print(adj)
print()
print()
#print(graph)   ([29, 54, 13], [63, 205, 40])

    #  [[4.375, 7.875], [2.6666666666666665, 11.380952380952381], [3.1666666666666665, 7.333333333333333]]
    
    #  [[4.222222222222222, 7.0], [2.6666666666666665, 11.380952380952381], [3.1666666666666665, 7.333333333333333]]


"""