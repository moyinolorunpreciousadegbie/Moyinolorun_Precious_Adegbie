#!/usr/bin/env python3

class Point:
	def __init__(self, a=-1, b=-1, c=-1):
		self.x = a
		self.y = b
		self.z = c
		
class Octree:
	TopLeftFront = 0
	TopRightFront = 1
	BottomRightFront = 2      # 0 ------->
	BottomLeftFront = 3       #          |
	TopLeftBottom = 4         #          |
	TopRightBottom = 5        # 7 <------|
	BottomRightBack = 6
	BottomLeftBack = 7
	
	#class Octree:
	#def __init__(self, x_min, y_min, z_min, x_max, y_max, z_max):
	
		# Initialize the octree with bounds
		#pass
	
		#def insert(self, x, y, z):
		#self.children = [None] * 8  # Assuming 8 children for a 3D space
		#self.point = None
		# Insert a point into the octree
		#pass
	
		#def find(self, x, y, z):
		# Find a point in the octree
		#return False  # Placeholder return value
	
	def __init__(self, x=None, y=None, z=None, x2=None, y2=None, z2=None):
	#def __init__(self, x , y , z , x2 , y2 , z2 ):
		#x , y , z , x2 , y2 , z2 = x_min, y_min, z_min, x_max, y_max, z_max 
		
		if x is not None and y is not None and z is not None and x2 is None and y2 is None and z2 is None:
			# To declare point node
			self.point = Point(x, y, z)
		elif x is not None and y is not None and z is not None and x2 is not None and y2 is not None and z2 is not None:
			# This use to construct Octree with boundaries defined
			if x2 < x or y2 < y or z2 < z:
				print("boundary points are not valid")
				return
			
			self.point = None
			self.topLeftFront = Point(x, y, z)
			self.bottomRightBack = Point(x2, y2, z2)
			
			# Assigning None to the children
			#self.children = [None] * 8
			self.children = {}
			for i in range(self.TopLeftFront, self.BottomLeftBack + 1):
				#self.children[i] = Octree()
				if i not in self.children :
					self.children[i] = Octree()
		else:
			# To declare empty node
			self.point = Point()
			
			
			
#            #class Octree:
	def insert(self, x, y, z):
			#print("9090909")
			# If the point already exists in the octree
		if self.find(x, y, z):
			print("Point already exist in the tree")
			return 
			#return True # x
		
		
		
			# If the point is out of bounds
		if (x < self.topLeftFront.x or x > self.bottomRightBack.x or
				y < self.topLeftFront.y or y > self.bottomRightBack.y or
				z < self.topLeftFront.z or z > self.bottomRightBack.z):
			print("Point is out of bound")
			return
	
			# Binary search to insert the point
		midx = (self.topLeftFront.x + self.bottomRightBack.x) // 2
		midy = (self.topLeftFront.y + self.bottomRightBack.y) // 2
		midz = (self.topLeftFront.z + self.bottomRightBack.z) // 2
	
		pos = -1
	
			# Checking the octant of the point
		if x <= midx:
			if y <= midy:
				pos = self.TopLeftFront if z <= midz else self.TopLeftBottom
			else:
				pos = self.BottomLeftFront if z <= midz else self.BottomLeftBack
		else:
			if y <= midy:
				pos = self.TopRightFront if z <= midz else self.TopRightBottom
			else:
				pos = self.BottomRightFront if z <= midz else self.BottomRightBack
				
		print(pos)
				
			# If an internal node is encountered
		#print( pos, self.children, len(self.children), (x,y,z) )   ## <<<<<<
													#|||
		if self.children[pos].point is None        or  self.children[pos].point == Point() :
			self.children[pos].insert(x, y, z)
			return 
	
			# If an empty node is encountered       #|||
		elif self.children[pos].point.x == -1      or  self.children[pos].point.y == -1  or self.children[pos].point.z == -1 :
			del self.children[pos]                  # x
			self.children[pos] = Octree(x, y, z)
			return 
		else:
			x_ = self.children[pos].point.x
			y_ = self.children[pos].point.y
			z_ = self.children[pos].point.z
			del self.children[pos]                  # x
			
			
			#x = self.children[pos].point.x # x
			#y = self.children[pos].point.y # x
			#z = self.children[pos].point.z # x
			
			
			self.children[pos] = None
			
			
			if pos == self.TopLeftFront:
				#print("1")
				self.children[pos] = Octree(self.topLeftFront.x,
															self.topLeftFront.y,
															self.topLeftFront.z,
															midx,
															midy,
															midz)
			elif pos == self.TopRightFront:
				#print("2")
				self.children[pos] = Octree(midx + 1,
															self.topLeftFront.y,
															self.topLeftFront.z,
															self.bottomRightBack.x,
															midy,
															midz)
			elif pos == self.BottomRightFront:
				#print("3")
				self.children[pos] = Octree(midx + 1,
															midy + 1,
															self.topLeftFront.z,
															self.bottomRightBack.x,
															self.bottomRightBack.y,
															midz)
			elif pos == self.BottomLeftFront:
				#print("4")
				self.children[pos] = Octree(self.topLeftFront.x,
															midy + 1,
															self.topLeftFront.z,
															midx,
															self.bottomRightBack.y,
															midz)
			elif pos == self.TopLeftBottom:
				#print("5")
				self.children[pos] = Octree(self.topLeftFront.x,
															self.topLeftFront.y,
															midz + 1,
															midx,
															midy,
															self.bottomRightBack.z)
			elif pos == self.TopRightBottom:
				#print("6")
				self.children[pos] = Octree(midx + 1,
															self.topLeftFront.y,
															midz + 1,
															self.bottomRightBack.x,
															midy,
															self.bottomRightBack.z)
			elif pos == self.BottomRightBack:
				#print("7")
				self.children[pos] = Octree(midx + 1,
															midy + 1,
															midz + 1,
															self.bottomRightBack.x,
															self.bottomRightBack.y,
															self.bottomRightBack.z)
			elif pos == self.BottomLeftBack:
				#print("8")
				self.children[pos] = Octree(self.topLeftFront.x,
															midy + 1,
															midz + 1,
															midx,
															self.bottomRightBack.y,
															self.bottomRightBack.z)
			self.children[pos].insert(x_, y_, z_)
			self.children[pos].insert(x, y, z)
			
			
			
				#class Node:
	#def __init__(self, top_left_front, bottom_right_back):
		#self.top_left_front = top_left_front
		#self.bottom_right_back = bottom_right_back
				#self.children = [None] * 8  # Assuming 8 children for a 3D space
				#self.point = None
				#print("KKKK") # topLeftFront    bottomRightBack
			
