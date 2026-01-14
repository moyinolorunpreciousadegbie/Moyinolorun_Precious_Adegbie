class TrieNode:
	def __init__(self):
		#self.root = TrieNode()
		self.children = {}
		self.is_end = False
		self.count = 0 
		
	def tree_print(self):
		#node = self.root
		node = self
		q = [ [ list(node.children.keys()) , node ] ]
		#print(q, len(q),"<<<<")
		vis = []
		cb = 0
		while q:
			#print("works")
			x, nodes  = q.pop(0)
			if x not in vis and x[-1] in nodes.children.keys() and nodes.children[x[-1]].is_end == True :
				cb += 1
				print(x , nodes.children[x[-1]].is_end , cb,)
				vis.append(x)
				#continue
			#print(x , node )
			xx = x[-1]
			for k , v in nodes.children[xx].children.items() :
					#print(k,v)
				q.append([ x + [k] ,nodes.children[xx]]) # 
		#maip.keys()
		#maip.values()
				
	# Insert a word
	def insert(self, word: str) -> None:
		#node = self.root
		node = self
		for ch in word:
			if ch not in node.children:
				#print(ch)
				node.children[ch] = TrieNode()
			node = node.children[ch]
		node.is_end = True
		node.count += 1
		
	# Exact word search
	def search(self, word: str) -> bool:
		#node = self.root
		node = self
		for ch in word:
			if ch not in node.children:
				return False
			node = node.children[ch]
		return node.is_end
	
	# Prefix check
	def starts_with(self, prefix: str) -> bool:
		#node = self.root
		node = self
		for ch in prefix:
			if ch not in node.children:
				return False
			node = node.children[ch]
		return True
	
	# Count how many times a word was inserted
	def frequency(self, word: str) -> int:
		#node = self.root
		node = self
		for ch in word:
			if ch not in node.children:
				return 0
			node = node.children[ch]
		return node.count if node.is_end else 0
	
	
	def words_with_prefix(self, prefix: str):
		#node = self.root
		node = self
		for ch in prefix:
			if ch not in node.children:
				return []
			node = node.children[ch]
			
		results = []
		
		def dfs(cur_node, path):
			if cur_node.is_end:
				results.append(prefix + path)
			for c, nxt in cur_node.children.items():
				dfs(nxt, path + c)
				
		dfs(node, "")
		return results
	
	
	def delete(self, word: str) -> None:
		def _delete(node, word, depth):
			if depth == len(word):
				if not node.is_end:
					return False
				node.is_end = False
				node.count = 0
				return len(node.children) == 0
			
			ch = word[depth]
			if ch not in node.children:
				return False
			
			should_delete = _delete(node.children[ch], word, depth + 1)
			
			if should_delete:
				del node.children[ch]
				return not node.is_end and len(node.children) == 0
			
			return False
		
		_delete(self.root, word, 0)
		
		
##############################################################################################################################################################################################################################################################################################################################################################################################################################################################################


def product(iterables):
	
	pools =  iterables 
	#print(pools	,'here')
	
	
	q = []
	result = [[]]
	cn= 0
	for pool in pools:
		
		q = []
		for x in result :
			if  len( x ) == ( len(iterables)  ) : 
				break
			
			for y in pool :
				
				cn += 1
				#if  len( x+[y] ) == (repeat * len(iterables)  )  : print(x+[y] , cn) # 365     876
				if  len(  x+[y]  ) == ( len(iterables)  ) : 
					print(x+[y] )
				q.append( x+[y]   )
				
		result = q
		
		
		
	return result  # or q 
