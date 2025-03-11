t = 8
li = [1,2,3,4,5,6,7,8]

FI = 21
LS = 29

for i in range(t,0,-1):
#for i in range(1,t+1)
	#print(i , t-i+1)
	togo = t-i+1
	
	ii = 0
	for rn in range(togo):
		print(li[rn:i+ii],[rn,i+ii], [rn+FI,i+ii+FI])
		
		ii+=1
	
	
	
