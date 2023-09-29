#!/usr/bin/env python3
import numpy as np


## CUMULATIVE % RETAINED IN EACH SIEVE VALUES IN NUMPY ARRAY
# MONAHANS SAND A 

a = np.array([1.402805611
, 2.004008016
, 3.206412826
, 5.01002004
, 40.08016032
, 92.38476954
, 92.98597194
, 94.38877756
, 95.19038076
, 95.79158317
, 96.79358717
, 97.79559118
, 99.19839679
, 100])
#print(np.percentile(a, 5))   

Graphic_Mean_a = ( np.percentile(a, 16) + np.percentile(a, 50) + np.percentile(a, 84)  )/ 3

Inclusive_Graphic_Mean_a = ( (np.percentile(a, 84) - np.percentile(a, 16))/ 4 )   +  ( (np.percentile(a, 95) - np.percentile(a, 5))/ 6.6 ) 

Simple_Sorting_a = 0.5 *  (np.percentile(a, 95) - np.percentile(a, 5))

Inclusive_Sorting_Skewness_a = (       (np.percentile(a, 84) + np.percentile(a, 16) - (2 * np.percentile(a, 50) )       )  / (2 *(np.percentile(a, 84) - np.percentile(a, 16))      ) +   (       (np.percentile(a, 95) + np.percentile(a, 5) - (2 * np.percentile(a, 50) ))  / (2 *  (np.percentile(a, 95) - np.percentile(a, 5))))  )

Simple_Skewness_Measure_a = (np.percentile(a, 95) + np.percentile(a, 5) )  - (2 * np.percentile(a, 50))

Graphic_Kurtosis_a = ( np.percentile(a, 95) - np.percentile(a, 5) ) /  (2.44 *  (np.percentile(a, 75) - np.percentile(a, 25)) )

print("MONAHANS SAND A:",end='\n')
print("Graphic Mean:",Graphic_Mean_a,"||  Inclusive Graphic Mean:",Inclusive_Graphic_Mean_a,"||  Simple Sorting:",Simple_Sorting_a,"||  Inclusive Sorting Skewness:",Inclusive_Sorting_Skewness_a, "||   Simple Skewness Measure:",Simple_Skewness_Measure_a,"||  Graphic_Kurtosis:",Graphic_Kurtosis_a)
print(end='\n')
############################################################################################################################################################################
# MONAHANS SAND B

b = np.array([0.201207243
, 0.804828974
, 1.207243461
, 2.816901408
, 42.65593561
, 94.56740443
, 96.57947686
, 97.78672032
, 98.18913481
, 98.79275654
, 99.19517103
, 99.39637827
, 99.79879276
,	100])
#print(np.percentile(b, 0))

Graphic_Mean_b = ( np.percentile(b, 16) + np.percentile(b, 50) + np.percentile(b, 84)  )/ 3

Inclusive_Graphic_Mean_b = ( (np.percentile(b, 84) - np.percentile(b, 16))/ 4 )   +  ( (np.percentile(b, 95) - np.percentile(b, 5))/ 6.6 ) 

Simple_Sorting_b = 0.5 *  (np.percentile(b, 95) - np.percentile(b, 5))

Inclusive_Sorting_Skewness_b = (       (np.percentile(b, 84) + np.percentile(b, 16) - (2 * np.percentile(b, 50) )       )  / (2 *(np.percentile(b, 84) - np.percentile(b, 16))      ) +   (       (np.percentile(b, 95) + np.percentile(b, 5) - (2 * np.percentile(b, 50) ))  / (2 *  (np.percentile(b, 95) - np.percentile(b, 5))))  )

Simple_Skewness_Measure_b = (np.percentile(b, 95) + np.percentile(b, 5) )  - (2 * np.percentile(b, 50))

Graphic_Kurtosis_b = ( np.percentile(b, 95) - np.percentile(b, 5) ) /  (2.44 *  (np.percentile(b, 75) - np.percentile(b, 25)) )

print("MONAHANS SAND B:",end='\n')
print("Graphic Mean:",Graphic_Mean_b,"||  Inclusive Graphic Mean:",Inclusive_Graphic_Mean_b,"||  Simple Sorting:",Simple_Sorting_b,"||  Inclusive Sorting Skewness:",Inclusive_Sorting_Skewness_b, "||   Simple Skewness Measure:",Simple_Skewness_Measure_b,"||  Graphic_Kurtosis:",Graphic_Kurtosis_b )
print(end='\n')


