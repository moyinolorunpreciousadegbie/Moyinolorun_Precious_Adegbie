#!/usr/bin/env python3

#!/usr/bin/env python3

#!/usr/bin/env python3
class Solution(object):
	def shortestPath(self, grid, k):
		#k += 3
		import collections
		arr = grid
		
		R = len(arr)
		C = len(arr[0])
		
		#QU = [[  [0,0] ]]
		
		QU = collections.deque([[  [0,0] ]])
		
		ANS = [] 
		
		
		
		mp = {}
		
		cn = 0
		
		if arr[0][0] == 1 : 
			QU[0].append(1)
		else :
			QU[0].append(0)
			
			#print(QU)
			
		mn = float('inf')
		
		
		ind = 0
		
		#   and ( len(Q[:-1])-1  < mn or    mn < float('inf')  )
		
		
		Q_NEW = collections.deque([]) #   []
		#for Q in QU : # [[0, 0], 0]     1 PATH
		
		
		while QU :
			
			Q = QU.popleft() #(0)
			
			#if len(Q[:-1])-1   > mn :
				#continue
			#print(ind)
			
			#if arr[  Q[-1][0] ][  Q[-1][1] ] == 1 : continue
			
			if Q[:-1] not in ANS and Q[-2] == [R-1,C-1] : 
				cn+=1
				print(Q[:-1],Q[-1], cn,"    ", len(Q[:-1])-1 )#, [R-1,C-1])  # <<
				#print(Q[-1])
				#ANS.append(Q[:-1]) # <<
				#if Q[-1][0] == R and  Q[-1][1] == C : break
				
				if Q[-1]  <= k  :
					mn = min( mn, len(Q[:-1])-1  )
					
					#return mn
					
					
			if Q[-2][0] < 0  or Q[-2][0] == R : 
				Q = Q[:ind]  + Q[ind+1:]
				#continue
				
				
			if Q[-2][1]  < 0  or Q[-2][1] == C :  
				Q = Q[:ind]  + Q[ind+1:]
				#continue
			IND = 0	
			
			ttt = []
			rnn = 0
			tempp = Q[-2]
			#for r in range(Q[-2][0]-1  , 	Q[-2][0]+2):
				#cnn = 0
				#for c in range(Q[-2][1]-1,  Q[-2][1]+2):
			
			for vr , vc in [(1, 0), (-1, 0), (0, 1), (0, -1)] :
				r = Q[-2][0] + vr
				c = Q[-2][1] + vc
				#print([r,c])
				
				
				
				
				rr = R - 1 - r
				cc = C - 1 - c
				
				
				tem = []
				#if r +1 == R and c+1 == C : break#return QU 
				if r < 0  or r == R : 
					
					continue
				
				
				#if rr < 0  or rr == R : 
					#if cnn < 2 : cnn += 1
					#if cnn == 2 : 
						#cnn = 0
						#rnn += 1
					#continue
				
				if c < 0  or c == C : 
					
					continue
				
				if ( r < 0  or r == R ) and (c < 0  or c == C ): 
					print('BOTH')
					continue
				
				#if cc < 0  or cc == C : 
					#if cnn < 2 : cnn += 1
					#if cnn == 2 : 
						#cnn = 0
						#rnn += 1
					#continue
				
				#if rnn == 1 and cnn == 1 :
					#cnn += 1
					#continue
				
				
				
				if Q[-2][0] + 1  == r  and  [ r, Q[-2][1] ]  not in Q   and Q[-1] -1 < k and  [ r, Q[-2][1] ]  not in ttt and ( len(Q[:-1])-1  < mn or    mn < float('inf')  ):# and arr[ r ][ Q[-2][1] ] != 1:
					_1 = Q[:-1]           + [[ r, Q[-2][1] ]]  
					IND += 1
					ttt.append( [ r, Q[-2][1] ]  )
				
					if arr[ r ][ Q[-2][1] ] == 1 :
						_1.append( Q[-1] + 1  )
						
						if _1 not in QU  and _1 not in Q_NEW:
							
							Q_NEW.append( _1)  ###############
							ind = -1
							
							QU = Q_NEW 
							
							
							
					if arr[ r ][ Q[-2][1] ] == 0 :
						_1.append( Q[-1]   )
						
						if _1 not in QU and _1 not in Q_NEW:
							Q_NEW.append( _1) ###############
							ind = -1
							
							QU = Q_NEW
							
							
							
							
							
							
							
			# [  [0,0]  ]         [1,0]
				if Q[-2][1] + 1  == c     and   [ Q[-2][0] , c]  not in Q and Q[-1]-1 < k and [ Q[-2][0] , c]  not in ttt and ( len(Q[:-1])-1  < mn or    mn < float('inf')  ):# and  arr[ Q[-2][0] ][ c] != 1 :
					_2 = Q[:-1]          + [[ Q[-2][0] , c] ]  
					IND += 1
					ttt.append( [ Q[-2][0] , c]  )
					#print(Q[::-1]          , [[ Q[-2][0] , c] ]  , [Q[-1]] , "HERE", _2)
				
					if arr[Q[-2][0] ][ c ] == 1 :
						_2.append( Q[-1] + 1  )
						
						if _2 not in QU and _2 not in Q_NEW:
							Q_NEW.append( _2)   ###############
							ind = -1
							
							QU = Q_NEW
							
							
					if arr[Q[-2][0] ][ c ] == 0 :
						_2.append( Q[-1]   )
						
						if _2 not in QU and _2 not in Q_NEW:
							Q_NEW.append( _2)   ###############
							ind = -1
							
							QU = Q_NEW
							
							
							
							
							
							
							
			# [  [0,0]  ]         [0,1]
						#if Q[-1][0] + 1  == r   and Q[-1][1] + 1  == c :
						#_3 = Q + [[r,c]]
						#if _3 not in QU :
						#QU.append( _3)
			# [  [0,0]  ]         [1,1]
							
				#############################################################################  VVVV  MINUS (BACKTRACK [-1 +1] [+1 -1] [-1 -1]   )
							
							#continue
							
				if Q[-2][0] - 1  == r     and  [ r, Q[-2][1] ]  not in Q and Q[-1]-1 < k and  [ r, Q[-2][1] ]  not in ttt and ( len(Q[:-1])-1  < mn or    mn < float('inf')  ):# and arr[ r ][ Q[-2][1] ] != 1:
					_1 = Q[:-1]           + [[ r, Q[-2][1] ]]  
					IND += 1
					ttt.append( [ r, Q[-2][1] ] )
				
					if arr[ r ][ Q[-2][1] ] == 1 :
						_1.append( Q[-1] + 1  )
						
						if _1 not in QU and _1 not in Q_NEW:
							Q_NEW.append( _1)  ###############
							ind = -1
							
							QU = Q_NEW
							
					if arr[ r ][ Q[-2][1] ] == 0 :
						_1.append( Q[-1]   )
						
						if _1 not in QU and _1 not in Q_NEW:
							Q_NEW.append( _1) ###############
							ind = -1
							
							QU = Q_NEW
							
							
							
							
							
							
							
							
							
							
							
			# [  [0,0]  ]         [1,0]
				if Q[-2][1] - 1  == c     and [ Q[-2][0] , c]    not in Q and Q[-1]-1 < k and [ Q[-2][0] , c]    not in ttt and ( len(Q[:-1])-1  < mn or    mn < float('inf')  ):# and  arr[ Q[-2][0] ][ c] != 1 :
					_2 = Q[:-1]          + [[ Q[-2][0] , c] ]  
					IND += 1
					ttt.append(  [ Q[-2][0] , c]  )
				
					#print(Q[::-1]          , [[ Q[-2][0] , c] ]  , [Q[-1]] , "HERE", _2)
				
					if arr[Q[-2][0] ][ c ] == 1 :
						_2.append( Q[-1] + 1  )
						
						if _2 not in QU  and _2 not in Q_NEW:
							Q_NEW.append( _2)   ###############
							ind = -1
							
							QU = Q_NEW
							
							
					if arr[Q[-2][0] ][ c ] == 0 :
						_2.append( Q[-1]   )
						
						if _2 not in QU and _2 not in Q_NEW:
							Q_NEW.append( _2)   ###############
							ind = -1
							
							QU = Q_NEW
							
							
							
							
							
				if 1 == 44 :
					print("HERE  VVVVVV")
				#####<<<<<<<<<<<<<<<<<<  1
					if Q[-2][0] + 1  == rr   and   [ rr, Q[-2][1] ] not in Q and Q[-1] -1 < k and  [ rr, Q[-2][1] ]  not in ttt and ( len(Q[:-1])-1  < mn or    mn < float('inf')  ):# and arr[ r ][ Q[-2][1] ] != 1:
						_1 = Q[:-1]           + [[ rr, Q[-2][1] ]]  
						IND += 1
						ttt.append( [ rr, Q[-2][1] ] )
						if arr[ rr ][ Q[-2][1] ] == 1 :
							_1.append( Q[-1] + 1  )   ###############
							
							if _1 not in QU and _1 not in Q_NEW:
								Q_NEW.append( _1)
								ind = -1
								
								QU = Q_NEW
								
								
						if arr[ rr ][ Q[-2][1] ] == 0 :
							_1.append( Q[-1]   )     ###############
							
							if _1 not in QU and _1 not in Q_NEW:
								Q_NEW.append( _1)
								ind = -1
								
								QU = Q_NEW
				#####<<<<<<<<<<<<<<<<<<		
								
								
				#####<<<<<<<<<<<<<<<<<<		2	
					if Q[-2][1] + 1  == cc     and [ Q[-2][0] , cc]   not in Q and Q[-1]-1 < k and [ Q[-2][0] , cc]    not in ttt and ( len(Q[:-1])-1  < mn or    mn < float('inf')  ):# and  arr[ Q[-2][0] ][ c] != 1 :
						_2 = Q[:-1]          + [[ Q[-2][0] , cc] ] 
						IND += 1
						ttt.append(  [ Q[-2][0] , cc]  )
					#print(Q[::-1]          , [[ Q[-2][0] , c] ]  , [Q[-1]] , "HERE", _2)
					
						if arr[Q[-2][0] ][ cc ] == 1 :
							_2.append( Q[-1] + 1  )
							
							if _2 not in QU and _2 not in Q_NEW:
								Q_NEW.append( _2)    ###############   
								ind = -1
								
								QU = Q_NEW
								
								
						if arr[Q[-2][0] ][ cc ] == 0 :
							_2.append( Q[-1]   )
							
							if _2 not in QU and _2 not in Q_NEW:
								Q_NEW.append( _2)    ###############
								ind = -1
								
								QU = Q_NEW
				#####<<<<<<<<<<<<<<<<<<	
								
								
				#####<<<<<<<<<<<<<<<<<<		3	
					if Q[-2][0] - 1  == rr     and  [ rr, Q[-2][1] ]  not in Q and Q[-1] -1 < k and  [ rr, Q[-2][1] ]  not in ttt and ( len(Q[:-1])-1  < mn or    mn < float('inf')  ):# and arr[ r ][ Q[-2][1] ] != 1:
						_1 = Q[:-1]           + [[ rr, Q[-2][1] ]] 
						IND += 1
						ttt.append(  [ rr, Q[-2][1] ]  )
					
						if arr[ rr ][ Q[-2][1] ] == 1 :
							_1.append( Q[-1] + 1  )   ###############
							
							if _1 not in QU and _1 not in Q_NEW :
								Q_NEW.append( _1)
								ind = -1
								
								QU = Q_NEW
								
						if arr[ rr ][ Q[-2][1] ] == 0 :
							_1.append( Q[-1]   )     ###############
							
							if _1 not in QU and _1 not in Q_NEW:
								Q_NEW.append( _1)
								ind = -1
								
								QU = Q_NEW
								
				#####<<<<<<<<<<<<<<<<<<
								
				#####<<<<<<<<<<<<<<<<<<   4
					if Q[-2][1] - 1  == cc     and  [ Q[-2][0] , cc]  not in Q and Q[-1]-1 < k and [ Q[-2][0] , cc]    not in ttt and ( len(Q[:-1])-1  < mn or    mn < float('inf')  ) :# and  arr[ Q[-2][0] ][ c] != 1 :       
						_2 = Q[:-1]          + [[ Q[-2][0] , cc] ]  
						IND += 1
						ttt.append(  [ Q[-2][0] , cc]  )
					#print(Q[::-1]          , [[ Q[-2][0] , c] ]  , [Q[-1]] , "HERE", _2)                          
					
						if arr[Q[-2][0] ][ cc ] == 1 :
							_2.append( Q[-1] + 1  )
							
							if _2 not in QU and _2 not in Q_NEW:
								Q_NEW.append( _2)    ###############
								ind = -1
								
								QU = Q_NEW
								
								
						if arr[Q[-2][0] ][ cc ] == 0 :
							_2.append( Q[-1]   )
							
							if _2 not in QU and _2 not in Q_NEW:
								Q_NEW.append( _2)    ###############
								ind = -1
								
								
								QU = Q_NEW
								
			#cnn+=1
				#####<<<<<<<<<<<<<<<<<<
			#rnn += 1
								
		#if IND != 0 : print(IND, "-", range(0, len(ttt) ), Q[-2])
		#if ttt != [] :  print(ttt, ">>>>>>>",tempp)
									
			IND += 1
			ind +=1 
			
			
		if mn == float('inf') : return -1
		
		return  mn
	
	
Obj = Solution()

grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]
k = 1
#Output: 6


print( Obj.shortestPath(grid, k) )
print()
print()

grid = [[0,1,1],[1,1,1],[1,0,0]]
k = 1
#Output: -1

print( Obj.shortestPath(grid, k) )