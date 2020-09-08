import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

user_cols=['DataTime','Temp max','Temp min']
date1=pd.read_table('Test.txt', sep=',',header=None,names=user_cols)
print(date1.head())

date1['DataTime'] = date1['DataTime'].map(lambda x: datetime.strptime(str(x), '%Y-%m-%d %H:%M:%S'))
x = date1['DataTime']
y = date1['Temp max']
z = date1['Temp min']
m = (date1['Temp max'] + date1 ['Temp min'])/2

plt.plot(x,y,c="red",label="Maximum temperature")
plt.plot(x,z,c="blue",label="Minimum temperature")
plt.plot(x,m,c="pink",label="Average temperature")

plt.gcf().autofmt_xdate()
plt.legend()
plt.show()


