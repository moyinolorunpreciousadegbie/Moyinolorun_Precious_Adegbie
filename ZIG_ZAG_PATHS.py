def my_abs(number):
	if number < 0:
		return -number
	else:
		return number
	
	
	
def zigzag(l):
	
	X = len(l[0])
	Y = len(l)
	
	
	for y in range(Y):
		maintop = l[y]
		revtop = maintop[::-1]
		
		maindown = l[Y-1-y]
		revdown = maindown[::-1]
		for x in range(X):
			
			print(maintop[x])
			

l = [[1,2,3,4,5],
	 [6,7,8,9,10],
	 [11,12,13,14,15],
	 [16,17,18,19,20],
	 [21,22,23,24,25],
	 [26,27,28,29,30],#
	 [31,32,33,34,35],#
	 [36,37,38,39,40]#
     ]		


X = len(l[0])
Y = len(l)


_1 = 1
for y in range(Y):
	maintop = l[y][::_1]
	print(maintop)
	
	_1 *= -1
print("1")

print()

_1 = -1
for y in range(Y):
	maintop = l[y][::_1]
	print(maintop)
	
	_1 *= -1
print("2")

print()
print()
	
_1 = 1
for y in range(Y):
	maindown = l[Y-1-y][::_1]
	print(maindown)
	
	_1 *= -1
print("3")	

print()

_1 = -1
for y in range(Y):
	maindown = l[Y-1-y][::_1]
	print(maindown)
	
	_1 *= -1
print("4")	

cou = 0

CC = 0
CCC = 0




one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirtheen,fourtheen,fiftheen,sixtheen =[],[],[],[] ,[],[],[],[]   ,[],[],[],[]   ,[],[],[],[]

