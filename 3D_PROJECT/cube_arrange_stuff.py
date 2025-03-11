#!/usr/bin/env python3

print('left < mid_l_r < right  and front < mid_f_ba < back ')

o = [   ['top', ', ','bottom']                                                                ]
oo = [                               [', left',', ','mid_l_r'] , [ ', mid_l_r',', ', 'right'] ]
ooo = [                             [', front',', ','mid_f_ba'],  [', mid_f_ba',', ','back'] ]

s =''

q = []
c = 1
for i in o :
	for j in oo :
		for k in ooo :
			all = i + j + k
			f = 'q.append([' 
			ass = ''
			for a in all :
				f += a
				ass += a
			new_all =  [ all[0]  , all[3]  , all[6]  , all[2] , all[5]  , all[8]   ]
			
			sg = 'if ['
			cv = 0
			for ib in new_all:
				sg += ib
				if cv > 1 and cv<len(new_all)-1 : sg += ', '
				cv += 1
			sg += '] not in intercept :'
			if f in q :
				continue
			if f not in q : q.append(f)
			print(sg)
			print(f, '])', '   ', c)
			c +=1
			
print()
print("######################################################################################################################################################")
print()


print('top < mid_t_bo < bottom   and front < mid_f_ba < back')

o = [                               ['top',', ','mid_t_bo'] , [ 'mid_t_bo',', ','bottom'] ]
oo = [  [', left',', ','right']                                                             ]
ooo = [                             [', front',', ','mid_f_ba'],  [', mid_f_ba',', ','back'] ]

s =''

q = []
c = 1
for i in o :
	for j in oo :
		for k in ooo :
			all = i + j + k
			f = 'q.append([' 
			ass = ''
			for a in all :
				f += a
				ass += a
			new_all =  [ all[0]  , all[3]  , all[6]  , all[2] , all[5]  , all[8]   ]
			
			sg = 'if ['
			cv = 0
			for ib in new_all:
				sg += ib
				if cv > 1 and cv<len(new_all)-1 : sg += ', '
				cv += 1
			sg += '] not in intercept :'
			if f in q :
				continue
			if f not in q : q.append(f)
			print(sg)
			print(f, '])', '   ', c)
			c +=1
			
print()
print("######################################################################################################################################################")
print()


print('top < mid_t_bo < bottom   and left < mid_l_r < right ')


o = [                                 ['top',', ','mid_t_bo'] , [ 'mid_t_bo',', ','bottom'] ]
oo = [                             [', left',', ','mid_l_r'] , [ ', mid_l_r',', ', 'right'] ]
ooo = [ [', front',', ','back']                                                             ]

s =''

q = []
c = 1
for i in o :
	for j in oo :
		for k in ooo :
			all = i + j + k
			f = 'q.append([' 
			ass = ''
			for a in all :
				f += a
				ass += a
			new_all =  [ all[0]  , all[3]  , all[6]  , all[2] , all[5]  , all[8]   ]
			
			sg = 'if ['
			cv = 0
			for ib in new_all:
				sg += ib
				if cv > 1 and cv<len(new_all)-1 : sg += ', '
				cv += 1
			sg += '] not in intercept :'
			if f in q :
				continue
			if f not in q : q.append(f)
			print(sg)
			print(f, '])', '   ', c)
			c +=1
			
			
print()
print("######################################################################################################################################################")
print()


#######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################


print('top < mid_t_bo < bottom ')

o = [                           ['top',', ','mid_t_bo'] , [ 'mid_t_bo',', ','bottom'] ]
oo = [ [', left',', ','right']                                                           ]
ooo = [ [', front',', ','back']                                                         ]

s =''

q = []
c = 1
for i in o :
	for j in oo :
		for k in ooo :
			all = i + j + k
			f = 'q.append([' 
			ass = ''
			for a in all :
				f += a
				ass += a
			new_all =  [ all[0]  , all[3]  , all[6]  , all[2] , all[5]  , all[8]   ]
			
			sg = 'if ['
			cv = 0
			for ib in new_all:
				sg += ib
				if cv > 1 and cv<len(new_all)-1 : sg += ', '
				cv += 1
			sg += '] not in intercept :'
			if f in q :
				continue
			if f not in q : q.append(f)
			print(sg)
			print(f, '])', '   ', c)
			c +=1
			
print()
print("######################################################################################################################################################")
print()


print('left < mid_l_r < right')

o = [    ['top', ', ','bottom']                                                               ]
oo = [                               [', left',', ','mid_l_r'] , [ ', mid_l_r',', ', 'right'] ]
ooo = [   [', front',', ','back']                                                            ]

s =''

q = []
c = 1
for i in o :
	for j in oo :
		for k in ooo :
			all = i + j + k
			f = 'q.append([' 
			ass = ''
			for a in all :
				f += a
				ass += a
			new_all =  [ all[0]  , all[3]  , all[6]  , all[2] , all[5]  , all[8]   ]
			
			sg = 'if ['
			cv = 0
			for ib in new_all:
				sg += ib
				if cv > 1 and cv<len(new_all)-1 : sg += ', '
				cv += 1
			sg += '] not in intercept :'
			if f in q :
				continue
			if f not in q : q.append(f)
			print(sg)
			print(f, '])', '   ', c)
			c +=1
			
			
