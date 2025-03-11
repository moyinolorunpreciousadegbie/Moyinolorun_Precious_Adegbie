#!/usr/bin/env python3

def fn( y1, y2, yy1, yy2):
	if y2 > yy2 and yy1 > y1 :
		return yy2 - yy1
	
	if yy2 > y2 and y1 > yy1 :
		return y2 - y1
	
	
	
	if y2 > yy2 and yy2 > y1  and y1 > yy1 :
		return yy2 - y1
	if yy2 > y2 and y2 > yy1  and yy1 > y1 :
		return y2 - yy1
	
	
	
	
	
	if y2 > yy2 and y1 == yy1 :
		return yy2 - yy1
	if yy2 > y2 and y1 == yy1 :
		return y2 - y1
	
	
	if y2 == yy2  and y1 > yy1 :
		return y2 - y1 
	if y2 == yy2  and yy1 > y1 :
		return yy2 - yy1
	
	
	
	if y2 == yy2  and yy1 == y1 :
		return y2 - y1 # yy2 - yy1
	
	
	if y1 >  yy2:   # NO AREA SHARED
		return 0
	if yy1 > y2:
		return 0

	return 0
	
class UnionFind:
	def __init__(self, ranges_list):
		self.par = {tuple(i):tuple(i) for i in ranges_list }
		self.rank = {}
		self.comb = {tuple(i):[i] for i in ranges_list}
		for i in ranges_list :
			self.rank[tuple(i)] = 1
			
		self.mx = -float('inf')
		self.mn = float('inf')
		
	def find(self, v1):
		while v1 != self.par[v1]:
			self.par[v1] = self.par[self.par[v1]]
			v1 = self.par[v1]
		return v1
	
	def union(self, v1, v2):
		
		p1, p2 = self.find(v1), self.find(v2)
		if p1 == p2:
			return False
		if self.rank[p1] > self.rank[p2]:
			self.par[p2] = p1
			self.comb[p1] += [ list(p2) ]
			self.rank[p1] += self.rank[p2]
		else:
			self.par[p1] = p2
			self.rank[p2] += self.rank[p1]
			self.comb[p2] += [ list(p1) ]
		return True
	
	
	
def rect( ALL_RANGES ):
	
	uf = UnionFind( ALL_RANGES )
	
	for i in range(len(ALL_RANGES)):          #    x1   x2          y1    y2            z1    z2
		for j in range(i+1,len(ALL_RANGES)):  # [ [0]   [3] ]     [ [1]   [4] ]      [ [2]   [5] ]
			#print([i,j])
			if fn( ALL_RANGES[i][0],  ALL_RANGES[i][3],               ALL_RANGES[j][0],  ALL_RANGES[j][3]) != 0 and fn( ALL_RANGES[i][1],  ALL_RANGES[i][4],               ALL_RANGES[j][1],  ALL_RANGES[j][4]) != 0 and fn( ALL_RANGES[i][2],  ALL_RANGES[i][5],               ALL_RANGES[j][2],  ALL_RANGES[j][5]) != 0 :
	
				v1, v2 = tuple(ALL_RANGES[i]) , tuple(ALL_RANGES[j])
			#if fn( ALL_RANGES[i][0],  ALL_RANGES[i][-1],               ALL_RANGES[j][0],  ALL_RANGES[j][-1]) != 0:
				
				uf.union(v1, v2)
				
				
				#print(uf.rank , uf.par )
	print()
	#print(uf.comb)
	
	ans = []
	for rang , rank in uf.rank.items() :
		#if uf.rank[rang] == 1 and  uf.par[rang] == rang and uf.comb[ rang ]  == [list(rang)]    and uf.comb[ rang ]  not in ans : # XXX
			#ans.append( uf.comb[ rang ]   )   # XXX  ON IT'S OWN, UNSHARED SO REMOVE THIS 2 LINES
		
		if uf.rank[rang] > 1 and  uf.par[rang] == rang  and uf.comb[ rang ]  not in ans : 
			ans.append( uf.comb[ rang ]   )                                               
			#ALL_RANGES = [1 for i in range(6)] 
			
	print(ans)
	
#01234567
#  2345   
#   34
	
ALL_RANGES = [[0,0,0, 7,7,7],[2,2,2, 5,5,5], [3,3,3,  4,4,4]]# 1
rect( ALL_RANGES )
print() 

ALL_RANGES = [[2,2,2,  5,5,5],[0,0,0,  7,7,7], [3,3,3, 4,4,4]]# 1
rect( ALL_RANGES )
print() 

#  234567
#012345
#   34


ALL_RANGES = [[2,2,2,  7,7,7],[0,0,0,  5,5,5], [3,3,3,   4,4,4]]# 2    
rect( ALL_RANGES )
print() 


ALL_RANGES = [[0,0,0,   5,5,5],[2,2,2,    7,7,7], [3,3,3,   4,4,4]]# 2
rect( ALL_RANGES )
print()

#  234567
#  2345
#   34    



ALL_RANGES = [[2,2,2,    7,7,7],[2,2,2,   5,5,5], [3,3,3,    4,4,4]]# 3
				#     #
rect( ALL_RANGES )
print() 


ALL_RANGES = [[2,2,2,   5,5,5],[2,2,2,   7,7,7], [3,3,3,   4,4,4]]# 3
				#     #
rect( ALL_RANGES )
print() 

#012345
#  2345
#   34    


ALL_RANGES = [[0,0,0,   5,5,5],[2,2,2,    5,5,5], [3,3,3,   4,4,4]]
				#     #
rect( ALL_RANGES )
print() 




ALL_RANGES = [[2,2,2,   5,5,5],[0,0,0,    5,5,5], [3,3,3,   4,4,4]]
				#     #
rect( ALL_RANGES )
print() 

#  2345
#  2345
#   34    


ALL_RANGES = [[2,2,2,   5,5,5],[2,2,2,   5,5,5], [3,3,3,    4,4,4]]
rect( ALL_RANGES )
print() 

#0123
#    4567   # corner volume case ><
#   34    

ALL_RANGES = [[0,0,0,   3,3,3],[4,4,4,   7,7,7], [3,3,3,   4,4,4]]
rect( ALL_RANGES )
print() 


#0123
#    4567
#    45
#  23

ALL_RANGES = [[0,0,0,  3,3,3],[4,4,4,   7,7,7], [4,4,4,  5,5,5],[2,2,2,  3,3,3]]
rect( ALL_RANGES )
print()        

ALL_RANGES = [[0,0,0,  3,3,3],[4,4,4,  7,7,7], [4,4,4,  5,5,5],[2,2,2,  3,3,3], [12,12,12,   15,15,15]]
rect( ALL_RANGES )
print()


###  1 - PLOT ALL THESE 1ST


"""
ln = 0
for rang , rank in uf.rank.items() :
	if rank > 1 :
		ln+=1
			
	if uf.rank[rang] == 1 and  uf.par[rang] == rang :
		ln += 1




0                    10
		3       8
0             8
		3              10
0                                          20
	2                                      20


[0,10]
[3,8 ]
[0,8 ]
[3,10]
[0,20]
[2,20]

"""