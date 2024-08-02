#!/usr/bin/env python3
def combinations(iterable):
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


def do(mat, variables):
	
	lin=[len(i) for i in mat] ## OR [ 4 , 3 , 5 , 4 ]
	mx = max(lin)  ## 5
	matt = [[0]* len(mat) for _ in range(mx)]
		
	cn = 0
	for row in lin:
		for col in range(row):                                     # 0-4
			matt[col][cn] = 	mat[cn][col]				   # 0-3
			                              			   # 0-5
											                       # 0-4
		cn += 1
		
	mat = matt
	
	q = [None]
	res = set()
	empty = []
	res2 = set()
	
	"""
	Kerogen_Conversion_and_Maturity  = [ "Oil zone" , "Condensate wet gas zone" , "Dry gas zone" ,  "Immature" ] # 4
	
	Kerogen_Type_and_Maturity = [ "Type I Kerogen" ,  "Type II Kerogen" ,  "Type III Kerogen"  ] # 3
	
	Kerogen_Quality_Plot =  [  "Type I Kerogen oil prone usually lacustrine" , 
							"Type II Kerogen oil prone usually marine" , "Mixed Type II/III Kerogen (oil/gas prone)" ,
							"Type III Kerogen (gas prone)" , "Type IV (dry gas prone)" ]  # 5
	
	Pseudo_Van_Krevelen_Plot  = [ "Type I Kerogen (highly oil prone)"  , "Type II Kerogen (oil prone)"  ,
								"Mixed Type II/III Kerogen (oil/gas prone)" , "Type III Kerogen (gas prone)" ] # 4
	
	#variables = [Pseudo_Van_Krevelen_Plot]+[Kerogen_Quality_Plot]+[Kerogen_Type_and_Maturity]+[Kerogen_Conversion_and_Maturity]
	#variables = [Kerogen_Conversion_and_Maturity]+[Kerogen_Type_and_Maturity]+[Kerogen_Quality_Plot]+[Pseudo_Van_Krevelen_Plot]
	variables = [Kerogen_Conversion_and_Maturity , Kerogen_Type_and_Maturity , Kerogen_Quality_Plot , Pseudo_Van_Krevelen_Plot]
	"""
	
	
	lin=[len(i) for i in variables]
	mx = max(lin)  ## 5
	
	mat2 = [[0]* len(variables) for _ in range(mx)]
	cn = 0
	for row in lin:
		for col in range(row):   # 0-4
			mat2[col][cn] = 	variables[cn][col]				   # 0-3
			
		cn+=1
	#print(mat2)
	def dfs(rw,cl, path,   path2):
		# rw cl
		
		if 0 >  rw  :
			return
		if rw == len(mat) :
			return
		if  cl >= len(mat[rw])  :
			return
		if  mat[rw][cl] == 0  :
			return
		
		
		
		# plt here rw , cl
		path = path + [mat[rw][cl]] 
		path2 =  path2 + [mat2[rw][cl] +" : " + str(path[-1]) ] 
		
		if  cl == len(mat[rw]) -1 :
			res.add( tuple( path + [sum(path)] )  )
			path2 = path2 + [sum(path)]
			res2.add(tuple( path2 ) )
			
			path = []
			path2 = []
		for j in range(1, len(mat)):
			if rw+j < len(mat):
				q.append( mat[rw][cl] )
				dfs(rw+j,cl+1, path, path2) # v
				
				
			q.append( mat[rw][cl] )
			dfs(rw,cl+1, path, path2) # ->
			
			if rw-j >= 0 :
				q.append( mat[rw][cl] )
				dfs(rw-j,cl+1, path, path2) # ^     -->
				
	for r in range(len(mat)):
		dfs(r,0, [], [])
		
		#res.sort(key=lambda e: e[-1])
	
	
	#print(res, len(res))
	ress = list(res2)
	
	ress.sort(key=lambda e: e[-1])
	print(ress)


"""
mat = [[1,1,1,1],
	  [2,2,2,2],
	 [3,3,2.5,2.5],
	  [4,0,3,3],
	  [0,0,4,0]
]
"""


mat =                [ [1,2,3,4] ,       # 4   Kerogen_Conversion_and_Maturity
		              [1,2,3] ,         # 3   Kerogen_Type_and_Maturity
					  [1,2,2.5,3,4] ,   # 5   Kerogen_Quality_Plot
					  [1,2,2.5,3] ]     # 4   Pseudo_Van_Krevelen_Plot



Kerogen_Conversion_and_Maturity  = [ "Oil zone" , "Condensate wet gas zone" , "Dry gas zone" ,  "Immature" ] # 4

Kerogen_Type_and_Maturity = [ "Type I Kerogen" ,  "Type II Kerogen" ,  "Type III Kerogen"  ] # 3

Kerogen_Quality_Plot =  [  "Type I Kerogen oil prone usually lacustrine" , 
						"Type II Kerogen oil prone usually marine" , "Mixed Type II/III Kerogen (oil/gas prone)" ,
						"Type III Kerogen (gas prone)" , "Type IV (dry gas prone)" ]  # 5

Pseudo_Van_Krevelen_Plot  = [ "Type I Kerogen (highly oil prone)"  , "Type II Kerogen (oil prone)"  ,
							"Mixed Type II/III Kerogen (oil/gas prone)" , "Type III Kerogen (gas prone)" ] # 4

#variables = [Pseudo_Van_Krevelen_Plot]+[Kerogen_Quality_Plot]+[Kerogen_Type_and_Maturity]+[Kerogen_Conversion_and_Maturity]
#variables = [Kerogen_Conversion_and_Maturity]+[Kerogen_Type_and_Maturity]+[Kerogen_Quality_Plot]+[Pseudo_Van_Krevelen_Plot]
variables = [Kerogen_Conversion_and_Maturity , Kerogen_Type_and_Maturity , Kerogen_Quality_Plot , Pseudo_Van_Krevelen_Plot]


#do(mat, variables )



# 4354




st = ['Kerogen Conversion and Maturity' , 'Kerogen Type and Maturity' , 'Kerogen Quality Plot' , 'Pseudo Van-Krevelen Plot' ]
for rw in list(   combinations(  range(   len(variables) )  )    )   :
	temp = []
	temp2 = []
	#print(rw)
	cn = 0
	for rww in rw : 
	
		temp.append(  mat[rww]  )
		temp2.append(  variables[rww]   )
		if cn < len(rw) -1 :
			print(st[rww]+" and ", end=" ")
		else:
			print(st[rww] , end=" ")
		cn += 1
	cn = 0	
	print()
	print("")
	
	do( temp,temp2 )
	temp = []
	temp2 = []
	
	
	print("#########################################################################################################################################")

	

		