import numpy as np
import time
#1)todo:class Generator
#2)todo: plots
#3)todo: random gekon position
#4)todo: random value in array exept gekon
#5)todo: make tuple to create more values
#6)todo: do point 5 for few animals
#7)todo: add name to Raport and make tuple to append next arrays and temp ( add min temp too)

animal=np.array([[22.4,22.45,22.54,22.67,22.87,22.45,22.75,22.64],
                 [22.56,22.78,20.49,20.87,21.54,23.48,22.56,22.43],
                 [22.65,22.57,21.65,21.76,20.54,23.40,22.86,22.24],
                 [22.67,22.75,21.54,22.43,21.54,23.56,22.68,22.35],
                 [22.46,22.44,22.65,21.43,21.47,23.38,23.32,22.67],
                 [22.35,20.76,22.34,20.43,20.13,20.78,21.56,22.54],
                 [22.94,20.30,21.40,21.30,20.63,20.95,21.67,22.64],
                 [22.65,22.76,22.65,22.65,22.45,22.46,22.98,22.56]])
#GEKON -> animal[1][5] : animal [4][5]

def coordinate(array):
    cor=np.where(array == array.max())
    array_i, array_j= cor[0], cor[1]
    array_i, array_j=int(array_i), int(array_j)
    #print(array_i,array_j)
    return(array_i,array_j) # tuple
    #array_value=array[array_i][array_j]
    #print(array_value)

def value_check(array,row,col):
    max_temp=(array[row][col])
    return max_temp

def Raport(array,max):
    raport = open("Raport.txt", "w")
    start="AMG88xx pixels\n-- Pixels Test --\n\n"
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    hour="\n\nCzas pomiaru: %s" % current_time
    max_temp="\nMaksymalna temperatura: %s C" % str(max)
    raport.write(start)
    raport.write(str(array))
    raport.write(hour)
    raport.write(max_temp)
    raport.close()

#cor_ij=coordinate(animal)
#Raport(animal,value_check(animal,cor_ij[0],cor_ij[1]))

#score_array= np.round(np.random.uniform(19.0,27.0,(8,8)),2)

for i in range(5):
    score_array = np.round(np.random.uniform(19.0, 27.0, (8, 8)),2)
    cor_ij = coordinate(animal)
    Raport(score_array, value_check(score_array, cor_ij[0], cor_ij[1]))
