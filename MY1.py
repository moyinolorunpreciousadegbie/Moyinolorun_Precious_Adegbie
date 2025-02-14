#!/usr/bin/env python3

def combinationSum( target) :
		#candidates = list(range(1,target+1))
		candidates = target
		target = sum(  target[-1])
		
				
		print(target,"here")
		res = []
		

		def ch(cur):
			
			ans = 0
			for r1 in range( len(cur)):		
				for r2 in range( 1,len(cur) ): # ONCE IS ENOUGH
					if r1 < r2:
						#print(r1,r2)
						for check in cur[r1] :
							if check in cur[r2] :
								return False
						
						
			return cur
				
	
		def dfs(i, cur, total,   mp):
			
			if total == target:
				
				if  ch(cur.copy()) :
					res.append(ch(cur.copy()) )
				
				
				return
			
			
			if i >= len(candidates) or total > target:
				
				return
						
			for jj in  candidates[i] 	:
				if jj not in mp :
					mp.add(jj) 
					
				
			cur.append(candidates[i])
								
			dfs(i+1, cur, total + sum(candidates[i])   ,   mp)
		
			cur.pop()
			
			dfs(i + 1, cur, total,   mp)
			
		
		dfs(0, [], 0,   set())
		return res
	
	
	
target1 = [(1,), (2,), (3,), (4,), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4), (1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4), (1, 2, 3, 4)] 

target = [(1,), (2,), (3,), (4,), (5,), (6,), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 3), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6), (4, 5), (4, 6), (5, 6), (1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 2, 6), (1, 3, 4), (1, 3, 5), (1, 3, 6), (1, 4, 5), (1, 4, 6), (1, 5, 6), (2, 3, 4), (2, 3, 5), (2, 3, 6), (2, 4, 5), (2, 4, 6), (2, 5, 6), (3, 4, 5), (3, 4, 6), (3, 5, 6), (4, 5, 6), (1, 2, 3, 4), (1, 2, 3, 5), (1, 2, 3, 6), (1, 2, 4, 5), (1, 2, 4, 6), (1, 2, 5, 6), (1, 3, 4, 5), (1, 3, 4, 6), (1, 3, 5, 6), (1, 4, 5, 6), (2, 3, 4, 5), (2, 3, 4, 6), (2, 3, 5, 6), (2, 4, 5, 6), (3, 4, 5, 6), (1, 2, 3, 4, 5), (1, 2, 3, 4, 6), (1, 2, 3, 5, 6), (1, 2, 4, 5, 6), (1, 3, 4, 5, 6), (2, 3, 4, 5, 6), (1, 2, 3, 4, 5, 6)]



target2=[(1,), (2,), (3,), (4,), (5,),
(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5),
(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5),
(1, 2, 3, 4), (1, 2, 3, 5), (1, 2, 4, 5), (1, 3, 4, 5), (2, 3, 4, 5) ,
(1, 2, 3, 4, 5) ]

#target2 = [(1,2,3),(3,4),(5,6)]

#print(   combinationSum( target2), len(combinationSum( target2))  ) #  [[1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 3], [1, 2, 2], [1, 4], [2, 3], [5]] 7
print()
print()
#print(   combinationSum( target1), len(combinationSum( target1))  )


print(   combinationSum( target2), len(combinationSum( target2))  ) ### THE ONE IN MY BOOK

from itertools import combinations_with_replacement
from itertools import combinations



#for i in range(1,len([1,2,3,4,5,6,7])):
	#print( list(combinations([1,2,3,4,5,6,7], i) )  )




new7 = [ (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (3, 4), (3, 5), (3, 6), (3, 7), (4, 5), (4, 6), (4, 7), (5, 6), (5, 7), (6, 7),
(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 2, 6), (1, 2, 7), (1, 3, 4), (1, 3, 5), (1, 3, 6), (1, 3, 7), (1, 4, 5), (1, 4, 6), (1, 4, 7), (1, 5, 6), (1, 5, 7), (1, 6, 7), (2, 3, 4), (2, 3, 5), (2, 3, 6), (2, 3, 7), (2, 4, 5), (2, 4, 6), (2, 4, 7), (2, 5, 6), (2, 5, 7), (2, 6, 7), (3, 4, 5), (3, 4, 6), (3, 4, 7), (3, 5, 6), (3, 5, 7), (3, 6, 7), (4, 5, 6), (4, 5, 7), (4, 6, 7), (5, 6, 7),
	(1, 2, 3, 4, 5, 6, 7)] 


#print(   combinationSum( new7)  ,  len(combinationSum( new7))-1 )



print(  list(combinations_with_replacement([0,1,2], 3) )    ,   len(list(combinations_with_replacement([1,2,3], 3) )))
"""
w = []
for i in range(1, 8 + 1):
	
	#n+= len( list(combinations([1,2,3,4,5,6,7,8],i) )  ) 
	#print( list(combinations([1,2,3,4,5,6,7,8],i) )  )
	for j in tuple(combinations([1,2,3,4,5,6,7,8],i) )  :
		w.append( j  )
	
	
		#print(   combinationSum( w), len(combinationSum( w))  )	
		#print(w)
"""
		
		
		
		
"""
n = 0
for i in range(1,len([1,2,3,4,5])+1):
	n+= len( list(combinations([1,2,3,4,5],i) )  ) 
	print( list(combinations([1,2,3,4,5],i) )  )
print(n,'n')

print( list(combinations_with_replacement([1,2,3],3) ) , len( list(combinations_with_replacement([1,2,3],3) )  )   )






4--0,1   same level    
   1
   do permutation for same level
	
  




5--0,2--3--1 




5-0
5-2-3-1
4-0
4-1



5{0
5{1

4{0
4{1


"""