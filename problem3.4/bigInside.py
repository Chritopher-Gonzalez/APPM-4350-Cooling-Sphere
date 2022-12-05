# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 18:35:51 2022

@author: Christopher
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import* #import all function from math

#load data
df = pd.read_excel("../Data/BigSphere.xlsx")

#define constants
n = 5
R = 0.03175 #radius of large sphere in meters
T = 239
k = 3.1443199047295477e-06 #thermal diffusivity
Tr = 18.023
Tb = 0.0

#define range
#r = np.arange(0, R, R/956)
r = 0
t = np.arange(0, T, 0.25)

#calc coefficents
An=[]

for i in range(n):
    an = (-2 * np.power(-1, i)) * (Tr - Tb)
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
sol = 0

for i in range(n):
    if i==0.0:
        sol += Tb
    else:
        sol += An[i] * Bn [i] * np.power(Cn[i], t)
   
print(sol)     
#add points to plot

#process data
x = df['Time [sec]'].to_numpy()
y = df['Temperature @ r=R/2 [C]'].to_numpy()

fig = plt.figure()
ax = plt.gca()
ax.plot(t, sol,'g')  
ax.plot(x, y,'b')  
ax.set_yscale('log')