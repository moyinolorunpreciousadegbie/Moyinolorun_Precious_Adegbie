
###############################################################################################################################################################
class Solution:
	def shortestPath(self, grid: list[list[int]], k: int) -> int:
		rows = len(grid)
		cols = len(grid[0])
		# Directions we'll use to change our location (down, up, right, left).
		directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
		# We'll use a deque for our BFS traversal.
		#q = collections.deque([])
		q  = []
		#head = q.all[0][0] # head
		#tail = q.all[0][1] # tail
		# Append our starting details to the q.
		# (row, col, steps, k)
		if grid == [[0]] : return 0
		
		ones = 0
		#q.append((0, 0, 0, k))
		q.append([ [[0, 0]], 0, k , ones])
		#print(q.getRear().path)
		# Use a set (O(1) lookup) to track the locations we've visited to avoid revisiting.
		# We track (r, c, k) - k: is tracked because there might be multiple ways to get to
		# a give (r, c) on the grid. With the addition of k, it ensures that multiple path
		# options can be explored, instead of simply eliminating a (r, c) after the first visit.        .next       .prev
		seen = set()
		mn = float('inf')
		PP = []
		mp = {}
		#q.getRear()  
		#q.getFront()  
		#q.insertFront(path, steps, rk)
		#q.insertLast(path, steps, rk)
		#q.deleteFront() 
		#q.deleteLast()
		#while       head.next.path != None         and          head.next.steps!=None           and              head.next.rk != None:
		while   q :
		#while       q.getFront() != -1:
			# Pop the next location from the q.
			NODE = q.pop(0)
			#NODE = q.deleteLast()
			path, steps, rk , ones = NODE 
			
			r , c = path[-1]  # path[-1][0]  ,   path[-1][1]                  {{{{ h =  path[-1][2]  }}}}
			# If we're at the finish location return the steps, given BFS this will be
			# guaranteed to be the first to hit this condition.
			                         #  00      01 10       20    02 good 
									 #  00      -11 -10       50    03 bad (out of bounds)    R_5   C_3  wont be appended
									# 00 deleted forever, never to be re-used
			#if r == rows-1 and c == cols - 1:
				#print(path)
				#return steps
	
			if r == rows-1 and c == cols - 1:                      # if r == 0 or  r == rows-1  or  c == 0 or  c == cols-1    ## middle  h == 0 or h == hei - 1
				print(path, ones) # [[0, 0]]
				PP.append(path)
				if rk == 0 :
					
					mn = min(mn, len(path)-1)
					
				#return steps
			# Otherwise we'll keep travelling throught the grid in our 4 directions.
				#else:
			# directions = [(-1, -1),(-1, 0),(-1, 1),               (0, -1),(0, 0),(0, 1),             (1, -1),(1, 0),(1, 1)]
			# z for nz in range(h,hei) :
			
			for y, x in directions:  
				nr = r + y
				nc = c + x
					# If the new location is on the board and has not been visited.
				if 0 <= nr < rows and 0 <= nc < cols :# and (nr, nc, rk) not in seen:                               #    and 0 <= nh < hei
						# If it's a blocker but we still have k left, we'll go there and k -= 1.
					if grid[nr][nc] == 1 and rk > 0 and [nr, nc] not in path:                                       # and [nr, nc, nh] not in path:
						#seen.add((nr, nc, rk))
						#q.append((nr, nc, steps + 1, rk - 1))
						q.append([path + [[nr, nc]], steps+1, rk-1 , ones+1 ])
						#q.append([path + [[nr, nc]], steps+1, rk , ones+1]) # TO SHOW ALL POSSIBLE PATHS
						
				
						#q.append([path + [[nr, nc, nh]], steps+1, rk-1 , ones+1 ])
						#q.append([path + [[nr, nc, nh]], steps+1, rk , ones+1]) # TO SHOW ALL POSSIBLE PATHS
				
						
						# Otherwise continue on  if it's a 0 - free location.
					elif grid[nr][nc] == 0 and [nr, nc] not in path:                                               # and [nr, nc, nh] not in path:
						#seen.add((nr, nc, rk))
						#q.append((nr, nc, steps + 1, rk))
						q.append([path + [[nr, nc]], steps+1, rk, ones])
						
						
						#q.append([path + [[nr, nc, nh]], steps+1, rk, ones])
						
						
						#if  nr < 0 or  rows <= nr        or     nc < 0 or  cols <= nc :
						#NODE.prev.next = NODE.next
						#NODE.next.prev = NODE.prev
						#q  = QQ
			#head = q.all[0][0] # head
			#tail = q.all[0][1] # tail
			#QQ = MyCircularDeque(float('inf'))
						
			#head = head.next
			
			
		li = []
		for i in PP:
			if len(i) - 1 == mn :
				li.append(i)
			
		
		print(mn, li)	
		if mn != float('inf')  : return mn
		# If we don't hit the end in our traversal we know it's not possible.
		return -1
	
	
	
Obj = Solution()

grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]
k = 1
#Output: 6
print( Obj.shortestPath(grid, k) )
print()


grid = [[0,1,1],[1,1,1],[1,0,0]]
k = 1
#Output: -1

print( Obj.shortestPath(grid, k) )
print()

