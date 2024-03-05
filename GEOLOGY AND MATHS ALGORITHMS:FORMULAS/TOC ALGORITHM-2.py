#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def makeplot(f, top_depth, bottom_depth):
    
    lithology_numbers =  {1: {'lith':'Sandstone', 'lith_num':1, 'hatch': '.', 'color':'#ffff00'},
                          2: {'lith':'Siltstone', 'lith_num':2, 'hatch': '..', 'color':'#ffff00'},
                          3: {'lith':'Shale', 'lith_num':3, 'hatch':'--', 'color':'#bebebe'},
                          4: {'lith':'Limestone', 'lith_num':4, 'hatch': '-\\', 'color':'#80ffff'},
                          5: {'lith':'DOLOMITE', 'lith_num':5, 'hatch':'-/', 'color':'#8080ff'},
                          6: {'lith':'ANHYDRITE', 'lith_num':6, 'hatch':'', 'color':'#ff80ff'},
                          7: {'lith':'COAL', 'lith_num':7, 'hatch':'', 'color':'black'},
                          8: {'lith':'Marl', 'lith_num':8, 'hatch':'', 'color':'#7cfc00'},
                          9: {'lith':'Chalk', 'lith_num':9, 'hatch':'..', 'color':'#80ffff'},
                          10: {'lith':'Halite', 'lith_num':10, 'hatch':'x', 'color':'#7ddfbe'},
                          11: {'lith':'Tuff', 'lith_num':11, 'hatch':'||', 'color':'#ff8c00'},
                          12: {'lith':'Basement', 'lith_num':12, 'hatch':'-|', 'color':'#ef138a'}}
   
         
    #fig, ax = plt.subplots(figsize=(2.5, 15))
    
    fig, ax = plt.subplots(figsize=(2.5, 7))

    ax12 = plt.subplot2grid((1,2), (0,0), rowspan=1, colspan = 1)
    
    
    
# Lithology track
    ax12.plot(f["Lithology"], f['DEPTH'], color = "black", linewidth = 0.5)  # 0.5
    ax12.set_xlabel("Lithology")
    ax12.set_xlim(0, 1)
    ax12.xaxis.label.set_color("black")
    ax12.tick_params(axis='x', colors="black")
    ax12.spines["top"].set_edgecolor("black")
    ax12.yaxis.set_ticks_position("left")
    ax12.yaxis.set_label_position("left")
    #ax12.set_ylim(  7500, 11000 )
    #plt.yticks(np.arange(7500, 11000, 100)) 
    
    #ax12.set_ylim(  5132, 11000 ) ##############################
   # plt.yticks(np.arange(5132, 11000, 150)) 
    
    for key in lithology_numbers.keys():
        color = lithology_numbers[key]['color']
        hatch = lithology_numbers[key]['hatch']
        ax12.fill_betweenx(f['DEPTH'], 0, f['Lithology'], where=(f['Lithology']==key),
                         facecolor=color, hatch=hatch)
        

    ax12.set_xticks([0, 1])

    for ax in [ax12]:
        #ax.set_ylim(8000 , 10880.0)## 8040.5, 10850.0)
        #ax.set_ylim(5132 , 11477.0)## 8040.5, 10850.0)
        ax.grid(which='major', color='lightgrey', linestyle='-')
        ax.xaxis.set_ticks_position("top")
        ax.xaxis.set_label_position("top")
        ax.spines["top"].set_position(("axes", 1.02))
    
  
    
    for ax in [ax12]:
        plt.setp(ax.get_yticklabels(), visible = True)
        ax.invert_yaxis()
    
    plt.tight_layout()
    
    fig.subplots_adjust(wspace = 0.15)  # 0.15
   
    
    
    


# In[ ]:


lithology_numbers =  {1: {'lith':'Sandstone', 'lith_num':1, 'hatch': '.', 'color':'#ffff00'},
                          2: {'lith':'Siltstone', 'lith_num':2, 'hatch': '..', 'color':'#ffff00'},
                          3: {'lith':'Shale', 'lith_num':3, 'hatch':'--', 'color':'#bebebe'},
                          4: {'lith':'Limestone', 'lith_num':4, 'hatch':'+-\\', 'color':'#80ffff'},  ###. '+',
                          5: {'lith':'DOLOMITE', 'lith_num':5, 'hatch':'-/', 'color':'#8080ff'},
                          6: {'lith':'ANHYDRITE', 'lith_num':6, 'hatch':'', 'color':'#ff80ff'},
                          7: {'lith':'Coal', 'lith_num':7, 'hatch':'', 'color':'black'},
                          8: {'lith':'Marl', 'lith_num':8, 'hatch':'', 'color':'#7cfc00'},
                          9: {'lith':'Chalk', 'lith_num':9, 'hatch':'..', 'color':'#80ffff'},
                          10: {'lith':'Halite', 'lith_num':10, 'hatch':'x', 'color':'#7ddfbe'},
                          11: {'lith':'Tuff', 'lith_num':11, 'hatch':'||', 'color':'#ff8c00'},
                          12: {'lith':'Basement', 'lith_num':12, 'hatch':'-|', 'color':'#ef138a'}}






y = [0, 1]
x = [1, 1]

fig, axes = plt.subplots(ncols=4,nrows=3, sharex=True, sharey=True,
                         figsize=(10,5), subplot_kw={'xticks': [], 'yticks': []})

