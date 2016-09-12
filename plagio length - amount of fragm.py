__author__ = 'dberesneva'


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import os
from sklearn import preprocessing
from sklearn.preprocessing import normalize

#encoding="utf-8-sig"

openinter=pd.read_csv('C:/Python27/new/Intersection2.csv', delimiter=';',encoding="utf-8-sig").convert_objects(convert_numeric=True)

new=opendata[['DocId', 'Shift','Size']].drop(opendata.index[-1])
l= openinter.groupby('DocId')['DocId'].count()
m = openinter.groupby(['DocId']).agg({'Size' : 'sum'}).reset_index()
plt.xlabel('Fragment length')
plt.ylabel('Amount of fragments')
plt.title(r'Plagio length - Amount of fragments')
plt.bar( m.Size, l)
plt.show()