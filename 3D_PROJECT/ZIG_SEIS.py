def my_abs(number):
	if number < 0:
		return -number
	else:
		return number
	
mxx = -float('inf')
mnn = float('inf')

def z_check(l_ZLi,z_point,ZZ_RAD,Zmax, se, MP,R,C, ____18 , FIL_MAT , lis_MAT ):
	if (R,C) in se : return
	
	# AREA HAS NOT BEEN VISITED
	#FIL_MAT[R,C] = 0
	
	if (R,C) not in lis_MAT : 
		lis_MAT[(R,C)] = []
		
	for zz in  range(ZZ_RAD):
		if 0<= z_point + zz < Zmax and (l_ZLi[z_point + zz,  R,C] < -____18 ):# len(seismic_data) closer
			if  FIL_MAT[R,C] == None : 
				FIL_MAT[R,C] = -float('inf')
			FIL_MAT[R,C] = max( FIL_MAT[R,C],  z_point + zz   )
			lis_MAT[(R,C)] .append(z_point + zz)
		if 0<= z_point - zz < Zmax  and (l_ZLi[z_point - zz,  R,C] < -____18 ):# len(seismic_data) closer
			if  FIL_MAT[R,C] == None : 
				FIL_MAT[R,C] = -float('inf')
			FIL_MAT[R,C] = max( FIL_MAT[R,C],  z_point - zz )
			lis_MAT[(R,C)] .append( z_point - zz )
		if 0<= z_point + ZZ_RAD - zz < Zmax and ( l_ZLi[z_point + ZZ_RAD - zz,  R,C]  < -____18 ):# len(seismic_data)
			if  FIL_MAT[R,C] == None : 
				FIL_MAT[R,C] = -float('inf')
			FIL_MAT[R,C] = max( FIL_MAT[R,C], z_point + ZZ_RAD - zz )
			lis_MAT[(R,C)] .append( z_point + ZZ_RAD - zz )
		if 0<= z_point - ZZ_RAD + zz < Zmax and ( l_ZLi[z_point - ZZ_RAD + zz,  R,C] < -____18 ):# len(seismic_data)
			if  FIL_MAT[R,C] == None : 
				FIL_MAT[R,C] = -float('inf')
			FIL_MAT[R,C] = max( FIL_MAT[R,C] ,  z_point - ZZ_RAD + zz )
			lis_MAT[(R,C)] .append(z_point - ZZ_RAD + zz )
														#zpoint(0)                         V       #rad(6),zpoint(6)-rad(6)= 0         
														#0                                 #       #0                                        V
		if z_point + ZZ_RAD - zz   <= z_point + zz  :   #1                                 #       #1                                        #
			break                                       #2      z_point + ZZ_RAD - zz      #       #2           z_point - zz                 #
														#3      #                z_point + zz      #3           #        z_point - ZZ_RAD + zz  
		if z_point - ZZ_RAD + zz  >= z_point - zz  :    #4      #                                  #4			#
			break                                       #5      #                                  #5			#
														#6      ^                                  #6 			^
														# rad(6),zpoint(0)+rad(6)= 6               #zpoint(6)  
