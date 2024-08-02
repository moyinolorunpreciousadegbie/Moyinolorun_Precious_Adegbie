def combination(iterable):
	pool = tuple(iterable)
	n = len(pool)
	for r in range(1, n+1):
		indices = list(range(r))
		
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

def combinations(all_variables, variables):
	from collections import defaultdict
	rang = [ len(i) for i in all_variables ] 
	adj = defaultdict(int)
	adj2 = defaultdict(int)
	lss = set()
	pool = tuple(rang)
	n = len(pool)      
	r = n 
	indices = [n]  * (n)
	cycles = [0] * (n)
	
		
	lin=[len(i) for i in all_variables] ## OR [ 4 , 3 , 5 , 4 ]
	mx = max(lin)  ## 5
	mat = [[0]* len(all_variables) for _ in range(mx)]
	mat2 = [[0]* len(all_variables) for _ in range(mx)]
	
	cn = 0
	for row in lin:
		for col in range(row):                                     # 0-4
			mat[col][cn] = 	all_variables[cn][col]				   # 0-3
			mat2[col][cn]	= 	variables[cn][col]				   # 0-5
											                       # 0-4
		cn += 1
		"""
		[1, 1, 1,  1]
		[2, 2, 2,  2]
		[3, 3, 2.5,2.5]
		[4, 0, 3,  3]
		[0, 0, 4,  0]
		
    #    Transpose all_variables
    #    4  3  5   4
		"""
		##########################################
		
	cyc = [ sum(i) for i in all_variables ] 
	#rang = [i+1 for i in rang ]
	
	while n:
		for i in reversed(range(r )):
			lss.add( tuple(cycles)  )
			temp = []
			cn=0
			q = []
			qw = []
			sm = 0
			for c in cycles:
				# c cn
				#print(c, cn) #                   c - row     |  cn - col
				temp.append(  mat[c][cn] )
				q.append( mat2[c][cn] +" : "  +  str( mat[c][cn])   )
				qw.append( mat2[c][cn])
				cn+=1
				#print()
			sm = sum( temp )   
			cn = 0
			adj[  tuple(q) ] = float(sm)
			adj2[  tuple(qw) ] = float(sm)
			cycles[i] += 1
			if cycles[i] == rang[i]:  #######
				cycles[i] = 0
			else:
				break 
		else:
			break
	sorted_dict = dict(sorted(adj.items(), key=lambda x: x[1]))
	sorted_dict2 = dict(sorted(adj2.items(), key=lambda x: x[1]))
	
	#print(lss)
	
	return sorted_dict,  sorted_dict2


all_variables = [ [1,2,3,4] ,       # 4   Kerogen_Conversion_and_Maturity
					[1,2,3] ,         # 3   Kerogen_Type_and_Maturity
					[1,2,2.5,3,4] ,   # 5   Kerogen_Quality_Plot
					[1,2,2.5,3] ]     # 4   Pseudo_Van_Krevelen_Plot
########################################################
#.   #  4 x 3 x 5 x 4 = 240 combinations 

Kerogen_Conversion_and_Maturity  = [ "Oil zone" , "Condensate wet gas zone" , "Dry gas zone" , "Immature" ] # 4

Kerogen_Type_and_Maturity = [ "Type I Kerogen" ,  "Type II Kerogen" ,  "Type III Kerogen"  ] # 3

Kerogen_Quality_Plot =  [  "Type I Kerogen oil prone usually lacustrine" , 
						"Type II Kerogen oil prone usually marine" , "Mixed Type II/III Kerogen (oil/gas prone)" ,
						"Type III Kerogen (gas prone)" , "Type IV (dry gas prone)" ]  # 5

Pseudo_Van_Krevelen_Plot  = [ "Type I Kerogen (highly oil prone)"  , "Type II Kerogen (oil prone)"  ,
							"Mixed Type II/III Kerogen (oil/gas prone)" , "Type III Kerogen (gas prone)" ] # 4

variables = [Kerogen_Conversion_and_Maturity]+[Kerogen_Type_and_Maturity]+[Kerogen_Quality_Plot]+[Pseudo_Van_Krevelen_Plot]
#variables = [Kerogen_Conversion_and_Maturity , Kerogen_Type_and_Maturity , Kerogen_Quality_Plot , Pseudo_Van_Krevelen_Plot]
##########################################


#print( combinations(all_variables, variables)[0], combinations(all_variables, variables)[1],'here')


st = ['Kerogen Conversion and Maturity' , 'Kerogen Type and Maturity' , 'Kerogen Quality Plot' , 'Pseudo Van-Krevelen Plot' ]
for rw in list(   combination(  range(   len(variables) )  )    )   :
	temp = []
	temp2 = []
	#print(rw)
	cn = 0
	for rww in rw : 
		
		temp.append(  all_variables[rww]  )
		temp2.append(  variables[rww]   )
		if cn < len(rw) -1 :
			print(st[rww]+" and ", end=" ")
		else:
			print(st[rww] , end=" ")
		cn += 1
	cn = 0	
	print()
	print("")
	
	print( combinations( temp,temp2 ) )
	temp = []
	temp2 = []
	
	
	print("#########################################################################################################################################")
	
	
	