se = set()
final = 0
_1m = -1
_1p = 1
for y in range(Y):
	maintop = l[y][::_1p]
	maintop_ = l[y][::_1m]
	
	maindown = l[Y-1-y][::_1p]
	maindown_ = l[Y-1-y][::_1m]
	#_1m *= -1
	#_1p *= -1
	
	jjtop = l[y]
	jjdown = l[Y-1-y]
	
	jjtop_ = l[y][::-1]
	jjdown_ = l[Y-1-y][::-1]
	
	xr= X
	for x in range(X): # set X to be max range
		xr -= (x)
	# PUT y results together do for  1, normal then change to the other 3
	# GET THE Y axis and X axis together
		T =  (cou) // X # <<<<<<<
		
		T =  (cou) // Y # NEW
		
		swch = (T % 2) # <<<<
		gh = ((X-1)*swch) # <<<<
		
		gh = ((Y-1)*swch) # NEW
		yy = cou%Y # NEW
		
		_1,_11 = x,my_abs(gh-x) # <<<<
		_2,_22 = X-1-x , my_abs(X-gh-x-1 )  # <<<<
		
		
		_1,_11 = yy,my_abs(gh-yy) # NEW
		_2,_22 = Y-1-yy , my_abs(Y-gh-yy-1 )  # NEW
		
	
		#print(T,x,my_abs(gh-x) ,'         ',X-1-T , X-1-x , my_abs(X-gh-x-1 ) ,'       '   )
		
		#print(T,_11,"           ",T,_22,"          ||          ",X-1-T,_11,"        ",X-1-T,_22)#<<<<<<<<
		ghy = ((X*Y)-cou-1)//Y 
		#print(T,_11,"           ",T,_22,"          ||          ",Y-3-T,_11,"        ",Y-3-T,_22,'            ',    )
		
		
		#print(T,_11,"           ",T,_22,"          ||          ",ghy,_11,"        ",ghy,_22,'            ',    ) #<<<
		#print(T,yy,"          ||          ",ghy,yy   ) #<<<
		#print(T,Y-1-yy,"          ||          ",ghy,Y-1-yy   ) #<<<
		#print(T,yy,'     ',T,Y-1-yy,"          ||          ",ghy,yy,'        ' ,ghy,Y-1-yy    ) #<<<<<<<
		
		
		xc1  , yc1 , xc2  , yc2 = T,_11 , T,_22
		xc1_  , yc1_ , xc2_  , yc2_ = ghy,_11 , ghy,_22
		
		
		#print(yc1,xc1,'   ',yc2,xc2,"  |  ",yc1_,xc1_,'   ',yc2_,xc2_)
		
		
		#print()
		
		
		xv , yv = T , yy
		xv_ , yv_ = ghy , yy
		se.add( l[yv ][ xv] )
		se.add( l[yv_ ][ xv_] )
		
		_xv , _yv = T , Y-1-yy
		_xv_ , _yv_ = ghy , Y-1-yy
		se.add( l[_yv ][ _xv] )
		se.add( l[_yv_ ][ _xv_] )
		
		
		#print(yv,xv,'   ',yv_,xv_,"  |  ",_yv,_xv,'   ',_yv_,_xv_)
		
		
		#print(yc1,xc1,'   ',yc2,xc2,"  |  ",yc1_,xc1_,'   ',yc2_,xc2_,"|||||",yv,xv,'   ',yv_,xv_,"  |  ",_yv,_xv,'   ',_yv_,_xv_) # all
		
		se.add(jjtop[x])
		se.add(jjdown[x])
		
		se.add(jjtop_[x])
		se.add(jjdown_[x])
		
		
		
		#print(   l[yc1 ][ xc1] , '       ',  l[yc2][ xc2] ,'        ||         ' , l[yc1_ ][ xc1_] , '       ', l[yc2_][ xc2_] ,"||",maintop[x],"|",maintop_[x],"|",maindown[x],"|",maindown_[x],"|",'      ', l[yv ][ xv],"|",l[yv_ ][ xv_],"|",l[_yv ][ _xv],"|",l[_yv_ ][ _xv_],"|",jjtop[x],"|",jjdown[x],"|",jjtop_[x],"|",jjdown_[x]   )
		
		#top = l[y]
		#down = l[Y-1-y]
		
		print(   l[yc1 ][ xc1] , '       ',  l[yc2][ xc2] ,'        ||         ' , l[yc1_ ][ xc1_] , '       ', l[yc2_][ xc2_] ,"||",l[y][::_1p][x],"|",l[y][::_1m][x],"|",l[Y-1-y][::_1p][x],"|",l[Y-1-y][::_1m][x],"|",'      ', l[yv ][ xv],"|",l[yv_ ][ xv_],"|",l[_yv ][ _xv],"|",l[_yv_ ][ _xv_],"|",l[y][x],"|",l[Y-1-y][x],"|",l[y][X-1-x],"|", l[Y-1-y][X-1-x]   )
		
		
		one.append(l[yc1 ][ xc1] )  
		two.append(l[yc2][ xc2] ) 
		three.append(l[yc1_ ][ xc1_] ) 
		four.append(l[yc2_][ xc2_] )
		five.append(l[y][::_1p][x])
		six.append(l[y][::_1m][x])
		seven.append(l[Y-1-y][::_1p][x])
		eight.append(l[Y-1-y][::_1m][x]) 
		nine.append(l[yv ][ xv])
		ten.append(l[yv_ ][ xv_])
		eleven.append(l[_yv ][ _xv])
		twelve.append(l[_yv_ ][ _xv_])
		thirtheen.append(l[y][x])
		fourtheen.append(l[Y-1-y][x])
		fiftheen.append(l[y][X-1-x]) 
		sixtheen.append(l[Y-1-y][X-1-x]   )
		
		# l[y][X-1-x],"|",l[Y-1-y][X-1-x] 
		#maintop = l[y][::_1p]              l[y][::_1p][x]
		#maintop_ = l[y][::_1m]             l[y][::_1m][x]
	
		#maindown = l[Y-1-y][::_1p]        l[Y-1-y][::_1p][x]
		#maindown_ = l[Y-1-y][::_1m]       l[Y-1-y][::_1m][x]
		#_1m *= -1
		#_1p *= -1
	
		#jjtop = l[y]                 l[y][x]
		#jjdown = l[Y-1-y]            l[Y-1-y][x] 
	
		#jjtop_ = l[y][::-1]          l[y][X-1-x]
		#jjdown_ = l[Y-1-y][::-1]     l[Y-1-y][X-1-x] 
		
		
		se.add( l[yc1 ][ xc1] )  
		se.add( l[yc2][ xc2] )
		se.add( l[yc1_ ][ xc1_] )
		se.add( l[yc2_][ xc2_] )
		
		
		se.add( maintop[x])  
		se.add( maintop_[x] )
		se.add( maindown[x] )
		se.add( maindown_[x] )
		
		
		if len(se) == X * Y and final == 0 :
			print("DONE", cou, X*Y)
			final += 1
		
		cou +=1
		
	_1m *= -1
	_1p *= -1
	
	
	
check_unique = [one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirtheen,fourtheen,fiftheen,sixtheen]

check_u = set(tuple(sublist) for sublist in check_unique)

print(len(check_unique), len(check_u) )
"""

XP , YP

RANGE_X    ,    RANGE_Y



XP - RANGE_X  , YP - RANGE_Y

XP   , YP - RANGE_Y

XP - RANGE_X  , YP 


MAT[YP:][XP:]

MAT[YP - RANGE_Y:][XP:]

MAT[YP:][XP - RANGE_X:]

MAT[YP - RANGE_Y:][XP - RANGE_X:]



for y in range(0,Y):
for x in range(0,X):

for y in range(YP,Y+YP):
for x in range(XP,X+XP):

for y in range(YP-Y,YP):
for x in range(XP,X+XP):


for y in range(YP,Y+YP):
for x in range(XP-X,XP):


for y in range(YP-Y,YP):
for x in range(XP-X,XP):


my = YP-Y + (y)
mx = XP-X + (x)

my = (y)-Y
mx = (x)-X

y, x <<< NORMAL  DO 
y, mx
my, x
my, mx




"""