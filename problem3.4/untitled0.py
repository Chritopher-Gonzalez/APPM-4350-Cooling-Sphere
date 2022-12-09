# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 23:17:09 2022

@author: Christopher
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import* #import all function from math

#define constants
n = 50
R = 0.0238125 #radius of large sphere in meters
T = 239
k = 3.1312109309164268e-06 #thermal diffusivity
Tr = 22.029
Tb = -0.0759

#define range
#r = np.arange(0, R, R/956)
r = 0
#t = np.arange(0, T, 0.25)

#calc coefficents
An=[]

for i in range(n):
    an = -2 * np.power(-1, i) * (Tr - Tb)
    An.append(an) 
 
#calc coefficents
Bn=[]

for i in range(n):
    bn =  np.sinc((r * i) / R)
    Bn.append(bn)

#calc coefficents
Cn=[]

for i in range(n):
    cn = np.exp(-1 * np.power(((i*np.pi)/R) , 2) * k)
    Cn.append(cn)


#calc Fourier Series expansion    
sol = 1000
t = 0.0

while(sol > -0.0758):
    sol = 0
    for i in range(n):
        if i==0.0:
            sol += Tb
        else:
            sol += An[i] * Bn [i] * np.power(Cn[i], t)
    t += 0.25
    print(sol, t)
    
            
print(0)