def z_check_(l_ZLi,z_point,ZZ_RAD,Zmax, se, MP,R,C, ____18 , FIL_MAT , lis_MAT ):
	if (R,C) in se : return
	if (R,C) not in lis_MAT : 
		lis_MAT[(R,C)] = []
		
		
	
	for zz in  range(ZZ_RAD):
		if 0<= z_point + zz < Zmax and ( ____18 < l_ZLi[z_point + zz,  R,C] ):# len(seismic_data) closer
			if  FIL_MAT[R,C] == None : 
				FIL_MAT[R,C] = float('inf')
			FIL_MAT[R,C] = min( FIL_MAT[R,C],  z_point + zz   )
			lis_MAT[(R,C)] .append(z_point + zz)
		if 0<= z_point - zz < Zmax  and (____18 < l_ZLi[z_point - zz,  R,C] ):# len(seismic_data) closer
			if  FIL_MAT[R,C] == None : 
				FIL_MAT[R,C] = float('inf')
			FIL_MAT[R,C] = min( FIL_MAT[R,C],  z_point - zz )
			lis_MAT[(R,C)] .append( z_point - zz )
		if 0<= z_point + ZZ_RAD - zz < Zmax and ( ____18 < l_ZLi[z_point + ZZ_RAD - zz,  R,C] ):# len(seismic_data)
			if  FIL_MAT[R,C] == None : 
				FIL_MAT[R,C] = float('inf')
			FIL_MAT[R,C] = min( FIL_MAT[R,C], z_point + ZZ_RAD - zz )
			lis_MAT[(R,C)] .append( z_point + ZZ_RAD - zz )
		if 0<= z_point - ZZ_RAD + zz < Zmax and ( ____18 < l_ZLi[z_point - ZZ_RAD + zz,  R,C]):# len(seismic_data)
			if  FIL_MAT[R,C] == None : 
				FIL_MAT[R,C] = float('inf')
			FIL_MAT[R,C] = min( FIL_MAT[R,C] ,  z_point - ZZ_RAD + zz )
			lis_MAT[(R,C)] .append(z_point - ZZ_RAD + zz )
														#zpoint(0)                         V       #rad(6),zpoint(6)-rad(6)= 0         
														#0                                 #       #0                                        V
		if z_point + ZZ_RAD - zz   <= z_point + zz  :   #1                                 #       #1                                        #
			break                                       #2      z_point + ZZ_RAD - zz      #       #2           z_point - zz                 #
														#3      #                z_point + zz      #3           #        z_point - ZZ_RAD + zz  
		if z_point - ZZ_RAD + zz  >= z_point - zz  :    #4      #                                  #4			#
			break                                       #5      #                                  #5			#
														#6      ^                                  #6 			^
														# rad(6),zpoint(0)+rad(6)= 6               #zpoint(6)  


	

#seismic_data = data_display[:,:,:]# Z layer    
seismic_data = data_display             ####<<<<<<<<<<<<<<<<<<<<
	
	
Zmax = len(seismic_data)                ####<<<<<<<<<<<<<<<<<<<<

l = seismic_data						 ####<<<<<<<<<<<<<<<<<<<<
	
RRR_ = len(seismic_data[0]) # 750       ####<<<<<<<<<<<<<<<<<<<<
CCC_ = len(seismic_data[0][0]) # 750    ####<<<<<<<<<<<<<<<<<<<<
X_, Y_,  Z_ = 334, 344, 678 # 525 
X__, Y__,  Z__ = X_, Y_,  Z_

ZZ_RAD = 56 # 46 # 36
____18 = 4 # 3

z_point = Z_

#FIL_MAT = np.zeros(( RRR_ ,  CCC_ ))    
FIL_MAT = np.full(   ( RRR_ ,  CCC_ )   , None)   ####<<<<<<<<<<<<<<<<<<<<


X = CCC_ # len(l[0]) # NORMAL MATRIX
Y = RRR_ # len(l)    # NORMAL MATRIX



cou = 0

CC = 0
CCC = 0




one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirtheen,fourtheen,fiftheen,sixtheen =[],[],[],[] ,[],[],[],[]   ,[],[],[],[]   ,[],[],[],[]

#one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirtheen,fourtheen,fiftheen,sixtheen =set(),set(),set(),set(),    set(),set(),set(),set()   ,set(),set(),set(),set()   ,set(),set(),set(),set()
centerquad1, centerquad2, centerquad3, centerquad4 = [],[],[],[]

stp = 1

