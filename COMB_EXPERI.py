
def subsets( nums):
        from collections import deque
        q= deque()
        for i in range(len(nums)):
            q.append(([nums[i]],[i]))  #. user4436H
        ml= [[]]
        n=0
    
    
        while q:
            st,li=q.pop()
            
            if st not in ml :
                #print(st)
                ml.append(st)
            for i in range(li[-1]+1,len(nums)):
                ls=li[:]
                ls.append(i)
                q.append((st+[nums[i]],ls))
        return ml

class Solution(object): # BEST SOLUTION
    def subsets(self, nums):

        def combinations_2(iterable ):
            # combinations('ABCD', 2) → AB AC AD BC BD CD
            # combinations(range(4), 3) → 012 013 023 123
            
            pool = tuple(iterable)
            n = len(pool)
            
            
            
            t = n
            
            mp = {}
            
            
            #for i in range(n,0,-1):   # for i in range(t,0,-1):
            for i in range(1,n+1):
                #print(i , t-i+1)
                togo = t-i+1
                
            
                ii = 0
                for rn in range(togo):
                    #print([rn,i+ii] ,end='')
                    #print( rn,i+ii-1, list(range(rn,i+ii ))  ,end='' )
                    #          r
                    mp[(rn,i+ii-1)] = list(range(rn,i+ii ))
                    ii+=1
                    #print()
                    #print(rn,i+ii-1)
                    #print()
            
            vis = [[]]
            
            yield []
            
            
            for r in range(1,n+1):
                rrrr = n-r+1 
                
                indices = list(range(r))
                
                #print(r, rrrr)
                if r > rrrr :
                    #print("<<<>>>")
                    break
                
                #if r > n-r+1 :
                    #break
                            
                #if tuple(pool[i] for i in indices) not in vis :
                yield tuple(pool[i] for i in indices)
                    #vis.append(tuple(pool[i] for i in indices))
                
                
                #if r > rrrr :
                    #print("<<<>>>")
                    #break
                
                end = [ i for i in range(n-r,n)   ] 
                while indices != end:
                    for i in reversed(range(r)):
                        if indices[i] < i + n - r:    #   012345     :3    012  + 6-3=3      345   i + n - r   || i + 3     indices[i:len(indices)]  indices[i:r]
                            break												# n-r        012   i <<
                    else:																	#+++3
                        break
                    indices[i] += 1
                    
                    indices = indices[:i]  +  mp[(indices[i],indices[i]+r-i-1)]
                    
                    
                        #print(indices ,"BEFORE", i,'<->',r-1,  indices[:i] , indices[i:r] , (indices[i],indices[i]+r-i-1),'  |||||||||',mp[(indices[i],indices[i]+r-i-1)])
                        ###############################          ^^^^^^       +                map of this ^^^^^^^^^^^^^
                        #print(indices ,"AFTER                        ",indices[i:r] )
                    
                    
                    
                    #if tuple(pool[i] for i in indices) not in vis :
                    yield tuple(pool[i] for i in indices)
                        #vis.append(tuple(pool[i] for i in indices))
                    
                #if r > rrrr :
                    #print("<<<>>>")
                    #break
                
                    
                 
                
                
                
                
                    
                indices_bbb = list(range(rrrr))
                #if tuple(pool[i] for i in indices_bbb) not in vis :
                yield tuple(pool[i] for i in indices_bbb)
                    #vis.append(tuple(pool[i] for i in indices_bbb))
                
                
                
                end_bbb = [ i for i in range(n-rrrr   ,n)   ] 
                while indices != end_bbb:
                    for i_bbb in reversed(range(  rrrr   )):
                        if indices_bbb[i_bbb] < i_bbb + n - rrrr :    #   012345     :3    012  + 6-3=3      345   i + n - r   || i + 3     indices[i:len(indices)]  indices[i:r]
                            break												# n-r        012   i <<
                    else:																	#+++3
                        break
                    indices_bbb[i_bbb] += 1
                
                    indices_bbb = indices_bbb[:i_bbb]  +  mp[(indices_bbb[i_bbb],indices_bbb[i_bbb]+rrrr-i_bbb-1)]
                
                
                        #print(indices ,"BEFORE", i,'<->',r-1,  indices[:i] , indices[i:r] , (indices[i],indices[i]+r-i-1),'  |||||||||',mp[(indices[i],indices[i]+r-i-1)])
                        ###############################          ^^^^^^       +                map of this ^^^^^^^^^^^^^
                        #print(indices ,"AFTER                        ",indices[i:r] )
                
                    #if tuple(pool[i] for i in indices_bbb) not in vis :
                    yield tuple(pool[i] for i in indices_bbb)
                        #vis.append(tuple(pool[i] for i in indices_bbb))
                
                #if (r +1 == rrrr) or (r == rrrr -1) or (r  == rrrr)  :
                    #break
                    
                #if r > rrrr :
                    #print("<<<>>>")
                    #break
            print("VIS", len(vis))
                    
        return  list( combinations_2( nums  ))

		

		
#####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
	
m = [1,2,3,4,5,6,7,8,9,10,11,12,13]#,14,15]	

Obj = Solution()

fan = Obj.subsets( m ) 

	
print( fan , len(fan)  )

print()
print("###############################################")
print("###############################################")
print()

fv = subsets( m )

print( fv , len(fv)  )
