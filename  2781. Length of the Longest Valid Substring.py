from collections import defaultdict
#  2781. Length of the Longest Valid Substring    THIS IS THE WORST SOLUTION. BETTER SOLUTIONS OUT THERE. 
def find(lst, lst2):
	
	#for i in lst:
	for j in lst2:
		if j in lst:
			return True
	return False

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
	
def main(word, forbidden):
	
	substit = do(word)
	#print( len(substit),"substit")
	adj = defaultdict(list)
	
	for sub in substit:
		#print(sub)
		se = set()
		for subsub in do(sub) :
			if subsub not in se:
				adj[sub].append(subsub)
				se.add(subsub)
			
				#		print(sub, adj[sub])
	q = []
	for sub in substit:
		if  sub not in forbidden :
			adj[sub].append(sub)
		if not find( adj[sub] , forbidden) :
			
			q.append( adj[sub] )
			#print(q)
	mx = 0		
	for rw in q:
		for rww in rw:
			mx = max(mx, len(rww))
			
	return  mx
word = "cbaaaabc"
forbidden = ["aaa","cb"]
#Output: 4
#Explanation: There are 11 valid substrings in word: "c", "b", "a", "ba", "aa", "bc", "baa", "aab", "ab", "abc" and "aabc". The length of the longest valid substring is 4. 

print( main(word, forbidden)  )



word = "leetcode"
forbidden = ["de","le","e"]
#Output: 4
#Explanation: There are 11 valid substrings in word: "l", "t", "c", "o", "d", "tc", "co", "od", "tco", "cod", and "tcod". The length of the longest valid substring is 4.
print( main(word, forbidden)  )