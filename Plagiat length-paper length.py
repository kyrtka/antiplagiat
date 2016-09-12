# -*- coding: utf-8 -*-
__author__ = 'dberesneva'

import pandas as pd
from pylab import *

node=pd.read_csv('C:/Python27/new/Nodecopy.csv', delimiter=';',encoding="utf-8-sig").convert_objects(convert_numeric=True)
dfff=node[node['PublicationDate'] < 2016]
dff=dfff[dfff['PublicationDate'] >= 2005]
df=dff[dff['PastPlagiarism'] != 0]
df['new_vak']=df['Vak'].str[:2]

#for each vak
#vakk=df[df['new_vak'] == '05']
#vakk['ratio']=(vakk.PastPlagiarism/vakk.TextLength)
#summ=vakk.groupby('new_vak').count()['DocId']
matplotlib.rc('font', family='Arial')
#xlabel(u'Длина работы')
#ylabel(u'Доля заимствования')
#title(u'Физмат')
#plot(vakk.TextLength/2000,  vakk.ratio, '.')
#x= vakk[vakk['ratio']>0.8]
#x[['DocId', 'Authors', 'ratio']].to_csv('C:/Python27/new/high_plag_05.csv', encoding="utf-8-sig" )
open=pd.read_csv('C:/Python27/new/diss-org/open.csv', delimiter=';',encoding="cp1251").convert_objects(convert_numeric=True)
df=df.rename(columns={'DissertationCouncilCode': 'diss'})
mixx=pd.merge(df, open, on=['diss'])
closed=df[~df['diss'].isin(open['diss'])]


#for all vak together
length=closed.groupby(['new_vak']).agg({'TextLength' : 'mean'}).reset_index()
plag=closed.groupby(['new_vak']).agg({'PastPlagiarism' : 'mean'}).reset_index()
df['ratio']=plag['PastPlagiarism']/length['TextLength']
closed['share']=closed['PastPlagiarism']/closed['TextLength']
percent=closed['share'].round(1).as_matrix().reshape(-1)
plt.xticks(np.arange(min(percent), max(percent), 0.1))
plt.hist(percent, bins=9)
#percent.to_csv('C:/Python27/new/histogramm_closed_dis.csv',encoding="cp1251")

#summ_all=df.groupby('percent').agg({'DocId': 'count'}).reset_index()


matplotlib.rc('font', family='Arial')
ylabel(u'Количество работ')
xlabel(u'Доля заимствования')
#plot(length['TextLength']/2000, length['share'], '.')

show()
#length[['share', 'TextLength']].to_csv('C:/Python27/new/47.csv')


#for i, txt in enumerate(length.new_vak):
    #annotate(txt, (length.TextLength[i],plag['PastPlagiarism'][i]/length['TextLength'][i]))
#xscale('log')
#show()

