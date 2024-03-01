from collections import defaultdict
import statistics

#####################################################################################################################

def convert(FEE_AL_910):
    
    FEE_AL_910_ = FEE_AL_910[['Depth','TOC','Calcite']]
    FEE_AL_910_[['Depth','TOC','Calcite']] = FEE_AL_910[['Depth','TOC','Calcite']].astype(int)
   
    FEE_AL_910_L = FEE_AL_910_[['Depth','TOC', 'Calcite']].values.tolist()
    FEE_AL_910_L[0].insert(0,0)   # left index       right value
    for i in range(1,len(FEE_AL_910_L)):
        FEE_AL_910_L[i].insert(0,   int(FEE_AL_910_L[i-1][1]) )
        
    return FEE_AL_910_L, FEE_AL_910

#####################################################################################################################

def transpose(l1, l2):
    l2 =[[row[i] for row in l1] for i in range(len(l1[0]))]
    return l2

#####################################################################################################################

def minOperationsQueries(edges, queries):
    n = len(edges) +1
    def dfs( p, x, t, b, e, w, w2, f, all , all2):
        all[x][::] = w[::]
        all2[x][::] = w2[::]
        f[x][0] = p
        b[x] = t[0] = t[0] + 1
        for y in adj[x]: 
            if y[0] != p:
                w[ y[0] ] += y[1]
                w2[ y[0] ] += y[2]
                dfs(x, y[0], t, b, e, w, w2,  f, all, all2 )
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
    adj = defaultdict(list)
    graph = {}
    graph2 = {}
    cnnn = 0
    for e in edges:
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
    dfs(-1, 0, t, b, e, w, w2, f, all, all2 )
    f[0][0] = 0
    for j in range(1,n):
        for i in range(n):
            f[i][j] =  f[  f[i][j-1] ][j-1]
    ans = []
    ans2 = []
    
    medianans = []
    for q  in queries:
        if q[0] == q[1]:
            continue
        tocmedians = []
        tocmedians.append( adj[   graph[ q[0] ]-1  ][0][1]  ) 
        #print(tocmedians)
        carbmedians = []
        carbmedians.append( adj[   graph[ q[0] ]-1  ][0][2] )
        #print(carbmedians)
        summ = 0
        summm = 0
        tlc = lcs( graph[ q[0]],   graph[ q[1]], b, e, f)
        tot = graph[ q[1]] - graph[ q[0]] +1  
        for i in range(n):  # TOC
            temp = all[  graph[ q[0] ] ][i]  +  all[  graph[ q[1] ] ][i]  - ( all[  graph[ graph2[tlc] ]   ][i] << 1 )
            summ += temp     # CARB
            
                
            temp2 =  all2[  graph[ q[0] ] ][i]  +  all2[  graph[ q[1] ] ][i]  - ( all2[  graph[ graph2[tlc] ]   ][i] << 1 )    
            summm += temp2
            if graph[ q[0]] < i <= graph[ q[1]]  :
                tocmedians.append(temp) # PATH
                #print(tocmedians  )
                #print(statistics.median(tocmedians) ,'TOC' )
                
                carbmedians.append(temp2) # # PATH
                #print(carbmedians  )
                #print(statistics.median(carbmedians) , 'CARB' )
                
                term = [statistics.median(tocmedians) ,    statistics.median(carbmedians) ]
        #print( tocmedians   )   # PATH
        #print(  carbmedians   )  #  PATH
        medianans.append(term)
        ans.append((summ + adj[   graph[ q[0] ]-1  ][0][1] )/ tot)
        ans2.append((summm + adj[   graph[ q[0] ]-1  ][0][2] )/ tot)
        #if len( tocmedians ) == tot and len( carbmedians ) == tot:
        #print( tocmedians )
       # print()
        #print( carbmedians )
    
    l1 = []
    #transpose(medianans , l1)
    #print(transpose(medianans , l1), 'TOC & Carbonate medianans')
    #print(medianans)
    l2 = []
    transpose([ans, ans2], l2)
    return transpose([ans, ans2], l2),  medianans

#####################################################################################################################

