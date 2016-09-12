# -*- coding: utf-8 -*-
__author__ = 'dberesneva'

import pandas as pd
import numpy as np
from pylab import *
#import matplotlib.pyplot as plt
matplotlib.rc('font', family='Arial')


#encoding="utf-8-sig"
#opendata=pd.read_csv('C:/Python27/new/DocVakDateTypeDiss_all.csv', delimiter=',',encoding="utf-8-sig").convert_objects(convert_numeric=True)
opendata=pd.read_csv('C:/Python27/new/Nodecopy.csv', delimiter=';',encoding="utf-8-sig")#.convert_objects(convert_numeric=True)
opendata['new_vak'] = opendata['Vak'].str[:2]

dff=opendata[opendata['PublicationDate'] < 2016] #all papers before 2016
df=dff[dff['PublicationDate'] > 1890]#all papers after 1890



candidate=df[df['Type']=='CandidateThesis'] #table for only for candidates
candidate_data=candidate[['PublicationDate']].as_matrix().reshape(-1)

doctor=df[df['Type']=='DoctorThesis']#table for only doctors
doctor_data=doctor[['PublicationDate']].as_matrix().reshape(-1)

can=candidate.groupby(['PublicationDate']).agg({'DocId':'count'}).reset_index()
doc=doctor.groupby(['PublicationDate']).agg({'DocId':'count'}).reset_index()
can.rename(columns={'DocId':'Candidate'}, inplace=True)
doc.rename(columns={'DocId':'Doctor'}, inplace=True)
doc['candidat']=can['Candidate']
#doc.to_csv('C:/Python27/new/Amount_of_papers.csv')

#vak=candidate[candidate['new_vak'] == '25']
#vakk=doctor[doctor['new_vak'] == '25']

#candy=vak[['PublicationDate']].as_matrix().reshape(-1)
#doc=vakk[['PublicationDate']].as_matrix().reshape(-1)


stepsize = 5
fig, ax = plt.subplots()
#plt.hist(candidate_data, bins=46, range=(1970, max(candidate_data)), stacked=True)
#plt.hist(doctor_data, bins=46, range=(1970, max(doctor_data)), stacked=True, color='r')
ax.bar(doc['candidat'], doc['PublicationDate'], width=1, color='r')
ax.bar(doc['Doctor'], doc['PublicationDate'], width=1)
start, end = ax.get_xlim()

ax.set_xlabel(u'Год')
ax.set_ylabel(u'Количество работ')
ax.xaxis.set_ticks(np.arange(start, end, stepsize))
plt.show()
