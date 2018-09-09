# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 12:22:24 2018

This script plots movements for specific users on a specific day, and outputs a list of lat/long coords
that can be fed into the Javascript application
@author: munib
"""



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

df_original = pd.read_csv('uc-wifi-dates.csv')


# 28970, 26, 4 - Seems to be working fine
# Also try 31200, 26, 4  - Does NOT seem to work anymore
# 38577 19, 4 - Does NOT work anymore

# New

# 39855, 3, 5
# 38577, 27, 4
#

user_id = 38577 
day = 27
month = 4


df = df_original[df_original.USER_ID == user_id]

df = df[(df.Day == day) & (df.Month == month)]

x, y = df['LATITUDE'], df['LONGITUDE']
print len(x)
for i in range(0, len(x), 2):
    plt.plot(x[i:i+2], y[i:i+2], 'ro-')
    

df = df_original[df_original.USER_ID == user_id]

df = df[(df.Day == day) & (df.Month == month)]
x, y = df['LATITUDE'], df['LONGITUDE']
latitudes = list(x)
longitudes = list(y)
f = open(str(user_id) + '.txt', 'w')
f.write('var line' + str(user_id) + '=[')
for i in range(0, len(x)-1):
    lat_next = latitudes[i + 1]
    long_next = longitudes[i + 1]
    lat_this = latitudes[i]
    long_this = longitudes[i]
    
    line_segment = '{lat:' + str(lat_this) + ', lng:' + str(long_this) + '},'
    line_segment += '\n' + '{lat:' + str(lat_next) + ', lng:' + str(long_next) + '}'
    
    if i != len(x)-2:
        line_segment += ','
    
    f.write(line_segment + '\n')
    
f.write('];')
f.close()
plt.show()