import matplotlib.pyplot as plt
# import matplotlib.pyplot.figure as figure
import numpy as np
import os

coordinates = [(0, 0), (1000, 1000), (1000, 2000), (2000, 3000), (3000, 4000), (3000, 5000)]
xcoordinates =[]
ycoordinates = []


for coord in coordinates:
    xcoordinates.append(coord[0])
    ycoordinates.append(coord[1])

print(os.listdir())
mapplot = plt.plot(xcoordinates,ycoordinates)
map = plt.imread('map.jpg')
plt.imshow(map)
plt.show()




