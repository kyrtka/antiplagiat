# -*- coding: utf-8 -*-
__author__ = 'dberesneva'

from pylab import *
matplotlib.rc('font', family='Arial')
import pandas as pd

edge=pd.read_csv('C:/Python27/new/Edgecopy.csv', delimiter=';',encoding="utf-8-sig").convert_objects(convert_numeric=True)
opendata=pd.read_csv('C:/Python27/new/Nodecopy.csv', delimiter=';',encoding="utf-8-sig").convert_objects(convert_numeric=True)
dff=opendata[opendata['PublicationDate'] < 2016]
df=dff[dff['PublicationDate'] > 1890]

candidate=df[df['Type']=='CandidateThesis']
candidate_length=candidate.groupby(['PublicationDate']).agg({'TextLength' : 'mean'}).reset_index()
candy=candidate_length.PublicationDate.as_matrix().reshape(-1)

doctor=df[df['Type']=='DoctorThesis']#table for only doctors
doctor_length=doctor.groupby(['PublicationDate']).agg({'TextLength' : 'mean'}).reset_index()
doc=doctor_length.PublicationDate.as_matrix().reshape(-1)

#vak=candidate[candidate['Vak'] == 22]
#vakk=doctor[doctor['Vak'] == 22]
file=candidate_length[['PublicationDate', 'TextLength']]
file['Doctor_length']=doctor_length['TextLength']
file.to_csv('C:/Python27/new/Length-year.csv', encoding="utf-8-sig")

stepsize = 10
fig, ax = plt.subplots()
#ax.bar(vakk.PublicationDate, vakk.TextLength, width=1, color='r')
#ax.bar(vak.PublicationDate, vak.TextLength, width=1)
ax.bar(doctor_length.PublicationDate, doctor_length.TextLength, width=1, color='r')
ax.bar(candidate_length.PublicationDate, candidate_length.TextLength, width=1)
start, end = ax.get_xlim()
ax.xaxis.set_ticks(np.arange(start, end, stepsize))
ax.set_xlabel(u'Год')
ax.set_ylabel(u'Объем работы')
ax.set_title(u'01 - Физико-математические науки')
plt.show()


