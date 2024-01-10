from itertools import combinations

def do(s):
	
	q = []

	for rw in combinations(s,5):
		#print( rw )
		for i in range(len(rw)) :
			if rw == rw[::-1]: 
				q.append(rw)
				break
				
	return q, len(q)




s = "103301"
#Output: 2
#Explanation: 
#There are 6 possible subsequences of length 5: "10330","10331","10301","10301","13301","03301". 
#Two of them (both equal to "10301") are palindromic.
print(do(s) )


s = "0000000"
#Output: 21
print(do(s) )


s = "9999900000"
#Output: 2
print(do(s) )