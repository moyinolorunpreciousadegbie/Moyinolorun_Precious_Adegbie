

print()
print()

########################################################################################################################################################################
########################################################################################################################################################################
########################################################################################################################################################################

def subsets( nums, r):
	
	n = len(nums)
	pool = nums
	
	indices = list( range(r) )
	
	yild = []
	numz = nums.copy()
	zer = 0
	for i in indices :
		numz.pop(i-zer)
		yild.append(pool[i])
		zer += 1
	yield yild, numz # AFFECTED BY THE FUNCTION BELOW SO USE UP  <<
	while True:
		for i in reversed( range(r) ):
			if indices[i] < i + n - r:
				break
		else:
			return
		indices[i] += 1
		for j in range(i+1, r):
			indices[j] = indices[j-1] + 1
			#print([pool[i] for i in indices])
		yild_ = []
		
		numzz = nums.copy()
		zerr = 0 
		for i in indices :
			numzz.pop(i-zerr)
			yild_.append(pool[i])
			zerr += 1
		yield yild_ , numzz
		
		

########################################################################################################################################################################
########################################################################################################################################################################
########################################################################################################################################################################

def product(iterables ):
	
	pools =   iterables 
	
	
	ch = 2 # < 5 
	
	# 2 & 3 BEST
	# 3 {4 CONSECUTIVES}
	# 4 {4 CONSECUTIVES}
	
	q1 = []
	result1 = [""]
	
	q2 = []
	result2 = [""]
	
	q3 = []
	result3 = [""]
	
	q4 = []
	result4 = [""]
	cn= 0
	
	FIRST_IND = 0
	
	COMMA = ""
	for pool in pools:
		
		if FIRST_IND > 0 :
			COMMA = ', '
			
		q1 = []
		q2 = []
		q3 = []
		q4 = []
		
		ind_result = 0
		for x in result1 :
			if  len( x ) == (  len(iterables)  ) : break
			
			
			res_ind = ind_result % len(result1)
			
			ii = res_ind
			n= len(result1)
			
			plus_minus = ( (ii%2)// (-1)  )  +  (((ii+1)%2)*1)
			plus_minus *= (ii//2)
			#print(  (ii%2),ii//2,  (ii%2)*n ,"|||",( (ii%2)*n)-(ii%2)   , plus_minus )
			flip = ( (ii%2)*n)-(ii%2)   + plus_minus
			
			
			
			x1,x2,x3,x4=[],[],[],[] 
			xx1,xx2,xx3,xx4=[],[],[],[]
			
			if ind_result < len(result1) :
				x1 = result1[ind_result]
				
			if ind_result < len(result2) :
				x2 = result2[ind_result]
				
			if ind_result < len(result3) :
				x3 = result3[ind_result]
				
			if ind_result < len(result4) :
				x4 = result4[ind_result]
				
				
				
			if flip < len(result1) :
				xx1 = result1[flip]
				
			if flip < len(result2) :
				xx2 = result2[flip]
				
			if flip < len(result3) :
				xx3 = result3[flip]
				
			if flip < len(result4) :
				xx4 = result4[flip]
				
			indd_result = 0
			for y in pool :
				
				cn += 1
				
				
				
				res_indd = indd_result % len(pool)
				
				iii = res_indd
				nn= len(pool)
				
				plus_minus_ = ( (iii%2)// (-1)  )  +  (((iii+1)%2)*1)
				plus_minus_ *= (iii//2)
				#print(  (iii%2),iii//2,  (iii%2)*nn ,"|||",( (iii%2)*nn)-(iii%2)   , plus_minus )
				flip_ = ( (iii%2)*nn)-(iii%2)   + plus_minus_
				
				y
				y_flip = pool[flip_]
				
				
				
				#print(yy)
				
				if  FIRST_IND == (len(iterables)-1  ) : 
					if ch == 1 :
						# print(x1+ COMMA +y+';')
						pass
					if ch == 2 :
						# print(x1+ COMMA +y_flip+';')
						pass
					if ch == 3 :
						# print(xx1+ COMMA +y+';')
						pass
					if ch == 4 :
						# print(xx1+ COMMA +y_flip+';')
						pass
					if ch == 5 :
						# print(x2+ COMMA +y+';')
						pass
					if ch == 6 :
						# print(x2+ COMMA +y_flip+';')
						pass
					if ch == 7 :
						# print(xx2+ COMMA +y+';')
						pass
					if ch == 8 :
						# print(xx2+ COMMA +y_flip+';')
						pass
					if ch == 9 :
						# print(x3+ COMMA +y+';')
						pass
					if ch == 10 :
						# print(x3+ COMMA +y_flip+';')
						pass
					if ch == 11 :
						# print(xx3+ COMMA +y+';')
						pass
					if ch == 12 :
						# print(xx3+ COMMA +y_flip+';')
						pass
					if ch == 13 :
						# print(x4+ COMMA +y+';')
						pass
					if ch == 14 :
						# print(x4+ COMMA +y_flip+';')
						pass
					if ch == 15 :
						# print(xx4+ COMMA +y+';')
						pass
					if ch == 16 :
						# print(xx4+ COMMA +y_flip+';')
						pass
						
						
				if ch == 1 :
					q1.append(x1+ COMMA +y)
				if ch == 2 :
					q1.append(x1+ COMMA +y_flip)
				if ch == 3 :
					q1.append(xx1+ COMMA +y)
				if ch == 4 :
					q1.append(xx1+ COMMA +y_flip)
				if ch == 5 :
					q2.append(x2+ COMMA +y)
				if ch == 6 :
					q2.append(x2+ COMMA +y_flip)
				if ch == 7 :
					q2.append(xx2+ COMMA +y)
				if ch == 8 :
					q2.append(xx2+ COMMA +y_flip)
				if ch == 9 :
					q3.append(x3+ COMMA +y)
				if ch == 10 :
					q3.append(x3+ COMMA +y_flip)
				if ch == 11 :
					q3.append(xx3+ COMMA +y)
				if ch == 12 :
					q3.append(xx3+ COMMA +y_flip)
				if ch == 13 :
					q4.append(x4+ COMMA +y)
				if ch == 14 :
					q4.append(x4+ COMMA +y_flip)
				if ch == 15 :
					q4.append(xx4+ COMMA +y)
				if ch == 16 :
					q4.append(xx4+ COMMA +y_flip)
					
					
				indd_result+=1
			ind_result+=1
			
		if ch == 1 :
			result1 = q1
		if ch == 2 :
			result1 = q1
		if ch == 3 :
			result1 = q1
		if ch == 4 :
			result1 = q1
		if ch == 5 :
			result2 = q2
		if ch == 6 :
			result2 = q2
		if ch == 7 :
			result2 = q2
		if ch == 8 :
			result2 = q2
		if ch == 9 :
			result3 = q3
		if ch == 10 :
			result3 = q3
		if ch == 11 :
			result3 = q3
		if ch == 12 :
			result3 = q3
		if ch == 13 :
			result4 = q4
		if ch == 14 :
			result4 = q4
		if ch == 15 :
			result4 = q4
		if ch == 16 :
			result4 = q4
			
		FIRST_IND += 1
		
	if ch == 1 :
		return result1
	if ch == 2 :
		return result1
	if ch == 3 :
		return result1
	if ch == 4 :
		return result1
	if ch == 5 :
		return result2
	if ch == 6 :
		return result2
	if ch == 7 :
		return result2
	if ch == 8 :
		return result2
	if ch == 9 :
		return result3
	if ch == 10 :
		return result3
	if ch == 11 :
		return result3
	if ch == 12 :
		return result3
	if ch == 13 :
		return result4
	if ch == 14 :
		return result4
	if ch == 15 :
		return result4
	if ch == 16 :
		return result4

########################################################################################################################################################################
########################################################################################################################################################################
########################################################################################################################################################################
	
def dofff(nums, mpp , MAPP,  i):
	
	if i > len(mpp)-1 :
		return
	
	w = list(subsets( nums, mpp[i]) ) 
	
	for fir , rest in w :
		
		if i == 0 and len(mpp)==1: 
			iterable = []
			for jkj in fir    :
				iterable.append( MAPP[jkj] )
				#print(iterable)
				#print(product(iterable))
				
				
			for ghg in product(iterable):
				
				
				
				
				FIN =  "-".join( fir ) +", " + "".join( ghg )
				
				#import re
				FIN = " ".join(FIN.split())
				FIN = FIN.replace(", ,", ",")
				if FIN[-1]==",":
					FIN=FIN[:-1]
				yield FIN
				
				
		if i == len(mpp)-1 :
			
			yield "-".join(fir)
			#yield "-".join(item for item in fir if item)
			
		if i < len(mpp)-1 :
			for lisk in list( dof(rest, mpp , MAPP, i+1 )  ):
				
				"""
				if i == 0 : 
					iterable = []
					for jkj in fir  + lisk  :
						iterable.append( MAPP[jkj] )
						#print(iterable)
						#print(product(iterable))
					
					for ghg in product(iterable):
						print(ghg)
						yield fir  + lisk  + ghg
					
					
				else :	
					yield " - ".join(fir  + lisk  )
				"""
				
				#"""
				if lisk != "" or lisk != " " :
					yield "-".join(fir)+ ", " + lisk
				if lisk == "" or lisk == " " :
					yield "-".join(fir)
				#"""
					
				#yield " - ".join(item for item in fir  + lisk if item)
					
					
	if i == len(mpp)-1 :
		return
	
########################################################################################################################################################################
########################################################################################################################################################################
########################################################################################################################################################################
	
def dof(nums, mpp , i):
	
	if i > len(mpp)-1 :
		return
	
	w = list(subsets( nums, mpp[i]) ) 
	
	for fir , rest in w :
		
		if i == len(mpp)-1 :
			
			yield "-".join(fir)
			#yield " - ".join(item for item in fir if item)
			
		if i < len(mpp)-1 :
			for lisk in list( dof(rest, mpp , i+1 )  ):
				
				
				yield "-".join(fir  + lisk  )
				
				#yield " - ".join(item for item in fir  + lisk if item)
				
				
	if i == len(mpp)-1 :
		return
	

########################################################################################################################################################################
########################################################################################################################################################################
########################################################################################################################################################################
	
	
def flip(pool):
	
	flipp = []
	
	for indd_result  in range(len(pool)):
		
		res_indd = indd_result % len(pool)
		
		iii = res_indd
		nn= len(pool)
		
		plus_minus_ = ( (iii%2)// (-1)  )  +  (((iii+1)%2)*1)
		plus_minus_ *= (iii//2)
		#print(  (iii%2),iii//2,  (iii%2)*nn ,"|||",( (iii%2)*nn)-(iii%2)   , plus_minus )
		flip_ = ( (iii%2)*nn)-(iii%2)   + plus_minus_
		
		
		yy = pool[flip_]
		
		flipp.append(yy)
		
	return flipp

########################################################################################################################################################################
########################################################################################################################################################################
########################################################################################################################################################################

def padd(l,pad , level ):
	
	final = []
	
	def paddvv(final , l,pad , level ):
		
		if level == 0 :
			final.append(l) 
			return
		
		res = []
		for i in range(pad):
			ans = l[i::pad]
			#if i % 2 :
			ans = flip(ans)#########################################
			res += ans
			
			
			
		paddvv(final , res,pad , level-1 )
		
		#return res
	paddvv(final , l,pad , level )	
	return  final[-1]


########################################################################################################################################################################
########################################################################################################################################################################
########################################################################################################################################################################


		
def dof(nums, mpp , i):
	
	if i > len(mpp)-1 :
		return
	
	w = list(subsets( nums, mpp[i]) ) 
	
	for fir , rest in w :
		
		if i == len(mpp)-1 :
			
			yield "-".join(fir)
			#yield " - ".join(item for item in fir if item)
			
		if i < len(mpp)-1 :
			for lisk in list( dof(rest, mpp , i+1 )  ):
				
				
				yield "-".join(fir)   + ", " +lisk  
				
				#yield " - ".join(item for item in fir  + lisk if item)
				
				
	if i == len(mpp)-1 :
		return
	

#!/usr/bin/env python3

########################################################################################################################################################################
########################################################################################################################################################################
########################################################################################################################################################################
# SANDSTONE


color = [
"lt",
"dk",
"trnsl",
"wh",
"offwht",
"crm",
"gy",
"brn",
"blk",
"pk",
"tan",	
"mky",
"yel",
"orng",
"gn",
"red",
"bf",
"olv"

]

color = [
	
#"red orng",
#"red brn",
#"mar red",
#"brn",
#"crm",
# "bf",
"offwht", 
"sap",
"tan",
"lt gy"]


color = list( dof(color, [2,2] , 0) )
#print(color)


grain_size_range = [
#"slt/slty",
"slt",
#"slty",
"vf",
#"f/fy",
"f",
"fy",
"med",
"c/csy",
"c",
#"csy",
#"v crs"
"v c",
"pbl"
]



grain_size_range =  [  "f", "med" ] 
grain_size_range =  [ "v f" , "f", "med" ] 

grain_size_range = list( dof(grain_size_range, [2] , 0) )
#print(grain_size_range)

grained = [
"gr",
#"grnd"
]


sorting = [
#"v w srt",
#"w srt",
#"mod srt",
#"p srt",
#"v p srt",
	
"v w",
"w",
"mod"
]



sorting  = list( dof(sorting, [2] , 0) )
#print(sorting)

sorting_append = ["srt"]

shape = [
#"v ang",
#"ang",
"sb ang",
"sr",
"rd",
#"w rd",
#"v w rd"
	
]   

shape  = list( dof(shape, [2] , 0) )
#print(shape)

consolidation = [
"uncons",
"v fri",
"fri",
"sl fri",
"sl hd",
"hd",
"v hd",
#"N/A"
	
]

consolidation = ["sl fri",  "fri"]

consolidation  = list( dof(consolidation, [2] , 0) )
#print(consolidation)

consolidation_clusters = ["clus"]

few_loose = ["few lse",""]

grain_texture = [
"gly",
"vit",
"ctd",
"fros",
#"pit"
"wthrd pit"

]



grain_texture = [
"gly surf",
"sl arg rthy",
"fros",
#"wthrd pit tex",
#"f gr tex",
#"cly tex",
	
#"vit surf lstr",
#"dk o ctd"
]

grain_texture  = list( dof(grain_texture, [2] , 0) )
#print(grain_texture)


texture_append = ["tex"]


cement= [  # mtrx/embd
"calc"
#"v calc",
#"mod calc",
#"sl calc",
#"sl-mod calc",
#"v-mod calc",
#"dolc",
#"silc",
#"sidc",
#"pyrc",
#"glauc",
	
]

cement_append = ["cmt"]

matrix = [
"arg",
#"anhy/anhyc",
#"anhy",
#"anhyc",
#"gyp",
]

accessories = [
"arg",  #######
#"pyr",
#"glau",
"carb", #######
#"lig",
#"mic fos/mic fosus",
#"mic fos",
#"mic fosus",

#"fos/fosus",
#"fos",
#"fosus",

#"mics",
#"mmica",
#"micmica",
#"kaol/kao",
#"kaol",
#"kao",

#"hem/hemc",
#"hem",
#"hemc",

#"lmn/lmnc",
#"lmn",
#"lmnc",

#"cht",

#"bent/bentc",
#"bent",
#"bentc"
	
]

accessories = ["sl-mod calc",
	"arg",
	"carb"
]


ALL = [ color , grain_size_range , grained , sorting , sorting_append , shape , consolidation , consolidation_clusters , few_loose , grain_texture , texture_append , cement , cement_append , matrix , accessories]
ALL = [ color , grain_size_range , grained , sorting , sorting_append , shape , consolidation , consolidation_clusters , few_loose , grain_texture , texture_append , accessories]


ALL = [ color , grain_size_range , grained , sorting , sorting_append , shape , consolidation , consolidation_clusters , few_loose , grain_texture , texture_append , cement , cement_append  ]

grain_size_range = [i + " gr" for i in grain_size_range]
sorting = [i + " srt" for i in sorting]
consolidation = [i + " clus" for i in consolidation]
grain_texture = [i + " tex" for i in grain_texture]

ALL = [ color , grain_size_range  , sorting  , shape , consolidation  , few_loose , grain_texture  , cement , cement_append  ]

print("SANDSTONE")
for a in ALL :
	#print(a)
	pass
print("###################################################################################################################################################################")


an = product(ALL)
pad = len(ALL[0])
#pad = 23
#print(pad)
level = 3
res = padd(an,pad,level)
for r in res :
	print("SS: "+r+";")
print("###################################################################################################################################################################")


########################################################################################################################################################################
########################################################################################################################################################################
########################################################################################################################################################################

# SILTSTONE

color = [
	
#"red orng",
#"red brn",
#"mar red",
"gyshblk",
"bnshblk",
"bnshgy",
"brn",
"tan",
"offwht",
"lt gy"]

color  = list( dof(color, [2] , 0) )
#print(color)


consolidation_hardness = [ # hardness
#"v sft",
"sft",

"frm",
"v frm",

#"sl hd",
#"brit",

#"hd",
#"v hd"
]

consolidation_hardness  = list( dof(consolidation_hardness, [2] , 0) )
#print(consolidation_hardness)


gummy = ["sl gmy ip"]



shape = [ 
#"sb blky-blky",  #<<<<
#"sb blky-sb plty",#<<<<
"sb blky",
# "occ sb plty",
"blky",
"sb plty",
# "occ amor", ###########
	
#"amor",
#"blky",
#"plty",
#"flky",
#"splt/fiss",
#"tab",
]

shape  = list( dof(shape, [2] , 0) )
#print(shape)

grain_size = [ 
	"v f", 
	"f", 
	#"med" ,
	#"c" , 
	#"v c" 
]

grain_size  = list( dof(grain_size, [2] , 0) )
#print(grain_size)

grained = [
"gr",
#"grnd"
]

texture = [
#"slky-c",
#"plas surf tex", 
#"f sm surf tex",#####
#"slky c surf tex",#<<<<<
#"vit lstr",#<<<<<
#"rthy tex", #####
#"slty rthy tex", #####
#"intbdd f sz clc silc grs" ###
#"intbdd f clc grs" ###  
	 #"vit surf lstr",
#"arg rthy", # if with shale
	
"rthy", # "cly sz rthy",
"f cly",
"sm surf",
"f slky"##########
	
#"wthrd pit surf" , # if with shale
]

texture  = list( dof(texture, [2] , 0) )
#print(texture)


texture_append = ["tex"]


accessories = [
	"arg", 
	#"sl carb" # if with shale, source rock
]


cement = [
#"slty cmt",
#"arg cmt",
#"v slty cmt",
"slty-arg cmt",
"v slty-arg cmt"
]

cement  = list( dof(cement, [1] , 0) )
#print(cement)


lamination = [ 
"",# non-laminated silt
"fy thn lam",
"lam"
]


ALL = [ color , consolidation_hardness , gummy ,  shape  , grain_size, grained ,  texture , texture_append , cement ]

grain_size = [i + " gr" for i in grain_size]
texture = [i + " tex" for i in texture]
ALL = [ color , consolidation_hardness , gummy ,  shape  , grain_size ,  texture  , cement ]

print("SILTSTONE")
for a in ALL :
	#print(a)
	pass
print("###################################################################################################################################################################")


an = product(ALL)
pad = len(ALL[0])
#pad = 23
#print(pad)
level = 3
res = padd(an,pad,level)
for r in res :
	print("SLTST: "+r+";")
print("###################################################################################################################################################################")



########################################################################################################################################################################
########################################################################################################################################################################
########################################################################################################################################################################

# DOLOMITE

color = [
	"lt gy",
	"offwht",
	"crm",
	"bf",
	"tan"
]

color  = list( dof(color, [2,1] , 0) )
#print(color)


MP = {"blky":["","occ sb blky"],
	"sb blky":["","occ blky"],
	"plty":["","occ sb plty"],
	"sb plty":["","occ plty"],
}

shape = [
	"blky",
	"sb blky",
	"plty",
	"sb plty"]


shape = list(dofff(shape, [2] , MP , 0))
#print(shape)



crystal_size = [
#"cryptoxln",
"mcxln",
"v f xln",
"f xln",
#"med xln",
#"c xln",
#"v c xln",
]

crystal_size = list( dof(crystal_size, [2] , 0) )
#print(crystal_size)

hardness = [
"v sft",
"sft",
"frm",
"sl hd",
"brit",
"hd",
"v hd",
]

hardness = list( dof(hardness, [2] , 0) )
#print(hardness)

texture = [
	"mas",
	#"dns"
]

texture_append = ["tex"]

accessories = ["tr arg ip"]

ALL = [ color , shape , crystal_size , texture , texture_append , accessories ]

texture = [i + " tex" for i in texture]
ALL = [ color , shape , crystal_size , texture  , accessories ]


print("DOLOMITE")
for a in ALL :
	#print(a)
	pass
print("###################################################################################################################################################################")


an = product(ALL)
pad = len(ALL[0])
#pad = 23
#print(pad)
level = 3
res = padd(an,pad,level)
for r in res :
	print("DOL: "+r+";")
print("###################################################################################################################################################################")




########################################################################################################################################################################
########################################################################################################################################################################
########################################################################################################################################################################

# LIMESTONE

color = [
#"lt/ltr",
#"lt",
#"ltr",
#"dk/dkr",
#"dk",
#"dkr",
#"wh",
#"crm",
#"bf",
#"tan",
#"brn",
#"blk",
#"gry"
#"gy",
#"red",
#"gn",
#"orsh",
#"orng",
#"pk",
	
"lt gy",
"crm",
"offwht",
"bf",
"tan"
]

color = list( dof(color, [2,1] , 0) )
#print(color)

dunham_classification = [
	"mudst",
	#"wkst",
	#"pckst",
	#"grnst",
	#"bdst"
]

crystal_size = [ 
	
	#"cryptoxln",
	"mcxln",
	#"v f xln",
	"f xln",
	#"med xln",
	#"c xln",
	#"v c xln",
]
# mcxln-f xln,

crystal_size = list( dof(crystal_size, [2] , 0) )
#print(crystal_size)


hardness = [ 
	#"v sft",
	#"sft",
	"frm",
	"v frm",
	#"sl hd",
	#"brit",
	#"hd",
	#"v hd",
	]
	
hardness = list( dof(hardness, [2] , 0) )
#print(hardness)
	
	
texture = [
#"gly",
"lith rthy",
"vit surf lstr",
"sl dns",
"mic suc-suc por"
	
	
#"lith",
#"dns",
#"mas",
#"suc",
#"mic suc",
#"chk/chky",
#"dtrl",
#"cgl & brec",
#"oolc",
#"pel",
#"nodr",
#"vit",
#"rsns",
#"rthy",
#"gran",
]

texture = list( dof(texture, [2,1] , 0) )
#print(texture)


texture_append = ["tex"] 

accessories = [
"sd/sdy",
"arg",
"pyr",
"fy dissm",
"nodr",
"mldc",
"drsy",
"glau/glauc",
"pel",
"gyp",
"anhy/anhyc",
"foss/fossus",
"mic fos/mic fosus",
"mmica",
#"micmica",
"carb"  
]

accessories = [
	"arg",
	#"sdy"
]


ALL = [ color , dunham_classification  , crystal_size  , hardness , texture , texture_append , accessories ]

texture = [i + " tex" for i in texture]

ALL = [ color , dunham_classification  , crystal_size  , hardness , texture  , accessories ]

print("LIMESTONE")
for a in ALL :
	#print(a)
	pass
print("###################################################################################################################################################################")


an = product(ALL)
pad = len(ALL[0])
#pad = 23
#print(pad)
level = 3
res = padd(an,pad,level)
for r in res :
	print("LS: "+r+";")
print("###################################################################################################################################################################")


########################################################################################################################################################################

# BENTONITE


color_plus = ["sft, f sm volc cly sz min mat" , "mod sft, f sm volc cly sz min mat" ]

color_plus = ["sft, f sm volc cly sz mat" , "mod sft, f sm volc cly sz mat" ]

ALL = [color,color_plus]


print("BENTONITE")
for a in ALL :
	#print(a)
	pass
print("###################################################################################################################################################################")


an = product(ALL)
pad = len(ALL[0])
#pad = 23
#print(pad)
level = 3
res = padd(an,pad,level)
for r in res :
	print("BENT: "+r+";")
print("###################################################################################################################################################################")


########################################################################################################################################################################


# CHALK

shape = [ # shape
"sb blky",
"blky",
"sb ang",
"sr"
#"brit"
]

hardness = [ # hardness
"v sft",
"sft",
#"sl hd",
#"brit"
]



color_plus = ["sb blky-sb ang, v f grnd, arg, sl hd, sl carb, calc cmt, f lam ip, mic fosus/fosus, occ f intbdd wi coarser intervals (mrly)"] # sl hd
color_plus = ["sb blky-sb ang, v f grnd, arg, sft, sl carb, calc cmt, f lam ip, mic fosus/fosus, occ f intbdd wi coarser intervals (mrly)"] # sft

color_plus =  ["v sft, cryptoxln, calc"]


ALL = [ color , color_plus ]




color_shape_hardness_plus = ["cryptoxln, sl carb, calc cmt, f lam ip, mic fosus/fosus, occ f intbdd wi coarser intervals"]

ALL = [ color , shape , hardness ,  color_shape_hardness_plus ]

print("CHALK")
for a in ALL :
	#print(a)
	pass
print("###################################################################################################################################################################")


an = product(ALL)
pad = len(ALL[0])
#pad = 23
#print(pad)
level = 3
res = padd(an,pad,level)
for r in res :
	print("CHK: "+r+";")
print("###################################################################################################################################################################")


########################################################################################################################################################################
########################################################################################################################################################################
########################################################################################################################################################################

# ANHYDRITE

color = [
"lt gy",
"crm",
"offwht",
	
"bf",
"sl pnk"# anhydrite
]

color = list( dof(color, [2,1] , 0) )
#print(color)

color_crystal = [
"clr",
"trnsl",
#"brit"
]

color_crystal = list( dof(color_crystal, [2] , 0) )
#print(color_crystal)


consolidation = [ # hardness
#"",
"cons",
#"sl hd",
"sft",
"mod sft",
"frm",
#"v frm",
#"brit",
]

consolidation = list( dof(consolidation, [2] , 0) )
#print(consolidation)


shape = ["blky","sb blky","plty","sb plty"] # ,"occ amor"] 

MP = {"blky":["","occ sb blky"],
	"sb blky":["","occ blky"],
	"plty":["","occ sb plty"],
	"sb plty":["","occ plty"],
}

shape = list(dofff(shape, [2] , MP , 0))
#print(shape)

crystal_size = [ "cryptoxln","mcxln" ] # "v f xln" , "f xln"]

crystal_size = list( dof(crystal_size, [2] , 0) )
#print(crystal_size)


texture = [  
"mas",
#"vit surf lstr",
#"dns tex",
"mic suc-suc por",
"xln",
"gran"
]

texture = list( dof(texture, [2,1] , 0) )
#print(texture)


texture_append = ["tex"]

texture_permanent =  ["fros tex" ] ## weathering/dissolution , partial hydration(conversion to gypsum) , efflorescence and salt crusts

ALL = [  color , color_crystal , consolidation , shape , crystal_size , texture , texture_append , texture_permanent ]

texture = [i + " tex" for i in texture]
ALL = [  color , color_crystal , consolidation , shape , crystal_size , texture  , texture_permanent ]

print("ANHYDRITE")
for a in ALL :
	#print(a)
	pass
print("###################################################################################################################################################################")


an = product(ALL)
pad = len(ALL[0])
#pad = 23
#print(pad)
level = 3
res = padd(an,pad,level)
for r in res :
	print("ANHY: "+r+";")
print("###################################################################################################################################################################")


########################################################################################################################################################################

# SALT


color = [
	
"lt gy",
"offwht",
"tan",
"wht",
		
]

color = list( dof(color, [2,1] , 0) )
#print(color)

clr_trnsl = [
"clr",
"trnsl"
]

clr_trnsl = list( dof(clr_trnsl, [2] , 0) )
#print(clr_trnsl)

grained = ["gr",]#"grnd"]  


consolidation = [ # hardness
"cons",
#"sl hd",
	
"sft",
"frm",
#"brit",
]

consolidation = list( dof(consolidation, [2] , 0) )
#print(consolidation)


shape = ["sb blky","blky"]#,"sb plty"] # ,"occ amor"] 

shape = list( dof(shape, [2] , 0) )
#print(shape)


crystal_size = [ "cryptoxln","mcxln" ] # "v f xln" , "f xln"]

crystal_size = list( dof(crystal_size, [2] , 0) )
#print(crystal_size)


texture = [
	
"sm surf",
"gly",
"mic suc-suc por"
]

texture = list( dof(texture, [2] , 0) )
#print(texture)

texture_append = ["tex"]




ALL = [ color , clr_trnsl , grained , consolidation  , shape , crystal_size , texture , texture_append ]


clr_trnsl = [i + " gr" for i in clr_trnsl]
texture = [i + " tex" for i in texture]

ALL = [ color , clr_trnsl  , consolidation  , shape , crystal_size , texture  ]

print("SALT")
for a in ALL :
	#print(a)
	pass
print("###################################################################################################################################################################")


an = product(ALL)
pad = len(ALL[0])
#pad = 23
#print(pad)
level = 3
res = padd(an,pad,level)
for r in res :
	print("SA: "+r+";")
print("###################################################################################################################################################################")

########################################################################################################################################################################
########################################################################################################################################################################
########################################################################################################################################################################

# SHALE

color = [
	
"bnshblk",
"dk gy",
"bnshgy",
"dk brn",
"blk",
"gyshblk",
#"gyshbrn",
# "mot",

#"yel",
#"ylshgy",
	
#"olblk",
#"olvgy",
	
#"gnshblk",
#"gnshgy",
]

color = list( dof(color, [2,2] , 0) )
#print(color)

hardness = [ # hardness
#"v sft",
#"sft",     
#"frm",

"sl hd",
"frm",
#"v frm",######
"brit",
	
#"hd",
#"v hd",
]

hardness = list( dof(hardness, [2] , 0) )
#print(hardness)

shape = [
"amor",
"blky",
"plty",
"flky",
"splt/fiss",
"tab"
]
shape = ["sb blky","blky","sb plty"] # ,"occ amor"] 

shape = list( dof(shape, [2] , 0) )
#print(shape)


interbedded = ["intbdd f clc grs"]

texture = [
"plas",
"wxy",
"sm",
"c",
"slky",

"gly/vit",
"vit",
"gly",
"gsy"
]

texture = ["plas surf","vit lstr","c sdy"]#,"sdy","org gsy"]

texture = list( dof(texture, [2] , 0) )
#print(texture)

texture_append = ["tex"]

accessories = [
"calc",
"dolc",
"silc",
"carb",
"slty",
"sdy",#=--
"aren",#=--
"glau",
"gluac",
"gyp",
"micmica",
"mmica",
"pyr",
"pyrc",
"mrly",
"ferr",
"bent"
	
]

accessories_calcareous = ["sl-mod calc ip",    "carb"
	#"v-mod calc"
]

accessories_calcareous = list( dof(accessories_calcareous, [2] , 0) ) +  list( dof(accessories_calcareous, [1] , 0) )  #########################


bedding_lamination = [ # bdd  
#"fy lam",
"fy thn lam",
#"ripple lam"
]





Fractures = [
"tab cal",
"euhed cal",
"sb euhed cal",
"anhed calc",
"tab pyr",
"tab gil" 
]


ALL = [ color , hardness , shape , interbedded, texture , texture_append , accessories_calcareous , bedding_lamination , Fractures ]
ALL = [ color , hardness , shape , interbedded, texture , texture_append , accessories_calcareous , bedding_lamination ]

texture = [i + " tex" for i in texture]
ALL = [ color , hardness , shape , interbedded, texture  , accessories_calcareous , bedding_lamination ]

print("SHALE")
for a in ALL :
	#print(a)
	pass
print("###################################################################################################################################################################")


an = product(ALL)
pad = len(ALL[0])
#pad = 23
#print(pad)
level = 3
res = padd(an,pad,level)
for r in res :
	print("SH: "+r+";")
print("###################################################################################################################################################################")



########################################################################################################################################################################

# MARLSTONE

hardness_marl  = [
"v frm",
"frm",
"sl hd" ,
"brit ip"
]

texture_marl = [ "f sm surf tex" ]

lamination_marl = ["f thn lam ip" , "f lam ip" ,]


ALL = [ color , hardness_marl , shape , texture_marl , lamination_marl ]


print("MARLSTONE")
for a in ALL :
	#print(a)
	pass
print("###################################################################################################################################################################")


an = product(ALL)
pad = len(ALL[0])
#pad = 23
#print(pad)
level = 3
res = padd(an,pad,level)
for r in res :
	print("MRLST: "+r+";")
print("###################################################################################################################################################################")

### COAL 