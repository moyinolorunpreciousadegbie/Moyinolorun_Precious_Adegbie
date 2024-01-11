from itertools import combinations

def main(word1, word2):
	q = []
	#print(do(s) )
	mx=0
	for i in range(1, len(word1)+1):
		for j in range(1, len(word2)+1):	
			for word11 in combinations(word1,i):
				for word22 in combinations(word2, j):
					nw = list(word11)  +  list(word22)
					nww = list(word22)  +  list(word11)
					if nw == nw[::-1]    or   nww == nww[::-1]   :
						mx = max(mx, len(nw))
						mx = max(mx, len(nww))
	return mx


word1 = "cacb"
word2 = "cbba"
#Output: 5

print( main(word1, word2)  )


word1 = "ab"
word2 = "ab"
#Output: 3
print( main(word1, word2)  )