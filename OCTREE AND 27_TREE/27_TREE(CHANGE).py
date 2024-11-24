#!/usr/bin/env python3

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
	
	North_West_Surface  = 0 #// tlf->x, tlf->y,tlf->z,          _1_3x,_1_3y, _1_3z   0                   
	North_Middle_Surface = 1 #// _1_3x + 1, tlf->y, tlf->z,       _2_3x,_1_3y ,_1_3z  1
	North_East_Surface   = 2  #// _2_3x + 1, tlf->y, tlf->z,       brb->x , _1_3y ,_1_3z  2
	Equator_West_Surface = 3 #// tlf->x, _1_3y + 1, tlf->z,        _1_3x, _2_3y , _1_3z  3
	Equator_Middle_Surface = 4 #//  _1_3x + 1, _1_3y + 1, tlf->z,       _2_3x,_2_3y ,_1_3z  4
	Equator_East_Surface =  5 #//   _2_3x + 1, _1_3y + 1,tlf->z,       brb->x,_2_3y ,_1_3z  5
	South_West_Surface  = 6 #//   tlf->x , _2_3y + 1, tlf->z,        _1_3x,brb->y ,_1_3z  6
	South_Middle_Surface =  7 #//   _1_3x + 1, _2_3y + 1, tlf->z,        _2_3x, brb->y ,_1_3z  7
	South_East_Surface =   8 #//   _2_3x + 1, _2_3y + 1, tlf->z,        brb->x,brb->y ,_1_3z  8
	
	#//  _1_3z + 1, _2_3z Down1
	North_West_Down1 = 9 #// tlf->x, tlf->y,_1_3z + 1,          _1_3x,_1_3y, _2_3z   9                  
	North_Middle_Down1 = 10 #// _1_3x + 1, tlf->y, _1_3z + 1,       _2_3x,_1_3y ,_2_3z  10
	North_East_Down1 =  11 #// _2_3x + 1, tlf->y, _1_3z + 1,       brb->x , _1_3y ,_2_3z  11
	Equator_West_Down1 = 12 #//  tlf->x, _1_3y + 1, _1_3z + 1,        _1_3x, _2_3y , _2_3z  12
	Equator_Middle_Down1 = 13 #//  _1_3x + 1, _1_3y + 1, _1_3z + 1,       _2_3x,_2_3y ,_2_3z  13
	Equator_East_Down1  = 14 #//  _2_3x + 1, _1_3y + 1,_1_3z + 1,       brb->x,_2_3y ,_2_3z  14
	South_West_Down1 =  15 #//   tlf->x , _2_3y + 1, _1_3z + 1,        _1_3x,brb->y ,_2_3z  15
	South_Middle_Down1 =  16 #//   _1_3x + 1, _2_3y + 1, _1_3z + 1,        _2_3x, brb->y ,_2_3z  16
	South_East_Down1   =  17 #//  _2_3x + 1, _2_3y + 1, _1_3z + 1,        brb->x,brb->y ,_2_3z  17
	
	#//    _2_3z + 1, ,brb->z     Down2
	North_West_Down2 = 18 #//tlf->x, tlf->y,_2_3z + 1,          _1_3x,_1_3y, brb->z    18                   
	North_Middle_Down2 = 19 #//_1_3x + 1, tlf->y, _2_3z + 1,       _2_3x,_1_3y ,brb->z   19
	North_East_Down2  = 20 #// _2_3x + 1, tlf->y, _2_3z + 1,       brb->x , _1_3y ,brb->z   20
	Equator_West_Down2 = 21 #//  tlf->x, _1_3y + 1, _2_3z + 1,        _1_3x, _2_3y , brb->z   21
	Equator_Middle_Down2 = 22 #// _1_3x + 1, _1_3y + 1, _2_3z + 1,       _2_3x,_2_3y ,brb->z   22
	Equator_East_Down2 =  23 #//  _2_3x + 1, _1_3y + 1, _2_3z + 1,       brb->x,_2_3y ,brb->z   23
	South_West_Down2  =   24 #// tlf->x , _2_3y + 1, _2_3z + 1,        _1_3x,brb->y ,brb->z   24
	South_Middle_Down2 = 25 #//   _1_3x + 1, _2_3y + 1, _2_3z + 1,        _2_3x, brb->y ,brb->z   25
	South_East_Down2  =  26 # //   _2_3x + 1, _2_3y + 1, _2_3z + 1,        brb->x,brb->y ,brb->z   26
	
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
		
		#print(x,y,z,x2,y2,z2)
		
		if x is not None and y is not None and z is not None and x2 is None and y2 is None and z2 is None:
			# To declare point node
			self.point = Point(x, y, z)
		elif x is not None and y is not None and z is not None and x2 is not None and y2 is not None and z2 is not None:
			# This use to construct Octree with boundaries defined
			if x2 < x or y2 < y or z2 < z:
				print("boundary points are not valid")
				return
			
			self.point = None
			self.tlf = Point(x, y, z)  # topLeftFront
			self.brb = Point(x2, y2, z2)  # bottomRightBack
			
			# Assigning None to the children
			#self.children = [None] * 8
			self.children = {}
			#for i in range(self.TopLeftFront, self.BottomLeftBack + 1):
			for i in range(self.North_West_Surface, self.South_East_Down2 + 1):
				#self.children[i] = Octree()
				if i not in self.children :
					#self.children[i] = Octree()
					self.children[i] =  Octree()
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
		if (x < self.tlf.x or x > self.brb.x or
				y < self.tlf.y or y > self.brb.y or
				z < self.tlf.z or z > self.brb.z):
			print("Point is out of bound")
			return
	
			# Binary search to insert the point
		#midx = (self.topLeftFront.x + self.bottomRightBack.x) // 2
		#midy = (self.topLeftFront.y + self.bottomRightBack.y) // 2
		#midz = (self.topLeftFront.z + self.bottomRightBack.z) // 2
	
	
		_2 = 2.000000000000000
		_3 = 3.000000000000000
	
		#_1_3x = (self.tlf.x + self.brb.x) / _3
		#_2_3x = ((self.tlf.x + self.brb.x) / _3) * _2
	
		#_1_3y = (self.tlf.y + self.brb.y) / _3
		#_2_3y = ((self.tlf.y + self.brb.y) / _3) * _2
	
		#_1_3z = (self.tlf.z + self.brb.z) / _3
		#_2_3z = ((self.tlf.z + self.brb.z) / _3) * _2
	
		_1_3x = self.tlf.x + ((self.brb.x - self.tlf.x) / _3)
		_2_3x = self.tlf.x + (2 * ((self.brb.x - self.tlf.x) / _3))
	
		_1_3y = self.tlf.y + ((self.brb.y - self.tlf.y) / _3)
		_2_3y = self.tlf.y + (2 * ((self.brb.y - self.tlf.y) / _3))
	
		_1_3z = self.tlf.z + ((self.brb.z - self.tlf.z) / _3)
		_2_3z = self.tlf.z + (2 * ((self.brb.z - self.tlf.z) / _3))
	
		#_1_3xxx = self.brb.x - (2 * ((self.brb.x - self.tlf.x) / _3))
		#_2_3xxx = self.brb.x - ((self.brb.x - self.tlf.x) / _3)
	
		#_1_3yyy = self.brb.y - (2 * ((self.brb.y - self.tlf.y) / _3))
		#_2_3yyy = self.brb.y - ((self.brb.y - self.tlf.y) / _3)
	
		#_1_3zzz = self.brb.z - (2 * ((self.brb.z - self.tlf.z) / _3))
		#_2_3zzz = self.brb.z - ((self.brb.z - self.tlf.z) / _3)
	
	
	
	
	
	
		pos = -1
	
			# Checking the octant of the point
		#if x <= midx:
			#if y <= midy:
				#pos = self.TopLeftFront if z <= midz else self.TopLeftBottom
			#else:
				#pos = self.BottomLeftFront if z <= midz else self.BottomLeftBack
		#else:
			#if y <= midy:
				#pos = self.TopRightFront if z <= midz else self.TopRightBottom
			#else:
				#pos = self.BottomRightFront if z <= midz else self.BottomRightBack
	
			# If an internal node is encountered
		#print( pos, self.children, len(self.children), (x,y,z) )   ## <<<<<<
	
	
	
	
	
	
	
		_000000000000001 =   0.000000000000001 # 0.00001 ##
	
	
		# HERE
	
	
	
		North_West_Surface  = 0                  
		North_Middle_Surface = 1 
		North_East_Surface   = 2 
		Equator_West_Surface = 3
		Equator_Middle_Surface = 4 
		Equator_East_Surface =  5 
		South_West_Surface  = 6 
		South_Middle_Surface =  7 
		South_East_Surface =   8 
	
		#//  _1_3z + 1, _2_3z Down1
		North_West_Down1 = 9                  
		North_Middle_Down1 = 10 
		North_East_Down1 =  11 
		Equator_West_Down1 = 12 
		Equator_Middle_Down1 = 13 
		Equator_East_Down1  = 14 
		South_West_Down1 =  15 
		South_Middle_Down1 =  16 
		South_East_Down1   =  17 
	
		#//    _2_3z + 1, ,brb->z     Down2
		North_West_Down2 = 18                  
		North_Middle_Down2 = 19 
		North_East_Down2  = 20 
		Equator_West_Down2 = 21 
		Equator_Middle_Down2 = 22 
		Equator_East_Down2 =  23 
		South_West_Down2  =   24 
		South_Middle_Down2 = 25 
		South_East_Down2  =  26 
	
		#   self.
	
		if self.tlf.z <= z <= _1_3z:
			if self.tlf.x <= x <= _1_3x:
				if self.tlf.y <= y <= _1_3y:
					pos = North_West_Surface
			if _1_3x + _000000000000001 <= x <= _2_3x:
				if self.tlf.y <= y <= _1_3y:
					pos = North_Middle_Surface
			if _2_3x + _000000000000001 <= x <= self.brb.x:
				if self.tlf.y <= y <= _1_3y:
					pos = North_East_Surface
					
			if self.tlf.x <= x <= _1_3x:
				if _1_3y + _000000000000001 <= y <= _2_3y:
					pos = Equator_West_Surface
			if _1_3x + _000000000000001 <= x <= _2_3x:
				if _1_3y + _000000000000001 <= y <= _2_3y:
					pos = Equator_Middle_Surface
			if _2_3x + _000000000000001 <= x <= self.brb.x:
				if _1_3y + _000000000000001 <= y <= _2_3y:
					pos = Equator_East_Surface
					
			if self.tlf.x <= x <= _1_3x:
				if _2_3y + _000000000000001 <= y <= self.brb.y:
					pos = South_West_Surface
			if _1_3x + _000000000000001 <= x <= _2_3x:
				if _2_3y + _000000000000001 <= y <= self.brb.y:
					pos = South_Middle_Surface
			if _2_3x + _000000000000001 <= x <= self.brb.x:
				if _2_3y + _000000000000001 <= y <= self.brb.y:
					pos = South_East_Surface
					
		###############################################
					
		if _1_3z + _000000000000001 <= z <= _2_3z:
			if self.tlf.x <= x <= _1_3x:
				if self.tlf.y <= y <= _1_3y:
					pos = North_West_Down1
			if _1_3x + _000000000000001 <= x <= _2_3x:
				if self.tlf.y <= y <= _1_3y:
					pos = North_Middle_Down1
			if _2_3x + _000000000000001 <= x <= self.brb.x:
				if self.tlf.y <= y <= _1_3y:
					pos = North_East_Down1
					
			if self.tlf.x <= x <= _1_3x:
				if _1_3y + _000000000000001 <= y <= _2_3y:
					pos = Equator_West_Down1
			if _1_3x + _000000000000001 <= x <= _2_3x:
				if _1_3y + _000000000000001 <= y <= _2_3y:
					pos = Equator_Middle_Down1
			if _2_3x + _000000000000001 <= x <= self.brb.x:
				if _1_3y + _000000000000001 <= y <= _2_3y:
					pos = Equator_East_Down1
					
			if self.tlf.x <= x <= _1_3x:
				if _2_3y + _000000000000001 <= y <= self.brb.y:
					pos = South_West_Down1
			if _1_3x + _000000000000001 <= x <= _2_3x:
				if _2_3y + _000000000000001 <= y <= self.brb.y:
					pos = South_Middle_Down1
			if _2_3x + _000000000000001 <= x <= self.brb.x:
				if _2_3y + _000000000000001 <= y <= self.brb.y:
					pos = South_East_Down1
					
		############################################
					
		if _2_3z + _000000000000001 <= z <= self.brb.z:
			if self.tlf.x <= x <= _1_3x:
				if self.tlf.y <= y <= _1_3y:
					pos = North_West_Down2
			if _1_3x + _000000000000001 <= x <= _2_3x:
				if self.tlf.y <= y <= _1_3y:
					pos = North_Middle_Down2
			if _2_3x + _000000000000001 <= x <= self.brb.x:
				if self.tlf.y <= y <= _1_3y:
					pos = North_East_Down2
					
			if self.tlf.x <= x <= _1_3x:
				if _1_3y + _000000000000001 <= y <= _2_3y:
					pos = Equator_West_Down2
			if _1_3x + _000000000000001 <= x <= _2_3x:
				if _1_3y + _000000000000001 <= y <= _2_3y:
					pos = Equator_Middle_Down2
			if _2_3x + _000000000000001 <= x <= self.brb.x:
				if _1_3y + _000000000000001 <= y <= _2_3y:
					pos = Equator_East_Down2
					
			if self.tlf.x <= x <= _1_3x:
				if _2_3y + _000000000000001 <= y <= self.brb.y:
					pos = South_West_Down2
			if _1_3x + _000000000000001 <= x <= _2_3x:
				if _2_3y + _000000000000001 <= y <= self.brb.y:
					pos = South_Middle_Down2
			if _2_3x + _000000000000001 <= x <= self.brb.x:
				if _2_3y + _000000000000001 <= y <= self.brb.y:
					pos = South_East_Down2
					
					
		#print(self.children[pos], pos, "PPPPPP")
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
			
			
			
			
			
		if pos == North_West_Surface:
				self.tlf.x = self.tlf.x
				self.tlf.y = self.tlf.y
				self.tlf.z = self.tlf.z
				self.brb.x = _1_3x
				self.brb.y = _1_3y
				self.brb.z = _1_3z
				self.children[pos] = Octree(self.tlf.x, self.tlf.y, self.tlf.z, _1_3x, _1_3y, _1_3z)
			
		elif pos == North_Middle_Surface:
				self.tlf.x = _1_3x + _000000000000001
				self.tlf.y = self.tlf.y
				self.tlf.z = self.tlf.z
				self.brb.x = _2_3x
				self.brb.y = _1_3y
				self.brb.z = _1_3z
				self.children[pos] = Octree(_1_3x + _000000000000001, self.tlf.y, self.tlf.z, _2_3x, _1_3y, _1_3z)
			
		elif pos == North_East_Surface:
				self.tlf.x = _2_3x + _000000000000001
				self.tlf.y = self.tlf.y
				self.tlf.z = self.tlf.z
				self.brb.x = self.brb.x
				self.brb.y = _1_3y
				self.brb.z = _1_3z
				self.children[pos] = Octree(_2_3x + _000000000000001, self.tlf.y, self.tlf.z, self.brb.x, _1_3y, _1_3z)
			
		elif pos == Equator_West_Surface:
				self.tlf.x = self.tlf.x
				self.tlf.y = _1_3y + _000000000000001
				self.tlf.z = self.tlf.z
				self.brb.x = _1_3x
				self.brb.y = _2_3y
				self.brb.z = _1_3z
				self.children[pos] = Octree(self.tlf.x, _1_3y + _000000000000001, self.tlf.z, _1_3x, _2_3y, _1_3z)
			
		elif pos == Equator_Middle_Surface:
				self.tlf.x = _1_3x + _000000000000001
				self.tlf.y = _1_3y + _000000000000001
				self.tlf.z = self.tlf.z
				self.brb.x = _2_3x
				self.brb.y = _2_3y
				self.brb.z = _1_3z
				self.children[pos] = Octree(_1_3x + _000000000000001, _1_3y + _000000000000001, self.tlf.z, _2_3x, _2_3y, _1_3z)
			
		elif pos == Equator_East_Surface:
				self.tlf.x = _2_3x + _000000000000001
				self.tlf.y = _1_3y + _000000000000001
				self.tlf.z = self.tlf.z
				self.brb.x = self.brb.x
				self.brb.y = _2_3y
				self.brb.z = _1_3z
				self.children[pos] = Octree(_2_3x + _000000000000001 , _1_3y + _000000000000001, self.tlf.z, self.brb.x, _2_3y, _1_3z)
			
		elif pos == South_West_Surface:
				self.tlf.x = self.tlf.x
				self.tlf.y = _2_3y + _000000000000001
				self.tlf.z = self.tlf.z
				self.brb.x = _1_3x
				self.brb.y = self.brb.y
				self.brb.z = _1_3z
				self.children[pos] = Octree(self.tlf.x, _2_3y + _000000000000001, self.tlf.z, _1_3x, self.brb.y, _1_3z)
			
		elif pos == South_Middle_Surface:
				self.tlf.x = _1_3x + _000000000000001
				self.tlf.y = _2_3y + _000000000000001
				self.tlf.z = self.tlf.z
				self.brb.x = _2_3x
				self.brb.y = self.brb.y
				self.brb.z = _1_3z
				self.children[pos] = Octree(_1_3x + _000000000000001, _2_3y + _000000000000001, self.tlf.z, _2_3x, self.brb.y, _1_3z)
			
		elif pos == South_East_Surface:
				self.tlf.x = _2_3x + _000000000000001
				self.tlf.y = _2_3y + _000000000000001
				self.tlf.z = self.tlf.z      
				self.brb.x = self.brb.x
				self.brb.y = self.brb.y
				self.brb.z = _1_3z
				self.children[pos] = Octree(_2_3x + _000000000000001, _2_3y + _000000000000001, self.tlf.z, self.brb.x, self.brb.y, _1_3z)
			
			
			#############################################################################################################################################################
			
		elif pos == North_West_Down1:
				self.tlf.x = self.tlf.x
				self.tlf.y = self.tlf.y
				self.tlf.z = _1_3z + _000000000000001
				self.brb.x = _1_3x
				self.brb.y = _1_3y
				self.brb.z = _2_3z
				self.children[pos] = Octree(self.tlf.x, self.tlf.y, _1_3z + _000000000000001, _1_3x, _1_3y, _2_3z)
			
		elif pos == North_Middle_Down1:
				self.tlf.x = _1_3x + _000000000000001
				self.tlf.y = self.tlf.y
				self.tlf.z = _1_3z + _000000000000001
				self.brb.x = _2_3x
				self.brb.y = _1_3y
				self.brb.z = _2_3z
				self.children[pos] = Octree(_1_3x + _000000000000001, self.tlf.y, _1_3z + _000000000000001, _2_3x, _1_3y, _2_3z)
			
		elif pos == North_East_Down1:
				self.tlf.x = _2_3x + _000000000000001
				self.tlf.y = self.tlf.y
				self.tlf.z = _1_3z + _000000000000001
				self.brb.x = self.brb.x
				self.brb.y = _1_3y
				self.brb.z = _2_3z
				self.children[pos] = Octree(_2_3x + _000000000000001, self.tlf.y, _1_3z + _000000000000001, self.brb.x, _1_3y, _2_3z)
			
		elif pos == Equator_West_Down1:
				self.tlf.x = self.tlf.x
				self.tlf.y = _1_3y + _000000000000001
				self.tlf.z = _1_3z + _000000000000001
				self.brb.x = _1_3x
				self.brb.y = _2_3y
				self.brb.z = _2_3z
				self.children[pos] = Octree( self.tlf.x, _1_3y + _000000000000001, _1_3z + _000000000000001, _1_3x, _2_3y, _2_3z)
			
		elif pos == Equator_Middle_Down1:
				self.tlf.x = _1_3x + _000000000000001
				self.tlf.y = _1_3y + _000000000000001
				self.tlf.z = _1_3z + _000000000000001
				self.brb.x = _2_3x
				self.brb.y = _2_3y
				self.brb.z = _2_3z
				self.children[pos] = Octree(_1_3x + _000000000000001, _1_3y + _000000000000001, _1_3z + _000000000000001, _2_3x, _2_3y, _2_3z)
			
		elif pos == Equator_East_Down1:
				self.tlf.x = _2_3x + _000000000000001
				self.tlf.y = _1_3y + _000000000000001
				self.tlf.z = _1_3z + _000000000000001
				self.brb.x = self.brb.x
				self.brb.y = _2_3y
				self.brb.z = _2_3z
				self.children[pos] = Octree(_2_3x + _000000000000001, _1_3y + _000000000000001, _1_3z + _000000000000001, self.brb.x, _2_3y, _2_3z)
			
		elif pos == South_West_Down1:
				self.tlf.x = self.tlf.x
				self.tlf.y = _2_3y + _000000000000001
				self.tlf.z = _1_3z + _000000000000001
				self.brb.x = _1_3x
				self.brb.y = self.brb.y
				self.brb.z = _2_3z
				self.children[pos] = Octree(self.tlf.x, _2_3y + _000000000000001, _1_3z + _000000000000001, _1_3x, self.brb.y, _2_3z)
			
		elif pos == South_Middle_Down1:
				self.tlf.x = _1_3x + _000000000000001
				self.tlf.y = _2_3y + _000000000000001
				self.tlf.z = _1_3z + _000000000000001
				self.brb.x = _2_3x
				self.brb.y = self.brb.y
				self.brb.z = _2_3z
				self.children[pos] = Octree(_1_3x + _000000000000001, _2_3y + _000000000000001, _1_3z + _000000000000001, _2_3x, self.brb.y, _2_3z)
			
		elif pos == South_East_Down1:
				self.tlf.x = _2_3x + _000000000000001
				self.tlf.y = _2_3y + _000000000000001
				self.tlf.z = _1_3z + _000000000000001
				self.brb.x = self.brb.x
				self.brb.y = self.brb.y
				self.brb.z = _2_3z
				self.children[pos] = Octree(_2_3x + _000000000000001, _2_3y + _000000000000001, _1_3z + _000000000000001, self.brb.x, self.brb.y, _2_3z)
			
			
			#############################################################################################################################################################
			
		elif pos == North_West_Down2:
				self.tlf.x = self.tlf.x
				self.tlf.y = self.tlf.y
				self.tlf.z = _2_3z + _000000000000001
				self.brb.x = _1_3x
				self.brb.y = _1_3y
				self.brb.z = self.brb.z
				self.children[pos] = Octree(self.tlf.x, self.tlf.y, _2_3z + _000000000000001, _1_3x, _1_3y, self.brb.z)
			
		elif pos == North_Middle_Down2:
				self.tlf.x = _1_3x + _000000000000001
				self.tlf.y = self.tlf.y
				self.tlf.z = _2_3z + _000000000000001
				self.brb.x = _2_3x
				self.brb.y = _1_3y
				self.brb.z = self.brb.z
				self.children[pos] = Octree(_1_3x + _000000000000001, self.tlf.y, _2_3z + _000000000000001, _2_3x, _1_3y, self.brb.z)
			
		elif pos == North_East_Down2:
				self.tlf.x = _2_3x + _000000000000001
				self.tlf.y = self.tlf.y
				self.tlf.z = _2_3z + _000000000000001
				self.brb.x = self.brb.x
				self.brb.y = _1_3y
				self.brb.z = self.brb.z
				self.children[pos] = Octree(_2_3x + _000000000000001, self.tlf.y, _2_3z + _000000000000001, self.brb.x, _1_3y, self.brb.z)
			
		elif pos == Equator_West_Down2:
				self.tlf.x = self.tlf.x
				self.tlf.y = _1_3y + _000000000000001
				self.tlf.z = _2_3z + _000000000000001
				self.brb.x = _1_3x
				self.brb.y = _2_3y
				self.brb.z = self.brb.z
				self.children[pos] = Octree(self.tlf.x, _1_3y + _000000000000001, _2_3z + _000000000000001, _1_3x, _2_3y, self.brb.z)
			
		elif pos == Equator_Middle_Down2:
				self.tlf.x = _1_3x + _000000000000001
				self.tlf.y = _1_3y + _000000000000001
				self.tlf.z = _2_3z + _000000000000001
				self.brb.x = _2_3x
				self.brb.y = _2_3y
				self.brb.z = self.brb.z
				self.children[pos] = Octree(_1_3x + _000000000000001, _1_3y + _000000000000001, _2_3z + _000000000000001, _2_3x, _2_3y, self.brb.z)
			
		elif pos == Equator_East_Down2:
				self.tlf.x = _2_3x + _000000000000001
				self.tlf.y = _1_3y + _000000000000001
				self.tlf.z = _2_3z + _000000000000001
				self.brb.x = self.brb.x
				self.brb.y = _2_3y
				self.brb.z = self.brb.z
				self.children[pos] = Octree(_2_3x + _000000000000001, _1_3y + _000000000000001, _2_3z + _000000000000001, self.brb.x, _2_3y, self.brb.z)
			
		elif pos == South_West_Down2:
				self.tlf.x = self.tlf.x
				self.tlf.y = _2_3y + _000000000000001
				self.tlf.z = _2_3z + _000000000000001
				self.brb.x = _1_3x
				self.brb.y = self.brb.y
				self.brb.z = self.brb.z
				self.children[pos] = Octree(self.tlf.x, _2_3y + _000000000000001, _2_3z + _000000000000001, _1_3x, self.brb.y, self.brb.z)
			
		elif pos == South_Middle_Down2:
				self.tlf.x = _1_3x + _000000000000001
				self.tlf.y = _2_3y + _000000000000001
				self.tlf.z = _2_3z + _000000000000001
				self.brb.x = _2_3x
				self.brb.y = self.brb.y
				self.brb.z = self.brb.z
				self.children[pos] = Octree(_1_3x + _000000000000001, _2_3y + _000000000000001, _2_3z + _000000000000001, _2_3x, self.brb.y, self.brb.z)
			
		elif pos == South_East_Down2:
				self.tlf.x = _2_3x + _000000000000001
				self.tlf.y = _2_3y + _000000000000001
				self.tlf.z = _2_3z + _000000000000001
				self.brb.x = self.brb.x
				self.brb.y = self.brb.y
				self.brb.z = self.brb.z
				self.children[pos] = Octree(_2_3x + _000000000000001, _2_3y + _000000000000001, _2_3z + _000000000000001, self.brb.x, self.brb.y, self.brb.z)			
			
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
		
		if (x < self.tlf.x or
			x > self.brb.x or
			y < self.tlf.y or
			y > self.brb.y or
			z < self.tlf.z or
			z > self.brb.z):
			return False
	
	
	
		# Otherwise perform binary search for each ordinate
		#midx = (self.topLeftFront.x + self.bottomRightBack.x) // 2
		#midy = (self.topLeftFront.y + self.bottomRightBack.y) // 2
		#midz = (self.topLeftFront.z + self.bottomRightBack.z) // 2
	
	
		_2 = 2.000000000000000
		_3 = 3.000000000000000
	
		#_1_3x = (self.tlf.x + self.brb.x) / _3
		#_2_3x = ((self.tlf.x + self.brb.x) / _3) * _2
	
		#_1_3y = (self.tlf.y + self.brb.y) / _3
		#_2_3y = ((self.tlf.y + self.brb.y) / _3) * _2
	
		#_1_3z = (self.tlf.z + self.brb.z) / _3
		#_2_3z = ((self.tlf.z + self.brb.z) / _3) * _2
	
		_1_3x = self.tlf.x + ((self.brb.x - self.tlf.x) / _3)
		_2_3x = self.tlf.x + (2 * ((self.brb.x - self.tlf.x) / _3))
	
		_1_3y = self.tlf.y + ((self.brb.y - self.tlf.y) / _3)
		_2_3y = self.tlf.y + (2 * ((self.brb.y - self.tlf.y) / _3))
	
		_1_3z = self.tlf.z + ((self.brb.z - self.tlf.z) / _3)
		_2_3z = self.tlf.z + (2 * ((self.brb.z - self.tlf.z) / _3))
	
		#_1_3xxx = self.brb.x - (2 * ((self.brb.x - self.tlf.x) / _3))
		#_2_3xxx = self.brb.x - ((self.brb.x - self.tlf.x) / _3)
	
		#_1_3yyy = self.brb.y - (2 * ((self.brb.y - self.tlf.y) / _3))
		#_2_3yyy = self.brb.y - ((self.brb.y - self.tlf.y) / _3)
	
		#_1_3zzz = self.brb.z - (2 * ((self.brb.z - self.tlf.z) / _3))
		#_2_3zzz = self.brb.z - ((self.brb.z - self.tlf.z) / _3)
	
	
		pos = -1
	
	
	
		# Deciding the position where to move
		#if x <= midx:
			#if y <= midy:
				#pos = 0 if z <= midz else 1  # TopLeftFront or TopLeftBottom
			#else:
				#pos = 2 if z <= midz else 3  # BottomLeftFront or BottomLeftBack
		#else:
			#if y <= midy:
				#pos = 4 if z <= midz else 5  # TopRightFront or TopRightBottom
			#else:
				#pos = 6 if z <= midz else 7  # BottomRightFront or BottomRightBack
	
		_000000000000001 =  0.000000000000001  # 0.00001 ##
	
	
	
	
	
		North_West_Surface  = 0                  
		North_Middle_Surface = 1 
		North_East_Surface   = 2 
		Equator_West_Surface = 3
		Equator_Middle_Surface = 4 
		Equator_East_Surface =  5 
		South_West_Surface  = 6 
		South_Middle_Surface =  7 
		South_East_Surface =   8 
	
		#//  _1_3z + 1, _2_3z Down1
		North_West_Down1 = 9                  
		North_Middle_Down1 = 10 
		North_East_Down1 =  11 
		Equator_West_Down1 = 12 
		Equator_Middle_Down1 = 13 
		Equator_East_Down1  = 14 
		South_West_Down1 =  15 
		South_Middle_Down1 =  16 
		South_East_Down1   =  17 
	
		#//    _2_3z + 1, ,brb->z     Down2
		North_West_Down2 = 18                  
		North_Middle_Down2 = 19 
		North_East_Down2  = 20 
		Equator_West_Down2 = 21 
		Equator_Middle_Down2 = 22 
		Equator_East_Down2 =  23 
		South_West_Down2  =   24 
		South_Middle_Down2 = 25 
		South_East_Down2  =  26 
	
	
	
		if self.tlf.z <= z <= _1_3z:
			if self.tlf.x <= x <= _1_3x:
				if self.tlf.y <= y <= _1_3y:
					pos = North_West_Surface
			if _1_3x + _000000000000001 <= x <= _2_3x:
				if self.tlf.y <= y <= _1_3y:
					pos = North_Middle_Surface
			if _2_3x + _000000000000001 <= x <= self.brb.x:
				if self.tlf.y <= y <= _1_3y:
					pos = North_East_Surface
					
			if self.tlf.x <= x <= _1_3x:
				if _1_3y + _000000000000001 <= y <= _2_3y:
					pos = Equator_West_Surface
			if _1_3x + _000000000000001 <= x <= _2_3x:
				if _1_3y + _000000000000001 <= y <= _2_3y:
					pos = Equator_Middle_Surface
			if _2_3x + _000000000000001 <= x <= self.brb.x:
				if _1_3y + _000000000000001 <= y <= _2_3y:
					pos = Equator_East_Surface
					
			if self.tlf.x <= x <= _1_3x:
				if _2_3y + _000000000000001 <= y <= self.brb.y:
					pos = South_West_Surface
			if _1_3x + _000000000000001 <= x <= _2_3x:
				if _2_3y + _000000000000001 <= y <= self.brb.y:
					pos = South_Middle_Surface
			if _2_3x + _000000000000001 <= x <= self.brb.x:
				if _2_3y + _000000000000001 <= y <= self.brb.y:
					pos = South_East_Surface
					
		###############################################
					
		if _1_3z + _000000000000001 <= z <= _2_3z:
			if self.tlf.x <= x <= _1_3x:
				if self.tlf.y <= y <= _1_3y:
					pos = North_West_Down1
			if _1_3x + _000000000000001 <= x <= _2_3x:
				if self.tlf.y <= y <= _1_3y:
					pos = North_Middle_Down1
			if _2_3x + _000000000000001 <= x <= self.brb.x:
				if self.tlf.y <= y <= _1_3y:
					pos = North_East_Down1
					
			if self.tlf.x <= x <= _1_3x:
				if _1_3y + _000000000000001 <= y <= _2_3y:
					pos = Equator_West_Down1
			if _1_3x + _000000000000001 <= x <= _2_3x:
				if _1_3y + _000000000000001 <= y <= _2_3y:
					pos = Equator_Middle_Down1
			if _2_3x + _000000000000001 <= x <= self.brb.x:
				if _1_3y + _000000000000001 <= y <= _2_3y:
					pos = Equator_East_Down1
					
			if self.tlf.x <= x <= _1_3x:
				if _2_3y + _000000000000001 <= y <= self.brb.y:
					pos = South_West_Down1
			if _1_3x + _000000000000001 <= x <= _2_3x:
				if _2_3y + _000000000000001 <= y <= self.brb.y:
					pos = South_Middle_Down1
			if _2_3x + _000000000000001 <= x <= self.brb.x:
				if _2_3y + _000000000000001 <= y <= self.brb.y:
					pos = South_East_Down1
					
		############################################
					
		if _2_3z + _000000000000001 <= z <= self.brb.z:
			if self.tlf.x <= x <= _1_3x:
				if self.tlf.y <= y <= _1_3y:
					pos = North_West_Down2
			if _1_3x + _000000000000001 <= x <= _2_3x:
				if self.tlf.y <= y <= _1_3y:
					pos = North_Middle_Down2
			if _2_3x + _000000000000001 <= x <= self.brb.x:
				if self.tlf.y <= y <= _1_3y:
					pos = North_East_Down2
					
			if self.tlf.x <= x <= _1_3x:
				if _1_3y + _000000000000001 <= y <= _2_3y:
					pos = Equator_West_Down2
			if _1_3x + _000000000000001 <= x <= _2_3x:
				if _1_3y + _000000000000001 <= y <= _2_3y:
					pos = Equator_Middle_Down2
			if _2_3x + _000000000000001 <= x <= self.brb.x:
				if _1_3y + _000000000000001 <= y <= _2_3y:
					pos = Equator_East_Down2
					
			if self.tlf.x <= x <= _1_3x:
				if _2_3y + _000000000000001 <= y <= self.brb.y:
					pos = South_West_Down2
			if _1_3x + _000000000000001 <= x <= _2_3x:
				if _2_3y + _000000000000001 <= y <= self.brb.y:
					pos = South_Middle_Down2
			if _2_3x + _000000000000001 <= x <= self.brb.x:
				if _2_3y + _000000000000001 <= y <= self.brb.y:
					pos = South_East_Down2
					
					
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
				
				
	#tree.insert(5, 5, 3)
				
