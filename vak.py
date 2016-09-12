# -*- coding: utf-8 -*-
__author__ = 'dberesneva'

import pandas as pd
from pylab import *
matplotlib.rc('font', family='Arial')
node=pd.read_csv('C:/Python27/vakAndData.csv', delimiter=';',encoding="utf-8-sig").convert_objects(convert_numeric=True)
dff=node[node['PublicationDate'] < 2016]
df=dff[dff['PublicationDate'] > 1890]

candidate=df[df['Type']=='CandidateThesis'] #table for only candidates
doctor=df[df['Type']=='DoctorThesis']#table for only doctors

vak=candidate[candidate['vak'] == 22]
vakk=doctor[doctor['vak'] == 22]
candy=vak.PublicationDate.as_matrix().reshape(-1)
doc=vakk.PublicationDate.as_matrix().reshape(-1)

stepsize = 5
fig, ax = plt.subplots()
plt.hist(candy, bins=max(candy) - 1970, range=(1970, max(candy)), stacked=True)
plt.hist(doc, bins=max(doc) - 1970, range=(1970, max(doc)), stacked=True, color='r')
start, end = ax.get_xlim()
ax.set_xlabel(u'Год')
ax.set_ylabel(u'Количество работ')
ax.set_title(u'22.00.00 - Социологические науки')
ax.xaxis.set_ticks(np.arange(start, end, stepsize))
plt.show()
