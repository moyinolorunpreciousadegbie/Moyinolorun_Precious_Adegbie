def product(iterables,r, repeat=1):
    r =  len(iterables) + 1 - r
    # product('ABCD', 'xy') → Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) → 000 001 010 011 100 101 110 111
    M =  [ [list(iterables[0+rr : r+rr])][0] for rr in range(  len(l)-r+1  )     ]  ####  COMB**
    #M = [ [iterables[i] for i in range(len(iterables) ) ] for _ in range(  r ) ]  #### COMB** WITH REPLACEMENT, PERMUT**
    
    #pools = [tuple(pool) for pool in iterables] * repeat
    pools = [tuple(pool) for pool in M] * repeat
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
        
    
            #return result
        
l = [1,2,3,4,5,6,7,8,9]   


r = 7   # 5 + 1 - r


# 5  1
#10  5
#10  10
#5   10
#1   5

#print(   list(product( l , r)   )  , len(list(product( l , r)   ) ))
    
from itertools import combinations_with_replacement
from itertools import combinations


#print( list(combinations_with_replacement(l, r)),   len(list(combinations_with_replacement(l, r)))  )



print(   list(product( l , r)   )  , len(list(product( l , r)   ) ) )
print()
print(   list(combinations(l, r)),   len(list(combinations(l, r)))  )


#r = 4


#print()
#print( [ [list(range(0+rr, r+rr))][0] for rr in range(  len(l)-r+1  )     ]  )


#print([ [i for i in range(len(l) ) ] for _ in range(  r ) ] )
#print(set([1,1,1,2,2,2,3,3,3]))

#print( list(combinations_with_replacement(l, r)), len(  list(combinations_with_replacement(l, r)) )  )
#print()






"""
print(   list(product( l , r)   )  , len(list(product( l , r)   ) ) )


q = []
for nn in range(1, len(l)):
    
    for m in list(combinations(l, nn)) :
        q.append(m)
        
print()
print()
print()


print(q, len(q))


















############################################################  >>>>>>>>>>>>>>>>>>>

def do(l, r):
    
    
    #mm =[ [  l[i-j:i+1]  for i in range(len(l)-r, len(l))  ]   for j in range(r)  ]
    
    iterables = l
    mm =  [[ [list(iterables[0+rr : r+rr])     ][0][vvv:]  for rr in range(  len(l)-r+1  ) ] for vvv in range(r-1,-1,-1)    ]
    
    mm_copy = mm
    
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
        
    
    print(  path2, len(path2))

#l = [1,2,3,4,5]
#r = 3


do(l, r)


############################################################   >>>>>>>>>>>>>>>>>>>

"""