def lll(listt, Level ):
	
	
	#q = listt
	count = 0
	trie = TrieNode()
	q =[listt + [ trie , TrieNode()  ] ]
	#TrieNode() , TrieNode()
	# listt = [   [ ((X1,X2,X_CUT)  ,   (Y1,Y2,Y_CUT)  ,   (Z1,Z2,Z_CUT))  ]   ]
	# listt = [   [ ((X1,X2,X_CUT)  ,   (Y1,Y2,Y_CUT)  ,   (Z1,Z2,Z_CUT))  ] ,  TrieNode() , TrieNode() ] = q.pop(0)
	#   [     [   [ ((X1,X2,X_CUT)  ,   (Y1,Y2,Y_CUT)  ,   (Z1,Z2,Z_CUT))  ] ,  TrieNode() , TrieNode() ]     ]
	#             ##########################################################    ##########   ##########            
	#                 q.pop(0)[0]                         					   q.pop(0)[1]   q.pop(0)[2] 	
	
	
	
	
	while q: #      [     [ ....[ [X1,X2,X_CUT]  ,   [Y1,Y2,Y_CUT]  ,   [Z1,Z2,Z_CUT]  ] ,,,,, ]         ]
		#print(q)
		qq , TTRRIIEE1 , TTRRIIEE2 = q.pop(0) #   [     [ [X1,X2,X_CUT]  ,   [Y1,Y2,Y_CUT]  ,   [Z1,Z2,Z_CUT]  ]   , ++++    ]
		#                 1     2                                                      2             1
		#print(qq)
		#return 
		
		
	
		qqq = qq[-1] #          [ [X1,X2,X_CUT]  ,   [Y1,Y2,Y_CUT]  ,   [Z1,Z2,Z_CUT]  ] 
	
		# if qqq not in TTRRIIEE1.children: 
		TTRRIIEE1.children[qqq] = TTRRIIEE2
			
			
	
		if len(qq) == Level :
			pass
			count += 1
			#print(qq,"qq",Level,len(qq), count, TTRRIIEE1 , TTRRIIEE2)
			#print(qq,"qq",Level,len(qq), count)
			TTRRIIEE2.is_end = True
			#trie.tree_print()
			
			words = qq #  [["123","abc"],["123"] ]
			#for w in words:
				#trie.insert(w)
			#trie.tree_print()
			continue
			#break
	
		layers = []
		for lenk in range( len(qqq) ) : # range(3)
			q_x1_x2_cut = qqq[lenk] # [X1,X2,X_CUT] 
			q_x1 , q_x2 , q_cut = q_x1_x2_cut[0], q_x1_x2_cut[1] , q_x1_x2_cut[2]
			#(q_x2 - q_x1) / q_cut
	
	
			_min_ = q_x1 # 10
			_max_ = q_x2 # 110
			CUT = q_cut
			numk = 1
			#for ct in range(CUT): #  octs [ [10.0, 35.0] [35.0, 60.0] [60.0, 85.0] [85.0, 110.0] ]4
	
			#octs =[ [      (_min_ + (((_max_-_min_)/CUT)*ct) )  , (_min_ + (((_max_-_min_)/CUT)*(ct+1)) )     , CUT   ] for ct in range(CUT) ]
	
			octs = (     tuple(((_min_ + (((_max_-_min_)/CUT)*ct) )  , (_min_ + (((_max_-_min_)/CUT)*(ct+1)) )     , CUT   ) for ct in range(CUT)) )
			#print(octs , numk)
			#numk += 1
	
			"""
			CUT = 6
			for ct in range(CUT+1) :
				_ = ct% (CUT)
				print(_, min([ct+1,CUT]) , [ct+1,CUT] )
			"""
	
			octss = (     tuple(((_min_ + (((_max_-_min_)/CUT)*(ct% CUT)  ) )  , (_min_ + (((_max_-_min_)/CUT)*(min([ct+1,CUT]))) )     , CUT   ) for ct in range(CUT+1)) )
	
	
			layers.append(octs) # [[10.0, 35.0], [35.0, 60.0], [60.0, 85.0], [85.0, 110.0]] x axis
	
	
			#layers.append(octss) # [[10.0, 35.0], [35.0, 60.0], [60.0, 85.0], [85.0, 110.0], [10.0, 110.0]] x axis
																							##############
	
	
	
		#return
