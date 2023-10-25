# Constrained Subsequence Sum - Leetcode 1425

def column_sum(lst):
	res=[]
	for i in range(0,len(lst[0])):
		s=0
		for j in range(0,len(lst[i])):
			s+=lst[j][i]
		res.append(s)
	return res	

def transpose(l1, l2):
	

	l2 =[[row[i] for row in l1] for i in range(len(l1[0]))]
	return l2
			
def do(A,k):

	if k == 1:
		return max(A)
	
	cn = 0
	cc = 0
	for i in range(len(A)):
		cc += 1
		if A[i] > 0 :
			cn+=1
			#print(cnt)
			if cn == 1 and cc == len(A):
				return A[i]
			 
	k -=1 

	AC = [[0] * len(A) for i in range(len(A))]

	#for jj in range(len(AC) // len(A) ):  # or
	for jj in range(1):
		for i in range(len(A)):
			for j in range(len(A)):
				AC[i+  len(AC) * jj][j] = A[j]


	for i in  range(len(A)):
		for kk in range(k):
			cnt = 0
			for move in range(kk + i +1):
				if move < len(A)  :
					AC[ i ][move] = 0
					cnt+=1

	for i in range(1,len(AC)):
		for j in range(0,i):
			AC[i][j] = A[j] 
			
	#print(AC)
		
	RR = len(A) - k + 1
	AC = AC[0:RR]
	l2 = []
	AC = transpose(AC, l2)
	
	#print(AC)

	return  max(column_sum(AC) ) 


A  = [10,2,-10,5,20]

nums1 = [-1,-2,-3]
kk = 1

nums2 = [10,-2,-10,-5,20]
k = 2


print( do(A, k) )

print()

print( do(nums1, kk) )

print()

print( do(nums2, k) )

print()



numm=[-1000,-2000,-3000,-4000,2] # answer is 2 working on a shorter, better faster solution

ki=2

print( do(numm, ki) )
