def combinations(iterable):
	# combinations('ABCD', 2) → AB AC AD BC BD CD
	# combinations(range(4), 3) → 012 013 023 123
	
	pool = tuple(iterable)
	n = len(pool)
	
	
	for r in range(2, 4 ):
		indices = list(range(r))
		
		if r < n :
			yield tuple(pool[i] for i in indices)
			while True:
				for i in reversed(range(r)):
					if indices[i] != i + n - r:
						break
				else:
					break
				indices[i] += 1
				for j in range(i+1, r):
					indices[j] = indices[j-1] + 1
				yield tuple(pool[i] for i in indices)
				
def combinations_(iterable):
	# combinations('ABCD', 2) → AB AC AD BC BD CD
	# combinations(range(4), 3) → 012 013 023 123
	
	pool = tuple(iterable)
	n = len(pool)
	
	
	for r in range(2, 4 ):
		indices = list(range(r))
		
		if r < n :
			
			if len(indices) >= 2 :
				ttt = ''
				for ig in indices[:-1] :
					#print(type(pool[ig]))
					ttt += pool[ig] + '-'
				ttt += pool[indices[-1] ]
				#print(ttt ,"<<<<", type(ttt))
				yield [(str(ttt))]
				ttt = ''
				#if len(indices) == 1 :
				#yield tuple(pool[i] for i in indices)
			while True:
				for i in reversed(range(r)):
					if indices[i] != i + n - r:
						break
				else:
					break
				indices[i] += 1
				for j in range(i+1, r):
					indices[j] = indices[j-1] + 1
				if len(indices) >= 2 :
					ttt = ''
					for ig in indices[:-1] :
						#print(type(pool[ig]))
						ttt += pool[ig] + '-'
					ttt += pool[indices[-1] ]
					#print(ttt ,"<<<<", type(ttt))
					tup = tuple(ttt)
					yield [(str(ttt))]
					#if len(indices) == 1 :
					#yield tuple(pool[i] for i in indices)
					ttt = ''
				
				
def product(iterables, repeat=1):
	
	pools = iterables
	#print(pools	,'here')
	
	
	q = []
	result = [[]]
	cn= 0
	C = 1
	ccc = 0
	for pool in pools:
		
		q = []
		for x in result :
			#if  len( x ) == (len(iterables)  ) : break
			if  C == (len(iterables)  ) +1 : break
			for y in pool :
		
				cn += 1
				#if  len(  x+[y]  ) == (len(iterables)  ) : 
					#print(x+[y] )
				
				
				
				SS = x+[y]
				STR = " "
				if  C == (len(iterables)  ) : 
					for ih in SS :
						tem = " "
						indddd = 0
						for ihh in ih :
							if indddd< len(ih)-1:
								tem += ihh + ", "
							if indddd== len(ih)-1:
								tem += ihh + " " 
							
							indddd += 1
							
						tem +=  ";"
						
						STR += tem
					print( STR , ccc)
					print()
					#print()
					ccc += 1
				
				q.append( x+[y]   )
		
		result = q
		C += 1
		
		
	
	return result  # or q 
	






"""
if one + len(pools[0]) == cn :
	break
"""
	
	
	
''
	
	
colors = [	
"lt gy-gy" ,
#"gy" ,
"offwht-wht" ,
#"wh" ,
#"crm" ,
"bf" ,
"mot" 
]


crystal_size = ["cryptoxln-mcxln" ]

textures = [
"lith mdst tex" ,
"mic suc-suc tex" ,
"vit ip tex" ,
"rthy tex" ,
"dull/rthy tex" 
]

accessories = [
"arg" ,
"slty" ,
"carb" 
]


Colors_crystal_size_textures_accessories = [colors , crystal_size, textures , accessories ]



PRODUCT = []

io = 0
for colors_crystal_size_textures_accessories in Colors_crystal_size_textures_accessories :
	

	#each = [i for i in combinations(colors_crystal_size_textures_accessories) ]
	
	if io > -1 :
		each = [i for i in combinations(colors_crystal_size_textures_accessories) ]
		#print(each,"after")
		if each != []:
			PRODUCT.append( each )

	if io == 1111111110 :
		eachh = [i for i in combinations_(colors_crystal_size_textures_accessories) ]
		#print(eachh, len(eachh))
		if eachh != []:
			PRODUCT.append( eachh )
	
		
	io += 1                                             
		
		
		#print(PRODUCT, len(PRODUCT))
		
		
_2nd = list( product( PRODUCT )  ) 		#  my form 
#print(  _2nd , len( _2nd )   )
	