#
	def find(self, x, y, z):
		#print("BOUND")
		# If point is out of bound
		
		if (x < self.topLeftFront.x or
			x > self.bottomRightBack.x or
			y < self.topLeftFront.y or
			y > self.bottomRightBack.y or
			z < self.topLeftFront.z or
			z > self.bottomRightBack.z):
			return False
	
		#if (x < self.top_left_front.x or
			#x > self.bottom_right_back.x or
			#y < self.top_left_front.y or
			#y > self.bottom_right_back.y or
			#z < self.top_left_front.z or
			#z > self.bottom_right_back.z):
			#return False
	
		# Otherwise perform binary search for each ordinate
		midx = (self.topLeftFront.x + self.bottomRightBack.x) // 2
		midy = (self.topLeftFront.y + self.bottomRightBack.y) // 2
		midz = (self.topLeftFront.z + self.bottomRightBack.z) // 2
	
		#midx = (self.top_left_front.x + self.bottom_right_back.x) // 2 # x
		#midy = (self.top_left_front.y + self.bottom_right_back.y) // 2 # x
		#midz = (self.top_left_front.z + self.bottom_right_back.z) // 2 # x
	
		pos = -1
	
		# Deciding the position where to move
		if x <= midx:
			if y <= midy:
				pos = 0 if z <= midz else 1  # TopLeftFront or TopLeftBottom
			else:
				pos = 2 if z <= midz else 3  # BottomLeftFront or BottomLeftBack
		else:
			if y <= midy:
				pos = 4 if z <= midz else 5  # TopRightFront or TopRightBottom
			else:
				pos = 6 if z <= midz else 7  # BottomRightFront or BottomRightBack
				
				#print(pos)
				
		# If an internal node is encountered
		if self.children[pos] is not None and self.children[pos].point is None:
			return self.children[pos].find(x, y, z)
	
		# If an empty node is encountered                                          # |||
		elif self.children[pos] is not None and ( self.children[pos].point.x == -1   and self.children[pos].point.y == -1 and self.children[pos].point.z == -1 ):
			return False
		else:
			# If node is found with the given value
			if (x == self.children[pos].point.x and
				y == self.children[pos].point.y and
				z == self.children[pos].point.z       and x != -1 and y!= -1 and z != -1 ):
													#
				return True
	
	
		return False
		#return True # x
	
	
	
	
	
	
	
def main():
	tree = Octree(1, 1, 1, 5, 5, 5)
	
	five = 5 #3#2
	
	for i in range(1 , five + 1):
		for j in range(1 , five + 1):
			for k in range(1 , five + 1):
				print( i, j, k )
				tree.insert(i, j, k)
				
	
				
	
if __name__ == "__main__":
	main()
	
	
"""


# If an empty node is encountered                                          # |||
elif self.children[pos] is not None and ( self.children[pos].point.x == -1   and self.children[pos].point.y == -1 and self.children[pos].point.z == -1 ):
	return False
else:
	# If node is found with the given value
	if (x == self.children[pos].point.x and
		y == self.children[pos].point.y and
		z == self.children[pos].point.z       and x != -1 and y!= -1 and z != -1 ):
											#
		return True
	

return False
#return True # x


"""
	