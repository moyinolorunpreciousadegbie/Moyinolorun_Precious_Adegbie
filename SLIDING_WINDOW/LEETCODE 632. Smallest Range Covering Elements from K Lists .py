from itertools import combinations

def do(nums):
	
	t = []
	for i in range(len(nums)):
		t.append(nums[i])
		if i + 1 < len(nums) and nums[i+1] in t:
			return [min(t[0]), min(t[-1])]

	
	qq = set()
	for ran in nums:
		for i in ran:
			qq.add(i)
			
	qq = list(qq)
	#print(qq)  #  [0, 4, 5, 9, 10, 12, 15, 18, 20, 22, 24, 26, 30]
	
	q = []

	for comb in combinations(qq, 2):
		q.append( list(comb) )
		#print(q)
	
		#for i in range(len(q)):
		#for j in range(q[i][0], q[i][-1] + 1): #, q[i][-1] - q[i][0] ):
		
	mini = 9999999
	
	cnt = 0
	cnt2 = 0
	fin = 0
	for i, j in q:
		#print(i,j)
		cnt3 = 0
		for rw in nums:
			cnt2 +=1
			
			for nm in rw:
				
				if i <= nm <= j:
					cnt+=1
					
					if cnt == cnt2 :
						
						#print(rw,"   ",i,nm, j)
						
						if rw in nums:
							cnt3+=1
							#print(cnt3)
							if cnt3 == len(nums):
								#print(rw,"   ",i,nm, j)
								#cnt3 = 0
								mini = min(mini, j - i)
								if j - i == mini :
									fin =  [i, j] 
									
					cnt = 0
					cnt2 = 0
					
	return fin 

	
			
nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
#Output: [20,24]

print( do(nums) )


nums = [[4,10,15,24,22],[0,9,12,20],[5,18,22,30]]

print( do(nums) )
#Output: [20,22]

nums = [[1,2,3],[1,2,3],[1,2,3]]
#Output: [1,1]

print( do(nums) )
