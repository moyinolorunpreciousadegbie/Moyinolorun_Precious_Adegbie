#!/usr/bin/env python3

DEPTH = [0,   1000,   2000,   3800,    5400,    6000,    7600]
VP =    [  9000,   7000,  12000,  10000,   14000,   10000] # DEPTH - 1
DENSITY=[   2.4,   2.2,   2.7,    2.5,     2.2,     2.5]   # DEPTH - 1



IMPEDENCE = []
REFLECTION_COEFFICIENT = []
SYNTHETIC = []


CUM_REFLECTION_COEFFICIENT = 0

REFLECTION_COEFFICIENT_REAL = []


for thickness in range(len(DEPTH)-1) :
	THICKNESS_depth = DEPTH[thickness+1]   -  DEPTH[thickness]
	ind = thickness
	#print(THICKNESS)
	IMPEDENCE.append(VP[ind]*DENSITY[ind])  
	
	if ind <= len(VP) - 2 :
		
	                                        # LAYER 2                        LAYER 1                         LAYER 2                        LAYER 1
		REFLECTION_COEFFICIENT_REAL.append( ( (VP[ind+1]*DENSITY[ind+1]) -  (VP[ind]*DENSITY[ind])  )  / ( (VP[ind+1]*DENSITY[ind+1]) +  (VP[ind]*DENSITY[ind])  )       ) 
		
		
		
	if ind == 0 :
		REFLECTION_COEFFICIENT.append(   (THICKNESS_depth * 2) / VP[ind]    )
	
	if ind > 0 :
		REFLECTION_COEFFICIENT.append(  REFLECTION_COEFFICIENT[-1] +  (THICKNESS_depth * 2) / VP[ind]    )
		
	
	if len(REFLECTION_COEFFICIENT) > 0 :
		SYNTHETIC.append(REFLECTION_COEFFICIENT[-1]* 1000)  # seconds to milliseconds  X 1000
	
	
	
print(IMPEDENCE)
print(REFLECTION_COEFFICIENT_REAL)
print()
	
print(REFLECTION_COEFFICIENT)
print(SYNTHETIC)
	
	
	
	
	


