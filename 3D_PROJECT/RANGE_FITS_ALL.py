#!/usr/bin/env python3

class SegmentTree:
	def __init__(self):
		
		
		self.intercept = []
		
		
	def  query( self, left, right  , lis_range ) :
		# query(  [mn , mx] , lis_range ) :
		
		
		
		mid = (left + right) // 2
		
		
		
		
		#if qright < left or right < qleft or left > right:
			#return 0
		
		
		cn  = 0 
		for  qleft , qright in lis_range:
			if qright < left or right < qleft or left > right:	 # DOES NOT FIT ATLEAST 1
				return
			if qleft <= left and right <= qright   : # FITS ONE THEN COUNT ++
				cn += 1
				
				
				
			
			
			
			
		if cn == len(lis_range): # FITS ALL
			if left not in self.intercept : self.intercept.append(left)
			if right not in self.intercept : self.intercept.append(right)	
			return
			
			
		
		
		if left == mid == right: return
		
		
		
		                      #>>>>>>>
		if left <= mid < right  :   #or (left==mid==right): 
		
			self.query(left, mid, lis_range)
			
			self.query(mid+1, right, lis_range)
			
			return
	
	
		
	
		
		

def lengthOfLIS( lis_range ) :
	
	rangg = []
	mn = float('inf')
	mx = -float('inf')
	for mnn, mxx in lis_range:
		mn = min(mn, mnn)
		mx = max(mx, mxx)
		
	segmentTree = SegmentTree(   )
			
	segmentTree.query( int(mn), int(mx)   , lis_range ) 
						
	return [ min(segmentTree.intercept) , max(segmentTree.intercept)  ]  #  max(segmentTree.intercept)  -  min(segmentTree.intercept) 

L = [
[0,10],
[3,8 ],
[0,8 ],
[3,10],
[0,20],
[2,20] ]


print( lengthOfLIS( L ))     

#  old function works on 2 ranges [3,8], [0,8] . This functions works on multiple (> 2) for overkill
	
# if ans != [] :
 #