print()
print("######################################################################################################################################################")
print()

print('front < mid_f_ba < back')


o = [      ['top', ', ','bottom']                                                             ]
oo = [     [', left',', ','right']                                                            ]
ooo = [                                [', front',', ','mid_f_ba'],  [', mid_f_ba',', ','back'] ]

s =''

q = []
c = 1
for i in o :
	for j in oo :
		for k in ooo :
			all = i + j + k
			f = 'q.append([' 
			ass = ''
			for a in all :
				f += a
				ass += a
			new_all =  [ all[0]  , all[3]  , all[6]  , all[2] , all[5]  , all[8]   ]
			
			sg = 'if ['
			cv = 0
			for ib in new_all:
				sg += ib
				if cv > 1 and cv<len(new_all)-1 : sg += ', '
				cv += 1
			sg += '] not in intercept :'
			if f in q :
				continue
			if f not in q : q.append(f)
			print(sg)
			print(f, '])', '   ', c)
			c +=1
			
			
print()
print("######################################################################################################################################################")
print()

# if top < mid_t_bo < bottom   and left < mid_l_r < right  and front < mid_f_ba < back :

print('if top < mid_t_bo < bottom   and left < mid_l_r < right  and front < mid_f_ba < back :')

o = [                       ['top',', ','mid_t_bo'] , [ 'mid_t_bo',', ','bottom'] ]
oo = [                      [', left',', ','mid_l_r'] , [ ', mid_l_r',', ', 'right'] ]
ooo = [                    [', front',', ','mid_f_ba'],  [', mid_f_ba',', ','back'] ]

s =''

q = []
c = 1
for i in o :
	for j in oo :
		for k in ooo :
			all = i + j + k
			f = 'q.append([' 
			ass = ''
			for a in all :
				f += a
				ass += a
			new_all =  [ all[0]  , all[3]  , all[6]  , all[2] , all[5]  , all[8]   ]
			
			sg = 'if ['
			cv = 0
			for ib in new_all:
				sg += ib
				if cv > 1 and cv<len(new_all)-1 : sg += ', '
				cv += 1
			sg += '] not in intercept :'
			if f in q :
				continue
			if f not in q : q.append(f)
			print(sg)
			print(f, '])', '   ', c)
			c +=1
			
			
for i in range(21):
	print('#'*150)
	
	
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
	
print('left < mid_l_r < right  and front < mid_f_ba < back ')

o = [   ['top', ', ','bottom']                                                                ]
oo = [  [', left',', ','right'],     [', left',', ','mid_l_r'] , [ ', mid_l_r',', ', 'right'] ]
ooo = [ [', front',', ','back']  ,   [', front',', ','mid_f_ba'],  [', mid_f_ba',', ','back'] ]

s =''

q = []
c = 1
for i in o :
	for j in oo :
		for k in ooo :
			all = i + j + k
			f = 'q.append([' 
			ass = ''
			for a in all :
				f += a
				ass += a
			new_all =  [ all[0]  , all[3]  , all[6]  , all[2] , all[5]  , all[8]   ]
			
			sg = 'if ['
			cv = 0
			for ib in new_all:
				sg += ib
				if cv > 1 and cv<len(new_all)-1 : sg += ', '
				cv += 1
			sg += '] not in intercept :'
			if f in q :
				continue
			if f not in q : q.append(f)
			print(sg)
			print(f, '])', '   ', c)
			c +=1
			
print()
print("######################################################################################################################################################")
print()


print('top < mid_t_bo < bottom   and front < mid_f_ba < back')

o = [  ['top', ', ','bottom'] ,    ['top',', ','mid_t_bo'] , [ 'mid_t_bo',', ','bottom'] ]
oo = [  [', left',', ','right']                                                             ]
ooo = [[', front',', ','back']  ,   [', front',', ','mid_f_ba'],  [', mid_f_ba',', ','back'] ]

s =''

q = []
c = 1
for i in o :
	for j in oo :
		for k in ooo :
			all = i + j + k
			f = 'q.append([' 
			ass = ''
			for a in all :
				f += a
				ass += a
			new_all =  [ all[0]  , all[3]  , all[6]  , all[2] , all[5]  , all[8]   ]
			
			sg = 'if ['
			cv = 0
			for ib in new_all:
				sg += ib
				if cv > 1 and cv<len(new_all)-1 : sg += ', '
				cv += 1
			sg += '] not in intercept :'
			if f in q :
				continue
			if f not in q : q.append(f)
			print(sg)
			print(f, '])', '   ', c)
			c +=1
			
print()
print("######################################################################################################################################################")
print()


print('top < mid_t_bo < bottom   and left < mid_l_r < right ')


o = [   ['top', ', ','bottom']  ,      ['top',', ','mid_t_bo'] , [ 'mid_t_bo',', ','bottom'] ]
oo = [ [', left',', ','right'] ,  [', left',', ','mid_l_r'] , [ ', mid_l_r',', ', 'right'] ]
ooo = [ [', front',', ','back']                                                             ]

