def gh(LL):
	Q = []
	ind = 0
	for i in LL:
		Q.append(i)
		if ind == len(LL) - 1 :
			break
		Q.append(0)
		ind += 1
	return Q
###########################################################################################################################################################################################################################################################################################################################

def combinations_ln(iterable):
	# combinations('ABCD', 2) → AB AC AD BC BD CD
	# combinations(range(4), 3) → 012 013 023 123
	#NEWLL = gh(iterable)
	#iterable = iterable#[:-1]
	n = len(iterable)
	pool = tuple(iterable)
	#pool = tuple([i for i in range(1, n+1)])
	
	
	n__2 = (n*2)
	
	yield [n]
	
	settt = []
	for  r in range(1,n):
		indices = list(range(r))
		
		
		#yield tuple(pool[i] for i in indices)
		
		while True:
			
			
			
			
			for i in reversed(range(r)):
				
				if indices[i] < i + n - r:    #   012345     :3    012  + 6-3=3      345   i + n - r   || i + 3   
					break												# n-r        012   i <<
			else:																	#+++3
				break
			indices[i] += 1
			for j in range(i+1, r):
				indices[j] = indices[j-1] + 1
				
			right = []
			if r == 1:
				right.append( len(pool[:indices[0]] )   )
				right.append( len(pool[indices[0]:] )   )
				#print("oooo", indices, pool[:indices[0]], pool[indices[0]:])
				#print("oooo", indices, right )
				if sorted(right) not in settt :
					settt.append( sorted(right)   )
					yield right 
					
			if r > 1 :
				res = []
				if pool[:indices[0]]  != () :
					res.append( len(pool[:indices[0]] )   )
					
				for iii in range(len(indices)-1):
					#print( pool[indices[iii] :indices[iii+1]])
					#if pool[indices[iii] :indices[iii+1]]  not in res :
					#if iii == 0 and len(pool[indices[iii] :indices[iii+1]]  ) in res:
						#continue
					res.append(   len(pool[indices[iii] :indices[iii+1]]  )   )
					
					if iii+1 == len(indices)-1 : # and pool[indices[iii+1]:] not in res :
						if pool[indices[iii+1]:] != () :
							res.append( len(pool[indices[iii+1]:] )   )
						if sorted(res) not in settt :
							settt.append( sorted(res) )
							yield res 
							
###########################################################################################################################################################################################################################################################################################################################
							
def combinations_len(iterable):
	# combinations('ABCD', 2) → AB AC AD BC BD CD
	# combinations(range(4), 3) → 012 013 023 123
	#NEWLL = gh(iterable)
	#iterable = iterable#[:-1]
	n = len(iterable)
	pool = tuple(iterable)
	#pool = tuple([i for i in range(1, n+1)])
	
	yield [n]
	
	n__2 = (n*2)
	
	settt = []
	for  r in range(1,n):
		indices = list(range(r))
		
		
		#yield tuple(pool[i] for i in indices)
		
		while True:
			
			
			
			
			for i in reversed(range(r)):
				
				if indices[i] < i + n - r:    #   012345     :3    012  + 6-3=3      345   i + n - r   || i + 3   
					break												# n-r        012   i <<
			else:																	#+++3
				break
			indices[i] += 1
			for j in range(i+1, r):
				indices[j] = indices[j-1] + 1
				
			right = []
			if r == 1:
				right.append( len(pool[:indices[0]] )   )
				right.append( len(pool[indices[0]:] )   )
				#print("oooo", indices, pool[:indices[0]], pool[indices[0]:])
				#print("oooo", indices, right )
				if right not in settt :
					settt.append( right )
					yield right 
					
			if r > 1 :
				res = []
				if pool[:indices[0]]  != () :
					res.append( len(pool[:indices[0]] )   )
					
				for iii in range(len(indices)-1):
					#print( pool[indices[iii] :indices[iii+1]])
					#if pool[indices[iii] :indices[iii+1]]  not in res :
					#if iii == 0 and len(pool[indices[iii] :indices[iii+1]]  ) in res:
						#continue
					res.append(   len(pool[indices[iii] :indices[iii+1]]  )   )
						
					if iii+1 == len(indices)-1 : # and pool[indices[iii+1]:] not in res :
						if pool[indices[iii+1]:] != () :
							res.append( len(pool[indices[iii+1]:] )   )
						if res not in settt :
							settt.append( res )
							yield res 
							
