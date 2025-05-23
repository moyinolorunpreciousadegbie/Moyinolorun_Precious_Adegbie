#!/usr/bin/env python3

from math import inf


class LazySegmentTree:
	def __init__(self, arr):
		self.arr = len(arr)
		self.arr_size = len(arr)
		self.size = arr #   4 * self.arr_size    #  4 x 8 = 32      + 1
		self.tree = [0] * self.arr
		
		
		self.nap = {}
		
		self.mp = {}
		
		self.build_tree(0, 0, self.arr, 2)
		
		
		
	def build_tree(self, node, start, end, two):
		
		self.mp[node] = (start, end)
		
		#print(start, end,"********", two)
		 
		if two not in self.nap : self.nap[two] = []
		self.nap[two].append((start, end))
		
		if start == end:
			#self.tree[node] = self.arr[start]
			print("JON JONES")
			return #self.tree[node]
		
		
		q = []
		#q = set()  ### <<<<<<<
		for y in  range( 1, two):
			this = start + (y * ((end-start)/two)   )
			#print( int(this) , end=" ")
			if int(this) in q :
				if (start, start) not in self.nap[two] :   #
					self.nap[two].append((start, start))   #
				if (end, end) not in self.nap[two] :       #
					self.nap[two].append((end, end))       #
				return
			q.append(int(this) )
			#q.add(int(this) )   ### <<<<<<<
		#print()
		
		
		
		
		q = [start] + q + [end]
		#q = [start] + list(q) + [end] ### <<<<<<<
		#print(q)
		for  y in range(len(q)-1):
			#q[y] , q[y+1]
			#print( q[y] , q[y+1] )
			self.build_tree(node , q[y] , q[y+1], two+1)  # two+1
			#self.tree[node] = max(
			#self.build_tree(node * 2 + 1, start, mid , two+1),
			#self.build_tree(node * 2 + 2, mid + 1, end, two+1), )
				
			#return self.tree[node]
		
class Solution:
	def fallingSquares(self, ttt ):
		
		st = LazySegmentTree([0] * ttt) # 
				
		print(st.nap , len( st.nap ))
		
		
		
		#print( [len(v)  for k, v in st.nap.items() ] )
		
		am = 0
		for k, v in st.nap.items() :
			am += len(v)
			
			#print(am)
		
		
		
S = Solution()

ii = 1
#for i in range(2,7):
	#ii *= i

	
print( S.fallingSquares(32) )  # 152      32
	#print( S.fallingSquares(ii) )  # 152      32



print()
print()

print( S.fallingSquares(156) ) 