for ax, key in zip(axes.flat, lithology_numbers.keys()):
    ax.plot(x, y)
    ax.fill_betweenx(y, 0, 1, facecolor=lithology_numbers[key]['color'], hatch=lithology_numbers[key]['hatch'])
    ax.set_xlim(0, 0.1)
    ax.set_ylim(0, 1)
    ax.set_title(str(lithology_numbers[key]['lith']))

plt.tight_layout()

plt.show()


# In[ ]:


def lith(well1_depth, well1_lith):
	
	#print(f)
	
	#well1_depth = [1,3,5,7,15,20,28,34]
	
	#well1_lith = [2, 2,1,1,4,3,3,2]
	
	
	well1 = []
	
	for i in range(len(well1_depth)  ):
		if len(well1_depth) == len(well1_lith) :
			well1.append([well1_depth[i], well1_lith[i]])
		#f['DEPTH'].iloc[i] = well1_depth[i]
		#f['Lithology'].iloc[i] = well1_lith[i]
			
			
	f = pd.DataFrame(well1,columns=['DEPTH', 'Lithology'])
		#print(f)
	makeplot(f, min(well1_depth), max(well1_depth)	)


# In[ ]:





# In[ ]:


import queue
from collections import defaultdict
import matplotlib as mpl
import matplotlib.pyplot as plt

	
	
	

	
def doe(m):
	cum = 0
#main = []
	q = [0]
	cn = 0
	for u in m:
		if cn == 0:
			u.append(u[1])
			q.append(u[1])
			
			
		else :
			#if u[1]:
			cum += u[1] - q[-1]
			u.append(cum)
			cum = 0
			#print(cum)
			q.append(u[1])
			
		cn += 1
		
	return m


def maxi(well):
	mx = 0

	for o, oo , _ , _ in well:
		#print(oo,'OO')
		
		mx = max(mx, oo)
	return mx

def findShortestCycle(n, edges, tar, tar2,  grph, hash) :
	
	
		
		graph = [[] for _ in range(n)]
		
		#  from   to  TOC   gape  
	
		graph2 = defaultdict(list)
	
	
	
		#graph2[n[1]].append(n[3])
		
		for   u,   v , toc, gape in edges: 
			graph[u].append((v,gape))
			graph[v].append((u,gape))
			graph2[v].append(toc)
		
		visited=[False]*(n)
		path = []
		tooc = []
		litho = []
		for u , vv ,tocc, gap in edges: 
			dist = {}
			queue1 = queue.deque([(u, -1, gap   )])
			while queue1: 
				u, p, d = queue1.popleft()
				if tar <= sum(path) <= tar2 : 
					ln = len(path)
					
					litho.append(hash[(path[-1] ,tooc[:ln-1][-1])][0])
					
					fig, ax = plt.subplots()
					plt.plot( tooc[:ln-1], path[1:], label =  'current TOC '  )
					plt.plot(  cumul(tooc[:ln-1] ) , path[1:], label = 'CUMMULATIVE TOC')
					plt.ylabel("Depth in ft" ) # , rotation='horizontal')
					#ax.yaxis.set_label_coords(-.1, 0 )
					plt.xlabel("TOC (BLUE) and  CUMMULATIVE TOC (ORANGE)")
					plt.title(grph[path[-1]])
					plt.ylim(max(path[1:]), min(path[1:]))
					#plt.pause(0.01)
					#plt.clf()
					#plt.invert_yaxis().invert_yaxis()
					plt.grid(True) 
					#lith( path[ sv - len(litho) +1:]   ,litho )
					sv = len(path[1:])
					#print(path[1:],   path[ sv - len(litho) +1:] ,litho ,'path[1:],litho <<<<<<<<<<<<<<<<')
					lith( path[ sv - len(litho) +1:]   ,litho )
					plt.show()
					
					#ln = len(path)
					print(path[1:],'     path in range          ',tar,'<=',sum(path),'<=',tar2,'     DEPTH:',path[-1],' ', grph[path[-1]])
					
					print(tooc[:ln-1],'     TOC so far          total TOC value',sum(tooc[:ln-1]),'      current TOC:',tooc[:ln-1][-1])
					print(cumul(tooc[:ln-1] ),'   Cumulative TOC',  cumul(tooc[:ln-1] )[-1])
					print()
					#print(hash[(path[-1] ,tooc[:ln-1][-1])][0], 'GRRRRRAAAAAPPPPPPHHHHHH')
					
					
					#break 
					#visited[u]=True
				
				path.append(u)
				#litho.append(hash[(path[-1] ,tooc[:ln-1][-1])][0] )
				for v , gapp in graph[u]: # or visited[v] == False
					
					if v != p:
						if graph2[v] :
							
							tooc.append(graph2[v][0])
							#print(tooc)
						queue1.append((v, u, d + gapp))
				#if queue1:
			#	queue1.popleft()
				#visited[u]=False
		return path

def each(w, tar):
	
	path = [ ]
	tooc = []
	toocc = []
	cum = 0
	tc = 0
	for   u in w : 
				
        #   depth
		if u[1] > tar :
			break
		
		cum += u[3]   # gape
		tc+= u[2]     # toc
		path.append(cum)
		tooc.append(tc)
		toocc.append(u[2])
		print(path,path[-1],'depth <',tar )
		print(toocc,toocc[-1],' current toc')
		print(tooc,tooc[-1],'toc seen so far')
		print()
        
        
# add(wells, tar, tar2)

def cumul(mat):
	q = []
	cum = 0
	for u in mat:
		cum += u
		q.append(cum)
	return q
		

