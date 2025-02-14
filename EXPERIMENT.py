#!/usr/bin/env python3

#print(9%3)
#print(13%4)
#print(17%5)


tem = 1
q = []
cum = -1

dc = {0:-1}

cd = {}


[2,3,2,5]

for i in range(1, 6 + 1):
#for i in [1,3,2,5] :
	tem *= i
	#print(tem)
	cum += tem
	#q.append([i for i in range(tem)])
	
	#print(q)
	
	#print(tem, cum , cum - tem + 1)
	
	q.append(tuple([i for i in range(cum - tem + 1, cum+1)]) )
	
	#print( cum - tem + 1, cum, "|||" , (cum - tem - cum)*-1   ) #, len(q[-1])  , [ i for i in q[-1] ])
	                 
	
	if len(q) >= 2 :
		#print()
		#print(q[-2] , q[-1])#########
	#print( cum ,  cum - tem + 1 )
		
		RAN = i
		#for i in q[-2]
		#print( [ [ q[-1][i + (RAN*j)] for  i in range(RAN) ] for  j in range(len(q[-1])//RAN) ]  )
		mat =  [ [ q[-1][i + (RAN*j)] for  i in range(RAN) ] for  j in range(len(q[-1])//RAN) ]  
		#print(RAN, q[-1], q[-2])
		
		for i in range(len(q[-2]) )  :
			
			dc[ q[-2][i] ]  = mat[i]
			
			for kk in mat[i] :
				cd[ kk ] = q[-2][i]
		
		#print()
	
	
		#print(q)

#print( [ len(i) for i in q ]  )


l = [1,2,3,4,5,6,7,8,9,10,11,12]

o = [  [l[0+jj:TWO+jj]    for jj in range(len(l)- len(l[0:TWO]) +1  ) ]    for TWO in range(1, len(l)+1  ) ] #for jj in range(len(l) - 1  - 2, 0, -1  ) ]


RAN = 3
oo = [  [l[0+jj:RAN+jj]    for jj in range(len(l)- len(l[0:RAN]) +1  ) ]    ] #for jj in range(len(l) - 1  - 2, 0, -1  ) ]

#print(o)
print()
#print(oo), "RAN"


ooo = [ [ l[i + (RAN*j)] for  i in range(RAN) ] for  j in range(len(l)//RAN) ]


print()
print(ooo , "*******"  )


print(dc, len(dc))

print()

print(cd)   ### breadth 1st search


"""
218. The Skyline Problem

493. Reverse Pairs

699. Falling Squares

715. Range Module

850. Rectangle Area II

2213. Longest Substring of One Repeating Character

2407. Longest Increasing Subsequence II

3161. Block Placement Queries

3165. Maximum Sum of Subsequence With Non-adjacent Elements

3187. Peaks in Array
"""

