# libraries
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde
import os

script_path = os.path.abspath(__file__)
script_dir = os.path.split(script_path)[0]
rel_path = ".images"
script_dir = script_dir.replace('\\', '/')
path = os.path.join(script_dir, rel_path)
dir = path.replace('\\', '/')
print(dir)

with open("macierze.txt") as myfile:
    lines_in_file = myfile.readlines()
    number_of_lines = len(lines_in_file)
    myfile.close()
skip = 0

for i in range(number_of_lines):
    file = "macierze.txt"
    matrix = np.loadtxt(file, usecols=range(8), max_rows=8, skiprows=skip)
    print(matrix)
    n = len([file for file in os.listdir(dir) if os.path.isfile(os.path.join(dir, file))])
    x = n + 1
    title = "{0}{1}".format('obserwacja', x)
    name = "{0}{1}".format('obserwacja', x)
    plt.contourf(matrix, 30)
    plt.title(title)
    plt.colorbar()
    plt.savefig(fname="{0}{1}.png".format('.images/obserwacja', x))
    plt.clf()
    plt.close()
    skip += 9





