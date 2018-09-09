# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 17:14:51 2018
The purpose of this script is to find users who visit many unique access points over the course of a day.
These are the ideal movements to plot.
@author: munib
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Iterate through user ids

# uc-wifi-dates is the dataset found at https://www.data.act.gov.au/Infrastructure-and-Utilities/University-of-Canberra-WiFi-Usage/pawc-bj4d
# I have basically just added two more columns to it, one for month and one for day
df = pd.read_csv('uc-wifi-dates.csv')

ids_checked = []
numChecked = 0; # There are 12233
most_unique = 0
most_unique_user = None
most_unique_day = 0
most_unique_month = 0
for user_id in df['USER_ID']:
    if user_id not in ids_checked:
        user_df = df[df.USER_ID == user_id]
        for day in range(0, 31):
            for month in range(0, 12):
                user_df_for_day = user_df[(user_df.Day == day) & (user_df.Month == month)]
                num_unique = user_df_for_day['LOCATION_DESC'].nunique()
                if num_unique > most_unique:
                    most_unique = num_unique
                    most_unique_user = user_id
                    most_unique_day = day
                    most_unique_month = month
                    
        ids_checked.append(user_id)
        numChecked += 1
        print("Num checked:", numChecked)
        print("Most unique:", str(most_unique), "User", str(most_unique_user), "Day", str(most_unique_day), "Month", str(most_unique_month))
        
        
print "________________"
print most_unique_user
print most_unique_day
print most_unique_month
        