def combinations(iterable, r):
	# combinations('ABCD', 2) --> AB AC AD BC BD CD
	# combinations(range(4), 3) --> 012 013 023 123
	pool = tuple(iterable)
	n = len(pool)
	if r > n:
		return
	indices = list(range(r))
	yield tuple(pool[i] for i in indices)
	while True:
		for i in reversed(range(r)):
			if indices[i] != i + n - r:
				break
		else:
			return
		indices[i] += 1
		for j in range(i+1, r):
			indices[j] = indices[j-1] + 1
		yield tuple(pool[i] for i in indices)
		
		
def depthsort(wellz):
	wellcombo = []
	for wel in list(wellz):   # wel each well
		for depth in wel:  #  [2,15]
			wellcombo.append(depth)
	
	#print(wellcombo ,'now')
	
	wellcombo.sort(key=lambda e: e[0])	 # sort by depth
	return wellcombo 
	#return wellcombo
	

	
def addbfs(wellss, tar, tar2):
	
	
	
	
	
	
	hash = wellss[0][1] # graph  hashmap
	
	wells = []
	cnpp = 0
	for ww in wellss :
		wells.append(doe(ww[0]))
		if cnpp > 0:
			hash.update(ww[1])
		cnpp +=1
	
	
	mat = 0
	n = 0
	edges ,  grph = 0, defaultdict(list)
	cnt = 0
	ser = set()
	for  i in wells:
		cnt += 1
		temp = cnt
		for j in i:
			
			#print(j[1], 'j[1]]')
			if j[1] in ser :
				#cnt +=1
				grph[ j[1]  ].append((' and ')  )
				grph[ j[1]  ].append(('WELL',cnt))
				#cnt -=1
				continue
			grph[ j[1]  ].append(('WELL',cnt))
			ser.add(j[1]  )
			

	
	
	for i in range(2, len(wells)+1):
		#n = 0
		for wellz in list(combinations(wells, i))  :
			
			n = maxi(depthsort(wellz)) + 1
		
			edges = depthsort(wellz) 
	
			#print(edges)
			findShortestCycle(n, edges, tar, tar2,   grph,     hash) 
			print("-------------------------------------------------------------------------------------------------------------------------------------------------")
			
			print()
			print()
			print()
			print()
			
# addbfs(wells, tar, tar2)


# In[ ]:


from collections import defaultdict
import matplotlib as mpl
import matplotlib.pyplot as plt





#!/usr/bin/env python3
def doe(m):
	cum = 0
#main = []
	q = [0]
	cn = 0
	for u in m:
		if cn == 0:
			u.append(u[1])
			q.append(u[1])
			
			
		else :
			#if u[1]:
			cum += u[1] - q[-1]
			u.append(cum)
			cum = 0
			#print(cum)
			q.append(u[1])
			
		cn += 1
		
	return m

def combinations(iterable, r):
	# combinations('ABCD', 2) --> AB AC AD BC BD CD
	# combinations(range(4), 3) --> 012 013 023 123
	pool = tuple(iterable)
	n = len(pool)
	if r > n:
		return
	indices = list(range(r))
	yield tuple(pool[i] for i in indices)
	while True:
		for i in reversed(range(r)):
			if indices[i] != i + n - r:
				break
		else:
			return
		indices[i] += 1
		for j in range(i+1, r):
			indices[j] = indices[j-1] + 1
		yield tuple(pool[i] for i in indices)
		
def maxi(well):
    #print(well)
    mx = 0
    for o, oo, _, _ in well:
		#print(oo,'OO')
        mx = max(mx, oo)
    return mx

def depthsort(wellz):
	wellcombo = []
	for wel in list(wellz):   # wel each well
		for depth in wel:  #  [2,15]
			wellcombo.append(depth)
	
	#print(wellcombo ,'now')
	
	wellcombo.sort(key=lambda e: e[0])	 # sort by depth
	return wellcombo 
	#return wellcombo
	
	

			
			
			
