#!/usr/bin/env python3
def findPaths(arr, k) :
	
	
	
	R = len(arr)
	C = len(arr[0])
	
	QU = [[  [0,0] ]]
	
	ANS = []
	
	
	
	mp = {}
	
	cn = 0
	
	if arr[0][0] == 1 : 
		QU[0].append(1)
	else :
		QU[0].append(0)
		
		#print(QU)
	
	for Q in QU : # [[0, 0], 0]     1 PATH
	
		
		#if arr[  Q[-1][0] ][  Q[-1][1] ] == 1 : continue
		
		if Q[:-1] not in ANS and Q[-2] == [R-1,C-1] : 
			cn+=1
			print(Q[:-1],Q[-1], cn)#, [R-1,C-1])
			ANS.append(Q[:-1])
			#if Q[-1][0] == R and  Q[-1][1] == C : break
		for r in range(0,R):
			for c in range(0, C):
				
				rr = R - 1 - r
				cc = C - 1 - c
				
				 
				tem = []
				#if r +1 == R and c+1 == C : break#return QU 
				
				if Q[-2][0] + 1  == r  and  [ r, Q[-2][1] ]  not in Q :# and arr[ r ][ Q[-2][1] ] != 1:
					_1 = Q[:-1]           + [[ r, Q[-2][1] ]]  
					
					if arr[ r ][ Q[-2][1] ] == 1 :
						_1.append( Q[-1] + 1  )
						
						if _1 not in QU :
							QU.append( _1)  ###############
							
					if arr[ r ][ Q[-2][1] ] == 0 :
						_1.append( Q[-1]   )
						
						if _1 not in QU :
							QU.append( _1) ###############
							
							
				if Q[-2][0] + 1  == rr   and   [ rr, Q[-2][1] ] not in Q :# and arr[ r ][ Q[-2][1] ] != 1:
					_1 = Q[:-1]           + [[ rr, Q[-2][1] ]]  
				
					if arr[ rr ][ Q[-2][1] ] == 1 :
						_1.append( Q[-1] + 1  )   ###############
						
						if _1 not in QU :
							QU.append( _1)
							
					if arr[ rr ][ Q[-2][1] ] == 0 :
						_1.append( Q[-1]   )     ###############
						
						if _1 not in QU :
							QU.append( _1)
							
							
							
						
							
							
							
							
			# [  [0,0]  ]         [1,0]
				if Q[-2][1] + 1  == c     and   [ Q[-2][0] , c]  not in Q :# and  arr[ Q[-2][0] ][ c] != 1 :
					_2 = Q[:-1]          + [[ Q[-2][0] , c] ]  
					#print(Q[::-1]          , [[ Q[-2][0] , c] ]  , [Q[-1]] , "HERE", _2)
					
					if arr[Q[-2][0] ][ c ] == 1 :
						_2.append( Q[-1] + 1  )
						
						if _2 not in QU :
							QU.append( _2)   ###############
							
					
					if arr[Q[-2][0] ][ c ] == 0 :
						_2.append( Q[-1]   )
						
						if _2 not in QU :
							QU.append( _2)   ###############
							
							
							
				if Q[-2][1] + 1  == cc     and [ Q[-2][0] , cc]   not in Q :# and  arr[ Q[-2][0] ][ c] != 1 :
					_2 = Q[:-1]          + [[ Q[-2][0] , cc] ]  
					#print(Q[::-1]          , [[ Q[-2][0] , c] ]  , [Q[-1]] , "HERE", _2)
				
					if arr[Q[-2][0] ][ cc ] == 1 :
						_2.append( Q[-1] + 1  )
						
						if _2 not in QU :
							QU.append( _2)    ###############
							
							
					if arr[Q[-2][0] ][ cc ] == 0 :
						_2.append( Q[-1]   )
						
						if _2 not in QU :
							QU.append( _2)    ###############
							
							
							
							
			# [  [0,0]  ]         [0,1]
						#if Q[-1][0] + 1  == r   and Q[-1][1] + 1  == c :
						#_3 = Q + [[r,c]]
						#if _3 not in QU :
						#QU.append( _3)
			# [  [0,0]  ]         [1,1]
						
				#############################################################################  VVVV  MINUS (BACKTRACK [-1 +1] [+1 -1] [-1 -1]   )
				
				if Q[-2][0] - 1  == r     and  [ r, Q[-2][1] ]  not in Q :# and arr[ r ][ Q[-2][1] ] != 1:
					_1 = Q[:-1]           + [[ r, Q[-2][1] ]]  
				
					if arr[ r ][ Q[-2][1] ] == 1 :
						_1.append( Q[-1] + 1  )
						
						if _1 not in QU :
							QU.append( _1)  ###############
							
					if arr[ r ][ Q[-2][1] ] == 0 :
						_1.append( Q[-1]   )
						
						if _1 not in QU :
							QU.append( _1) ###############
							
							
				if Q[-2][0] - 1  == rr     and  [ rr, Q[-2][1] ]  not in Q :# and arr[ r ][ Q[-2][1] ] != 1:
					_1 = Q[:-1]           + [[ rr, Q[-2][1] ]]  
				
					if arr[ rr ][ Q[-2][1] ] == 1 :
						_1.append( Q[-1] + 1  )   ###############
						
						if _1 not in QU :
							QU.append( _1)
							
					if arr[ rr ][ Q[-2][1] ] == 0 :
						_1.append( Q[-1]   )     ###############
						
						if _1 not in QU :
							QU.append( _1)
							
							
							
							
							
							
							
							
			# [  [0,0]  ]         [1,0]
				if Q[-2][1] - 1  == c     and [ Q[-2][0] , c]    not in Q :# and  arr[ Q[-2][0] ][ c] != 1 :
					_2 = Q[:-1]          + [[ Q[-2][0] , c] ]  
					#print(Q[::-1]          , [[ Q[-2][0] , c] ]  , [Q[-1]] , "HERE", _2)
				
					if arr[Q[-2][0] ][ c ] == 1 :
						_2.append( Q[-1] + 1  )
						
						if _2 not in QU :
							QU.append( _2)   ###############
							
							
					if arr[Q[-2][0] ][ c ] == 0 :
						_2.append( Q[-1]   )
						
						if _2 not in QU :
							QU.append( _2)   ###############
							
							
							
				if Q[-2][1] - 1  == cc     and  [ Q[-2][0] , cc]  not in Q  :# and  arr[ Q[-2][0] ][ c] != 1 :
					_2 = Q[:-1]          + [[ Q[-2][0] , cc] ]  
					#print(Q[::-1]          , [[ Q[-2][0] , c] ]  , [Q[-1]] , "HERE", _2)
				
					if arr[Q[-2][0] ][ cc ] == 1 :
						_2.append( Q[-1] + 1  )
						
						if _2 not in QU :
							QU.append( _2)    ###############
							
							
					if arr[Q[-2][0] ][ cc ] == 0 :
						_2.append( Q[-1]   )
						
						if _2 not in QU :
							QU.append( _2)    ###############
						
						
						
grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]
k = 1
#Output: 6


findPaths(grid, k)