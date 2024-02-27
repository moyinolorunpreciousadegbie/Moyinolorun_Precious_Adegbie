from collections import defaultdict
#adj = defaultdict(list)
def transpose(l1, l2):
    
    # we have nested loops in comprehensions
    # value of i is assigned using inner loop
    # then value of item is directed by row[i]
    # and appended to l2
    l2 =[[row[i] for row in l1] for i in range(len(l1[0]))]
    return l2

def minOperationsQueries(edges, queries):
    n = len(edges) +1
    
    tc = 0
    for _, _, tcc , _ in edges:
        tc = max( tc, tcc)
    tc = tc+1 
    
    carb = 0
    for _, _, _ , car in edges:
        carb = max( carb, car)
    carb = carb+1  
    def dfs( p, x, t, b, e, w, w2, f, all , all2, cn):
        all[x][::] = w[::]
        all2[x][::] = w2[::]
        f[x][0] = p
        b[x] = t[0] = t[0] + 1
        for y in adj[x]:
            if y[0] != p:
                #print(y[1])
                #print(y[0])
                w[ y[0] ] += y[1]
                w2[ y[0] ] += y[2]
                #print(y[1],'hh')
                dfs(x, y[0], t, b, e, w, w2,  f, all, all2 , cn)
                #print(y[1],'h')
                w2[ y[0] ] -=y[2]
                w[ y[0] ] -= y[1]
        e[x]  = t[0]
    def ancestor(x, y, b, e):
        return b[x]  <= b[y] and e[x]  >= e[y]
    def lcs(x, y, b, e, f):
        if  ancestor(x, y, b, e):
            return x
        if  ancestor(y, x, b, e):
            return y
        r = 0
        for i in range(n-1,-1,-1):
            temp = f[x][i]
            if ancestor(temp, y, b, e):
                r = temp
            else:
                x = temp
        return r
    #adj = [[]for _ in range(len(FEE_AL_910))]
    adj = defaultdict(list)
    graph = {}
    graph2 = {}
    cnnn = 0
    last = 0
    for e in edges:
    #                depth e[1]
        adj[cnnn].append((cnnn+1, e[2],e[3]))
        graph[e[1] ] = cnnn+1
        graph2[cnnn+1] = e[1]
        cnnn += 1
    f = [[0]*(n) for _ in range(n)]
    all = [[0]*(n) for _ in range(n)] # # TOC
    all2 = [[0]*(n) for _ in range(n)] # CARBONATE
    b = [0] * (n)
    e = [0] * (n)
    w = [0] *  n #(tc+1) # TOC
    w2 = [0] *  n #(carb+1) # CARBONATE
    t = [0]
    cn = 0
    #print(graph,'   >>>>>>', graph[ graph2[2] ])
    #_ , ttc, crb = adj[0]
   # w[0] = ttc
    #w2[0] = crb
    #print(adj)
    dfs(-1, 0, t, b, e, w, w2, f, all, all2 , cn)
    f[0][0] = 0
    for j in range(1,n):
        for i in range(n):
            f[i][j] =  f[  f[i][j-1] ][j-1]
    ans = []
    ans2 = []
    for q  in queries:
        if q[0] == q[1]:
            continue
        _max = 0
        summ = 0
        summm = 0
        tlc = lcs( graph[ q[0]],   graph[ q[1]], b, e, f)
        tot = graph[ q[1]] - graph[ q[0]] +1  
        #print(adj[graph[ q[0] ]],'      ', adj[   graph[ q[0] ]-1  ][0][1],'    ',adj[   graph[ q[0] ]-1  ][0][2],'     ',q[0],'        ', graph[ q[0] ]-1 )
        #print(tlc,'       ', q[0],  q[1], graph[ q[0] ], graph[ q[1] ])
        #print(tlc, q[0],  q[1],'    ', graph[ graph2[tlc] ] )
        for i in range(n):  # TOC
            #print(all[  graph[ q[0] ] ][i] )
            #print(all[  graph[ q[1] ] ][i] )
            
            temp = all[  graph[ q[0] ] ][i]  +  all[  graph[ q[1] ] ][i]  - ( all[  graph[ graph2[tlc] ]   ][i] << 1 )
            
            
            
            
            #print(temp)
            #_max = max(_max, temp)
            summ += temp
        for j in range(n):  # CARB
            temp2 = all2[  graph[ q[0] ] ][j]  +  all2[  graph[ q[1] ] ][j]  - ( all2[  graph[ graph2[tlc] ]   ][j] << 1 )
            summm += temp2
           # print(temp2)
        #print(tot)
        ans.append((summ + adj[   graph[ q[0] ]-1  ][0][1] )/ tot)
        ans2.append((summm + adj[   graph[ q[0] ]-1  ][0][2] )/ tot)
        
    l2 = []
    transpose([ans, ans2], l2)
    return transpose([ans, ans2], l2)

FEE_AL_910  = [[0, 8040, 3, 0], [8040, 8055, 6, 0], [8055, 8072, 5, 0], [8072, 8083, 12, 0], [8083, 9341, 2, 0], [9341, 9350, 2, 0], [9350, 9360, 3, 24], [9360, 9370, 3, 5], [9370, 9861, 2, 34], [9861, 9869, 4, 5], [9869, 9881, 2, 26], [9881, 9903, 4, 3], [9903, 9918, 1, 0], [9918, 9974, 1, 0], [9974, 9984, 3, 0], [9984, 9995, 4, 0], [9995, 10009, 1, 0], [10009, 10020, 2, 0], [10020, 10590, 4, 5], [10590, 10600, 1, 14], [10600, 10610, 2, 21], [10610, 10622, 3, 10], [10622, 10632, 2, 13], [10632, 10641, 8, 10], [10641, 10652, 2, 7], [10652, 10673, 1, 27], [10673, 10692, 4, 46], [10692, 10702, 3, 0], [10702, 10740, 2, 18], [10740, 10750, 1, 8], [10750, 10760, 5, 7], [10760, 10778, 2, 2], [10778, 10787, 3, 3], [10787, 10795, 6, 4], [10795, 10805, 2, 2], [10805, 10815, 0, 2], [10815, 10825, 3, 0], [10825, 10839, 7, 4], [10839, 10850, 1, 32]]


quaries = [[8055, 9861],[9861,10740],[10795, 10850]]

quaries2 = [[8040, 9861],[9861,10740],[10795, 10850]]

print( minOperationsQueries( FEE_AL_910  , quaries) )  #  [[4.375, 7.875], [2.6666666666666665, 11.380952380952381], [3.1666666666666665, 7.333333333333333]]
print()

print( minOperationsQueries( FEE_AL_910  , quaries2) ) 



#[[4.375, 7.875], [2.6666666666666665, 11.380952380952381], [3.1666666666666665, 7.333333333333333]]

#[[4.222222222222222, 7.0], [2.6666666666666665, 11.380952380952381], [3.1666666666666665, 7.333333333333333]]

