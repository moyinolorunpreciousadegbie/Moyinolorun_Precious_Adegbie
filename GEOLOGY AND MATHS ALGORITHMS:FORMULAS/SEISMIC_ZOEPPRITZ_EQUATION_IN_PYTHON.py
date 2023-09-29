###############################################################################################################################
# PYTHON ALGORITHM TEST 

import numpy as np
from numpy.linalg import inv

u=np.array([[1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16]])
           
g= np.array([[1],
             [2],
             [3],
             [4]])
# g= np.array([1,2,3,4])     
             
print(np.dot(u,g))

# np.matmul(u,g)


theta1 = 2.57
theta2 = 2.9
phi1 = 2.57
phi2 = 2.9
    
Vp1 = 2.45
Vp2 = 2.5

Vs1 = 2.4
Vs2 = 2.35
    
Rho1 = 2.15
Rho2 = 2.53

A= np.array([ [-np.sin(theta1), -np.cos(phi1), np.sin(theta2), np.cos(phi2)     ],
         [ np.cos(theta1),  -np.sin(phi1), np.cos(theta2), -np.sin(phi2)   ],
                
[np.sin(2*theta1), ((Vp1/Vs1)*np.cos(2*phi1)), 
 ( ( (Rho2*(Vs2**2)*Vp1)/(Rho1*(Vs1**2)*Vp2) ) * np.sin(2*theta2) ),
                  ( (Rho2*Vs2*Vp1)/(Rho1*(Vs1**2)) ) * np.cos(2*phi2)],
                      
[-np.cos(2*phi1), (Vs1/Vp1)*np.sin(2*phi1), 
  ( (Rho2*Vp2)/(Rho1*Vp1) ) * np.cos(2*phi2),
                              (-(Rho2*Vs2)/(Rho1*Vp1 )) * np.sin(2*phi2)]])
                              
A2 = np.array([[np.sin(theta1)],
               [np.cos(theta1)],
               [np.sin(2*theta1)],
               [np.cos(2*phi1)  ]])
               
A1= inv(A)  

determinant = np.linalg.det(A)
Adjoint  = np.linalg.inv(A)* determinant
print("\nThe Adjoint is :")
print("\n",Adjoint )
print("\nThe Inverse is :")
print("\n",np.round(np.linalg.inv(A),6))
print("\nThe Determinant is :")
print("\n",np.linalg.det(A))

print("\nThe Zoeppritz is :")
print("\n",np.dot(A1,A2))
