#  EXPAND ((100a+10b+c)^4)


# https://www.google.com/search?q=expand+%28100a+%2B+10b+%2B+c%29%5E4&sca_esv=1052824479652a46&sxsrf=ADLYWIIUS6XduOrcwXeLJlH45RltJM1OKA%3A1727982824006&ei=6Oz-Zq0Hq7fA3g-JiI3YAg&ved=0ahUKEwitm5zT9fKIAxWrG9AFHQlEAysQ4dUDCA8&uact=5&oq=expand+%28100a+%2B+10b+%2B+c%29%5E4&gs_lp=Egxnd3Mtd2l6LXNlcnAiGWV4cGFuZCAoMTAwYSArIDEwYiArIGMpXjQyBRAhGKABMgUQIRigATIFECEYoAFIuAtQxgRY1whwAXgAkAEAmAGBAaAB7gGqAQMwLjK4AQPIAQD4AQGYAgOgAvwBwgIOEAAYgAQYsAMYhgMYigXCAgsQABiwAxiiBBiJBcICCxAAGIAEGLADGKIEwgIFECEYnwWYAwCIBgGQBgeSBwMxLjKgB8gK&sclient=gws-wiz-serp



def product(iterables, square):
	# product('ABCD', 'xy') → Ax Ay Bx By Cx Cy Dx Dy
	# product(range(2), repeat=3) → 000 001 010 011 100 101 110 111
	
	
	
	
	pools = [tuple(iterables) for i in range(square)]
	
	#print(pools,"here")
	
	def mul(l):
		one = 1
		for i in l:
			one *= i
		return one
	
	
	result = [[]]
	for pool in pools:
		result = [[mul(x)*mul([y]) ] for x in result for y in pool]
	
	cn = {}
	for i in result:
		if tuple(i) not in cn :
			cn[tuple(i)] = 0
		cn[tuple(i)] += 1
	
		#print(cn)
	
	for prod in result:
		yield tuple(prod)
		
def product_str(iterables, square):
	# product('ABCD', 'xy') → Ax Ay Bx By Cx Cy Dx Dy
	# product(range(2), repeat=3) → 000 001 010 011 100 101 110 111
	
	
	
	
	pools = [tuple(iterables) for i in range(square)]
	
	#print(pools,"here")
	
	
	result = [[]]
	for pool in pools:
		result = [x + [y] for x in result for y in pool]
	
	
	
		
	cnt = {}
	
	q = []
	for i in result  :
		for ii in i :
			if ii not in cnt:
				cnt[ii] = 0
		
			cnt[ii] += 1
		
		mykeys = list(cnt.keys())
		mykeys.sort()
		cnt = {i:cnt[i] for i in mykeys}
		q.append( cnt )
		cnt = {}
		
		#print(q,"qq")
	return q
	#return result
		
	
		
		


iterables = ['100 A', '10 B',  'C']

one = 10 ** (len(iterables )  - 1  )
print(one)
cn = 0
iterables_let = []
iterables_num = []

for i in  iterables :
	iterables_let.append(i[-1])
	iterables_num.append(int(one)   )
	one/= 10
	cn += 1
#iterables_let = ['A', 'B',  'C']
#iterables_num = [100, 10,  1]

print(iterables_let, iterables_num)


#print(list(product_str(iterables_let, 4)),   len(list(product_str(iterables_let, 4))))






print()
print()







#print(list(product(iterables_num, 4)),   len(list(product(iterables_num, 4))))





q = {}


ccc = 0
for j in list(product_str(iterables_let, 4)) :
	
	if tuple(    [k+str(v) for k, v in j.items()]    ) not in q :
		q[ tuple(    [k+str(v) for k, v in j.items()]    ) ] = 0
		
		
	q[tuple(    [k+str(v) for k, v in j.items()]    ) ] +=    list(product(iterables_num, 4))[ccc][0]
	
	print(j  , list(product(iterables_num, 4))[ccc])
	ccc+=1


print(q,"QQQ" , )


#print( [k+str(v) for k, v in {'A': 1, 'B': 1, 'C': 2}.items()]  )