###########################################################################################################################################################################################################################################################################################################################
							
def combinations(iterable):
	# combinations('ABCD', 2) → AB AC AD BC BD CD
	# combinations(range(4), 3) → 012 013 023 123
	#NEWLL = gh(iterable)
	#iterable = iterable#[:-1]
	n = len(iterable)
	pool = tuple(iterable)
	#pool = tuple([i for i in range(1, n+1)])
	
	yield pool
	n__2 = (n*2)
	
	settt = []
	for  r in range(1,n):
		indices = list(range(r))
	
		
		#yield tuple(pool[i] for i in indices)
		
		while True:
			
			
			
		
			for i in reversed(range(r)):
				
				if indices[i] < i + n - r:    #   012345     :3    012  + 6-3=3      345   i + n - r   || i + 3   
					break												# n-r        012   i <<
			else:																	#+++3
				break
			indices[i] += 1
			for j in range(i+1, r):
				indices[j] = indices[j-1] + 1
				
			right = []
			if r == 1:
				right.append( pool[:indices[0]] )
				right.append( pool[indices[0]:] )
				#print("oooo", indices, pool[:indices[0]], pool[indices[0]:])
				#print("oooo", indices, right )
				if right not in settt :     ########
					settt.append( right )   ########
					yield right             ########
				
				
			if r > 1 :
				res = []
				if pool[:indices[0]]  != () :
					res.append( pool[:indices[0]] )
				
				for iii in range(len(indices)-1):
					#print( pool[indices[iii] :indices[iii+1]])
					if pool[indices[iii] :indices[iii+1]]  not in res :
						res.append(   pool[indices[iii] :indices[iii+1]]  )
					
					if iii+1 == len(indices)-1 and pool[indices[iii+1]:] not in res :
						res.append( pool[indices[iii+1]:] )
						if res not in settt :   ########
							settt.append( res ) ########
							yield res           ########
							
						
			#yield tuple(pool[i] for i in indices)
			
################################################################################################################################################################################################################################################################################################################################################################
		
LL = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
LL = [i for i in range(1,  12 +1)] # 13
#kkk = list(  combinations( LL  )  )	
#kkk = list(  combinations_len( LL  )  )	
kkk = list(  combinations_ln( LL  )  )
print(kkk)
"""		
		
		
def gh(LL):
	Q = []
	ind = 0
	for i in LL:
		Q.append(i)
		if ind == len(LL) - 1 :
			break
		Q.append(0)
		ind += 1
	return Q
	



LL = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]

[1  ,  2  ,  3  ,  4  ,  5  ,  6  ,  7  ,  8  ,  9  ,  10]
#   1     2     3     4     5     6     7     8     9 
#   |     |     |     |     |     |     |     |     |
#1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18

#   0     1     2     3     4     5     6     7      8
#   1     3     5     7     9     11    13    15     17

# FIRST len(LL)-1, 10-1, 9 {ODD NUMBERS} 

#l = [1,2,3,4,5,6,7,8,9]


NEWLL = gh(LL) 

for i in range( 1,len(LL)):##### 9 BLOCKINGS ,  1<->10, 9
	for se in list(  combinations( LL , i )  ):
	
		print(  se , NEWLL)
		
		
print(  )







#tem2 =  indices + [n]
#print(tem2)
#right = []
#for iii in range(len(tem2)-2):
#yes = pool_REAL[(pool[ tem2[iii] ] ) :   (pool[ tem2[iii+1] ] )] 
#right.append(yes)
right = []
pool[ :indices[0] ]
for iii in range(len(indices)-1):
	if r == 1:
		right.append(pool[ :indices[0] ] )
		right.append(pool[ indices[-1]: ] )
		print(pool[ :indices[0] ] , pool[ indices[-1]: ]  ,"<<<<" )
#yes1 = pool_REAL[ : pool[   indices[iii]    ]  ]
#yes = pool_REAL[  pool[   indices[iii]    ]:   pool[   indices[iii+1]    ]   ]
#yes2 = pool_REAL[     pool[   indices[iii+1]    ] :  ]
#if iii == 0 :
	#right.append(yes1)
#right.append(yes)
#if iii == len(indices)-1 : 
	#right.append(yes2)
	
	pass	
pool[ indices[-1]: ]
"""