if __name__ == "__main__":
	main()
	
	
"""
		print(tlf.x," tlf x")
		#print()
		print(_1_3x ," 0.3 x")
		#print()
		print(_2_3x ," 0.6 x")
		#print()
		print(brb.x," brb x")
		print()
	
		print(tlf.y," tlf y")
		#print()
		print(_1_3y ," 0.3 y")
		#print()
		print(_2_3y ," 0.6 y")
		#print()
		print(brb.y," brb y")
		print()
	
		print(tlf.z," tlf z")
		#print()
		print(_1_3z ," 0.3 z")
		#print()
		print(_2_3z ," 0.6 z")
		#print()
		print(brb.z," brb z")
		print()




print(tlf.x," tlf x")
#print()
print(_1_3x ," 0.3 x ", _1_3x + _000000000000001)
#print()
print(_2_3x ," 0.6 x ", _2_3x + _000000000000001)
#print()
print(brb.x," brb x")
print()

print(tlf.y," tlf y")
#print()
print(_1_3y ," 0.3 y ", _1_3y + _000000000000001)
#print()
print(_2_3y ," 0.6 y ", _2_3y + _000000000000001)
#print()
print(brb.y," brb y")
print()

print(tlf.z," tlf z")
#print()
print(_1_3z ," 0.3 z ", _1_3z + _000000000000001)
#print()
print(_2_3z ," 0.6 z ", _2_3z + _000000000000001)
#print()
print(brb.z," brb z")
print()




if pos == North_West_Surface:
		self.tlf.x = self.tlf.x
		self.tlf.y = self.tlf.y
		self.tlf.z = self.tlf.z
		self.brb.x = _1_3x
		self.brb.y = _1_3y
		self.brb.z = _1_3z
		self.children[pos] = Octree(self.tlf.x, self.tlf.y, self.tlf.z, _1_3x, _1_3y, _1_3z)
	
elif pos == North_Middle_Surface:
		self.tlf.x = _1_3x + _000000000000001
		self.tlf.y = self.tlf.y
		self.tlf.z = self.tlf.z
		self.brb.x = _2_3x
		self.brb.y = _1_3y
		self.brb.z = _1_3z
		self.children[pos] = Octree(_1_3x + _000000000000001, self.tlf.y, self.tlf.z, _2_3x, _1_3y, _1_3z)
	
elif pos == North_East_Surface:
		self.tlf.x = _2_3x + _000000000000001
		self.tlf.y = self.tlf.y
		self.tlf.z = self.tlf.z
		self.brb.x = self.brb.x
		self.brb.y = _1_3y
		self.brb.z = _1_3z
		self.children[pos] = Octree(_2_3x + _000000000000001, self.tlf.y, self.tlf.z, self.brb.x, _1_3y, _1_3z)
	
elif pos == Equator_West_Surface:
		self.tlf.x = self.tlf.x
		self.tlf.y = _1_3y + _000000000000001
		self.tlf.z = self.tlf.z
		self.brb.x = _1_3x
		self.brb.y = _2_3y
		self.brb.z = _1_3z
		self.children[pos] = Octree(self.tlf.x, _1_3y + _000000000000001, self.tlf.z, _1_3x, _2_3y, _1_3z)
	
elif pos == Equator_Middle_Surface:
		self.tlf.x = _1_3x + _000000000000001
		self.tlf.y = _1_3y + _000000000000001
		self.tlf.z = self.tlf.z
		self.brb.x = _2_3x
		self.brb.y = _2_3y
		self.brb.z = _1_3z
		self.children[pos] = Octree(_1_3x + _000000000000001, _1_3y + _000000000000001, self.tlf.z, _2_3x, _2_3y, _1_3z)
	
elif pos == Equator_East_Surface:
		self.tlf.x = _2_3x + _000000000000001
		self.tlf.y = _1_3y + _000000000000001
		self.tlf.z = self.tlf.z
		self.brb.x = self.brb.x
		self.brb.y = _2_3y
		self.brb.z = _1_3z
		self.children[pos] = Octree(_2_3x + _000000000000001 , _1_3y + _000000000000001, self.tlf.z, self.brb.x, _2_3y, _1_3z)
	
elif pos == South_West_Surface:
		self.tlf.x = self.tlf.x
		self.tlf.y = _2_3y + _000000000000001
		self.tlf.z = self.tlf.z
		self.brb.x = _1_3x
		self.brb.y = self.brb.y
		self.brb.z = _1_3z
		self.children[pos] = Octree(self.tlf.x, _2_3y + _000000000000001, self.tlf.z, _1_3x, self.brb.y, _1_3z)
	
elif pos == South_Middle_Surface:
		self.tlf.x = _1_3x + _000000000000001
		self.tlf.y = _2_3y + _000000000000001
		self.tlf.z = self.tlf.z
		self.brb.x = _2_3x
		self.brb.y = self.brb.y
		self.brb.z = _1_3z
		self.children[pos] = Octree(_1_3x + _000000000000001, _2_3y + _000000000000001, self.tlf.z, _2_3x, self.brb.y, _1_3z)
	
elif pos == South_East_Surface:
		self.tlf.x = _2_3x + _000000000000001
		self.tlf.y = _2_3y + _000000000000001
		self.tlf.z = self.tlf.z      
		self.brb.x = self.brb.x
		self.brb.y = self.brb.y
		self.brb.z = _1_3z
		self.children[pos] = Octree(_2_3x + _000000000000001, _2_3y + _000000000000001, self.tlf.z, self.brb.x, self.brb.y, _1_3z)
	
	
	#############################################################################################################################################################
	
elif pos == North_West_Down1:
		self.tlf.x = self.tlf.x
		self.tlf.y = self.tlf.y
		self.tlf.z = _1_3z + _000000000000001
		self.brb.x = _1_3x
		self.brb.y = _1_3y
		self.brb.z = _2_3z
		self.children[pos] = Octree(self.tlf.x, self.tlf.y, _1_3z + _000000000000001, _1_3x, _1_3y, _2_3z)
	
elif pos == North_Middle_Down1:
		self.tlf.x = _1_3x + _000000000000001
		self.tlf.y = self.tlf.y
		self.tlf.z = _1_3z + _000000000000001
		self.brb.x = _2_3x
		self.brb.y = _1_3y
		self.brb.z = _2_3z
		self.children[pos] = Octree(_1_3x + _000000000000001, self.tlf.y, _1_3z + _000000000000001, _2_3x, _1_3y, _2_3z)
	
elif pos == North_East_Down1:
		self.tlf.x = _2_3x + _000000000000001
		self.tlf.y = self.tlf.y
		self.tlf.z = _1_3z + _000000000000001
		self.brb.x = self.brb.x
		self.brb.y = _1_3y
		self.brb.z = _2_3z
		self.children[pos] = Octree(_2_3x + _000000000000001, self.tlf.y, _1_3z + _000000000000001, self.brb.x, _1_3y, _2_3z)
	
elif pos == Equator_West_Down1:
		self.tlf.x = self.tlf.x
		self.tlf.y = _1_3y + _000000000000001
		self.tlf.z = _1_3z + _000000000000001
		self.brb.x = _1_3x
		self.brb.y = _2_3y
		self.brb.z = _2_3z
		self.children[pos] = Octree( self.tlf.x, _1_3y + _000000000000001, _1_3z + _000000000000001, _1_3x, _2_3y, _2_3z)
	
elif pos == Equator_Middle_Down1:
		self.tlf.x = _1_3x + _000000000000001
		self.tlf.y = _1_3y + _000000000000001
		self.tlf.z = _1_3z + _000000000000001
		self.brb.x = _2_3x
		self.brb.y = _2_3y
		self.brb.z = _2_3z
		self.children[pos] = Octree(_1_3x + _000000000000001, _1_3y + _000000000000001, _1_3z + _000000000000001, _2_3x, _2_3y, _2_3z)
	
elif pos == Equator_East_Down1:
		self.tlf.x = _2_3x + _000000000000001
		self.tlf.y = _1_3y + _000000000000001
		self.tlf.z = _1_3z + _000000000000001
		self.brb.x = self.brb.x
		self.brb.y = _2_3y
		self.brb.z = _2_3z
		self.children[pos] = Octree(_2_3x + _000000000000001, _1_3y + _000000000000001, _1_3z + _000000000000001, self.brb.x, _2_3y, _2_3z)
	
elif pos == South_West_Down1:
		self.tlf.x = self.tlf.x
		self.tlf.y = _2_3y + _000000000000001
		self.tlf.z = _1_3z + _000000000000001
		self.brb.x = _1_3x
		self.brb.y = self.brb.y
		self.brb.z = _2_3z
		self.children[pos] = Octree(self.tlf.x, _2_3y + _000000000000001, _1_3z + _000000000000001, _1_3x, self.brb.y, _2_3z)
	
elif pos == South_Middle_Down1:
		self.tlf.x = _1_3x + _000000000000001
		self.tlf.y = _2_3y + _000000000000001
		self.tlf.z = _1_3z + _000000000000001
		self.brb.x = _2_3x
		self.brb.y = self.brb.y
		self.brb.z = _2_3z
		self.children[pos] = Octree(_1_3x + _000000000000001, _2_3y + _000000000000001, _1_3z + _000000000000001, _2_3x, self.brb.y, _2_3z)
	
elif pos == South_East_Down1:
		self.tlf.x = _2_3x + _000000000000001
		self.tlf.y = _2_3y + _000000000000001
		self.tlf.z = _1_3z + _000000000000001
		self.brb.x = self.brb.x
		self.brb.y = self.brb.y
		self.brb.z = _2_3z
		self.children[pos] = Octree(_2_3x + _000000000000001, _2_3y + _000000000000001, _1_3z + _000000000000001, self.brb.x, self.brb.y, _2_3z)
	
	
	#############################################################################################################################################################
	
elif pos == North_West_Down2:
		self.tlf.x = self.tlf.x
		self.tlf.y = self.tlf.y
		self.tlf.z = _2_3z + _000000000000001
		self.brb.x = _1_3x
		self.brb.y = _1_3y
		self.brb.z = self.brb.z
		self.children[pos] = Octree(self.tlf.x, self.tlf.y, _2_3z + _000000000000001, _1_3x, _1_3y, self.brb.z)
	
elif pos == North_Middle_Down2:
		self.tlf.x = _1_3x + _000000000000001
		self.tlf.y = self.tlf.y
		self.tlf.z = _2_3z + _000000000000001
		self.brb.x = _2_3x
		self.brb.y = _1_3y
		self.brb.z = self.brb.z
		self.children[pos] = Octree(_1_3x + _000000000000001, self.tlf.y, _2_3z + _000000000000001, _2_3x, _1_3y, self.brb.z)
	
elif pos == North_East_Down2:
		self.tlf.x = _2_3x + _000000000000001
		self.tlf.y = self.tlf.y
		self.tlf.z = _2_3z + _000000000000001
		self.brb.x = self.brb.x
		self.brb.y = _1_3y
		self.brb.z = self.brb.z
		self.children[pos] = Octree(_2_3x + _000000000000001, self.tlf.y, _2_3z + _000000000000001, self.brb.x, _1_3y, self.brb.z)
	
elif pos == Equator_West_Down2:
		self.tlf.x = self.tlf.x
		self.tlf.y = _1_3y + _000000000000001
		self.tlf.z = _2_3z + _000000000000001
		self.brb.x = _1_3x
		self.brb.y = _2_3y
		self.brb.z = self.brb.z
		self.children[pos] = Octree(self.tlf.x, _1_3y + _000000000000001, _2_3z + _000000000000001, _1_3x, _2_3y, self.brb.z)
	
elif pos == Equator_Middle_Down2:
		self.tlf.x = _1_3x + _000000000000001
		self.tlf.y = _1_3y + _000000000000001
		self.tlf.z = _2_3z + _000000000000001
		self.brb.x = _2_3x
		self.brb.y = _2_3y
		self.brb.z = self.brb.z
		self.children[pos] = Octree(_1_3x + _000000000000001, _1_3y + _000000000000001, _2_3z + _000000000000001, _2_3x, _2_3y, self.brb.z)
	
elif pos == Equator_East_Down2:
		self.tlf.x = _2_3x + _000000000000001
		self.tlf.y = _1_3y + _000000000000001
		self.tlf.z = _2_3z + _000000000000001
		self.brb.x = self.brb.x
		self.brb.y = _2_3y
		self.brb.z = self.brb.z
		self.children[pos] = Octree(_2_3x + _000000000000001, _1_3y + _000000000000001, _2_3z + _000000000000001, self.brb.x, _2_3y, self.brb.z)
	
elif pos == South_West_Down2:
		self.tlf.x = self.tlf.x
		self.tlf.y = _2_3y + _000000000000001
		self.tlf.z = _2_3z + _000000000000001
		self.brb.x = _1_3x
		self.brb.y = self.brb.y
		self.brb.z = self.brb.z
		self.children[pos] = Octree(self.tlf.x, _2_3y + _000000000000001, _2_3z + _000000000000001, _1_3x, self.brb.y, self.brb.z)
	
elif pos == South_Middle_Down2:
		self.tlf.x = _1_3x + _000000000000001
		self.tlf.y = _2_3y + _000000000000001
		self.tlf.z = _2_3z + _000000000000001
		self.brb.x = _2_3x
		self.brb.y = self.brb.y
		self.brb.z = self.brb.z
		self.children[pos] = Octree(_1_3x + _000000000000001, _2_3y + _000000000000001, _2_3z + _000000000000001, _2_3x, self.brb.y, self.brb.z)
	
elif pos == South_East_Down2:
		self.tlf.x = _2_3x + _000000000000001
		self.tlf.y = _2_3y + _000000000000001
		self.tlf.z = _2_3z + _000000000000001
		self.brb.x = self.brb.x
		self.brb.y = self.brb.y
		self.brb.z = self.brb.z
		self.children[pos] = Octree(_2_3x + _000000000000001, _2_3y + _000000000000001, _2_3z + _000000000000001, self.brb.x, self.brb.y, self.brb.z)
	
"""
	
	
	
	
	