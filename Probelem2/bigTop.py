# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 15:21:31 2022

@author: Christopher
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import data
df = pd.read_excel("../Data/BigSphere.xlsx")
R = 0.03175
print(df)
#process data
# x-axis
x = df['Time [sec]'].to_numpy()
x = x[100:600]
time = x
# y-axis
y = df['Temperature @ r=0 [C]'].to_numpy()
y = y[100:600]
temp = np.log(y)

#find line of best fit
a, b = np.polyfit(time, temp, 1)
print( (np.power(R,2)/ np.power(np.pi,2)) *  a)
print((np.power(R,2)/ np.power(np.pi,2)) * np.exp(a) )
#add points to plot
fig = plt.figure()
ax = plt.gca()
ax.scatter(x, y)
#add line of best fit to plot
ax.plot(x, np.exp(a*time + b))        
ax.set_yscale('log')
