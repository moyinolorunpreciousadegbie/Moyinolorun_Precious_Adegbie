
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


def main(s):
	q = []
	#print(do(s) )
	for word in do(s):
		if word == word[::-1]  :
			q.append(word)

			#print(q)
	
	return len(q[0]) * len(q[1]),  q




s = "ababbb"
#Output: 9
print( main(s)  )


s = "zaaaxbbby"
#Output: 9

print( main(s)  )