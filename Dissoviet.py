# -*- coding: utf-8 -*-
__author__ = 'dberesneva'

import pandas as pd
from pylab import *
matplotlib.rc('font', family='Arial')
import matplotlib.pyplot as plt

node=pd.read_csv('C:/Python27/new/DocVakDateTypeDiss_all.csv', delimiter=',',encoding="utf-8-sig").convert_objects(convert_numeric=True)
dff=node[node['PublicationDate'] < 2016]
df=dff[dff['PublicationDate'] > 1890]

candidate=df[df['Type']=='CandidateThesis']
doctor=df[df['Type']=='DoctorThesis']

candy=candidate.groupby('PublicationDate').agg({'DissertationCouncilCode': lambda x: x.notnull().sum(), 'PublicationDate': 'count'})
candy['x']=candy.DissertationCouncilCode/candy.PublicationDate

doc=doctor.groupby('PublicationDate').agg({'DissertationCouncilCode': lambda x: x.notnull().sum(), 'PublicationDate': 'count'})
doc['x']=doc.DissertationCouncilCode/doc.PublicationDate

#candidat_plot=candy.drop(['PublicationDate', 'DissertationCouncilCode'], axis=1)
doc_plot=doc.drop(['PublicationDate', 'DissertationCouncilCode'], axis=1)
#candidat_plot.plot(legend=None)
doc_plot.plot(color='r', legend=None)

xlabel(u'Год')
#ylabel(u'Доля ненулевых вак')
#title(u'Доля ненулевых вак по годам (докторские)')

plt.show()
#fig, axes = plt.subplots(nrows=1, ncols=2)
