class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def combinations(iterable, r):
    
            pool = tuple(range(1,iterable+1) )
            n = len(pool)
    
            if r > n :
                return
    
            indices  = list( range(r))
            yield list(  pool[i] for i in indices  )
    
            while True :
                for i in reversed(range(r)):
                    if indices[i] < i + n - r :
                        break
                else:
                    return
                indices[i] += 1
                for j in range(i+1, r):
                    indices[j] = indices[j-1]  + 1
                yield list(  pool[i] for i in indices  )
        return list( combinations(n, k) )
    
    
Obj = Solution()
n = 10
k = 7
#Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

print(   Obj.combine(n, k) , len(Obj.combine(n, k))  )




class Solution2(object):
    def combine2(self, n, k):
        iterables = list(    range(1, n + 1) )  
        r = k
        
        #def combine2(self, iterables,r, repeat=1):
        #iterables = list(    range(1, iterables + 1) )  
        l = iterables
        r =  len(iterables) + 1 - r
        # product('ABCD', 'xy') → Ax Ay Bx By Cx Cy Dx Dy
        # product(range(2), repeat=3) → 000 001 010 011 100 101 110 111
        M =  [ [list(iterables[0+rr : r+rr])][0] for rr in range(  len(l)-r+1  )     ]  ####  COMB**
        #M = [ [iterables[i] for i in range(len(iterables) ) ] for _ in range(  r ) ]  #### COMB** WITH REPLACEMENT, PERMUT**
        
        #pools = [tuple(pool) for pool in iterables] * repeat
        pools = [tuple(pool) for pool in M] * 1#repeat
        result = [[]]
        
        
        
        #vis = []
        q=[]
        for pool in pools  :
            result = [ x+[y]  for x in result for y in pool       if y not in x and x+[y] not in result ] #    ####  COMB**
            
            
            
        q = []
        for i in result:
            if set(i) not in q :
                q.append(set(i))
        return q



class Solution3(object):   
    def combine3(self, n, k):
        
        l = list(    range(1, n + 1) )  
        r = k
        #def do(l, r):
        
    
    
        #mm =[ [  l[i-j:i+1]  for i in range(len(l)-r, len(l))  ]   for j in range(r)  ]
    
        iterables = l
        mm =  [[ [list(iterables[0+rr : r+rr])     ][0][vvv:]  for rr in range(  len(l)-r+1  ) ] for vvv in range(r-1,-1,-1)    ]
    
        row = r - 1
    
    
        path2 = []
    
    
        #print(mm, )
    
        def dfs(row, col,                  mm ) :
        
            q =   [(row, col,     row, col)  ]
        
        
            while  q :
                row_ , col_ , nrow , ncol = q.pop()
            
                news = mm[row_][col_][:len(mm[row_][col_])- len( mm[nrow][ncol] ) ] + mm[nrow][ncol] 
            
            
            
                #if  mm[row][col][:len(mm[row][col])- len( news) ]  + news  not in path2 :
            
                path2.append(  mm[row][col][:len(mm[row][col])- len( news) ]  + news    )  # ORIGINAL TO CUMMULATIVE NEWS   {row_ , col_} == {row , col}
            
                #path2.append(   mm[row][col][:len(mm[row][col])- len( mm[row_][col_] ) ] + mm[row_][col_]   )
                #path2.append(   mm[row][col][:len(mm[row][col])- len( mm[nrow][ncol] ) ] + mm[nrow][ncol]   )
            
            
                #if  nrow  ==   0 or ncol ==  len(mm[0])-1:
                    #print( path,"ans")
                    #print()
                    #print( path2,"PATH2" )
            
            
                for ROW in range(1, len(mm)):
                    for COL in range(1,  len(mm[0])):
                        new_row = nrow - ROW
                        new_col = ncol + COL
                        if  0 <= new_row < len(mm) and 0 <= new_col <  len(mm[0]) :
                        
                            #q.append( (row_, col_,   new_row, new_col)  )              #  1ST JOURNEY
                            q.append( ( nrow , ncol ,  new_row, new_col)  )  # <<<<<<<    (nrow , ncol )    ORIGINAL to ALL 1ST {NON_CUMULATIVE} new options
                        
                        
                        
                        
                        
        for col in range(len(mm[0])):
            #print(mm[row][col])
        
            dfs(row, col,               mm ) 
        
        
            #print(  path2, len(path2))
        return path2
    
Obj2 = Solution2()
n = 10
k = 7
#Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

print(   Obj2.combine2(n, k) , len(Obj2.combine2(n, k))     )


Obj3 = Solution3()
print(   Obj3.combine3(n, k) ,   len(Obj3.combine3(n, k))     )


L = [1,2,3,4,5]




r = 4

#for i in range(len(L)-r , len(L)) :
    #print(L[i])
    #for j in range(r):
        #print(  L[i-j:1+i]  )
        