X_ = (X // stp )
Y_ = (Y // stp )

se =  set()
final = 0
_1m = -1
_1p = 1
lis_MAT  = {}
MP = {}
for y in range(0,Y,stp):
	#if len(se) == X * Y and final != 0 : 
		#break
	if len(se) >= X_ * Y_ and final != 0 : 
		break
	
	#_1m *= -1
	#_1p *= -1
	
	
	
	xr= X
	for x in range(0,X,stp): # set X to be max range
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
		
	
		_xv , _yv = T , Y-1-yy
		_xv_ , _yv_ = ghy , Y-1-yy
		
		
		
		
		if _1p == 1 :
			_1px = x
			
		if _1m == 1 :
			_1mx = x
			
		if _1p == -1 :
			_1px = X-1-x
			
		if _1m == -1 :
			_1mx = X-1-x
		
		
		
		
		one.append((yc1 , xc1) )  
		z_check(l,z_point,ZZ_RAD, Zmax , se, MP, yc1 , xc1, ____18, FIL_MAT, lis_MAT )
		two.append((yc2, xc2) ) 
		z_check(l,z_point,ZZ_RAD, Zmax , se, MP, yc2, xc2, ____18, FIL_MAT, lis_MAT )
		three.append((yc1_ , xc1_) ) 
		z_check(l,z_point,ZZ_RAD, Zmax , se, MP, yc1_ , xc1_, ____18, FIL_MAT, lis_MAT )
		four.append((yc2_, xc2_) )
		z_check(l,z_point,ZZ_RAD, Zmax , se, MP, yc2_, xc2_, ____18, FIL_MAT, lis_MAT )
		#five.append(l[y][::_1p][x])       ########
		#six.append(l[y][::_1m][x])        ########
		#seven.append(l[Y-1-y][::_1p][x])  ########
		#eight.append(l[Y-1-y][::_1m][x])  ########
		five.append((y,_1px ))
		z_check(l,z_point,ZZ_RAD, Zmax , se, MP, y,_1px , ____18, FIL_MAT, lis_MAT )
		six.append((y, _1mx ))
		z_check(l,z_point,ZZ_RAD, Zmax , se, MP, y, _1mx , ____18, FIL_MAT, lis_MAT )
		seven.append((Y-1-y, _1px))
		z_check(l,z_point,ZZ_RAD, Zmax , se, MP, Y-1-y, _1px, ____18, FIL_MAT, lis_MAT )
		eight.append((Y-1-y, _1mx ))
		z_check(l,z_point,ZZ_RAD, Zmax , se, MP, Y-1-y, _1mx , ____18, FIL_MAT, lis_MAT )
	
	
		nine.append((yv , xv))
		z_check(l,z_point,ZZ_RAD, Zmax , se, MP, yv , xv, ____18, FIL_MAT, lis_MAT )
		ten.append((yv_ , xv_))
		z_check(l,z_point,ZZ_RAD, Zmax , se, MP, yv_ , xv_, ____18, FIL_MAT, lis_MAT )
		eleven.append((_yv , _xv))
		z_check(l,z_point,ZZ_RAD, Zmax , se, MP, _yv , _xv, ____18, FIL_MAT, lis_MAT )
		twelve.append((_yv_ , _xv_))
		z_check(l,z_point,ZZ_RAD, Zmax , se, MP, _yv_ , _xv_, ____18, FIL_MAT, lis_MAT )
		thirtheen.append((y,x))
		z_check(l,z_point,ZZ_RAD, Zmax , se, MP, y,x, ____18, FIL_MAT, lis_MAT )
		fourtheen.append((Y-1-y,x))
		z_check(l,z_point,ZZ_RAD, Zmax , se, MP, Y-1-y,x, ____18, FIL_MAT, lis_MAT )
		fiftheen.append((y,X-1-x)) 
		z_check(l,z_point,ZZ_RAD, Zmax , se, MP, y,X-1-x, ____18, FIL_MAT, lis_MAT )
		sixtheen.append((Y-1-y,X-1-x)   )
		z_check(l,z_point,ZZ_RAD, Zmax , se, MP, Y-1-y,X-1-x, ____18, FIL_MAT, lis_MAT )
	
	
	
		if 0 <= (Y//2)+y < Y and  0<= (X//2)+x  < X :
			se.add(l[(Y//2)+y][(X//2)+x])
			centerquad1.append(l[(Y//2)+y][(X//2)+x])
			z_check(l,z_point,ZZ_RAD, Zmax , se, MP, (Y//2)+y,(X//2)+x, ____18, FIL_MAT, lis_MAT )
		if 0 <= (Y//2)+y < Y and  0<= (X//2)-x  < X :
			se.add(l[(Y//2)+y][(X//2)-x])
			centerquad2.append(l[(Y//2)+y][(X//2)-x])
			z_check(l,z_point,ZZ_RAD, Zmax , se, MP, (Y//2)+y,(X//2)-x, ____18, FIL_MAT, lis_MAT )
			
		if 0 <= (Y//2)-y < Y and  0<= (X//2)+x  < X :
			se.add(l[(Y//2)-y][(X//2)+x])
			centerquad3.append(l[(Y//2)-y][(X//2)+x])
			z_check(l,z_point,ZZ_RAD, Zmax , se, MP, (Y//2)-y,(X//2)+x, ____18, FIL_MAT, lis_MAT )
		if 0 <= (Y//2)-y < Y and  0<= (X//2)-x  < X :
			se.add(l[(Y//2)-y][(X//2)-x])
			centerquad4.append(l[(Y//2)-y][(X//2)-x])
			z_check(l,z_point,ZZ_RAD, Zmax , se, MP, (Y//2)-y,(X//2)-x, ____18, FIL_MAT, lis_MAT )
	
		#ZZ_ZZ 
	
		#z_check(l,z_point,ZZ_RAD, Zmax , se, MP, )
		#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		
		#xv , yv = T , yy
		#xv_ , yv_ = ghy , yy
		se.add( (yv , xv )   )
		se.add( (yv_ , xv_ )   )
		
		#_xv , _yv = T , Y-1-yy
		#_xv_ , _yv_ = ghy , Y-1-yy
		se.add( (_yv , _xv )      )
		se.add( (_yv_ , _xv_ )   )
		
		
		#print(yv,xv,'   ',yv_,xv_,"  |  ",_yv,_xv,'   ',_yv_,_xv_)
		
		
		#print(yc1,xc1,'   ',yc2,xc2,"  |  ",yc1_,xc1_,'   ',yc2_,xc2_,"|||||",yv,xv,'   ',yv_,xv_,"  |  ",_yv,_xv,'   ',_yv_,_xv_) # all
		
		
		
		#jjtop = l[y]
		#jjdown = l[Y-1-y]
	
		#jjtop_ = l[y][::-1]
		#jjdown_ = l[Y-1-y][::-1]
		
		se.add((y,x)   )
		se.add((Y-1-y,x)    )
		
		se.add((y,X-1-x) )
		se.add((Y-1-y,X-1-x) )
		
		
		
		#print(   l[yc1 ][ xc1] , '       ',  l[yc2][ xc2] ,'        ||         ' , l[yc1_ ][ xc1_] , '       ', l[yc2_][ xc2_] ,"||",maintop[x],"|",maintop_[x],"|",maindown[x],"|",maindown_[x],"|",'      ', l[yv ][ xv],"|",l[yv_ ][ xv_],"|",l[_yv ][ _xv],"|",l[_yv_ ][ _xv_],"|",jjtop[x],"|",jjdown[x],"|",jjtop_[x],"|",jjdown_[x]   )
		
		#top = l[y]
		#down = l[Y-1-y]
		
		#print(   l[yc1 ][ xc1] , '       ',  l[yc2][ xc2] ,'        ||         ' , l[yc1_ ][ xc1_] , '       ', l[yc2_][ xc2_] ,"||",l[y][::_1p][x],"|",l[y][::_1m][x],"|",l[Y-1-y][::_1p][x],"|",l[Y-1-y][::_1m][x],"|",'      ', l[yv ][ xv],"|",l[yv_ ][ xv_],"|",l[_yv ][ _xv],"|",l[_yv_ ][ _xv_],"|",l[y][x],"|",l[Y-1-y][x],"|",l[y][X-1-x],"|", l[Y-1-y][X-1-x]   )
		
		
	
			
		#one.append(l[yc1 ][ xc1] )  
		#two.append(l[yc2][ xc2] ) 
		#three.append(l[yc1_ ][ xc1_] ) 
		#four.append(l[yc2_][ xc2_] )
		#five.append(l[y][::_1p][x])       ########
		#six.append(l[y][::_1m][x])        ########
		#seven.append(l[Y-1-y][::_1p][x])  ########
		#eight.append(l[Y-1-y][::_1m][x])  ########
		#five.append(l[y][_1px ])
		#six.append(l[y][ _1mx ])
		#seven.append(l[Y-1-y][ _1px])
		#eight.append(l[Y-1-y][ _1mx ])
		
		
		#nine.append(l[yv ][ xv])
		#ten.append(l[yv_ ][ xv_])
		#eleven.append(l[_yv ][ _xv])
		#twelve.append(l[_yv_ ][ _xv_])
		#thirtheen.append(l[y][x])
		#fourtheen.append(l[Y-1-y][x])
		#fiftheen.append(l[y][X-1-x]) 
		#sixtheen.append(l[Y-1-y][X-1-x]   )
		
		#################################
		
		
		
		
		####################################################
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
		####################################################
		
		
		se.add( ( yc1 , xc1 )  )  
		se.add( ( yc2, xc2 )  )
		se.add( ( yc1_ , xc1_)  )
		se.add( ( yc2_, xc2_ )  )
		
		
		#se.add( maintop[x])  
		#se.add( maintop_[x] )
		#se.add( maindown[x] )
		#se.add( maindown_[x] )
		se.add( (y,_1px )  )
		se.add( (y, _1mx )  )
		se.add( (Y-1-y, _1px)  )
		se.add( (Y-1-y, _1mx )  )
		
		
		#if len(se) == X * Y and final == 0 :
			#print("DONE", cou, X*Y,"|||",RRR_*CCC_,len(three))
			#final += 1
			#break
		if len(se) >= X_ * Y_ and final == 0 : 
			print("DONE", cou, X_*Y_,"|||",RRR_*CCC_,len(three),"|||", (X_*Y_)/cou)
			final += 1
			break
		
		cou +=1
	
	#if len(se) == X * Y and final != 0 : 
		#break	
	
	if len(se) >= X_ * Y_ and final != 0 : 
		break
	_1m *= -1
	_1p *= -1
	
	
print(len(one),len(two),len(three),len(four),len(five),len(six),len(seven),len(eight),len(nine),len(ten),len(eleven),len(twelve),len(thirtheen),len(fourtheen),len(fiftheen),len(sixtheen) )
check_unique = [one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirtheen,fourtheen,fiftheen,sixtheen]



check_u = set( tuple(sublist) for sublist in check_unique)

print(len(check_unique), len(check_u) )
#print(len(one),len(two))

ch222 = [len(centerquad1),len(centerquad2),len(centerquad3),len(centerquad4)]
print("QUAD", ch222)


fug = go.Surface( z= FIL_MAT ,colorscale=[[0, "green"], [1, "green"   ]]   )


FIG= go.Figure()

###############################################################################################################################################################


X = len(seismic_data[0][0]) # 170,750   INLINE
Y = len(seismic_data[0]) # 170,750    CROSSLINE
Z = len(seismic_data)

x2 = len(seismic_data[0][0]) -1 # 170,750
y2 = len(seismic_data[0]) -1 # 170,750
z2 = len(seismic_data) -1
inline  = X__#300 # 250

crossline = Y__#250# 600

twt_z = Z__ + 150 #500
_001 = 0.00001

_000001 = 1 # 0.001
																	#                            Y
#####m1 = [ [ (i * _000001) for i in range(Z)] for y in range( Y) ]
y1_ = [0,Y]
x1_ = [ inline , inline + _001 ]
col1 = seismic_data[:,:,inline].T#.tolist()


y2_ = [crossline , crossline + _001 ]
x2_ = [0,X]
col2 = seismic_data[:,crossline,:]#.tolist()


y1_ = []
x1_ = []

y2_ = []
x2_ = []

pllll = []
ZID = []
for i in range(Z):
	y1_.append(i)#[0,Y]
	x1_.append( (i*_001) + inline )
#x1_ = [(i*_001) + inline for i in range( Z)]#[ inline , inline + _001 ]   Z>Y
	y2_.append( (i*_001) + crossline  )
	x2_.append(i)#[0,Y]
	
	pllll.append((i * _000001))
	
	ZID.append(i)
	
x1_ = np.array(x1_ )
y1_ = np.array(y1_ )
#m1 = np.array(m1 )

x2_ = np.array(x2_ )
y2_ = np.array(y2_ )
#m2 = np.array(m2 )

#plane = go.Surface(x= x1_ , y=y1_, z= m1, surfacecolor=col1  , colorscale= 'Picnic', opacity=1) #<<<<
#plane2 = go.Surface(x= x2_ , y=y2_, z= m2, surfacecolor=col2  , colorscale= 'Picnic', opacity=1) #<<<<

#twt_z
col3 = seismic_data[twt_z,:,:]
vj =  ( (_000001 * Z) / Z ) * twt_z
#####m3 = [ [vj ] * X for _ in range(Y) ]


																	#                            Y
#####m1 = [ [ (i * _000001) for i in range(Z)] for y in range( Y) ]
#                                          X
#####m2 = [ [ (i * _000001) for x in range(X)]  for i in range(Z) ]

mc = max([X,Y,Z])
m1 = []
m2 = []
m3 = []

Y_r = []
X_r = []
for i in range(mc):
	if i < Y : # m1 and m3
			_ =  pllll
			m1.append(_)
	
			__ = [vj ] * X
			m3.append( __ )
	if i < Z :
			_ii = [ (i * _000001)] * X
			m2.append(_ii)
		
	if i < X :
		X_r.append(i)
	if i < Y :
		Y_r.append(i)
		
		
m1 = np.array(m1 )
m2 = np.array(m2 )

m3 = np.array(m3 )

_None = None

col1_ = col1.copy()
col2_ = col2.copy()
col3_ = col3.copy()

col1_[col1_ == _None] = 0
col2_[col2_ == _None] = 0
col3_[col3_ == _None] = 0


plane = go.Surface(x= x1_ , y=y1_, z= m1, surfacecolor=col1  , text =  col1 , colorscale= 'Picnic', opacity=1) #<<<<
plane2 = go.Surface(x= x2_ , y=y2_, z= m2, surfacecolor=col2  , text = col2 ,colorscale= 'Picnic', opacity=1) #<<<<

plane3 = go.Surface(x= x2_ , y=y1_, z= m3, surfacecolor=col3  , text = col3 ,colorscale= 'Picnic', opacity=1) #<<<<

#print([len(col1),len( col1[0] )],[len(m1),len( m1[0] )])
#print([len(col2),len( col2[0] )],[len(m2),len( m2[0] )])

#minii = np.max( W.matrix )

#W.matrix[W.matrix == 0] = minii
#W.matrix = np.where(W.matrix == 0, minii, W.matrix)
single_color = 'green' # A shade of blue

# Create a custom colorscale with the single color
# The format is [[normalized_value, 'color_string'], ...]
# For a single color, both 0 and 1 map to the same color.
#one_color = [[np.min( W.matrix2 ), single_color], [np.max( W.matrix2 ), single_color]]# 'Earth' 0.3
#one_color = [[0, "white"], [1/10**9, single_color], [1, single_color]]# 'Earth' 0.3


#plane4 = go.Surface(x= x2_ , y=y1_, z= W.matrix , surfacecolor=  W.matrix2,  text = W.matrix2,  colorscale= one_color, opacity=0.6) #<<<< MAIN
#plane4 = go.Surface(x= X_r , y=Y_r, z= W.matrix , surfacecolor=  W.matrix2  , colorscale= 'Picnic', opacity=1) #<<<<

# 334, 344, ++ +- -+ -- 5
minus = 25 
#ZID = ZID[::-1]
__20 = 20
_X, _Y,  _Z = X_, Y_,  len(seismic_data)
_Viridis = 'Viridis'


FIG.add_traces([plane])#
FIG.add_traces([plane2])#

FIG.add_traces([ fug ])#

#FIG.add_traces([plane3])


FIG.update_layout(   title_text="Inline: "+str(X_)+"\n"+"Crossline: "+str(Y_)+"\n"+"TWT: "+str(Z_) ,
		autosize=False,
		width=1150,#800
		height=950,#800
		margin=dict(l=65, r=50, b=65, t=90) ,  scene=dict(   zaxis=dict(autorange='reversed')   ,
                    xaxis_title_text="Inline: "+str(X_),  yaxis_title_text="Crossline: "+str(Y_),   zaxis_title_text='TWT: '+str(Z_)       )
	)

###############################################################################################################################################################


FIG.show()

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


############################
############################
RRR_ = 750
CCC_ = 750

c = 1
ma = []
for i in range(RRR_):
	ro = []
	for j in range(CCC_):
		
		ro.append(c)
		c += 1
	ma.append(ro)
	
#print(ma)
	
l = ma
############################
############################

_700 = 700
uu = 40
zz = [[uu]*_700 for v in range(_700)] 

_3 = 3
_100 = 100
_100_ = 100
for i in range(_3):
	for j in range(_3):
		zz[_100+i][_100_+j] = None
ig = go.Figure(go.Surface(
					
				x = [0,_700],
				y = [0,_700],
						#z = [[uu]*(int(right)-int(left) ) for v in range( int(bottom) - int(top) )   ]
					
				z= zz  # [[uu]*2 for v in range(2)]   
					#,colorscale=[[0, red_blue[0] ], [1, red_blue[0]   ]]   ))
				,colorscale=[[0, "green"], [1, "green"   ]]   ))

ig.show()
"""