############################################################################################################################################################################
# MONAHANS SAND C

c = np.array([0.60483871
, 1.008064516
, 1.612903226
, 4.435483871
, 42.74193548
, 93.75
, 94.55645161
, 95.56451613
, 96.37096774
, 97.37903226
, 97.98387097
, 98.79032258
, 99.39516129
,	100])
#  print(np.percentile(c, 95))

Graphic_Mean_c = ( np.percentile(c, 16) + np.percentile(c, 50) + np.percentile(c, 84)  )/ 3

Inclusive_Graphic_Mean_c = ( (np.percentile(c, 84) - np.percentile(c, 16))/ 4 )   +  ( (np.percentile(c, 95) - np.percentile(c, 5))/ 6.6 ) 

Simple_Sorting_c = 0.5 *  (np.percentile(c, 95) - np.percentile(c, 5))

Inclusive_Sorting_Skewness_c = (       (np.percentile(c, 84) + np.percentile(c, 16) - (2 * np.percentile(c, 50) )       )  / (2 *(np.percentile(c, 84) - np.percentile(c, 16))      ) +   (       (np.percentile(c, 95) + np.percentile(c, 5) - (2 * np.percentile(c, 50) ))  / (2 *  (np.percentile(c, 95) - np.percentile(c, 5))))  )

Simple_Skewness_Measure_c = (np.percentile(c, 95) + np.percentile(c, 5) )  - (2 * np.percentile(c, 50))

Graphic_Kurtosis_c = ( np.percentile(c, 95) - np.percentile(c, 5) ) /  (2.44 *  (np.percentile(c, 75) - np.percentile(c, 25)) )

print("MONAHANS SAND c:",end='\n')
print("Graphic Mean:",Graphic_Mean_c,"||  Inclusive Graphic Mean:",Inclusive_Graphic_Mean_c,"||  Simple Sorting:",Simple_Sorting_c,"||  Inclusive Sorting Skewness:",Inclusive_Sorting_Skewness_c, "||   Simple Skewness Measure:",Simple_Skewness_Measure_c,"||  Graphic_Kurtosis:",Graphic_Kurtosis_c )
print(end='\n')

print("########################################################################################################################################################################")
############################################################################################################################################################################
#   MONAHANS CLASSWORK EXERCISE

m = np.array([0.128040973
, 1.05924805
, 70.4341753
, 99.06879292
, 99.53439646
,	100])
#print(np.percentile(m, 95))

Graphic_Mean_m = ( np.percentile(m, 16) + np.percentile(m, 50) + np.percentile(m, 84)  )/ 3

Inclusive_Graphic_Mean_m = ( (np.percentile(m, 84) - np.percentile(m, 16))/ 4 )   +  ( (np.percentile(m, 95) - np.percentile(m, 5))/ 6.6 ) 

Simple_Sorting_m = 0.5 *  (np.percentile(m, 95) - np.percentile(m, 5))

Inclusive_Sorting_Skewness_m = (       (np.percentile(m, 84) + np.percentile(m, 16) - (2 * np.percentile(m, 50) )       )  / (2 *(np.percentile(m, 84) - np.percentile(m, 16))      ) +   (       (np.percentile(m, 95) + np.percentile(m, 5) - (2 * np.percentile(m, 50) ))  / (2 *  (np.percentile(m, 95) - np.percentile(m, 5))))  )

Simple_Skewness_Measure_m = (np.percentile(m, 95) + np.percentile(m, 5) )  - (2 * np.percentile(m, 50))

Graphic_Kurtosis_m = ( np.percentile(m, 95) - np.percentile(m, 5) ) /  (2.44 *  (np.percentile(m, 75) - np.percentile(m, 25)) )

print("MONAHANS CLASSWORK EXERCISE:",end='\n')
print("Graphic Mean:",Graphic_Mean_m,"||  Inclusive Graphic Mean:",Inclusive_Graphic_Mean_m,"||  Simple Sorting:",Simple_Sorting_m,"||  Inclusive Sorting Skewness:",Inclusive_Sorting_Skewness_m, "||   Simple Skewness Measure:",Simple_Skewness_Measure_m,"||  Graphic_Kurtosis:",Graphic_Kurtosis_m )
print(end='\n')

