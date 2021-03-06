import numpy as np
import time
import os.path
import Generator_GUI

#3)todo: random gekon position
#6)todo: change variable name,observation to read from GUI class Generator

'''animal=np.array([[22.4,22.45,22.54,22.67,22.87,22.45,22.75,22.64],
                 [22.56,22.78,20.49,20.87,21.54,23.48,22.56,22.43],
                 [22.65,22.57,21.65,21.76,20.54,23.40,22.86,22.24],
                 [22.67,22.75,21.54,22.43,21.54,23.56,22.68,22.35],
                 [22.46,22.44,22.65,21.43,21.47,23.38,23.32,22.67],
                 [22.35,20.76,22.34,20.43,20.13,20.78,21.56,22.54],
                 [22.94,20.30,21.40,21.30,20.63,20.95,21.67,22.64],
                 [22.65,22.76,22.65,22.65,22.45,22.46,22.98,22.56]])
#GEKON -> animal[1][5] : animal [4][5]
'''
class Generator:

    def coordinate_max(self,array):
        cor=np.where(array == array.max())
        array_i, array_j= cor[0], cor[1]
        array_i, array_j=int(array_i), int(array_j)
        return(array_i,array_j) # tuple

    def coordinate_min(self,array):
        cor=np.where(array == array.min())
        array_i, array_j= cor[0], cor[1]
        array_i, array_j=int(array_i), int(array_j)
        return(array_i,array_j) # tuple

    def value_check(self,array,row,col):
        max_temp=(array[row][col])
        return max_temp

    def Raport(self,array,max, min,name,obs):
        animal_name = "Raport_%(name)s.txt" % {'name': name}
        if os.path.exists(animal_name) == False:
            raport = open(animal_name, "w")
        start = "\nAMG88xx pixels\n-- Pixels Test --\n\n"
        obs="Obserwacja: %s" % (obs+1)
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        hour = "\n\nCzas pomiaru: %s" % current_time
        max_C = "\nMaksymalna temperatura: %s C" % str(max)
        min_C = "\nMinimalna temperatura: %s C\n\n" % str(min)
        raport=open(animal_name,"a")
        raport.write(obs)
        raport.write(start)
        raport.write(str(array))
        raport.write(hour)
        raport.write(max_C)
        raport.write(min_C)
        raport.close()

    def temperature_raport(self,max,min,name,obs):
        animal_name = "Temp_raport_%(name)s.txt" % {'name': name}
        if os.path.exists(animal_name) == False:
            raport = open(animal_name, "w")
        obs = "Obserwacja: %s -> " % (obs+1)
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        hour = "%s," % str(current_time)
        max_C = "%s," % str(max)
        min_C = "%s\n" % str(min)
        raport_temp = open(animal_name, "a")
        raport_temp.write(obs)
        raport_temp.write(hour)
        raport_temp.write(max_C)
        raport_temp.write(min_C)
        raport_temp.close()

    def repeat(self,observations):
        for i in range(observations): # 192
            try:
                score_array = np.round(np.random.uniform(19.0, 27.0, (8, 8)),2)
                cor_ij_max = self.coordinate_max(score_array)
                cor_ij_min = self.coordinate_min(score_array)
                self.Raport(score_array, self.value_check(score_array, cor_ij_max[0], cor_ij_max[1]), self.value_check(score_array, cor_ij_min[0], cor_ij_min[1]),name,i)
                self.temperature_raport(self.value_check(score_array, cor_ij_max[0], cor_ij_max[1]), self.value_check(score_array, cor_ij_min[0], cor_ij_min[1]),name,i)
                time.sleep(1)
                print ("Raport %i" % (i))
            except:
                print("Array Error")
                continue
        print("finish")

#Variables-------------------------------------------------------------------------------
name= "PLOT_TEST"
#192
#observations=5
#name=input("Podaj nazwę osobnika: ")
#observations=int(input("Podaj liczbę obserwacji:"))
#=======================================================================================
#gen = Generator()
#gen.repeat(observations)
