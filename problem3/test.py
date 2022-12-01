# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 12:10:52 2022

@author: Christopher
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from math import* #import all function from math

#define constants
n = 50
R = 1.25 #radius of large sphere
T = 239
k = -14.0 #thermal diffusivity
Tr = 18.023
Tb = 0.06

#define range
r = np.arange(0, R, 0.001)
t = np.arange(0, T, 0.25)

#define functions
f =  lambda r: r * (Tr - Tb)
fs = lambda r: f(r) * sin(np.pi*r / R)
bn = quad(fs, 0, R)[0] * (2.0 / np.power(R,2))

sol = []

for i in t:
    sol.append(Tb + (bn * sin(np.pi* (0) / R) * np.exp(-1 * np.power((np.pi / R), 2) * k * i) ))
    
#sol = lambda t: Tb + (bn * sin(np.pi*r / R) * np.exp(-1 * np.power((np.pi / R), 2) * k * t) ) 

plt.plot(t, sol,'g')

plt.title("fourier series")

plt.show()    