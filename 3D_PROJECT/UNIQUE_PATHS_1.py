#!/usr/bin/env python3

def findPaths(arr) :
	
	
     
	R = len(arr)
	C = len(arr[0])
	
	QU = [[  [0,0] ]]
	
	ANS = []
	
	cn = 0
	for Q in QU : # [  [0,0] ]      1 PATH
		#print(Q)
		if Q not in ANS and Q[-1] == [R-1,C-1] : 
			cn+=1
			print(Q, cn)#, [R-1,C-1])
			ANS.append(Q)
			#if Q[-1][0] == R and  Q[-1][1] == C : break
			
		ttt = []
		for r in range(    Q[-1][0]-1  , 	 Q[-1][0]+2):
			for c in range(Q[-1][1]-1  ,     Q[-1][1]+2):
				tem = []
				#if r +1 == R and c+1 == C : break#return QU 
				if r < 0  or r == R : continue
				
				
				if c < 0  or c == C : continue
				
				if Q[-1][0] + 1  == r :
					_1 = Q          + [[ r, Q[-1][1] ]] 
					if _1 not in QU and [ r, Q[-1][1] ] not in ttt:
						ttt.append([ r, Q[-1][1] ])
						QU.append( _1)
			# [  [0,0]  ]         [1,0]
				if Q[-1][1] + 1  == c :
					_2 = Q          + [[ Q[-1][0] , c] ]
					if _2 not in QU and [Q[-1][0] , c] not in ttt:
						ttt.append([ Q[-1][0] , c])
						QU.append( _2)
			# [  [0,0]  ]         [0,1]
				if Q[-1][0] + 1  == r   and Q[-1][1] + 1  == c :
					_3 = Q + [[r,c]]
					if _3 not in QU and [r,c] not in ttt:
						ttt.append([r,c])
						QU.append( _3)
			# [  [0,0]  ]         [1,1]
			
				

	
arr = [[0]* 5 for i in range(4)]

findPaths(arr)  

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