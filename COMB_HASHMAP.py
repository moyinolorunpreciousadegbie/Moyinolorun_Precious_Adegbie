def combinations_2(iterable, r):
	# combinations('ABCD', 2) → AB AC AD BC BD CD
	# combinations(range(4), 3) → 012 013 023 123
	
	pool = tuple(iterable)
	n = len(pool)
	if r > n:
		return
	indices = list(range(r))
	
	t = n
	
	mp = {}
	for i in range(t,0,-1):
	#for i in range(1,t+1)
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
	
	yield tuple(pool[i] for i in indices)
	
	end = [ i for i in range(n-r,n)   ] 
	while indices != end:
		for i in reversed(range(r)):
			if indices[i] < i + n - r:    #   012345     :3    012  + 6-3=3      345   i + n - r   || i + 3     indices[i:len(indices)]  indices[i:r]
				break												# n-r        012   i <<
		else:																	#+++3
			return
		indices[i] += 1
		
		indices = indices[:i]  +  mp[(indices[i],indices[i]+r-i-1)]
		
		
			#print(indices ,"BEFORE", i,'<->',r-1,  indices[:i] , indices[i:r] , (indices[i],indices[i]+r-i-1),'  |||||||||',mp[(indices[i],indices[i]+r-i-1)])
			###############################          ^^^^^^       +                map of this ^^^^^^^^^^^^^
			#print(indices ,"AFTER                        ",indices[i:r] )
		
		yield tuple(pool[i] for i in indices)
		
		
def combinations(iterable, r):
	# combinations('ABCD', 2) → AB AC AD BC BD CD
	# combinations(range(4), 3) → 012 013 023 123
	
	pool = tuple(iterable)
	n = len(pool)
	if r > n:
		return
	indices = list(range(r))
	
	
	yield tuple(pool[i] for i in indices)
	end = [ i for i in range(n-r,n)   ] 
	while indices != end:
		for i in reversed(range(r)):
			if indices[i] < i + n - r:    #   012345     :3    012  + 6-3=3      345   i + n - r   || i + 3     indices[i:len(indices)]  indices[i:r]
				break												# n-r        012   i <<
		else:																	#+++3
			return
		indices[i] += 1
		for j in range(i+1, r):#
			indices[j] = indices[j-1] + 1#
		yield tuple(pool[i] for i in indices)
		
#####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
def combinations2_2(iterable, r):
	# combinations('ABCD', 2) → AB AC AD BC BD CD
	# combinations(range(4), 3) → 012 013 023 123
	
	pool = tuple(iterable)
	n = len(pool)
	if r > n:
		return
	
	
	t = n
	
	mp = {}
	for i in range(t,0,-1):
	#for i in range(1,t+1)
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
			
	indices =  list(range( n-r , n  )) 
	yield tuple(pool[i] for i in indices)
	while True:
		for i in range(r):
			if indices[i] >  i:  # n - i -1 :  #  n - r + i
				break
		else:
			return
		indices[i] -= 1
		#indices = mp[(indices[i],indices[i]+r-i-1)]  + indices[i+1:]
		indices = mp[(indices[i]-i,indices[i])]  + indices[i+1:]
		#print(indices[i],indices[i]+r-i-1, indices,i)
		#for j in range(i-1, -1, -1):
			#indices[j] = indices[j+1] - 1
		yield tuple(pool[i] for i in indices)
			
def combinations2(iterable, r):
	# combinations('ABCD', 2) → AB AC AD BC BD CD
	# combinations(range(4), 3) → 012 013 023 123
	
	pool = tuple(iterable)
	n = len(pool)
	if r > n:
		return
	#indices = list(range(r))
	#indices = list(range(r))[::-1]
	#indices =   list(range( n -1, n -r-1, -1))   # 543     210      3
	
												#  345
	                                            #  012  i
												#  210 <<<
	
	indices =  list(range( n-r , n  )) 
	yield tuple(pool[i] for i in indices)
	while True:
		for i in range(r):
			if indices[i] >  i:  # n - i -1 :  #  n - r + i
				break
		else:
			return
		indices[i] -= 1
		for j in range(i-1, -1, -1):
			indices[j] = indices[j+1] - 1
		yield tuple(pool[i] for i in indices)
		
		
		
#####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
	
m = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]	

_4 = 4
	
_ = list( combinations(m, _4))

__ = list( combinations_2(m, _4))
	
print( len(_),len(__)   )
#print(  _ )
print()
#print("#"*130)
print()
#print(__  )

print()
#print("#"*130)
print()
print()


_2 = list( combinations2(m, _4))

__2 = list( combinations2_2(m, _4))

print( len(_2),len(__2)   )
#print( _2)
print()
#print("#"*130)
print()
#print(__2 )	







	
	