def printAllPathsUtil(tar , tar2, edges, n, grph,  hash):

	graph = defaultdict(list) 
	se = {}
	#print(n,'NN')
	#print()
	#print(edges,'EGDES')
	tocgraph = defaultdict(list)
	q = []
	for u, v , t ,tt in edges:
		#se[(u,v)] = w
		if [u, v,t, tt ] not in q:
			se[(u,v)] = t
			q.append( [u, v,t, tt ])
		graph[u].append((v))
		tocgraph[v].append(t)  # TOC
		
		#print(graph)
		#print()
		#print(se)
	print()
	
	def printAllPathsUtil(edges, n,   path,toooc, cumtoooc , par, u, cum ):
	
		visited[u]= True
		path.append(u)
		#litho = []
		
		if  tar <=  path[-1] <= tar2 and par != -1 :
			cum += se[(par,u)]  
			print(path, 'DEPTH')
			print()
			toooc.append(tocgraph[u][0])  #  current TOC
			cumtoooc.append(cum)  #  cumlative TOC
			
			#litho.append(hash[(path[-1] ,tooc[:ln-1][-1])][0])
			
			
			
			
			em = [0] *   (len(path)  - len(toooc))
			
			print(path, '  Depths')
			
			if len(path) ==  len( em + toooc) and len(path) == len(em + cumtoooc) :
				
				print(em + toooc, 'current TOC') #, len(path) - len(toooc), len(toooc), len(path)-1)
				print(em + cumtoooc, 'CUMMULATIVE TOC')
				print()
				tccc = em + toooc 
				ctccc =  em + cumtoooc 
				tccc = tccc[1:]
				ctccc = ctccc[1:]
				#litho = []
				temp = path[1:]
				sv = len(path[1:])
				litho.append(hash[(temp[-1],  tccc[-1])][0])
				#print( litho   , ' <<<<<<<<<<<<<<<<<<<<<<<<<<<< litho  ', path[ sv - len(litho) +1:])
				
				
				
				fig, ax = plt.subplots()
				plt.plot( tccc, path[1:], label =  'current TOC '  )
				plt.plot(  ctccc  , path[1:], label = 'CUMMULATIVE TOC')
				plt.ylabel("Depth in ft" )#, rotation='horizontal')
				#ax.yaxis.set_label_coords(-.1, 0 )
				plt.xlabel("TOC (BLUE) and  CUMMULATIVE TOC (ORANGE)")
				plt.title(grph[path[-1]])
				plt.ylim(max(path[1:]), min(path[1:]))
				#plt.pause(0.01)
				#plt.clf()
				#plt.invert_yaxis().invert_yaxis()
				plt.grid(True) 
				
				lith( path[ sv - len(litho) +1:]   ,litho )
				
				plt.show()
				#em = [0] *   (len(path)  - len(toooc))
			print(tar, '<=', path[-1], '<=', tar2,'      cummulative TOC:  ', cum,"    Depth: ",path[-1],'         CURRENT TOC     ',tocgraph[u][0],'   ',grph[path[-1]])
			

			
		print("-------------------------------------------------------------------------------------------------------------------------------------------------")
			
		
		for v in graph[u]:
			#print(v)
			#if  par != v and visited[v] == False:
			#cum += se[(u,v)]
			#print(cum)
			printAllPathsUtil(edges, n,   path, toooc, cumtoooc ,u, v, cum)
		print()			
		path.pop()
		visited[u]= False
		
	visited =[False]*(n)
		
	path = []
	litho = []
	cumtoooc = []
	toooc = []
	
	cum = 0
	printAllPathsUtil(edges, n,   path,toooc, cumtoooc ,  -1, 0, cum)

def adddfs(wellss, tar, tar2):
	
	hash = wellss[0][1] # graph  hashmap
	
	wells = []
	cnpp = 0
	for ww in wellss :
		wells.append(doe(ww[0]))
		if cnpp > 0:
			hash.update(ww[1])
		cnpp +=1
		
		
	n = 0
	edges ,  grph = 0, defaultdict(list)
	cnt = 0
	ser = set()
	for  i in wells:
		cnt += 1
		temp = cnt
		for j in i:
			
			
			if j[1] in ser :
				#cnt +=1
				grph[ j[1]  ].append((' and ')  )
				grph[ j[1]  ].append(('WELL',cnt))
				#cnt -=1
				continue
			grph[ j[1]  ].append(('WELL',cnt))
			ser.add(j[1]  )
	
	
	for i in range(2, len(wells)+1):
		#n = 0
		for wellz in list(combinations(wells, i))  :
			#print( depthsort(wellz) ,"HERE BOY" )
			#n = len(depthsort(wellz)  ) + 1
			#n = len(depthsort(wellz)  ) + 2
			n = maxi(depthsort(wellz)) + 1
			#print(n,'NN')
			edges = depthsort(wellz) 
			#print(edges, n,'lll')
			printAllPathsUtil(tar ,tar2, edges, n, grph, hash)
			print()
			print()
			
			#return mat
	
			

"""
2 0 1 3 
2 0 3 
2 1 3 
"""
#edges = [[-1, 0, 0],     [0, 1, 20],   [0,2,15]   , [1,6,12]  , [2,5,3], [6,9,11], [5,7,21],  ]



# adddfs(wells, tar, tar2)


# In[173]:


import numpy as np 
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import matplotlib as mpl
import matplotlib.pyplot as plt


# In[174]:


FEE_AL_910 = pd.read_excel("/Users/moyinolorunadegbie/Documents/THESIS/FEE AL 910.xlsx",sheet_name="Sheet1")
FEE_BI_307 = pd.read_excel("/Users/moyinolorunadegbie/Documents/THESIS/FEE BI 307.xlsx",sheet_name="Sheet1")
FEE_AW_3402 = pd.read_excel("/Users/moyinolorunadegbie/Documents/THESIS/FEE AW 3402.xlsx", sheet_name="Sheet1")  
#FEE_AL_910
#FEE_BI_307
#FEE_AW_3402


# In[ ]:


#FEE_AL_910['Depth']
#FEE_AL_910['TOC']
#FEE_AL_910
from collections import defaultdict



def convert(FEE_AL_910):
    
    FEE_AL_910_ = FEE_AL_910[['Depth','TOC']]
    FEE_AL_910_[['Depth','TOC']] = FEE_AL_910[['Depth','TOC']].astype(int)
   
    FEE_AL_910_L = FEE_AL_910_[['Depth','TOC']].values.tolist()
    FEE_AL_910_L[0].insert(0,0)   # left index       right value
    for i in range(1,len(FEE_AL_910_L)):
        FEE_AL_910_L[i].insert(0,   int(FEE_AL_910_L[i-1][1]) )
      
    
    FEE_AL_910_2 = FEE_AL_910['lith_num']
    FEE_AL_910_2 = FEE_AL_910_2.values.tolist()
    
    graphix = defaultdict(list)
    
    
    
    for i in range(len(FEE_AL_910_L)):
        graphix[(FEE_AL_910_L[i][1], FEE_AL_910_L[i][2])].append( FEE_AL_910_2[i]  )
        #.            PRESENT DEPTH.                 TOC
   # for Depth, TOC in  FEE_AL_910_L :
        #graph[(Depth, TOC)].append( ())
        #print(graph)
    
   
       
   
    
    return FEE_AL_910_L, graphix   ## FEE_AL_910  # dataframe


