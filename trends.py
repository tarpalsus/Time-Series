# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 13:47:15 2017


"""
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

df=pd.read_excel(r'champagne-sales.xlsx')
df['Month']=df['Month'].map(lambda x: '200'+str(x))
df['Month']=pd.to_datetime(df['Month'])
df=df.set_index('Month')
df.plot()
plt.show()
decomposition = sm.tsa.seasonal_decompose(df, model='additive')
fig = decomposition.plot()
plt.show()