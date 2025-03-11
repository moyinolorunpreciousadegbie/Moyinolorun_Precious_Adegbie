#!/usr/bin/env python3

def findPaths(arr) :
	
	
	
	R = len(arr)
	C = len(arr[0])
	
	QU = [[  [0,0] ]]
	
	ANS = []
	
	cn = 0
	lnnn = 0
	ln_cum = 0
	#for Q in QU : # [  [0,0] ]      1 PATH
	Q_N = []
	while QU :
		Q = QU.pop()
		lnnn = len(Q)
		#ln_cum += lnnn 
		#print(Q)
		if arr[  Q[-1][0] ][  Q[-1][1] ] == 1 : continue
		if Q not in ANS and Q[-1] == [R-1,C-1] : 
			cn+=1
			print(Q, cn)#, [R-1,C-1])
			ANS.append(Q)
			#if Q[-1][0] == R and  Q[-1][1] == C : break
		ttt = []
		for r in range(Q[-1][0]-1  , 	Q[-1][0]+2):
			for c in range(Q[-1][1]-1,  Q[-1][1]+2):
				
					
				tem = []
				#if r +1 == R and c+1 == C : break#return QU 
				
				if r < 0  or r == R : continue
				
				
				if c < 0  or c == C : continue
		
				
				if Q[-1][0] + 1  == r  and arr[ r ][ Q[-1][1] ] != 1:
					_1 = Q          + [[ r, Q[-1][1] ]] 
					if _1 not in QU and  [ r, Q[-1][1] ] not in ttt:
						ttt.append([ r, Q[-1][1] ])
						Q_N.append( _1)
						QU = Q_N
			# [  [0,0]  ]         [1,0]
				if Q[-1][1] + 1  == c  and  arr[ Q[-1][0] ][ c] != 1 :
					_2 = Q          + [[ Q[-1][0] , c] ]
					if _2 not in QU and [ Q[-1][0] , c] not in  ttt:
						ttt.append([ Q[-1][0] , c])
						Q_N.append( _2)
						QU = Q_N
			# [  [0,0]  ]         [0,1]
						#if Q[-1][0] + 1  == r   and Q[-1][1] + 1  == c :
						#_3 = Q + [[r,c]]
						#if _3 not in QU :
						#QU.append( _3)
			# [  [0,0]  ]         [1,1]
			
						#QU = QU[lnnn:]
		
						
						#Q_N = []
	
obstacleGrid  = [[0,0,0],[0,1,0],[0,0,0]]

findPaths(obstacleGrid)  
print()


obstacleGrid = [[0,1],[0,0]]


findPaths(obstacleGrid) 

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