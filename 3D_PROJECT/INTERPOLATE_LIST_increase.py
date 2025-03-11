#!/usr/bin/env python3


def interp( main, expand_to ):

	_25 = len(main)


	print(main)
	print()

	_161 = expand_to

# 25 / 161      0.234.....


	
	minn = main[1] - main[0] 


	if _161 / _25  > _161 // _25 :
		an = (_161 // _25) + 1
	
	
	_161  += _161 // _25 
	
	print(minn )

	nl = [ min(main)+(i *  minn * (len(main)/_161)) for i in range( _161  )  if  min(main)+(i *  minn * (len(main)/_161))  <= main[-1]] 
	
	print(len(nl))
	return nl 

main = [ 0.25 * i for i in range(1, 25 + 1)]

print( interp( main, 500 )  )


	
	
rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]



rectangles = [[0,0,  0,   2,2,  1],[1,0,  0,    2,3,     1],[1,0,   0,   3,1,     1]]