# In[ ]:


#print( convert(FEE_AL_910  ) ,end = ' ')

tar = 7000.0
tar2 = 10000.5


wells =  [   convert(FEE_AL_910),    convert(FEE_BI_307),     convert(FEE_AW_3402)    ]

adddfs(wells, int(tar), int(tar2)) 
#doe(convert(FEE_AL_910))
#doe(convert(FEE_BI_307))


# In[ ]:





# In[ ]:


tar = 7000.0
tar2 = 70000.5


wells =  [   convert(FEE_AL_910),    convert(FEE_BI_307),     convert(FEE_AW_3402)    ]
addbfs(wells, int(tar), int(tar2)) 


# In[ ]:


"""
tar = 7000.0
tar2 = 10000.5
"""


# In[ ]:


#FEE_AL_910[['Depth','TOC']]
#FEE_BI_307[['Depth','TOC']]
#FEE_AW_3402[['Depth','TOC']]


# In[ ]:


#FEE_AL_910[['Depth','TOC']]
#FEE_BI_307[['Depth','TOC']]
#FEE_AW_3402[['Depth','TOC']]


# In[ ]:


#FEE_AL_910[['Depth','TOC']]
#FEE_BI_307[['Depth','TOC']]
#FEE_AW_3402[['Depth','TOC']]


# In[658]:


FEE_AL_910 = pd.read_excel("/Users/moyinolorunadegbie/Documents/THESIS/FEE AL 910.xlsx",sheet_name="Sheet4")
FEE_BI_307 = pd.read_excel("/Users/moyinolorunadegbie/Documents/THESIS/FEE BI 307.xlsx",sheet_name="Sheet4")
FEE_AW_3402 = pd.read_excel("/Users/moyinolorunadegbie/Documents/THESIS/FEE AW 3402.xlsx", sheet_name="Sheet4")  


# In[659]:


def convert(FEE_AL_910):
    
    FEE_AL_910_ = FEE_AL_910[['Depth','TOC','Calcite']]
    FEE_AL_910_[['Depth','TOC','Calcite']] = FEE_AL_910[['Depth','TOC','Calcite']].astype(int)
   
    FEE_AL_910_L = FEE_AL_910_[['Depth','TOC', 'Calcite']].values.tolist()
    FEE_AL_910_L[0].insert(0,0)   # left index       right value
    for i in range(1,len(FEE_AL_910_L)):
        FEE_AL_910_L[i].insert(0,   int(FEE_AL_910_L[i-1][1]) )
        
    return FEE_AL_910_L, FEE_AL_910


# In[660]:


print(convert(FEE_AL_910)[0])
print()
print(convert(FEE_BI_307)[0])
print()
print(convert(FEE_AW_3402)[0])



queries3 = [[8285,9333],[9717,10010],[10166,10366] ]

quaries4 = [[7952,9520], [9644,10216], [10291, 10718]]


# In[689]:


from collections import defaultdict
import statistics

#####################################################################################################################

def convert(FEE_AL_910):
    
    FEE_AL_910_ = FEE_AL_910[['Depth','TOC','Calcite']]
    FEE_AL_910_[['Depth','TOC','Calcite']] = FEE_AL_910[['Depth','TOC','Calcite']].astype(int)
   
    FEE_AL_910_L = FEE_AL_910_[['Depth','TOC', 'Calcite']].values.tolist()
    FEE_AL_910_L[0].insert(0,0)   # left index       right value
    for i in range(1,len(FEE_AL_910_L)):
        FEE_AL_910_L[i].insert(0,   int(FEE_AL_910_L[i-1][1]) )
        
    return FEE_AL_910_L, FEE_AL_910

#####################################################################################################################

def transpose(l1, l2):
    l2 =[[row[i] for row in l1] for i in range(len(l1[0]))]
    return l2

#####################################################################################################################

