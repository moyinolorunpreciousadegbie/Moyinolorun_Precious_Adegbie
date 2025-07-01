#!/usr/bin/env python3

def compress(data, selectors):
	# compress('ABCDEF', [1,0,1,0,1,1]) → A C E F
	#return (datum  for datum, selector in zip(data, selectors) if selector)
	#return ([d[0] , i]  for i , d in enumerate(zip(data, selectors)) if d[1])
	ind = []
	val = []
	notind = []
	notval = []
	
	for i , d in enumerate(zip(data, selectors)) :
		if d[1]:
			ind.append(i)
			val.append(d[0])
		if not d[1]:
			notind.append(i)
			notval.append(d[0])
	return ind, val #, notind , notval

def product(iterables, iterable, ga):
	_9 = len(iterable)
	
	u = _9 # 4 redundants
	repeat = u
	#repeat = [ tuple(iterables[0]) ]
	f = [tuple(pool) for pool in iterables] 
	ff = [tuple(pool)[::-1] for pool in iterables] #<<<
	#print(pools	,'here')
	pools = []
	poolz = []#<<<
	
	cn = 0
	while u > 0 :
		
		
		pools.append(f[cn])
		
		poolz.append(ff[cn])#<<<
		
		if cn + 1 == len(f) : cn = -1
		
		
		
		cn += 1
		u -= 1
		
		
	print(pools)
	print(poolz)
	pools2 = poolz
	
	_1 = 1
	
	q = []
	result = [[]]
	resultz = [[]]
	result2 = [[]]
	cn= 0
	
	ans = []
	anss = []
	ans2 = []
	
	ind = 0
	final = 1
	for pool in pools:
		pool_=poolz[-_1]
		pool2 = pools2[ind]
		_1 +=1
		
		q = []
		qq = []
		
		q2 = []
		
		__1 = 1
		indd = 0
		for x in result :
			#xx = resultz[-__1] #<<<<<<<
			xiiii = result2[indd] 
			__1+=1 
			indd += 1
			
			
			
			___1 = 1 
			inddd = 0
			for y in pool :
				#yy =pool_[-___1] #<<<<<<<
				yiiii  = pool2[inddd]
				___1 += 1
				inddd += 1
				
				cn += 1
				
				
				#if  sum(x + [y]) > _9 : 
					#continue
				
				#if  sum([yy]+xx) > _9 : #<<<<<<<
					#continue #<<<<<<<
				
				
				#if  sum([yiiii]+xiiii) > _9 : 
					#continue
				
				if len(x+[y]) == _9 : 
					#print(x+[y])
					ans.append(x+[y])
					
					#if len([yy]+xx) == _9 : 
					#print([yy]+xx)
					#anss.append([yy]+xx)
					
					
				if len(xiiii+[yiiii]) == _9 : 
					#print([yy]+xx)
					ans2.append(xiiii+[yiiii])
					
				ooo = [yiiii]+xiiii
				
				neb = x+[y]        #VVV AREA MUST CHANGE X,Y != 0,0      
				if len(x+[y]) == _9    :        #   GAURANTEED
					#print(x+[y], [yy]+xx, ooo[::-1])
					#_1 = list(compress(iterable, x+[y]))
					#_2_ = list(compress(iterable, ooo[::-1])) 
					#print(x+[y],  ooo[::-1], final,  list(compress([1,2,3,4,5,6,7,8], x+[y]))  , list(compress([1,2,3,4,5,6,7,8], ooo[::-1])) )
					#print( _2_[-1],_1[-1],_2_[0])
					#print(x+[y],  ooo[::-1],' ,')
					#print(neb," ,")
					print(ooo[::-1])
					final += 1
					#if x+[y] ==   ooo[::-1] or sum(x+[y]) == sum(ooo):
						#print("############################")
						#print("MID")
						#print("############################")
				
				q.append( x+[y]   )
				
				#qq.append([yy]+xx) #<<<<<<<
				
				
				q2.append([yiiii]+xiiii)
			___1 = 1
			inddd = 0
		__1 = 1
		indd = 0
		
		result = q
		
		#resultz = qq   #<<<<<<<
		
		
		
		result2 = q2
		
		ind += 1
		
		
		
	#return ans # result  # or q 


_00,_01,_10,_11 = [[0,0,     0],[0,0,     1]],    [[0,1,    0],[0,1,    1]],    [[1,0,    0],[1,0,    1]], [[1,1, 0],[1,1, 1]]
UPS = ['00','01','10','11']
DOWNS = ['00','01','10','11']



iterable = [1,2,3]#,4]#,5,6,7,8]
ga = 4

	
product( [ [-1,1], [-1,1]]  , iterable, ga ) 

#_2nd = list( product([ [0,1], [0,1]]   )  ) 		#  my form 

#print(  _2nd , len( _2nd )   )


x_span = 5 # 11
y_span = 5 # 11
z_span = 10 # 36
z_step = 1
for i in range(x_span-1,x_span):
	for j in range(y_span-1,y_span):
		for k in range(1,z_span,z_step):# or    subsets(    (range(1,z_span))    )
			print( 'i x X, j x Y, k x Z',[i,j,k] ) # pick from any 

# hash map the area (x,y) :::: not in visited for 1 z layer
			
# hash map the area (x,y, z) :::: not in visited for multiple z layers  
			
			#  and checkfunction(seismicdata[ x,y,z]  )   X, Y,  Z = 334, 344, 525


