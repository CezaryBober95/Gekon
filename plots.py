import matplotlib.pyplot as plt
#import numpy as np
import pandas as pd
from datetime import datetime
#from tkinter import filedialog
#from tkinter import messagebox

'''def baseopen(): #To chyba dzia³a
    db=filedialog.askopenfilename(initialdir = "D:\Studia\Magisterka\Semestr_1\Projekty_1\IBD",
                                  title = "Wybierz baze danych",
                                  filetypes = (("Bazy danych","*.db"),("all files","*.*")))
'''
#todo: JUST DO IT! for temperature, possition,
user_cols=['DataTime','Temp max','Temp min']
# change file in date1 to get new plot
#'Temp_raport_Dino.txt' -> 'Temp_raport_Denver'
#file_me='Temp_raport_Test14.txt'
#file_me=input("File name: ")
date1=pd.read_table('Temp_raport_Test14.txt', sep=',',header=None,names=user_cols)
#date1=pd.read_table(file_me, sep=',',header=None,names=user_cols)
print(date1.head())
print("Wczytane")

date1['DataTime'] = date1['DataTime'].map(lambda x: datetime.strptime(str(x), '%Y-%m-%d %H:%M:%S'))
x = date1['DataTime']
y = date1['Temp max']
z = date1['Temp min']

plt.plot(x,y,c="red")
plt.plot(x,z,c="blue")
plt.gcf().autofmt_xdate()
plt.show()