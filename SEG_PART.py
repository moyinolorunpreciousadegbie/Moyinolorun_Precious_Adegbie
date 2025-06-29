def product(iterables, summ, N):
	
	pools = [ list(range(1,summ+1) ) ] * len(iterables)
	#print(pools	,'here')
	#return
	
	q = []
	result = [[]]
	ind = 0
	for pool in pools:
		
		q = []
		for x in result :
			if  len( x ) == (repeat * len(iterables)  ) : break
			
			for y in pool :
				
				if y*(iterables[ind]) <= N :
				
				
					q.append( x+[y]   )
				
		result = q
		
		ind += 1
		
		
	return result  # or q 

def dv( iterables, summ, N , SS,SD) :
	
	
	
	def dfs(iterables, summ, N, ind, cumu, st ,ALL_path):
		if ind == len(iterables): return
		if cumu == N :
			ALL_path.append( st )
			print(st)
			return
		old_cumu = cumu
		old_st = st
		for j in range(1, summ+1):
			cumu += (  (iterables[ind]) * j )
			#if (iterables[ind]) * j  <= N :
			if cumu < N :
				#cumu += (  (iterables[ind]) * j )
				#st = ''
				st += str(j) + ' ('+ str(iterables[ind]) + ') ' + '+ '
				dfs(iterables, summ, N, ind+1, cumu, st ,ALL_path)
				
			if cumu == N :
				
				if st not in ALL_path : 
					ALL_path.append( st )
					print(st)
					st=''
			#cumu = old_cumu
			cumu -= (  (iterables[ind]) * j )
		
		dfs(iterables, summ, N, ind+1, old_cumu, old_st ,ALL_path)
	
	ALL_path = []
		
	#dfs(iterables, summ, N, 0,  0, '', ALL_path)
	
	#it = iterables[::-1]
	it = iterables
	llli = iterables
	#llli = iterables[::-1]
	q = []
	mp = {}
	inds=0
	for i in it :
		mp[i] = inds
		llli_ = llli[:inds] + llli[inds+1:]
		inds +=1
		q.append( [i,'', 0 , llli_ , set()    ])
		
	
	#q = [  [i,'', 0 , llli] for i in it ]
	vis = []
	prin = []
	ALLse = []
	
	cou = 1
	while q:
		
		val, stt , cumu , lll , sss = q.pop(0)
		
		
		
		if cumu == N and stt not in prin  and sss not in ALLse :
			#print(stt, '              ',cou)
			prin.append(stt )
			ALLse.append(sss)
			cou+=1
			
			if stt not in SS and sss not in SD : 
				
				SS.append(stt)
				SD.append(sss)
			
		
		for j in range(1, summ+1):
			
			#if cumu == N :
				#stt += str(j) + ' ('+ str( val ) + ') ' + '+ '
				#if stt not in vis: 
					#q.append([val,stt,cumu])
					#vis.append(stt)          #  cumu + (  j / ( val ) )  < N   cumu + (  j ** ( val ) )  < N , cumu + (  (1/j) ** ( val ) )  < N
			if cumu + (  ( val ) * j )  < N : #  cumu + (  ( val ) / j )  < N   cumu + (  ( val ) ** j )  < N , cumu + (  ( val ) ** (1/j) )  < N
			#if cumu + (  ( val ) + j )  < N :#
				#stt + str(j) + ' ('+ str( val ) + ') ' + '+ '
				for ran in range(len( lll) ) :
					vv = lll[ran]
					#print(vv,val)
					if vv !=  val  and vv + (cumu + (  ( val ) * j )) <= N:
						
						
						nwl = lll[:ran] + lll[ran+1:]
						if stt + str(j) + ' ('+ str( val ) + ') ' + '+ ' not in vis  :
							stt__ = stt + str(j) + ' ('+ str( val ) + ') ' + '+ '
							temp = str(j) + ' ('+ str( val ) + ') ' + '+ '
							#print( [vv,stt__,  (cumu + (  ( val ) * j ))  , nwl] )
							#sss.add(temp)
							sss_set = sss.union({temp})
							if sss not in ALLse:
								q.append([vv,stt__,  (cumu + (  ( val ) * j ))  , nwl,   sss_set     ])
								vis.append(stt__)
							
							
							
							
					
			if   cumu + (  ( val ) * j )  == N  :
				stt____ = stt + str(j) + ' ('+ str( val ) + ') ' #+ '+ ' 
				temp_ =  str(j) + ' ('+ str( val ) + ') ' + '+ ' 
				sss.add(temp_)
				#sss_set2 = sss.union({temp_})
				#ALLse.append(sss)
				
				q.append([val,stt____,  (cumu + (  ( val ) * j ))  , lll, sss ])
					
	#print(len(prin))
	
	

					
							
def combinations(iterable):
	# combinations('ABCD', 2) → AB AC AD BC BD CD
	# combinations(range(4), 3) → 012 013 023 123
	
	pool = tuple(iterable)
	n = len(pool)
	
	
	for r in range(1, n+1):
		indices = list(range(r))
		yield tuple(pool[i] for i in indices)
		while True:
			for i in reversed(range(r)):
				if indices[i] < i + n - r:    #   012345     :3    012  + 6-3=3      345   i + n - r   || i + 3   
					break												# n-r        012   i <<
			else:																	#+++3
				break
			indices[i] += 1
			for j in range(i+1, r):
				indices[j] = indices[j-1] + 1
			yield tuple(pool[i] for i in indices)
	
n = 16
iterable = [1,2,4,8]
#iterable = list(range(1,n+1)) # XXXXXX
LL =  list(combinations(iterable))
print(  LL )

SS = []
SD = []
for l in LL :
	#product( l , sum(iterable[1:]), n)
	#print("#############################")
	#print("#############################")
	#dv( l  , sum(iterable[1:]), n)
	dv( l  , 16, n, SS,SD)
	#print("#############################")
	#print("#############################")
	
	
print(len(SS))

for s in SS :
	print(str(n),'= ',s)