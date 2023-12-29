#!/usr/bin/env python3
def chk(nums):
	q = []
	cnt= 0
	for i in nums:
		if i not in q:
			cnt+=1
		q.append(i)
		
	return cnt

def do(AA, k):
	

	q = []
	for ii in range( 2, len(AA) +1): #
		for t in range(len(AA)-1):
			for h in range(0,ii,ii-1):  # STEP
				if(h+t < len(AA) and ii- h + t - 1 < len(AA) ):
					
					q.append([h+t , ii-h-1 + t])
					
					
	q = q[0::2]
	#print(q)
	qq = []
	for rw in range(len(q)):
		#print(AA[q[rw][0]:q[rw][1]+1])
		if chk(AA[q[rw][0]:q[rw][1]+1] )  == k :
			qq.append(AA[q[rw][0]:q[rw][1]+1])
			
	return qq, len(qq)
	
	
nums = [1,2,1,2,3]
k = 2
#Output 7
print( do(nums, k)  )
print()


nums = [1,2,1,3,4]
k = 3
#Output: 3
print( do(nums, k)  )
	