def minOperationsQueries(edges, queries):
    n = len(edges) +1
    def dfs( p, x, t, b, e, w, w2, f, all , all2):
        all[x][::] = w[::]
        all2[x][::] = w2[::]
        f[x][0] = p
        b[x] = t[0] = t[0] + 1
        for y in adj[x]: 
            if y[0] != p:
                w[ y[0] ] += y[1]
                w2[ y[0] ] += y[2]
                dfs(x, y[0], t, b, e, w, w2,  f, all, all2 )
                w2[ y[0] ] -=y[2]
                w[ y[0] ] -= y[1]
        e[x]  = t[0]
    def ancestor(x, y, b, e):
        return b[x]  <= b[y] and e[x]  >= e[y]
    def lcs(x, y, b, e, f):
        if  ancestor(x, y, b, e):
            return x
        if  ancestor(y, x, b, e):
            return y
        r = 0
        for i in range(n-1,-1,-1):
            temp = f[x][i]
            if ancestor(temp, y, b, e):
                r = temp
            else:
                x = temp
        return r
    adj = defaultdict(list)
    graph = {}
    graph2 = {}
    cnnn = 0
    for e in edges:
        adj[cnnn].append((cnnn+1, e[2],e[3]))
        graph[e[1] ] = cnnn+1
        graph2[cnnn+1] = e[1]
        cnnn += 1
    f = [[0]*(n) for _ in range(n)]
    all = [[0]*(n) for _ in range(n)] # # TOC
    all2 = [[0]*(n) for _ in range(n)] # CARBONATE
    b = [0] * (n)
    e = [0] * (n)
    w = [0] *  n #(tc+1) # TOC
    w2 = [0] *  n #(carb+1) # CARBONATE
    t = [0]
    dfs(-1, 0, t, b, e, w, w2, f, all, all2 )
    f[0][0] = 0
    for j in range(1,n):
        for i in range(n):
            f[i][j] =  f[  f[i][j-1] ][j-1]
    ans = []
    ans2 = []
    
    medianans = []
    for q  in queries:
        if q[0] == q[1]:
            continue
        tocmedians = []
        tocmedians.append( adj[   graph[ q[0] ]-1  ][0][1]  ) 
        #print(tocmedians)
        carbmedians = []
        carbmedians.append( adj[   graph[ q[0] ]-1  ][0][2] )
        #print(carbmedians)
        summ = 0
        summm = 0
        tlc = lcs( graph[ q[0]],   graph[ q[1]], b, e, f)
        tot = graph[ q[1]] - graph[ q[0]] +1  
        for i in range(n):  # TOC
            temp = all[  graph[ q[0] ] ][i]  +  all[  graph[ q[1] ] ][i]  - ( all[  graph[ graph2[tlc] ]   ][i] << 1 )
            summ += temp     # CARB
            
                
            temp2 =  all2[  graph[ q[0] ] ][i]  +  all2[  graph[ q[1] ] ][i]  - ( all2[  graph[ graph2[tlc] ]   ][i] << 1 )    
            summm += temp2
            if graph[ q[0]] < i <= graph[ q[1]]  :
                tocmedians.append(temp) # PATH
                #print(tocmedians  )
                #print(statistics.median(tocmedians) ,'TOC' )
                
                carbmedians.append(temp2) # # PATH
                #print(carbmedians  )
                #print(statistics.median(carbmedians) , 'CARB' )
                
                term = [statistics.median(tocmedians) ,    statistics.median(carbmedians) ]
        #print( tocmedians   )   # PATH
        #print(  carbmedians   )  #  PATH
        medianans.append(term)
        ans.append((summ + adj[   graph[ q[0] ]-1  ][0][1] )/ tot)
        ans2.append((summm + adj[   graph[ q[0] ]-1  ][0][2] )/ tot)
        #if len( tocmedians ) == tot and len( carbmedians ) == tot:
        #print( tocmedians )
       # print()
        #print( carbmedians )
    
    l1 = []
    #transpose(medianans , l1)
    #print(transpose(medianans , l1), 'TOC & Carbonate medianans')
    #print(medianans)
    l2 = []
    transpose([ans, ans2], l2)
    return transpose([ans, ans2], l2),  medianans

#####################################################################################################################

def quary(FEE_AL_910, quaries):
    graph = defaultdict(list)
    graphtoc = {}
    graphcarbonate = {}
    for u, v , toc , carbonate in FEE_AL_910 :
        graph[u].append(v)
        graphtoc[v] = toc
        graphcarbonate[v] = carbonate
    def dfs(start, stop, sumtoc,sumcarbonate , cnt):
        seen.add(start)
        tocpath.append(graphtoc[start])
        carbonatepath.append(graphcarbonate[start])
        sumtoc += graphtoc[start]
        sumcarbonate += graphcarbonate[start]
        cnt += 1
        for v in graph[start]:      #print( sumtoc / cnt , sumcarbonate / cnt,'     sumtoc / cnt , sumcarbonate / cnt     ' ,sumtoc,sumcarbonate, cnt)
            if v not in seen and start < v   :
                if v == stop:
                    sumtoc += graphtoc[v]
                    sumcarbonate += graphcarbonate[v]
                    cnt += 1
                    tocpath.append(graphtoc[v])
                    carbonatepath.append(graphcarbonate[v])
                    
                    ans.append([sumtoc / cnt , sumcarbonate / cnt]) 
                    #print(tocpath)
                    #print(carbonatepath)
                    tocmedian.append(statistics.median(tocpath))
                    carbonatemedian.append(statistics.median(carbonatepath))
                    median.append([statistics.median(tocpath), statistics.median(carbonatepath)  ])
                dfs(v , stop, sumtoc,sumcarbonate , cnt )
    ans = []
    tocmedian = []
    carbonatemedian = []
    median = []
    
    for start, stop in quaries:  ## ([29, 54, 13], [63, 205, 40])
        sumtoc = 0
        sumcarbonate = 0
        cnt = 0
        seen = set()
        tocpath = []
        carbonatepath = []
        
        dfs(start, stop, sumtoc, sumcarbonate, cnt)
    #print(tocmedian,'TOCmedian')
    #print()
    #print( carbonatemedian , 'Carbonatemedian' )
    #print()
    #print(median)
    return ans, median

#####################################################################################################################

def checking( well ,  quaries, formationZZZ):
    
    #(convert(FEE_AL_910)[0]
    #(convert(FEE_AL_910)[1]
    FEE_AL_910 = well[1]
    FEE_AL_910_ = well[0]
    import matplotlib.pyplot as plt
    import numpy as np
    fig, ax1 = plt.subplots(figsize=(3, 15))
    plt.ylabel("Depth ft")
    lis = list(  range( len(FEE_AL_910['Depth'] )     )     )   
    dep = FEE_AL_910['Depth'].astype(int).tolist()


    gar =  defaultdict(list)
    for i in range(len(lis)):
        gar[ dep[i] ].append(  lis[i]  )

