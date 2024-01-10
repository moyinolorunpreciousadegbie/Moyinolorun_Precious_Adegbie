#!/usr/bin/env python3
def find(d):
	
	q = []
	
	cnt = 0
	for dd in d:
		if dd not in q:
			cnt+=1
		q.append(dd)
		
	return cnt 


def do(word):
	
	q = []
	for ii in range( 2, len(word) +1): #
		for t in range(len(word)-1):
			for h in range(0,ii,ii-1):  # STEP
				if(h+t < len(word) and ii- h + t - 1 < len(word) ):
					
					q.append([h+t , ii-h-1 + t])
					
	q = q[0::2]
	
	qq = []
	for rw in range(len(q)):
		
		qq.append(  word[q[rw][0] : q[rw][1]+1 ]  )
		
		
	qq = qq[::-1]  # reverse 
	#qq = qq[1::]  # exclude banana FULL WORD
	#print(qq)
	
	for i in range(len(word)):
		qq.append(word[i])
		#return qq
	
	temp = 0
	for mat in qq:
		temp += find(mat)
	
	return temp




s = "abbca"
#Output: 28

print(  do(s) )


s = "code"
#Output: 20
print(  do(s) )


  
	
	
	
	
		
	