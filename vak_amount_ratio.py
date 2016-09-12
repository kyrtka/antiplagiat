# -*- coding: utf-8 -*-
__author__ = 'dberesneva'

#plots the graph of share of plagiarism for each dissovet or vak according to the amount of papers

import pandas as pd
from pylab import *
matplotlib.rc('font', family='Arial')

node=pd.read_csv('C:/Python27/new/Node.csv', delimiter=';',encoding="cp1251").convert_objects(convert_numeric=True)
author=pd.read_csv('C:/Python27/new/test.csv', delimiter=';',encoding="cp1251").convert_objects(convert_numeric=True)
node = node[~node.DocId.isin(author.DocId)]
node=node[node['PublicationDate'] > 2005]
edge=pd.read_csv('C:/Python27/new/Edgecopy.csv', delimiter=';',encoding="utf-8-sig").convert_objects(convert_numeric=True)
n=node[['DocId', 'PastPlagiarism', 'TextLength', 'Vak', 'DissertationCouncilCode']]
n=n.rename(columns={'DissertationCouncilCode': 'diss'})
e=edge[['DocId']]
mix=pd.merge(n, e, on=['DocId'])
mix['new_vak']=mix['Vak'].str[:2]

#org=pd.read_csv('C:/Python27/new/diss-org/orgdis.csv', delimiter=';',encoding="cp1251").convert_objects(convert_numeric=True)
#k=pd.merge(mix, org, on =['diss'])


#k=pd.merge(n, cll, on=['diss'])
open=pd.read_csv('C:/Python27/new/diss-org/orgdis.csv', delimiter=';',encoding="cp1251").convert_objects(convert_numeric=True)
mixx=pd.merge(mix, open, on=['diss'])
closed=mix[~mix['diss'].isin(open['diss'])]
mixx['org+vak']=mixx['org'] +','+ mixx['new_vak']

length=mixx.groupby(['diss']).agg({'TextLength' : 'mean', 'DocId':'count'}).reset_index()
plag=mixx.groupby(['diss']).agg({'PastPlagiarism' : 'mean'}).reset_index()
z= pd.merge(length, plag, on=['diss'])
z['ratio']=z.PastPlagiarism/z.TextLength
#a=z.sort(['DocId', 'ratio'], ascending=[True,True])
#z[['ratio', 'DocId', 'diss']].to_csv('C:/Python27/new/open_dissovet.csv',encoding="utf-8-sig")

print z[z['ratio']>0.7]
plot( z['DocId'], z['ratio'], '.')
xlabel(u'Количество работ')
ylabel(u'Средняя доля заимствований')
title(u'Доля заимствований (ВАК+Организация)')
#xscale('log')
#plt.text(0.75, 900,  u'Точка - пара "Организация - ВАК"')
show()



#vak=pd.read_csv('C:/Python27/new/vak-amount.csv', delimiter=';',encoding="utf-8-sig").convert_objects(convert_numeric=True)
#plot( vak.amount, vak.ratio, '.')
#ylabel(u'Средняя доля заимствований')
#xlabel(u'Количество работ')
#title(u'Доля заимствований по количеству работ')
#for i, txt in enumerate(vak.new_vak):
    #annotate(txt, (vak.amount[i], vak.ratio[i]))





