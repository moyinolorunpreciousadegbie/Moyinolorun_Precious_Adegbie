#!/usr/bin/env python3

def findPaths(arr) :
	

	
	R = len(arr)  
	C = len(arr[0]) 
	
	#QU = [[  [0,0] ]]   
	
	VISI = [[0] *  C for _ in range(R)]
	
	start = []
	
	end = []
	__1  = 0
	zz = 0
	for r in range(0,R):
		for c in range(0, C):
			if arr[r][c]  == 1 :
				start.append([r,c]) 
				
			if arr[r][c]  == -1 : 
				__1 += 1
				
			if arr[r][c]  == 2 :
				end.append([r,c])
				
			if arr[r][c]  == 0 :
				zz +=1
				
	
	QU = [start]
	
	ANS = []
	
	cn = 0
	
	
	
	RR = abs(start[0][0] - end[0][0])
	CC = abs(start[0][1] - end[0][1])
	
	#RR = 0
	#CC = 0
	
	ind = 0
	indd = 0
	vis = set()
	#for Q in QU : # [  [0,0] ]      1 PATH
	while QU :
		Q = QU.pop()
		#print(ind)
		#print(Q)
		#if arr[  Q[-1][0] ][  Q[-1][1] ] == -1 : continue
		if Q not in ANS and arr[  Q[-1][0] ][  Q[-1][1] ] == 2 and len(Q) - 2 == zz : 
			cn+=1
			print(Q, cn,"   ",len(Q), zz) #, [R-1,C-1])     #  start + zz (0)  + end    = zz + 2
			ANS.append(Q)
			
			
			#QU =   QU[:ind] + QU[ind +1:]
			
			#if Q[-1][0] == R and  Q[-1][1] == C : 
			
		if Q[-1][0] < 0  or Q[-1][0] == R : 
			Q = Q[:ind]  + Q[ind+1:]
			#continue
		
	
		if Q[-1][1]  < 0  or Q[-1][1] == C :  
			Q = Q[:ind]  + Q[ind+1:]
			#continue
	
		
		ttt = []
		for r in range(Q[-1][0]-1  , 	Q[-1][0]+2):
			for c in range(Q[-1][1]-1,  Q[-1][1]+2):
				#if (r,c) in vis : continue
				rr = R - 1 - r
				cc = C - 1 - c
					
				tem = []
				#if r +1 == R and c+1 == C : break#return QU 
				
				if r < 0  or r == R : 
					#print("1", ind, indd, len(QU))
					continue
				
				if rr < 0  or rr == R : 
					#print("2", ind, indd , len(QU))
					continue
					
				if c < 0  or c == C : 
					#print("3", ind, indd , len(QU))
					continue
				
				if cc < 0  or cc == C : 
					#print("4", ind, indd , len(QU))
					continue
				
				###############################
				
				if     Q[-1][0] + 1  == r    and [ r, Q[-1][1] ] not in Q   and arr[ r][ Q[-1][1] ] != -1:# and  VISI[ r][ Q[-1][1] ]   == 0 :     # r
					_1 = Q          + [[ r, Q[-1][1] ]] 
					VISI[ r][ Q[-1][1] ] = 1
					if _1 not in QU and [ r, Q[-1][1] ] not in ttt:
						ttt.append([ r, Q[-1][1] ])
						QU.append( _1)
						vis.add((Q[-1][0] + 1, c ))
						ind = -1
						indd = 0
			# [  [0,0]  ]         [1,0]
				if     Q[-1][1] + 1  == c   and [ Q[-1][0] , c] not in Q and arr[ Q[-1][0] ][ c]  != -1 :# and VISI[ Q[-1][0] ][ c] == 0:    #   c
					_2 = Q          + [[ Q[-1][0] , c] ]
					VISI[ Q[-1][0] ][ c] = 1
					if _2 not in QU and  [ Q[-1][0] , c] not in ttt :
						ttt.append( [ Q[-1][0] , c] )
						QU.append( _2)
						vis.add((r , Q[-1][1] + 1 ))
						ind = -1
						indd = 0
						
				
				if   Q[-1][0] - 1  == r  and [ r, Q[-1][1] ] not in Q and arr[ r][ Q[-1][1] ]  != -1:# and VISI[ r][ Q[-1][1] ] == 0:    #   r
					_3 = Q          + [[ r, Q[-1][1] ]] 
					VISI[ r][ Q[-1][1] ] = 1
					if _3 not in QU and [ r, Q[-1][1] ] not in ttt:
						ttt.append([ r, Q[-1][1] ])
						QU.append( _3)
						vis.add((Q[-1][0] - 1, c ))
						ind = -1
						indd = 0
			# [  [0,0]  ]         [1,0]
				if  Q[-1][1] - 1  == c  and [ Q[-1][0] , c]  not in Q and arr[ Q[-1][0] ][ c]  != -1:# and VISI[ Q[-1][0] ][ c] == 0:    #    c
					_4 = Q          + [[ Q[-1][0] , c] ]
					VISI[ Q[-1][0] ][ c]  = 1
					if _4 not in QU and  [ Q[-1][0] , c] not in ttt:
						ttt.append( [ Q[-1][0] , c] )
						QU.append( _4)
						vis.add((r , Q[-1][1] - 1 ))
						ind = -1
						indd = 0
			# [  [0,0]  ]         [0,1]
						#if Q[-1][0] + 1  == r   and Q[-1][1] + 1  == c :
						#_3 = Q + [[r,c]]
						#if _3 not in QU :
						#QU.append( _3)
			# [  [0,0]  ]         [1,1]
			
			###############################
			###############################
						
						
			###############################
			###############################
			
				
			
				
				
				if 1 == 44 :
					print("HERE  VVVVVV")
					if      Q[-1][0] + 1  == rr   and [ rr, Q[-1][1] ] not in Q and arr[ rr][ Q[-1][1] ]  != -1:# and VISI[ rr][ Q[-1][1] ] == 0:     # rr
						_1 = Q          + [[ rr, Q[-1][1] ]] 
						VISI[ rr][ Q[-1][1] ] = 1
						if _1 not in QU and [ rr, Q[-1][1] ] not in ttt:
							ttt.append([ rr, Q[-1][1] ])
							QU.append( _1)
							vis.add((Q[-1][0] + 1, cc ))
							ind = -1
							indd = 0
				# [  [0,0]  ]         [1,0]
					if      Q[-1][1] + 1  == cc  and [ Q[-1][0] , cc] not in Q and arr[ Q[-1][0] ][ cc]  != -1:# and  VISI[ Q[-1][0] ][ cc] == 0:    #   cc
						_2 = Q          + [[ Q[-1][0] , cc] ]
						VISI[ Q[-1][0] ][ cc] = 1
						if _2 not in QU and  [ Q[-1][0] , cc] not in ttt:
							ttt.append( [ Q[-1][0] , cc] )
							QU.append( _2)
							vis.add((rr , Q[-1][1] + 1 ))
							ind = -1
							indd = 0
							
							
					if       Q[-1][0] - 1  == rr  and [ rr, Q[-1][1] ] not in Q and arr[ rr ][ Q[-1][1] ]  != -1:# and VISI[ rr ][ Q[-1][1] ] == 0:    #   rr
						_3 = Q          + [[ rr, Q[-1][1] ]] 
						VISI[ rr ][ Q[-1][1] ]  = 1
						if _3 not in QU and [ rr, Q[-1][1] ] not in ttt:
							ttt.append([ rr, Q[-1][1] ])
							QU.append( _3)
							vis.add((Q[-1][0] - 1, cc ))
							ind = 0
							indd = 0
				# [  [0,0]  ]         [1,0]
					if  Q[-1][1] - 1  == cc  and [ Q[-1][0] , cc]  not in Q and arr[ Q[-1][0] ][ cc]   != -1:# and VISI[ Q[-1][0] ][ cc] == 0:    #    cc
						_4 = Q          + [[ Q[-1][0] , cc] ]
						VISI[ Q[-1][0] ][ cc] = 1
						if _4 not in QU and  [ Q[-1][0] , cc] not in ttt:
							ttt.append( [ Q[-1][0] , cc] )
							QU.append( _4)
							vis.add((rr , Q[-1][1] - 1 ))
							ind = -1
							indd = 0
				# [  [0,0]  ]         [0,1]
							#if Q[-1][0] + 1  == r   and Q[-1][1] + 1  == c :
							#_3 = Q + [[r,c]]
							#if _3 not in QU :
							#QU.append( _3)
				# [  [0,0]  ]         [1,1]
							
				###############################
		
			
			
		ind += 1
		
		indd += 1
				

	
grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]

findPaths(grid)  
print()
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
# 2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
#     1     2     3     4     5     6     7      8     9    10    11    


grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]


findPaths(grid)
print()
# 1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
# 2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
# 3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
# 4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)

grid = [[0,1],[2,0]]

findPaths(grid) 
print()


############XXXXXXXXXXXXXx]
grid = [[0,0,0,0], [0,1,0,0],[0,0,0,0],[0,0,0,0],[0,0,2,-1]]
findPaths(grid) 
print()


grid = [[0,0,0,0], [0,2,0,0],[0,0,0,0],[0,0,0,0],[0,0,1,-1]]
findPaths(grid) 
print()



#
#				main                                            
#   													mp[ (r,c) ] --> [                  
# if 0 <  r-1                                         append                      [  [r-1,c], [r,c]]   , 
# if 0 <  c-1                      				                             [  [r-1,c], [r,c]]   ,	     
# if 0 <  r-1 and  0 <  c-1 													  [  [r-1,c], [r,c]]   ,
#																										]
#  [[r-1,c]]      +  [[r,c]]
#  [[r,c-1]]      +  [[r,c]]
#  [[r-1,c-1]]    +  [[r,c]]


"""


temp = mp[ (r,c) ]   # STORE LIST OF KIDS   [  [r-1,c], [r,c]]               [  [r-1,c], [r,c]]          [  [r-1,c], [r,c]] 




if (r-1,c) in mp    for u in mp[(r-1,c)]    u[:-1] + 


if (r,c-1) in mp


if (r-1,c-1) in mp

"""