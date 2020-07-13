# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 10:48:46 2019

@author: harsh
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import itertools
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn.metrics import confusion_matrix
import copy
df = pd.read_excel(r'C:\Users\harsh\OneDrive\Desktop\globalterrorism.xlsx', encoding='ISO-8859-1')

#def heatmap(data,country):
#    plt.subplots(figsize=(15,10))
#    d = data[data['country_txt']==country]
#    d2 = d.groupby(['iyear','imonth'])['nkill'].sum()
#    d2 = pd.DataFrame(d2)
#    d2 = d2.fillna(0)
#    d2.columns = ['count']
#    d2.reset_index(inplace=True)
#    d2.columns = ['Year','Month','count']
#    d2 = d2.pivot("Month","Year","count")
#    d2 = d2.fillna(0)
#    sns.heatmap(d2).set_title("Number of Deaths")
#    plt.show()
#heatmap(df,'India')  
#
#
#def succ_fail(data,country):
#    s = data[data['country_txt']==country]
#    s2 = pd.DataFrame(s.groupby(['iyear','success'])['iyear'].count())
#    s2.columns=['count']
#    s2.reset_index(inplace=True)
#    s2["dummy"]=0
#    color_set2 = ['#f71325','#20d813']
#    p = sns.tsplot(time='iyear',value='count',condition='success',data=s2,unit='dummy',color = sns.color_palette(color_set2))
#    p.set_title(country)
#    p.set_ylabel("Number of Attacks")
#    p.set_xlabel("Year")
#    plt.show()
#
#plot_countries =['India']
#for i in plot_countries:
#    succ_fail(df,i)
#    
    
import folium

# Get a basic world map.
gtd_map = folium.Map(location=[30, 0], zoom_start=2);

# Take a sample of the data points
gtd_sample = df.sample(3000);

# Draw markers on the map.
for index, row in gtd_sample.iterrows():
    folium.CircleMarker([row[7], row[8]], radius=0.5, color='#E74C3C', 
                        fill_color='#E74C3C').add_to(gtd_map);


# Show the map
gtd_map