############################################################################################################################################################################
#   PADRE ISLAND CLASSWORK EXERCISE  


p = np.array([0.349344978
, 0.786026201
, 1.484716157
, 97.55458515
, 98.60262009
, 	100])
#print(np.percentile(p, 0))

Graphic_Mean_p = ( np.percentile(p, 16) + np.percentile(p, 50) + np.percentile(p, 84)  )/ 3

Inclusive_Graphic_Mean_p = ( (np.percentile(p, 84) - np.percentile(p, 16))/ 4 )   +  ( (np.percentile(p, 95) - np.percentile(p, 5))/ 6.6 ) 

Simple_Sorting_p = 0.5 *  (np.percentile(p, 95) - np.percentile(p, 5))

Inclusive_Sorting_Skewness_p = (       (np.percentile(p, 84) + np.percentile(p, 16) - (2 * np.percentile(p, 50) )       )  / (2 *(np.percentile(p, 84) - np.percentile(p, 16))      ) +   (       (np.percentile(p, 95) + np.percentile(p, 5) - (2 * np.percentile(p, 50) ))  / (2 *  (np.percentile(p, 95) - np.percentile(p, 5))))  )

Simple_Skewness_Measure_p = (np.percentile(p, 95) + np.percentile(p, 5) )  - (2 * np.percentile(p, 50))

Graphic_Kurtosis_p = ( np.percentile(p, 95) - np.percentile(p, 5) ) /  (2.44 *  (np.percentile(p, 75) - np.percentile(p, 25)) )

print("PADRE ISLAND CLASSWORK EXERCISE:",end='\n')
print("Graphic Mean:",Graphic_Mean_p,"||  Inclusive Graphic Mean:",Inclusive_Graphic_Mean_p,"||  Simple Sorting:",Simple_Sorting_p,"||  Inclusive Sorting Skewness:",Inclusive_Sorting_Skewness_p, "||   Simple Skewness Measure:",Simple_Skewness_Measure_p,"||  Graphic_Kurtosis:",Graphic_Kurtosis_p )
print(end='\n')

############################################################################################################################################################################
#  CHIMAYO CLASSWORK EXERCISE 

c = np.array([ 0
, 6.827309237
, 23.4939759
, 65.6626506
, 90.76305221
,	100])
# print(np.percentile(c, 0))

Graphic_Mean_c = ( np.percentile(c, 16) + np.percentile(c, 50) + np.percentile(c, 84)  )/ 3

Inclusive_Graphic_Mean_c = ( (np.percentile(c, 84) - np.percentile(c, 16))/ 4 )   +  ( (np.percentile(c, 95) - np.percentile(c, 5))/ 6.6 ) 

Simple_Sorting_c = 0.5 *  (np.percentile(c, 95) - np.percentile(c, 5))

Inclusive_Sorting_Skewness_c = (       (np.percentile(c, 84) + np.percentile(c, 16) - (2 * np.percentile(c, 50) )       )  / (2 *(np.percentile(c, 84) - np.percentile(c, 16))      ) +   (       (np.percentile(c, 95) + np.percentile(c, 5) - (2 * np.percentile(c, 50) ))  / (2 *  (np.percentile(c, 95) - np.percentile(c, 5))))  )

Simple_Skewness_Measure_c = (np.percentile(c, 95) + np.percentile(c, 5) )  - (2 * np.percentile(c, 50))

Graphic_Kurtosis_c = ( np.percentile(c, 95) - np.percentile(c, 5) ) /  (2.44 *  (np.percentile(c, 75) - np.percentile(c, 25)) )

print("CHIMAYO CLASSWORK EXERCISE:",end='\n')
print("Graphic Mean:",Graphic_Mean_c,"||  Inclusive Graphic Mean:",Inclusive_Graphic_Mean_c,"||  Simple Sorting:",Simple_Sorting_c,"||  Inclusive Sorting Skewness:",Inclusive_Sorting_Skewness_c, "||   Simple Skewness Measure:",Simple_Skewness_Measure_c,"||  Graphic_Kurtosis:",Graphic_Kurtosis_c )
print(end='\n')