############################################################################################################################################################
		iterables = layers
		pools =  iterables 
		q_prod = []
		result = [[]]
		#result = [tuple()]
		cn= 0
		indD = 0
		for pool in pools:
			q_prod = []
			#q_prod = tuple()
			
			for x in result :
				if  len( x ) == ( len(iterables)  ) : 
					break
				
				FIRSZT = x+[ qqq[indD] ]
								#      x+[qqq[indD]]
											#                   pool y-############   x+[y]
				if len(  FIRSZT  ) == ( len(iterables)  )  :
					#print(qqq != tuple(FIRSZT) )
					if qqq != tuple(FIRSZT)  :
						TTRRIIEE2_NEW = TrieNode()
						#q.append( (qq+[tuple(FIRSZT)] ) ) # <<< MAIN
						#TTRRIIEE2.children[ tuple(FIRSZT) ] = TTRRIIEE2_NEW
						#q.append( (qq+[tuple(FIRSZT)] , TTRRIIEE2 , TTRRIIEE2_NEW  ) ) 
						q.append( (qq+[tuple(FIRSZT)] , TTRRIIEE1.children[qqq] , TTRRIIEE2_NEW  ) ) 
						#TTRRIIEE1.children[qqq] = TTRRIIEE2
						
				if len(  FIRSZT  ) < ( len(iterables)  )  :
					q_prod.append( FIRSZT   ) #     X ############
					#print( x,  qqq[indD]   , FIRSZT, )
						
				
				for y in pool :
					
					
					cn += 1
					XX_YY_ZZ = x+[y]
					
					#XX_YY_ZZ = x+tuple(y)
					
					
						
					
					
					if  len(  XX_YY_ZZ  ) == ( len(iterables)  ) : 
						#print(   qqq , tuple(XX_YY_ZZ) ,  qqq != tuple(XX_YY_ZZ)  )
						#        OLD     NEW              OLD !=  NEW
						#print(qq+[tuple(XX_YY_ZZ)] )
						#print(qqq, "--->>>",tuple(XX_YY_ZZ)) # parent --->>> child
						
						
						
						if qqq != tuple(XX_YY_ZZ)  :
							#q.append( (qq+[tuple(XX_YY_ZZ)] ) ) # <<< MAIN
							TTRRIIEE2_NEWW = TrieNode()
							#TTRRIIEE2.children[ tuple(XX_YY_ZZ) ] = TTRRIIEE2_NEWW
							#q.append( (qq+[tuple(XX_YY_ZZ)] , TTRRIIEE2 , TTRRIIEE2_NEWW   ) )
							q.append( (qq+[tuple(XX_YY_ZZ)] , TTRRIIEE1.children[qqq] , TTRRIIEE2_NEWW   ) )
							#TTRRIIEE1.children[qqq] = TTRRIIEE2 
						#q.append(qq + [XX_YY_ZZ] ) # [     [ [X1,X2,X_CUT]  ,   [Y1,Y2,Y_CUT]  ,   [Z1,Z2,Z_CUT]  ]    , *   ]    , 
											# * [ [X1,X2,X_CUT]  ,   [Y1,Y2,Y_CUT]  ,   [Z1,Z2,Z_CUT]  ] 
						#q.append(qq + [tuple(XX_YY_ZZ)] ) 
						#print(qq + [XX_YY_ZZ])
						#print(XX_YY_ZZ )
					
					
					q_prod.append( XX_YY_ZZ   )
					
			indD += 1
			
			result = q_prod
			
	trie.tree_print() # 5
	
############################################################################################################################################################
			
			
			
			
			
X1=0
X2=1000
X_CUT=3#2#8

Y1=0 # 1000#0
Y2=1000 # 2000#1000
Y_CUT=3#2#9

Z1=0
Z2=1000
Z_CUT=2#10

Level =  3 # 4  {3,,,}



#listt = [[    [ [X1,X2,X_CUT]  ,   [Y1,Y2,Y_CUT]  ,   [Z1,Z2,Z_CUT]  ]    ]]


listt = [[    ((X1,X2,X_CUT)  ,   (Y1,Y2,Y_CUT)  ,   (Z1,Z2,Z_CUT))      ]]


lll(listt, Level )

"""
iterables = [ [[111,333,"CUT"],[333,555,"CUT"],[555,777,"CUT"],[777,999,"CUT"]],
			  [[222,444,"CUT"],[444,666,"CUT"],[666,888,"CUT"]],
			  [[10,20,"CUT"],[20,30,"CUT"],[30,40,"CUT"],[40,50,"CUT"],[50,60,"CUT"],[60,70,"CUT"],[70,80,"CUT"],[80,90,"CUT"],[90,100,"CUT"]]  ]

def mulj(l):
	mm = 1
	for k in l:
		mm*=len(k)
	return mm

praw = mulj(iterables)
prodf = product(  iterables ,   )


print(praw , len(prodf))








|
|
|whole
|\
| \
#\ \ #   /#
# \ \#  / #
#  \ # /  #
#   \#/   #
#    #    #



* []
^  x


** #
** #
** #
** #
** #
** #
** *
^^ x

"""





		