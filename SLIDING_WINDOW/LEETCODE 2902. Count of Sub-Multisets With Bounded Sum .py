
def combinationSum2(candidates, target):   # LEETCODE 40, BACKTRACKING
		candidates.sort()
	
		res = []
	
		def backtrack(cur, pos, target):
			if target == 0:
				res.append(cur.copy())
				return
			if target <= 0:
				return
			
			prev = -1
			for i in range(pos, len(candidates)):
				if candidates[i] == prev:   #  -1 IS JUST GOING REDUCE THE ANSWER (<= 0  OR < 1)  WILL ADD !!! POSITIVE NUMBERS , (CONTINUE) SKIPS NEGATIVES AND ZERO(0)
					continue
				cur.append(candidates[i])
				backtrack(cur, i + 1, target - candidates[i])  # +1  INDEX (NO DUPLICATE !!)
				cur.pop()  #  APPEND AND POP , ADD/REMOVE PER INDEX FOR TESTING
				prev = candidates[i]
				
		backtrack([], 0, target)
		return res


def do(l, r, nums):
	
	
	q = []
	for i in range(l,r+1):
		for rr in combinationSum2(nums, i) :
			if rr not in q:
				q.append(rr)
	print(q,"  =  " ,len(q))
				
nums = [2,1,4,2,7]
l = 1
r = 5
#Output: 7    {1}, {2}, {4}, {2, 2}, {1, 2}, {1, 4}, and {1, 2, 2}.
do(l, r, nums)


nums = [1,2,2,3]
l = 6
r = 6
#Output: 1
do(l, r, nums)

nums = [1,2,1,3,5,2]
l = 3
r = 5
#Output: 9   {3}, {5}, {1, 2}, {1, 3}, {2, 2}, {2, 3}, {1, 1, 2}, {1, 1, 3}, and {1, 2, 2}.
do(l, r, nums)