s =''

q = []
c = 1
for i in o :
	for j in oo :
		for k in ooo :
			all = i + j + k
			f = 'q.append([' 
			ass = ''
			for a in all :
				f += a
				ass += a
			new_all =  [ all[0]  , all[3]  , all[6]  , all[2] , all[5]  , all[8]   ]
			
			sg = 'if ['
			cv = 0
			for ib in new_all:
				sg += ib
				if cv > 1 and cv<len(new_all)-1 : sg += ', '
				cv += 1
			sg += '] not in intercept :'
			if f in q :
				continue
			if f not in q : q.append(f)
			print(sg)
			print(f, '])', '   ', c)
			c +=1
			
			
print()
print("######################################################################################################################################################")
print()


#######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################
######################################################################################################################################################


print('top < mid_t_bo < bottom ')

o = [                           ['top',', ','mid_t_bo'] , [ 'mid_t_bo',', ','bottom'] ]
oo = [ [', left',', ','right']                                                           ]
ooo = [ [', front',', ','back']                                                         ]

s =''

q = []
c = 1
for i in o :
	for j in oo :
		for k in ooo :
			all = i + j + k
			f = 'q.append([' 
			ass = ''
			for a in all :
				f += a
				ass += a
			new_all =  [ all[0]  , all[3]  , all[6]  , all[2] , all[5]  , all[8]   ]
			
			sg = 'if ['
			cv = 0
			for ib in new_all:
				sg += ib
				if cv > 1 and cv<len(new_all)-1 : sg += ', '
				cv += 1
			sg += '] not in intercept :'
			if f in q :
				continue
			if f not in q : q.append(f)
			print(sg)
			print(f, '])', '   ', c)
			c +=1
			
print()
print("######################################################################################################################################################")
print()


print('left < mid_l_r < right')

o = [    ['top', ', ','bottom']                                                               ]
oo = [                               [', left',', ','mid_l_r'] , [ ', mid_l_r',', ', 'right'] ]
ooo = [   [', front',', ','back']                                                            ]

s =''

q = []
c = 1
for i in o :
	for j in oo :
		for k in ooo :
			all = i + j + k
			f = 'q.append([' 
			ass = ''
			for a in all :
				f += a
				ass += a
			new_all =  [ all[0]  , all[3]  , all[6]  , all[2] , all[5]  , all[8]   ]
			
			sg = 'if ['
			cv = 0
			for ib in new_all:
				sg += ib
				if cv > 1 and cv<len(new_all)-1 : sg += ', '
				cv += 1
			sg += '] not in intercept :'
			if f in q :
				continue
			if f not in q : q.append(f)
			print(sg)
			print(f, '])', '   ', c)
			c +=1
			
			
print()
print("######################################################################################################################################################")
print()

print('front < mid_f_ba < back')


o = [      ['top', ', ','bottom']                                                             ]
oo = [     [', left',', ','right']                                                            ]
ooo = [                                [', front',', ','mid_f_ba'],  [', mid_f_ba',', ','back'] ]

s =''

q = []
c = 1
for i in o :
	for j in oo :
		for k in ooo :
			all = i + j + k
			f = 'q.append([' 
			ass = ''
			for a in all :
				f += a
				ass += a
			new_all =  [ all[0]  , all[3]  , all[6]  , all[2] , all[5]  , all[8]   ]
			
			sg = 'if ['
			cv = 0
			for ib in new_all:
				sg += ib
				if cv > 1 and cv<len(new_all)-1 : sg += ', '
				cv += 1
			sg += '] not in intercept :'
			if f in q :
				continue
			if f not in q : q.append(f)
			print(sg)
			print(f, '])', '   ', c)
			c +=1
			
			
print()
print("######################################################################################################################################################")
print()


		
print('if top < mid_t_bo < bottom   and left < mid_l_r < right  and front < mid_f_ba < back :')

o = [   ['top', ', ','bottom']  ,     ['top',', ','mid_t_bo'] , [ 'mid_t_bo',', ','bottom']   ]
oo = [  [', left',', ','right'],     [', left',', ','mid_l_r'] , [ ', mid_l_r',', ', 'right'] ]
ooo = [ [', front',', ','back']  ,   [', front',', ','mid_f_ba'],  [', mid_f_ba',', ','back'] ]

s =''

q = []
c = 1
for i in o :
	for j in oo :
		for k in ooo :
			all = i + j + k
			f = 'q.append([' 
			ass = ''
			for a in all :
				f += a
				ass += a
			new_all =  [ all[0]  , all[3]  , all[6]  , all[2] , all[5]  , all[8]   ]
			
			sg = 'if ['
			cv = 0
			for ib in new_all:
				sg += ib
				if cv > 1 and cv<len(new_all)-1 : sg += ', '
				cv += 1
			sg += '] not in intercept :'
			if f in q :
				continue
			if f not in q : q.append(f)
			print(sg)
			print(f, '])', '   ', c)
			c +=1
			