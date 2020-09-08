"""This example is for Raspberry Pi (Linux) only!
It will not work on microcontrollers running CircuitPython!"""
import os
import math
import time
import busio
import board
import numpy as np
import pygame
from scipy.interpolate import griddata
from colour import Color
import adafruit_amg88xx
import os.path
import datetime

#x = datetime.datetime.now()
#name = x.strftime("%A->%d-%b-%Y->%H:%M:%S")
# ------------------------------------------------------------------------------------------
'''
def Raport(array, max, min, name, obs):
    # animal_name = "/media/pi/CEZARO/Raport_%(name)s.txt" % {'name': name}
    animal_name = "Raport_%(name)s.txt" % {'name': name}
    if os.path.exists(animal_name) == False:
        raport = open(animal_name, "w")
    start = "\nAMG88xx pixels\n-- Pixels Test --\n\n"
    obs = "Obserwacja: %s" % (obs + 1)
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    hour = "\n\nCzas pomiaru: %s" % current_time
    max_C = "\nMaksymalna temperatura: %s C" % str(max)
    min_C = "\nMinimalna temperatura: %s C\n\n" % str(min)
    raport = open(animal_name, "a")
    raport.write(obs)
    raport.write(start)
    raport.write(str(array))
    raport.write(hour)
    raport.write(max_C)
    raport.write(min_C)
    raport.close()


def temperature_raport(max, min, name):
    # animal_name = "/media/pi/CEZARO/Temp_raport_%(name)s.txt" % {'name': name}
    animal_name = "Temp_raport_%(name)s.txt" % {'name': name}
    if os.path.exists(animal_name) == False:
        raport = open(animal_name, "w")
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    hour = "%s," % str(current_time)
    max_C = "%s," % str(max)
    min_C = "%s\n" % str(min)
    raport_temp = open(animal_name, "a")
    raport_temp.write(hour)
    raport_temp.write(max_C)
    raport_temp.write(min_C)
    raport_temp.close()
'''

# ------------------------------------------------------------------------------------------

i2c_bus = busio.I2C(board.SCL, board.SDA)

MINTEMP = 24
MAXTEMP = 28

COLORDEPTH = 1024
os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()

sensor = adafruit_amg88xx.AMG88XX(i2c_bus)

points = [(math.floor(ix / 8), (ix % 8)) for ix in range(0, 64)]
grid_x, grid_y = np.mgrid[0:7:80j, 0:7:80j]

height = 640
width = 640

# the list of colors we can choose from
blue = Color("white")
colors = list(blue.range_to(Color("black"), COLORDEPTH))

# create the array of colors
colors = [(int(c.red * 255), int(c.green * 255), int(c.blue * 255)) for c in colors]
displayPixelWidth = width / 78
displayPixelHeight = height / 78


lcd = pygame.display.set_mode((width, height))
lcd.fill((255,0 ,0 ))
pygame.display.update()
pygame.mouse.set_visible(False)
lcd.fill((0, 0, 0))
pygame.display.update()

# some utility functions
def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))


def map_value(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


i = 0

# let the sensor initialize
time.sleep(.1)

while True:
    time.sleep(180)
    # read the pixels
    pixels = []
    for row in sensor.pixels:
        pixels = pixels + row
    pixels = [map_value(p, MINTEMP, MAXTEMP, 0, COLORDEPTH - 1) for p in pixels]

    # perform interpolation
    bicubic = griddata(points, pixels, (grid_x, grid_y), method='cubic')

    # draw everything
    for ix, row in enumerate(bicubic):
      for jx, pixel in enumerate(row):
         pygame.draw.rect(lcd, colors[constrain(int(pixel), 0, COLORDEPTH- 1)],
                          (displayPixelHeight * ix, displayPixelWidth * jx,
                           displayPixelHeight, displayPixelWidth))

    # ----------------------------------------------------------------------------------------------------------------------------------------
    i2c = busio.I2C(board.SCL, board.SDA)
        amg=adafruit_amg88xx.AMG88XX(i2c)

    Matrix = []

    for row in sensor.pixels:
        Matrix.append(['{0:.2f}'.format(temp) for temp in row])

    my_array1 = np.asfarray(Matrix, float)
    print(my_array1)
    print("Raport %i" % (i + 1))
    i = i + 1
    print("\n")

    pygame.display.update()
