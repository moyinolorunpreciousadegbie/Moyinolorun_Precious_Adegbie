import numpy as np

hh=np.array([[1,2,30,40,5],[6,7,8,9,10],[110,12,13,14,15],[16,17,1800,19,20]])

i = -1
while i <=2:
  i += 1
  print( np.where(   (hh[i,0:5]) == (np.max(hh,axis=1)[i])  )  )
 

