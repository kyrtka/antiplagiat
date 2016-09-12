
__author__ = 'dberesneva'

import pandas as pd
from pylab import *

intersection=pd.read_csv('C:/Python27/FinalInt.csv', delimiter=';',encoding="utf-8-sig").convert_objects(convert_numeric=True)
p=pd.read_csv('C:/Python27/NewIntersection.csv', delimiter=';',encoding="utf-8-sig").convert_objects(convert_numeric=True)
intersection['Size']=p.Size

#intersection=intersection[intersection.Shift>1000]

intersection=intersection[intersection.Size>30]
intersection['cut']=intersection['Shift']/intersection['TextLength']*100
intersection.cut = intersection.cut.round()
amount= intersection.groupby(['cut']).count()['TextLength']

int=intersection[intersection.Size>100]
int['cut']=int['Shift']/int['TextLength']*100
int.cut = int.cut.round()
am=int.groupby(['cut']).count()['TextLength']

inn=intersection[intersection.Size>200]
inn['cut']=inn['Shift']/inn['TextLength']*100
inn.cut = inn.cut.round()
a=inn.groupby(['cut']).count()['TextLength']

def smooth(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth

matplotlib.rc('font', family='Arial')
plot(smooth(amount,9), 'r-', lw=2, label='30')
plot(smooth(am,9), 'b-', lw=2, label='100')
plot(smooth(a,9), 'g-', lw=2, label='200')
#title(u'Размер и позиция блоков')
#xlabel(u'Позиция в документе')
#ylabel(u'Количество фрагментов')
legend()
show()


