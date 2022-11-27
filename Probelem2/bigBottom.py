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
print(df)
#process data
# x-axis
x = df['Time [sec]'].to_numpy()
x = x[300:]
time = np.log(x)
# y-axis
y = df['Temperature @ r=R/2 [C]'].to_numpy()
y = y[300:]
temp = np.log(y)

#find line of best fit
a, b = np.polyfit(time, temp, 1)
print(a,b)
print(np.exp(a),np.exp(b))
#add points to plot
plt.scatter(x, y)
#add line of best fit to plot
plt.plot(x, np.exp(a*time + b ))        
#log scale
plt.loglog()