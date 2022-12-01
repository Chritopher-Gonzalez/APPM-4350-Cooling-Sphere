# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 10:30:16 2022

@author: Christopher
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from math import* #import all function from math

#define constants
n = 10
R = 1.25 #radius of large sphere
T = 239
k = 14.0 #thermal diffusivity
Tr = 18.023
Tb = 1.0


#define range
r = np.arange(0, R, 0.001)
t = np.arange(0, T, 0.25)

#define functions
f =  lambda r: r * (Tr - Tb)
fs = lambda r: f(r) * sin(np.pi*r * i/ R)

#calc coefficents
Bn=[]

for i in range(n):
    bn = quad(fs, 0, R)[0] * (2.0 / np.power(R,2))
    #putting value in array Bn
    Bn.append(bn) 
 
#calc Fourier Series expansion
FST = 0

for i in range(n):
    FST += Bn[i] * np.sin(i*np.pi*r / R) #* np.exp(- np.power(((i*np.pi)/R) , 2) * k
                                                      
#time dependence
sol = 0 

for i in range(n):
    if i==0.0:
        sol += Tb
    else:
        sol += FST[i] * np.exp(-1 * np.power(((i*np.pi)/R) , 2) * k * t)
    
print(sol)
                                                 
plt.plot(t, sol,'g')

#plt.plot(x,y,'r--')

plt.title("fourier series")

plt.show()                                                      