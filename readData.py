# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 15:21:31 2022

@author: Christopher
"""

import pandas as pd
df = pd.read_excel("Data/BigSphere.xlsx")
print(df)

ax1 = df.plot.scatter(x='Time [sec]', y='Temperature @ r=0 [C]', c='DarkBlue', logx=True)