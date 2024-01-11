#!/usr/bin/env python3

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
	
	
	return qq


def main(s):
	q = set()
	#print(do(s) )
	cn=0
	ser = list( set(do(s))  )
	possibilities = set() 
	
	possibilities = sorted(ser, key = lambda item: ( item), reverse = True)
		
	#print(possibilities[0])
				
	return possibilities[0]


s = "abab"
#Output: "bab"
#Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. The lexicographically maximum substring is "bab".


print(  main(s)  )


s = "leetcode"
#Output: "tcode"

print(  main(s)  )