#print(gar)
#print(lis,dep)
    ax1.plot(FEE_AL_910['TOC'].tolist(), lis, label= 'TOC',color='red',marker='o' )
#plt.xticks(np.arange(0, 15, 5))
#fig.tight_layout(pad=200)

## mask  = FEE_AL_910['Calcite'] != 8400
 
#ax2 = ax1.twiny()      
    ax2 = ax1.twiny()
    ax2.plot( FEE_AL_910['Calcite'].tolist()  , lis , label= 'Calcite', color='blue',marker='P')
    ax2.set_title("% Carbonate")


    plt.yticks( dep )

    plt.xlabel("TOC (wt%)")
    plt.ylim(max(lis)+2, min(lis)-2)
    ax2.xaxis.set_label_position('bottom')
    ax2.xaxis.set_label_coords(0.5,-0.05)
    plt.grid()     
    ax2.legend(loc = 'upper right')
    ax1.legend(loc = 'lower right')
#ax1.legend(loc = 'lower left')
    ax1.grid()   
    ax2.grid()


    ax1.set_yticks(lis)
    ax2.set_yticks(lis)

    ax1.set_yticklabels(dep)
    ax2.set_yticklabels(dep)


    import random
    number_of_colors = len( quaries )

    color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(number_of_colors)]
    #print(color)

    formations = {}
    
    cnt= 0
    for u, v in quaries:
       # print(u, v)
        #rangg = [u, v]
        em = ''
        for key, value in formationZZZ.items():
            if  value[0] <= u  <=  value[1]  and value[0] <= v  <=  value[1] :
                em = key 
        rangg = [gar[u][0], gar[v][0]  ] 
        #rang = '                                       '+str(u)+' ft to '+str(v)+' ft : AVG TOC of '+ str( quary( FEE_AL_910_  , quaries)[0][cnt][0] )+ ', Median TOC of '+ str( quary( FEE_AL_910_  , quaries)[1][cnt][0] ) +  ',     AVG Carbonate of ' + str( quary( FEE_AL_910_  , quaries)[0][cnt][1]  )  +', Median Carbonate of ' + str( quary( FEE_AL_910_  , quaries)[1][cnt][1]  ) 
        rang = em  + '   AVG TOC of '+str( int(quary( FEE_AL_910_  , quaries)[0][cnt][0]) )+ ', Median TOC of '+ str( int(quary( FEE_AL_910_  , quaries)[1][cnt][0] )) +  ',     AVG Carbonate of ' + str( int(quary( FEE_AL_910_  , quaries)[0][cnt][1] ) )  +', Median Carbonate of ' + str( int(quary( FEE_AL_910_  , quaries)[1][cnt][1] ) ) 


        #print(  rang)  #  string label
       # print()
    #print( rangg)  # list of quary range
    #print(   '', minOperationsQueries( FEE_AL_910  , quaries)[cnt][0]  , minOperationsQueries( FEE_AL_910  , quaries)[cnt][1] )
        cnt+=1
    
        formations[ rang ] = rangg
    
    #print(formations)

    
    zone_colours = color

    for depth, colour in zip(formations.values(), zone_colours):
        # use the depths and colours to shade across the subplots
            ax2.axhspan(depth[0], depth[1] , color=colour, alpha=0.2)
        
    formation_midpoints = []
    for key, value in formations.items():
        formation_midpoints.append(value[0] + (value[1]-value[0])/2)
    
#formation_midpoints  # rotation=90   # 95
        
    for label, formation_mid in zip(formations.keys(), 
                                    formation_midpoints):
            ax2.text(94.5, formation_mid, label, rotation=0,
                verticalalignment='center', fontweight='bold',
                fontsize='large')

        
    plt.show()
    
#####################################################################################################################  
    
#quaries1 = [[8055, 9861],[9861,10740],[10795, 10850]]  
#quaries2 = [[8040, 9861],[9861,10740],[10795, 10850]]
#quaries3 = [[9341,9370],[9861,9903],[9974,10009],[10590,10750]]

#checking( convert(FEE_AL_910) ,  quaries1)   

#checking( convert(FEE_AL_910) ,  quaries2)  

#checking( convert(FEE_AL_910) ,  quaries3) 


####################################################################################################################


well1 = [[10590,10850],[9974,10020],[9861,9918],[9341,9370],[8040,8083]]


formationWell1 = { "PERMIAN" : [8040, 10590]  ,
    "PENNSYLVANIAN" : [10590, 10850]  ,
    "STRAWN" : [10850,10850]  }

print('FEE_AL_910')

checking( convert(FEE_AL_910) ,  well1 ,formationWell1 ) 


print()
print('####################################################################################################################')
print()
             ###
well2 = [   [8285,9609]       ,[10390,10729],[10353,10380],[10335,10346],[10292,10325],[10166,10283],[10000,10032],[9962,9995],[9938,9956]
         ,[9740,9853],[9717,9731],[9657,9663]]
    
#well2 = [[8285,9609]     , [10390,10832],[10353,10380],[10325,10353],[10292,10325],[9956, 10166],[9740,9853],[9717,9731],[9657,9684]]  

formationWell2 = { "PERMIAN":[8285,10283], 
                "PENNSYLVANIAN":[10283,11022]  }

print('FEE_BI_307')

checking( convert(FEE_BI_307) ,  well2 , formationWell2) 


