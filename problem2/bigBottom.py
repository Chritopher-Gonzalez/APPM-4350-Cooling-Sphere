# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 15:21:31 2022

@author: Christopher
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import data
df = pd.read_excel("../data/BigSphere.xlsx")
R = 0.03175
#print(df)
#process data
# x-axis
x = df['Time [sec]'].to_numpy()
time = x[100:500]
# y-axis
y = df['Temperature @ r=R/2 [C]'].to_numpy()
temp = np.log(y[100:500])

#find line of best fit
a, b = np.polyfit(time, temp, 1)
print(a,b)
print(-1 * (np.power(R,2)/ np.power(np.pi,2)) *  a)
#add points to plot
fig = plt.figure()
ax = plt.gca()
ax.scatter(x, y,  label='data')
#add line of best fit to plot
ax.plot(time, np.exp(a*time + b), 'ro', label='linear Fit')        
ax.set_yscale('log')
ax.legend()
ax.set_title('Big Sphere Time [sec] vs Temperature @ r=R/2 [C]')
ax.set_ylabel('Temperature @ r=R/2 [C]')
ax.set_xlabel("Time [sec]")
