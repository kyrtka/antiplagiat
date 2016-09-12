# -*- coding: utf-8 -*-
__author__ = 'dberesneva'



import pandas as pd
from pylab import *
matplotlib.rc('font', family='Arial')


opp=pd.read_csv('C:/Python27/new/diss-org/open.csv', delimiter=';',encoding="cp1251").convert_objects(convert_numeric=True)
#a=opp.groupby(['org']).agg({'amount' : 'sum', 'unique': 'mean', 'demand': 'mean', 'origin': 'mean'}).reset_index()
cll=pd.read_csv('C:/Python27/new/diss-org/closed.csv', delimiter=';',encoding="cp1251").convert_objects(convert_numeric=True)
#b=cll.groupby(['org']).agg({'amount' : 'sum', 'unique': 'mean', 'demand': 'mean', 'origin': 'mean'}).reset_index()


matplotlib.rc('font', family='Arial')

node=pd.read_csv('C:/Python27/new/Node.csv', delimiter=';',encoding="cp1251").convert_objects(convert_numeric=True)
author=pd.read_csv('C:/Python27/new/test.csv', delimiter=';',encoding="cp1251").convert_objects(convert_numeric=True)
node = node[~node.DocId.isin(author.DocId)]
disorg=pd.read_csv('C:/Python27/new/diss-org/orgdis.csv', delimiter=';',encoding="cp1251").convert_objects(convert_numeric=True)
edge=pd.read_csv('C:/Python27/new/Edgecopy.csv', delimiter=';',encoding="utf-8-sig").convert_objects(convert_numeric=True)
n=node[['DocId', 'PastPlagiarism', 'TextLength', 'Vak', 'DissertationCouncilCode']]
e=edge[['DocId']]
merg=pd.merge(n, e, on=['DocId'])
merg= n.rename(columns={'DissertationCouncilCode': 'diss'})
mix=pd.merge(merg, cll, on=['diss'])
mix['new_vak']=mix['Vak'].str[:2]
mix['diss'].str.upper()

length=mix.groupby(['diss']).agg({'TextLength' : 'mean', 'DocId':'count'}).reset_index()
plag=mix.groupby(['diss']).agg({'PastPlagiarism' : 'mean'}).reset_index()
z= pd.merge(length, plag, on=['diss'])
z['ratio']=z.PastPlagiarism/z.TextLength
#a=z.sort(['DocId', 'ratio'], ascending=[True,True])
#z[['diss', 'ratio']].to_csv('C:/Python27/new/open_dissovet.csv',encoding="cp1251")

plot( z['DocId'], z['ratio'], '.')
xlabel(u'Количество работ')
ylabel(u'Средняя доля заимствований')
title(u'Доля заимствований для закрытых диссоветов')
#xscale('log')
plt.text(0.69, 1310, u'Точка - диссовет')
show()