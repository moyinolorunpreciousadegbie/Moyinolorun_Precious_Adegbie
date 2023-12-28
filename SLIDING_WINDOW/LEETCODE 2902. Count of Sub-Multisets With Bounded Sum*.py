def subsetsWithDup( nums) :
		res = []
		nums.sort()
	
		def backtrack(i, subset):
			if i == len(nums):
				res.append(subset[::])
				return
			
			# All subsets that include nums[i]
			subset.append(nums[i])
			backtrack(i + 1, subset)
			subset.pop()
			# All subsets that don't include nums[i]
			while i + 1 < len(nums) and nums[i] == nums[i + 1]:
				i += 1
			backtrack(i + 1, subset)
			
		backtrack(0, [])
		return res

def do(l, r, nums):
	q=[]
	for rw in subsetsWithDup( nums) :
		if l <= sum(rw) <=  r:
			q.append(rw)
	
	return q, len(q)
			




#6 <=   <= 6


nums = [1,2,2,3]
l = 6
r = 6
#Output: 1
print(  do(l, r, nums))
print()

nums = [2,1,4,2,7]
l = 1
r = 5
#Output: 7
print(  do(l, r, nums))
print()

nums = [1,2,1,3,5,2]
l = 3
r = 5
#Output: 9
print(  do(l, r, nums))
print()