from itertools import combinations

def main(s):
	
	ser = set()
	
	for i in range(1, len(s)+1):
		for se in  combinations(s, i) :
			ser.add(se)
	return len(ser), ser

s = "abc"
#Output: 7
print(main(s) )

s = "aba"
#Output: 6
print(main(s) )


s = "aaa"
#Output: 3
print(main(s) )