# In[662]:


#FEE_AL_910['Depth'] 
#FEE_AL_910['TOC']
#FEE_AL_910['Calcite']


# In[664]:



# FEE_AL_910

PERMIAN = [8040, 10590]
PENNSYLVANIAN = [10590, 10850]
STRAWN = [10850,10850]


# FEE_BI_307

                          # 9657,
formationZZZ = { " PERMIAN":[8285,10283], 
                " PENNSYLVANIAN":[10283,11022]  }


# In[665]:


import matplotlib.pyplot as plt
import numpy as np
fig, ax1 = plt.subplots(figsize=(3, 15))
plt.ylabel("Depth ft")
lis = list(  range( len(FEE_AL_910['Depth'] )     )     )   
dep = FEE_AL_910['Depth'].astype(int).tolist()


gar =  defaultdict(list)
for i in range(len(lis)):
    gar[ dep[i] ].append(  lis[i]  )

#print(gar)
#print(lis,dep)
ax1.plot(FEE_AL_910['TOC'].tolist(), lis, label= 'TOC',color='red',marker='o' )
#plt.xticks(np.arange(0, 15, 5))
#fig.tight_layout(pad=200)

## mask  = FEE_AL_910['Calcite'] != 8400
 
#ax2 = ax1.twiny()      
ax2 = ax1.twiny()
ax2.plot( FEE_AL_910['Calcite'].tolist()  , lis , label= 'Calcite', color='blue',marker='P')
ax2.set_title("FEE_AL_910 \n % Carbonate")


plt.yticks( dep )

plt.xlabel("TOC (wt%)")
plt.ylim(max(lis)+2, min(lis)-2)
ax2.xaxis.set_label_position('bottom')
ax2.xaxis.set_label_coords(0.5,-0.05)
plt.grid()     
ax2.legend(loc = 'upper right')
ax1.legend(loc = 'lower right')
#ax1.legend(loc = 'lower left')
ax1.grid()   
ax2.grid()


ax1.set_yticks(lis)
ax2.set_yticks(lis)

ax1.set_yticklabels(dep)
ax2.set_yticklabels(dep)

formations = { "                                       1st Spraberry": [gar[9881][0], gar[10795][0]  ]  }
    
zone_colours = ["darkslateblue"]

for depth, colour in zip(formations.values(), zone_colours):
        # use the depths and colours to shade across the subplots
        ax2.axhspan(depth[0], depth[1] , color=colour, alpha=0.1)
        
formation_midpoints = []
for key, value in formations.items():
    formation_midpoints.append(value[0] + (value[1]-value[0])/2)
    
#formation_midpoints  # rotation=90
        
for label, formation_mid in zip(formations.keys(), 
                                    formation_midpoints):
        ax2.text(0.5, formation_mid, label, rotation=0,
                verticalalignment='center', fontweight='bold',
                fontsize='large')
#plt.rcParams['figure.figsize'] = [34, 34]
#plt.gca().set_aspect('equal', adjustable='datalim') 
#plt.yscale("linear")
#plt.yscale('mercator')

plt.show()


# In[666]:


import matplotlib.pyplot as plt
import numpy as np
fig, ax1 = plt.subplots(figsize=(3, 15))
plt.ylabel("Depth ft")
lis = list(  range( len(FEE_BI_307['Depth'] )     )     )   
dep = FEE_BI_307['Depth'].astype(int).tolist()


gar =  defaultdict(list)
for i in range(len(lis)):
    gar[ dep[i] ].append(  lis[i]  )

#print(gar)
#print(lis,dep)
ax1.plot(FEE_BI_307['TOC'].tolist(), lis, label= 'TOC',color='red',marker='o' )
#plt.xticks(np.arange(0, 15, 5))
#fig.tight_layout(pad=200)

## mask  = FEE_AL_910['Calcite'] != 8400
 
#ax2 = ax1.twiny()      
ax2 = ax1.twiny()
ax2.plot( FEE_BI_307['Calcite'].tolist()  , lis , label= 'Calcite', color='blue',marker='P')
ax2.set_title("FEE_BI_307 \n % Carbonate")


plt.yticks( dep )

plt.xlabel("TOC (wt%)")
plt.ylim(max(lis)+2, min(lis)-2)
ax2.xaxis.set_label_position('bottom')
ax2.xaxis.set_label_coords(0.5,-0.05)
plt.grid()     
ax2.legend(loc = 'upper right')
ax1.legend(loc = 'lower right')
#ax1.legend(loc = 'lower left')
ax1.grid()   
ax2.grid()


ax1.set_yticks(lis)
ax2.set_yticks(lis)

ax1.set_yticklabels(dep)
ax2.set_yticklabels(dep)

formations = { "                                       1st Spraberry": [gar[9398][0], gar[10360][0]  ]  }
    
zone_colours = ["darkslateblue"]

for depth, colour in zip(formations.values(), zone_colours):
        # use the depths and colours to shade across the subplots
        ax2.axhspan(depth[0], depth[1] , color=colour, alpha=0.1)
        
formation_midpoints = []
for key, value in formations.items():
    formation_midpoints.append(value[0] + (value[1]-value[0])/2)
    
#formation_midpoints  # rotation=90

for label, formation_mid in zip(formations.keys(), 
                                    formation_midpoints):
       
        ax2.text(20, formation_mid,  label, rotation=0,
                verticalalignment='center', fontweight='bold',
                fontsize='large')
        


plt.show()


# In[ ]:




