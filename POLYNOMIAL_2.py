#!/usr/bin/env python3

#  EXPAND ((100a+10b+c)^4)


# https://www.google.com/search?q=expand+%28100a+%2B+10b+%2B+c%29%5E4&sca_esv=1052824479652a46&sxsrf=ADLYWIIUS6XduOrcwXeLJlH45RltJM1OKA%3A1727982824006&ei=6Oz-Zq0Hq7fA3g-JiI3YAg&ved=0ahUKEwitm5zT9fKIAxWrG9AFHQlEAysQ4dUDCA8&uact=5&oq=expand+%28100a+%2B+10b+%2B+c%29%5E4&gs_lp=Egxnd3Mtd2l6LXNlcnAiGWV4cGFuZCAoMTAwYSArIDEwYiArIGMpXjQyBRAhGKABMgUQIRigATIFECEYoAFIuAtQxgRY1whwAXgAkAEAmAGBAaAB7gGqAQMwLjK4AQPIAQD4AQGYAgOgAvwBwgIOEAAYgAQYsAMYhgMYigXCAgsQABiwAxiiBBiJBcICCxAAGIAEGLADGKIEwgIFECEYnwWYAwCIBgGQBgeSBwMxLjKgB8gK&sclient=gws-wiz-serp


# expand (100a + 10b + c)^8


def product(iterables, square):
	# product('ABCD', 'xy') → Ax Ay Bx By Cx Cy Dx Dy
	# product(range(2), repeat=3) → 000 001 010 011 100 101 110 111
	
	
	
	
	pools = [tuple(iterables) for i in range(square)]
	
	
	#print( iterables[ 0 ] ** square )
	#print( iterables[ -1 ] ** square )  # 1
	
	#print(pools,"here") # (100,10,1)
	
	def mul(l):
		one = 1
		for i in l:
			one *= i
		return one
	
	
	# len(iterables) ** square
	
	
	q = []
	result = [() ]
	cn= 0
	
	cnn = {}
	for pool in pools:
		
		q = []
		for x in result :
			if  len(result)  == len(iterables) ** square : break
			
			for y in pool :
				
				cn += 1
				#if  len(result)     == len(iterables) ** square : #iterables[-1] ** square  : 
				if mul(x)*mul([y])  == iterables[ -1 ] ** square  :
					i = mul(x)*mul([y])
					#print(i)
					if i not in cnn :
						cnn[ i ] = 0
					cnn[ i ] += 1
				q.append( [ mul(x)*mul([y]) ]  )
				
				
		result = q
		
		
	return result
		
def product_str(iterables, square):
	# product('ABCD', 'xy') → Ax Ay Bx By Cx Cy Dx Dy
	# product(range(2), repeat=3) → 000 001 010 011 100 101 110 111
	
	
	repeat = 1
	
	pools = [tuple(iterables) for i in range(square)]  
	
	#print(pools,"here")
	
	
	
		
	q = []
	result = [[]]
	cn= 0
	
	qu = []
	cnt = {}
	for pool in pools:
		
		q = []
		for x in result :
			if  len( x ) == square  :  break #len( x ) == (repeat * len(iterables)  ) : break
			
			for y in pool :
				
				cn += 1
				#if  len( x+[y] ) == (repeat * len(iterables)  )  : print(x+[y] , cn) # 365     876
				if  len(  x+[y]  ) == square  :   #   (repeat * len(iterables)  ) : #print(x+[y] )
					i = x+[y]
					#print(i," <<<")
					for ii in i :
						if ii not in cnt:
							cnt[ii] = 0
							
						cnt[ii] += 1
					mykeys = list(cnt.keys())
					mykeys.sort()
					cnt = {i:cnt[i] for i in mykeys}
					qu.append( cnt )
					cnt = {}
				
				q.append( x+[y]   )
				
		result = q
		

		
		#print(q,"qq")
	return qu
	#return result
	
	
	
	
	


#iterables = ['100 A', '10 B',  'C']

#one = 10 ** (len(iterables )  - 1  )

#cn = 0
#iterables_let = []
#iterables_num = []

#for i in  iterables :
	#iterables_let.append(i[-1])
	#iterables_num.append(int(one)   )
	#one/= 10
	#cn += 1
	
	
	






num = 100   ##################
race_to_power = 8    # 8 you are pushing it

alphabet = [    "A", "B", "C" , "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"    ]
len( str(   num)    )		

#cn = 0
iterables_let = []
iterables_num = []
one = 10 ** (len( str(   num)    ) - 1  )
for i in  range(  len( str(   num)    )	 ) :
	iterables_let.append(alphabet[i])
	iterables_num.append(int(one)   )
	one/= 10
	
	
	
	
	
	
print()
print()




q = {}


ccc = 0
for j in list(product_str(iterables_let, race_to_power)) :
	
	if tuple(    [k+str(v) for k, v in j.items()]    ) not in q :
		q[ tuple(    [k+str(v) for k, v in j.items()]    ) ] = 0
		
		
	q[tuple(    [k+str(v) for k, v in j.items()]    ) ] +=    list(product(iterables_num, race_to_power))[ccc][0]
	
	#print(j  , list(product(iterables_num, 4))[ccc])
	ccc+=1
	
	
	#print(q,"QQQ" , )
	
	
	
print([[v,k]  for k, v in q.items()])


#print( [k+str(v) for k, v in {'A': 1, 'B': 1, 'C': 2}.items()]  )

