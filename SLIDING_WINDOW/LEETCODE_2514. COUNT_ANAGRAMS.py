#!/usr/bin/env python3
import collections

	
	
	
# Python program to check if two strings are 
# Permutations of each other
NO_OF_CHARS = 256

# Function to check whether two strings are
# Permutation of each other
def arePermutation(str1, str2):
	
	# Create two count arrays and initialize
	# all values as 0
	count1 = [0] * NO_OF_CHARS
	count2 = [0] * NO_OF_CHARS
	
	# For each character in input strings,
	# increment count in the corresponding
	# count array
	for i in str1:
		count1[ord(i)]+=1
		
	for i in str2:
		count2[ord(i)]+=1
		
	# If both strings are of different length.
	# Removing this condition will make the 
	# program fail for strings like
	# "aaca" and "aca"
	if len(str1) != len(str2):
		return 0
	
	# Compare count arrays
	for i in range(NO_OF_CHARS):
		if count1[i] != count2[i]:
			return 0
		
	return 1

def shapenew(width , lent,  mat):
	
	vis2 = [[0] * width for _ in range(   lent )]
	for r in range(lent):
		for c in range(width):
			index = r *   width   + c
			
			vis2[r][c] = mat[index]
			
	return vis2

def shape(new , mat):
	
	mat2 = []
	for i in range(len(mat)):
		if mat[i] != ' ':
			mat2.append( mat[i] )
	
	R = len(new)
	vis2 = [[]  for _ in range(R)]
	for r in range(R):
		for c in range(  len(new[r])  ):
			C = len(new[r]) 
			index = r * C + c
			
			vis2[r].append(mat2[index] ) 
			
	return vis2
	
def permuteUnique( nums):
	result = []
	counter = collections.Counter(nums)
		
	def backtrack(perm, counter):
		if len(perm) == len(nums):
			result.append(perm.copy())
				
		for n in counter:
			if counter[n] == 0:
				continue
			perm.append(n)
			counter[n] -= 1
			backtrack(perm, counter)
			perm.pop()
			counter[n] += 1
				
	backtrack([], counter)
		
	return result





def anagram(s):



	t = ['#'] * len(s)

	for i , val in  enumerate(s):
		if val != ' ':
			t[i] = i   #  append index of letters not empty ' ' string
		
			#print(t,'t')

	nm  = 0

	for i in t :
		if i == '#':
			nm +=1

	q = [[] for _ in range(nm+1)]  # nm + 1  means 1 '#' divides string to 2 ,  2 '#' divides string to 3 , and so on to get the groupings of full string for rows amounts
	j = 0
	for i in t:
		if i != '#':
			q[j].append(i)
		if i == '#':
			j+=1   #  skip '#' to q next row 
		
			#print(q, '{[')

		
	qq = [ ] 



	for i in q:
		if len(i) == 0:   #  skip empty rows
			continue
	
		qq.append(i)
	
		
	#print(qq,"m")  ###  THIS  [[0, 1, 2], [4, 5, 6]] 


	nw = [[] for _ in range(len(qq) ) ]

	o = -1
	for i in qq:
		o += 1       # increament per row
		for ii in i:
		
			nw[o].append( s[ii] )    #   switch from index to letter 
		
			#print(nw,"new")  # [['t', 'o', 'o'], ['h', 'o', 't']] new
	
	qs = []
	for i in range(len(s)):
		if s[i]  == ' ':   #  append index of places with empty string  ' '
			qs.append(i)
		
		#print(qs, 'qs') # [3] qs
	
	
		#print()
		
		
#print(permuteUnique( s))
		
	ms = []
	for i in qs:
		for h in permuteUnique( s) :
		
			if h[i]  == ' ':     #  if those permutation share the index with empty string  ' ' append
				ms.append( shape(nw, h))	

	
	
			
	qw = []
	for i in range(len(ms) ):
		V = ms[i] 
	#print(V)
		if V != nw:
			for i, t in enumerate(V):
				t = ''.join(t)
				nw[i] = ''.join(nw[i])
				if arePermutation(nw[i], t) == 1 :    #  if they are string permutation of each other 
					qw.append(t)
				#print(i, t,end=" ")
				#print()
		
				#print( qw ,'qw')  # answer



	width = len(nw)
	length = len(qw) // len(nw)
	#print( length ,' = length' , '||',width , ' = width')		 

	return shapenew(width , length,  qw) ,len(  shapenew(width , length,  qw) )   
			

	
	
s = "too hot"
print(   anagram(s))
print()

s = "aa"
#Output: 1
print(   anagram(s))
print()
"""
s = " too hot "
print(   anagram(s))
print()

s = "t oo ho t"
print(   anagram(s))
print()

s = " too hot"
print(   anagram(s))
print()


s = "t oo hot"
print(   anagram(s))
print()

s = "too hot "
print(   anagram(s))
print()

s = "too ho t"
print(   anagram(s))
print()


"""