def quary(FEE_AL_910, quaries):
    graph = defaultdict(list)
    graphtoc = {}
    graphcarbonate = {}
    for u, v , toc , carbonate in FEE_AL_910 :
        graph[u].append(v)
        graphtoc[v] = toc
        graphcarbonate[v] = carbonate
    def dfs(start, stop, sumtoc,sumcarbonate , cnt):
        seen.add(start)
        tocpath.append(graphtoc[start])
        carbonatepath.append(graphcarbonate[start])
        sumtoc += graphtoc[start]
        sumcarbonate += graphcarbonate[start]
        cnt += 1
        for v in graph[start]:      #print( sumtoc / cnt , sumcarbonate / cnt,'     sumtoc / cnt , sumcarbonate / cnt     ' ,sumtoc,sumcarbonate, cnt)
            if v not in seen and start < v   :
                if v == stop:
                    sumtoc += graphtoc[v]
                    sumcarbonate += graphcarbonate[v]
                    cnt += 1
                    tocpath.append(graphtoc[v])
                    carbonatepath.append(graphcarbonate[v])
                    
                    ans.append([sumtoc / cnt , sumcarbonate / cnt]) 
                    #print(tocpath)
                    #print(carbonatepath)
                    tocmedian.append(statistics.median(tocpath))
                    carbonatemedian.append(statistics.median(carbonatepath))
                    median.append([statistics.median(tocpath), statistics.median(carbonatepath)  ])
                dfs(v , stop, sumtoc,sumcarbonate , cnt )
    ans = []
    tocmedian = []
    carbonatemedian = []
    median = []
    
    for start, stop in quaries:  ## ([29, 54, 13], [63, 205, 40])
        sumtoc = 0
        sumcarbonate = 0
        cnt = 0
        seen = set()
        tocpath = []
        carbonatepath = []
        
        dfs(start, stop, sumtoc, sumcarbonate, cnt)
    #print(tocmedian,'TOCmedian')
    #print()
    #print( carbonatemedian , 'Carbonatemedian' )
    #print()
    #print(median)
    return ans, median

#####################################################################################################################

def checking( well ,  quaries):
    
    #(convert(FEE_AL_910)[0]
    #(convert(FEE_AL_910)[1]
    FEE_AL_910 = well[1]
    FEE_AL_910_ = well[0]
    
    import matplotlib.pyplot as plt
    import numpy as np
    fig, ax1 = plt.subplots(figsize=(3, 18))
    plt.ylabel("Depth ft")
    ax1.plot(FEE_AL_910['TOC'], FEE_AL_910['Depth'], label= 'TOC',color='red',marker='o' )
#plt.xticks(np.arange(0, 15, 5))
    
    ax2 = ax1.twiny()      
    ax2.plot( FEE_AL_910['Calcite'], FEE_AL_910['Depth'], label= 'Calcite', color='blue',marker='P')
    ax2.set_title("% Carbonate")
#fig.tight_layout()
#ax2.set_position(pos=bottom, which='both')
#plt_1 = plt.figure(figsize=(6, 3))
#plt.xticks(np.arange(0, 90, 5)) 
    plt.yticks(np.arange(8000, max(FEE_AL_910['Depth'])+50, 100))
#plt.ylim( 11000, 9000  )
    plt.xlabel("TOC (wt%)")
    plt.ylim(max(FEE_AL_910['Depth'])+50, min(FEE_AL_910['Depth'])-50)
    ax2.xaxis.set_label_position('bottom')
    ax2.xaxis.set_label_coords(0.5,-0.05)
    plt.grid()     
    ax2.legend(loc = 'upper right')
    ax1.legend(loc = 'lower right')
#ax1.legend(loc = 'lower left')
    ax1.grid()   
    ax2.grid()




    import random
    number_of_colors = len( quaries )

    color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(number_of_colors)]
    #print(color)

    formations = {}


    cnt= 0
    for u, v in quaries:
       # print(u, v)
        rangg = [u, v]
        rang = '                                       '+str(int(u))+' ft to '+str(int(v))+' ft : AVG TOC of '+ str( quary( FEE_AL_910_  , quaries)[0][cnt][0] )+ ', Median TOC of '+ str( quary( FEE_AL_910_  , quaries)[1][cnt][0] ) +  ',     AVG Carbonate of ' + str( quary( FEE_AL_910_  , quaries)[0][cnt][1]  )  +', Median Carbonate of ' + str( quary( FEE_AL_910_  , quaries)[1][cnt][1]  ) 
        #print(  rang)  #  string label
       # print()
    #print( rangg)  # list of quary range
    #print(   '', minOperationsQueries( FEE_AL_910  , quaries)[cnt][0]  , minOperationsQueries( FEE_AL_910  , quaries)[cnt][1] )
        cnt+=1
    
        formations[ rang ] = rangg
    
    #print(formations)

    
    zone_colours = color

    for depth, colour in zip(formations.values(), zone_colours):
        # use the depths and colours to shade across the subplots
            ax2.axhspan(depth[0], depth[1] , color=colour, alpha=0.1)
        
    formation_midpoints = []
    for key, value in formations.items():
        formation_midpoints.append(value[0] + (value[1]-value[0])/2)
    
#formation_midpoints  # rotation=90
        
    for label, formation_mid in zip(formations.keys(), 
                                    formation_midpoints):
            ax2.text(0.5, formation_mid, label, rotation=0,
                verticalalignment='center', fontweight='bold',
                fontsize='large')

        
    plt.show()
    
#####################################################################################################################  
    
quaries1 = [[8055, 9861],[9861,10740],[10795, 10850]]  
quaries2 = [[8040, 9861],[9861,10740],[10795, 10850]]
quaries3 = [[9341,9370],[9861,9903],[9974,10009],[10590,10750]]

checking( convert(FEE_AL_910) ,  quaries1)   

checking( convert(FEE_AL_910) ,  quaries2)  

checking( convert(FEE_AL_910) ,  quaries3) 