#!/usr/bin/env python3

def t(n, amou):
	
	def fn(numb):
		an = []
		num = numb
		for i in range((num//2)+1):
			if num >= i : 
				#print(i, num)
				an.append([i, num])
				#an.append([num,  i ])#####
			num -=1
			
		#print(an[1:])
		
		return an[1:]
		
	
	ss = []
	for i in range(n+1):
		#print(i)
		ss.append(i)
	
	rest = [0]*(amou-1)
	arr = rest + [n] #[n] + rest
	seq = 0
	#arr = [n] + rest ################
	
	#mp = {ind : arr[ind] for ind in range(len(arr)) if arr[ind] == 0}
	mp = {ind : arr[ind] for ind in range(len(arr)-1) if arr[ind] == 0}
	q = [   [arr, mp, {amou-1:arr[-1]}, len(arr)-1]   ] 
	#print(q, "<<<<", amou - 2)
	
	#del mp['b']
	
	# sum , same X
	# set [5,0,0,0] = [5,0] X
	# sorted !!!!
	
	#fn(5)
	VIS = [arr]
	ans = [arr]
	
	import copy
	
	while q :
		arrr , zeros , not_zeros , zero_len = q.pop(0)
		
		arr_C = arrr
		
		#if sorted(arr) not in ans : ans.append( sorted(arr) )
		
		
		for k,v in not_zeros.items(): 
			if v > 1 and zeros != {} :
				li_ = fn(v) # 5
				
				for li in li_ :
					arrr_tem = arr_C.copy()
					temp_not_zeros =  not_zeros.copy()
					temp_zeros     =   zeros.copy()  # copy.deepcopy(zeros)  # dict(zeros )
					
					smallnum  , bignum  = li
					lij = [   bignum, smallnum]
					lij = [   smallnum , bignum]####
						
					cn = 0
					mmpp = list( temp_zeros.items() ) 
					
					
					
					new_not_0 = {}
					while cn < 1 and mmpp != []:
						# 0))1 
						kk , vv =  mmpp.pop()
						new_val = lij.pop()  # small number >>> next>>>> bug number
						arrr_tem[kk] = new_val
						del temp_zeros[kk] 
						#temp_zeros.pop(kk)
						
						
						new_not_0[kk] = new_val
					
						cn+= 1
						
					new_val_ = lij.pop()
					arrr_tem[k] = 	new_val_
					temp_not_zeros[k] = new_val_
					#new_not_0 = temp_not_zeros |  new_not_0
					
					
					
					if cn == 1 :
						#new_not_0           # <<<  DDDDDDDOOOOOO
						new_0 = temp_zeros  # <<<
						new_not_0.update(temp_not_zeros)
						#temp_not_zeros | new_not_0
					
						
						
						#if sorted(arrr_tem) not in ans    :
						#if new_0 != {}    :
						#print("???????", arrr_tem , new_0 , new_not_0 , zero_len)
						
						if sorted(arrr_tem) not in  ans  : 
							ans.append(sorted(arrr_tem))
							if new_0 != {}    : q.append([arrr_tem , new_0 , new_not_0 , zero_len - 1 ])
						
		
	#print(VIS,"<><>")
	print()
	print(ans, len(ans))
	
n = 30
amou = 10#50
t(n, amou)

print()
t(4, 4)
