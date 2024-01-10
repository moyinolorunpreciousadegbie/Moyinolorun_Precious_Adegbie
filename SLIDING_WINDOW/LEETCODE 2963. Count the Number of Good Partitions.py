# LEETCODE 2963. Count the Number of Good Partitions

from itertools import combinations

def check2(s):
	
	for ii, rw in enumerate(s):
	
		for j in  range(len(s)):
			#print(ii, j)
			for i in range(len(rw)):
				if   ii != j  and s[ii][i] in s[j] :
					#print(ii, j)
					return True

	return  False 

def sums(mat):
	su = 0
	for i in mat:
		su += sum(i)
	
	return su

def do(AA):
	
	q = []		
	for r1 in range( len(AA[0])):		
		for r2 in range( 2,len(AA[0]) + 1): 
			if r1 < r2-1:   # KEEP LEFT FROM OVER TAKING RIGHT
				#print(r1, r-1)
				q.append([r1, r2-1])
			
	ACD = [['#'] * len(AA[0]) for i in range(len(AA)*len(AA[0]) )]
	
	for jj in range(len(ACD) // len(AA) ):
		
		for i in range(len(AA)):
			for j in range(len(AA[0])):
				
				if i +  len(AA) * jj == j :
					ACD[i+  len(AA) * jj][j] = AA[i][j]
					
	AC = [['#'] * len(AA[0]) for _ in range(len(q))]
	#print(AC)
	
	for rw in range(len(q)):
		for on in range(q[rw][0],q[rw][1]+1) :
			#print( on)
			AC[rw][on] = AA[0][on] 
			#print()
			
	for append in range(len(AC)):
		ACD.append(AC[append])

	w = []
	for rw in ACD:
		rw = [x for x in rw if x != '#']
		w.append(rw)
	return w




def main(A):
	AA = []
	AA.append(A)
	
	tot = sums(AA)
	
	q = []
	#print(do(A))
	for i in range(1, len( do(AA)  )   ):
		for comb in combinations(do(AA)  , i):
			lst = list(comb)
			if sums(lst) == tot :
				if not check2(lst):
					q.append(lst)
	
	print(q)

	print(len(q))




A = [1,2,3,4]  # 8
main(A)	
print()

A = [1,1,1,1] # 1
main(A)	
print()

A  = [1,2,1,3] #  2
main(A)	
print()

		
		