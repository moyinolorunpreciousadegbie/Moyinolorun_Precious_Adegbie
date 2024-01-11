
def do(s):
	
	q = []	
	qq = []
	for r in range( 1,len(s)):
		
		q.append( [s[0:r]])
		qq.append( [s[r-len(s):len(s)]])
			
		#print(q, "pref")
	
	
	qq=qq[::-1]
	#print(qq,"suff")
	mx=0
	for on in q:
		for onn in qq:
			if on == onn:
				mx= max(mx, len(on) )
				if len(on) == mx:
					fin = on
					break
	return fin[0]



s = "level"
#Output: "l"
#Explanation: s contains 4 prefix excluding itself ("l", "le", "lev", "leve"), and suffix ("l", "el", "vel", "evel"). The largest prefix which is also suffix is given by "l".


print(do(s))



s = "ababab"
#Output: "abab

print(do(s))