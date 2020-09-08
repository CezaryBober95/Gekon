import re
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import seaborn as sns
'''with open("Raport_Friday-21-Aug-2020-221715.txt") as myfile:
    file = open("dane.txt", "w+")
    for line in myfile.readlines():
        if line.strip().startswith('['):
            matrix = re.sub("[,\[\]]", " ", line).strip()
            matrix = re.sub(" +", " ", matrix)
            print(matrix)
            file.write(matrix)'''

with open("macierze.txt") as myfile:
    lines_in_file = myfile.readlines()
    number_of_lines = int(len(lines_in_file)/9)
    myfile.close()
    print(number_of_lines)

skip = 0
'''
for i in range(number_of_lines):
    matrix = np.loadtxt("macierze.txt", usecols=range(8), max_rows=8, skiprows=skip)
    skip += 9
    print(matrix)
    is_empty = matrix.size == 0
    if (is_empty):
        break'''

matrix = np.loadtxt("macierze.txt", usecols=range(8))
array_1d = matrix.flatten()
dane = pd.DataFrame(data={'data': array_1d})
s = pd.Series(range(1, 9))
dane['column'] = s.append([s]*4226, ignore_index=True)
z = pd.Series(np.repeat((np.arange(1, 9)), 8))
dane['row'] = z.append([z]*4226, ignore_index=True)
w = pd.Series(np.repeat((np.arange(1, 452)), 64))
dane['obiekt'] = w.append([w]*4226, ignore_index=True)
print(dane)

# Transform it to a long format
df=dane

# Make the plot
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_trisurf(df['row'], df['column'], df['data'], cmap=plt.cm.viridis, linewidth=0.2)
plt.show()

# to Add a color bar which maps values to colors.
surf = ax.plot_trisurf(df['row'], df['column'], df['data'], cmap=plt.cm.viridis, linewidth=0.2)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()

# Rotate it
ax.view_init(30, 45)
plt.show()

# Other palette
ax.plot_trisurf(df['row'], df['column'], df['data'], cmap=plt.cm.jet, linewidth=0.01)
plt.show()