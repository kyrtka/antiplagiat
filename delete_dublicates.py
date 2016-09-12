# -*- coding: utf-8 -*-
__author__ = 'dberesneva'
import pandas as pd



next=pd.read_csv('C:/Python27/new/Edge2.csv', delimiter=';',encoding="utf-8-sig").convert_objects(convert_numeric=True)
#next=next.drop_duplicates(subset=['DocId', 'SourceId'])
#df = inter[inter.groupby('DocId').DocId.transform(len) > 1]
#df= inter[inter['DocId'].isin(inter.loc[inter['DocId'].duplicated(), 'DocId'])]
#next=inter[~inter['DocId'].isin(df['DocId'])] #работы, где источник заимствования только один

node=pd.read_csv('C:/Python27/new/Node.csv', delimiter=';',encoding="cp1251").convert_objects(convert_numeric=True)
mix = pd.merge(next, node, on=['DocId'], how='inner')
mix = mix[['DocId', 'Authors', 'PublicationDate']]
mixx=pd.merge(next, node, on=['SourceId'], how='inner')

mixx=mixx.rename(columns={'Authors':'Authors_source', 'PublicationDate':'PublicationDate_source'})
mix[['SourceId', 'Authors_source', 'PublicationDate_source']]=mixx[['SourceId', 'Authors_source', 'PublicationDate_source']]
mix=mix.drop_duplicates(subset=['DocId', 'SourceId'])

#mix=mix.drop_duplicates(subset=['DocId', 'SourceId'])
#z = mix[mix.Authors==mix.Authors_source]
#print z
#print z[-z.PublicationDate + z.PublicationDate_source <= 1]
#print mix[(mix.Authors == mix.Authors_source)] #& (df.b < df.c)]


list = mix.set_index('Authors').index.get_duplicates()
a= mix[mix['Authors'].isin(list)].reset_index() #работы, где источник заимствования один, и автор источника совпадает с автором работы
final_statuses = a[a.groupby('Authors')['PublicationDate'].diff() <= 1]['Authors']#разница между работой и её источникам не более одного года
final_table = a.loc[a['Authors'].isin(final_statuses)]#итоговая таблица


mix.to_csv('C:/Python27/new/Fake_plagio.csv', delimiter=';',encoding="cp1251")

