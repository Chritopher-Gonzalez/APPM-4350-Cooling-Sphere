# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 22:14:35 2022

@author: Christopher
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import data
df = pd.read_excel("../data/SmallSphereNitrogen.xlsx")
R = 0.03175
#process data
# x-axis
x = df['Time [sec]'].to_numpy()
time = x[0:]
# y-axis
y = -1 * df['Temperature @ r=R/2 [C]'].to_numpy()
temp = np.log(y[0:])

#find line of best fit
a, b = np.polyfit(time, temp, 1)
print( (np.power(R,2)/ np.power(np.pi,2)) *  a)
#add points to plot
fig = plt.figure()
ax = plt.gca()
ax.scatter(x, y)
#add line of best fit to plot
ax.plot(time, np.exp(a*time + b), 'ro')        
ax.set_yscale('symlog')