############################################################################################################################################################################
#  WHITE SANDS CLASSWORK EXERCISE

w = np.array([0
,	0
,	42.33870968
,	99.39516129
,	100
,	100])
#print(np.percentile(w, 75))

Graphic_Mean_w = ( np.percentile(w, 16) + np.percentile(w, 50) + np.percentile(w, 84)  )/ 3

Inclusive_Graphic_Mean_w = ( (np.percentile(w, 84) - np.percentile(w, 16))/ 4 )   +  ( (np.percentile(w, 95) - np.percentile(w, 5))/ 6.6 ) 

Simple_Sorting_w = 0.5 *  (np.percentile(w, 95) - np.percentile(w, 5))

Inclusive_Sorting_Skewness_w = (       (np.percentile(w, 84) + np.percentile(w, 16) - (2 * np.percentile(w, 50) )       )  / (2 *(np.percentile(w, 84) - np.percentile(w, 16))      ) +   (       (np.percentile(w, 95) + np.percentile(w, 5) - (2 * np.percentile(w, 50) ))  / (2 *  (np.percentile(w, 95) - np.percentile(w, 5))))  )

Simple_Skewness_Measure_w = (np.percentile(w, 95) + np.percentile(w, 5) )  - (2 * np.percentile(w, 50))

Graphic_Kurtosis_w = ( np.percentile(w, 95) - np.percentile(w, 5) ) /  (2.44 *  (np.percentile(w, 75) - np.percentile(w, 25)) )
	
print("WHITE SANDS CLASSWORK EXERCISE:",end='\n')
print("Graphic Mean:",Graphic_Mean_w,"||  Inclusive Graphic Mean:",Inclusive_Graphic_Mean_w,"||  Simple Sorting:",Simple_Sorting_w,"||  Inclusive Sorting Skewness:",Inclusive_Sorting_Skewness_w, "||   Simple Skewness Measure:",Simple_Skewness_Measure_w,"||  Graphic_Kurtosis:",Graphic_Kurtosis_w )
print(end='\n')	
############################################################################################################################################################################
# OAKWOOD BEACHSAND CLASSWORK EXERCISE

o = np.array([0
,	6.451612903
,	97.98387097
,	100
,	100])
# print(np.percentile(o, 16))

Graphic_Mean_o = ( np.percentile(o, 16) + np.percentile(o, 50) + np.percentile(o, 84)  )/ 3

Inclusive_Graphic_Mean_o = ( (np.percentile(o, 84) - np.percentile(o, 16))/ 4 )   +  ( (np.percentile(o, 95) - np.percentile(o, 5))/ 6.6 ) 

Simple_Sorting_o = 0.5 *  (np.percentile(o, 95) - np.percentile(o, 5))

Inclusive_Sorting_Skewness_o = (       (np.percentile(o, 84) + np.percentile(o, 16) - (2 * np.percentile(o, 50) )       )  / (2 *(np.percentile(o, 84) - np.percentile(o, 16))      ) +   (       (np.percentile(o, 95) + np.percentile(o, 5) - (2 * np.percentile(o, 50) ))  / (2 *  (np.percentile(o, 95) - np.percentile(o, 5))))  )

Simple_Skewness_Measure_o = (np.percentile(o, 95) + np.percentile(o, 5) )  - (2 * np.percentile(o, 50))

Graphic_Kurtosis_o = ( np.percentile(o, 95) - np.percentile(o, 5) ) /  (2.44 *  (np.percentile(o, 75) - np.percentile(o, 25)) )

print("OAKWOOD BEACHSAND CLASSWORK EXERCISE:",end='\n')
print("Graphic Mean:",Graphic_Mean_o,"||  Inclusive Graphic Mean:",Inclusive_Graphic_Mean_o,"||  Simple Sorting:",Simple_Sorting_o,"||  Inclusive Sorting Skewness:",Inclusive_Sorting_Skewness_o, "||   Simple Skewness Measure:",Simple_Skewness_Measure_o,"||  Graphic_Kurtosis:",Graphic_Kurtosis_o )
print(end='\n')	