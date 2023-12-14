def do(s):
	
	q = []
	for ii in range( 2, len(s) +1): #
		for t in range(len(s)-1):
			for h in range(0,ii,ii-1):  # STEP
				if(h+t < len(s) and ii- h + t - 1 < len(s) ):
					
					q.append([h+t , ii-h-1 + t])
										
	q = q[0::2]
	
	qq = []
	for rw in range(len(q)):
		
		qq.append(  s[q[rw][0] : q[rw][1]+1 ]  )
	
	
	qq = qq[::-1]  # reverse 
	qq = qq[1::]  # exclude banana FULL WORD
	#print(qq)
	
	for i in range(len(qq)):
		for j in range(len(qq)):
				if qq[i] == qq[j] and i !=j: return qq[i]
			
	for i in range(len(qq)):
		for j in range(len(qq)):
				if qq[i] != qq[j] and i !=j: return " "
		

s = "banana"
#Output: "ana"

print( do(s) )

s = "abcd"
#Output: ""
print( do(s) )