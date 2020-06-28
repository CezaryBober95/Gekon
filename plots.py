import matplotlib.pyplot as plt
import numpy as np
import csv

#todo: JUST DO IT! for temperature, possition,
#file = open("Raport.txt","r")
#print (file.readline(3))
data =np.genfromtxt('Temp_raport_PLOT_TEST.txxt',delimiter=',')

plt.title("Max and min temperature in the Lizard terrarium")
plt.xlabel("Minutes")
plt.ylabel("Degrees C")
plt.plot(data['time'],data['max'],color='red')
plt.plot(data['time'],data['min'],color='blue')
plt.show()
