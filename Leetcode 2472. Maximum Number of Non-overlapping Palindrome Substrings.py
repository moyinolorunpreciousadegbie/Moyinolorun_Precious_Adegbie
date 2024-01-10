
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
	qq = qq[1::]  # exclude banana FULL WORD
	#print(qq)
	
	for i in range(len(word)):
		qq.append(word[i])
	return qq


def main(s, k):
	q = []
	#print(do(s) )
	for word in do(s):
		if word == word[::-1] and len(word) >= k:
			q.append(word)

			#print(q)
			
	return q, len(q)
s = "abaccdbbd"
k = 3
#Output: 2
#Explanation: We can select the substrings underlined in s = "abaccdbbd". Both "aba" and "dbbd" are palindromes and have a length of at least k = 3.
#It can be shown that we cannot find a selection with more than two valid substrings.


print( main(s, k)  )


s = "adbcda"
k = 2
#Output: 0

print( main(s, k)  )