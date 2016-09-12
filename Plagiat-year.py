# -*- coding: utf-8 -*-
__author__ = 'dberesneva'

import pandas as pd
from pylab import *
matplotlib.rc('font', family='Arial')

opendata=pd.read_csv('C:/Python27/new/Node.csv', delimiter=';',encoding="cp1251").convert_objects(convert_numeric=True)
edge=pd.read_csv('C:/Python27/new/Edgecopy.csv', delimiter=';',encoding="utf-8-sig").convert_objects(convert_numeric=True)
author=pd.read_csv('C:/Python27/new/test.csv', delimiter=';',encoding="cp1251").convert_objects(convert_numeric=True)
opendata = opendata[~opendata.DocId.isin(author.DocId)]

dff=opendata[opendata['PublicationDate'] < 2015] #all papers before 2016
df=dff[dff['PublicationDate'] > 2004]#all papers after 1970
k= pd.merge(df,edge, on=['DocId'])
length=df.groupby(['PublicationDate']).agg({'TextLength' : 'mean'}).reset_index()
plag=df.groupby(['PublicationDate']).agg({'PastPlagiarism' : 'mean'}).reset_index()
plag['l']=plag.PastPlagiarism/length.TextLength
k= pd.merge(length,plag, on=['PublicationDate']).drop(['PublicationDate', 'PastPlagiarism'], axis=1)
#k.to_csv('C:/Python27/Data/yearplag.csv')
plag[['PublicationDate', 'l']].to_csv('C:/Python27/new/year-plag.csv', encoding="utf-8-sig")


matplotlib.rc('font', family='Arial')
stepsize = 1
fig, ax = plt.subplots()
print plag.PublicationDate
ax.bar(plag.PublicationDate, plag.l)
start, end = ax.get_xlim()
ax.set_xlabel(u'Год')
ax.set_ylabel(u'Доля заимствований в работе')
ax.set_title(u'Объём заимствований по годам')
ax.xaxis.set_ticks(np.arange(start, end, stepsize))
plt.show()







