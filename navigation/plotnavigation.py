import matplotlib.pyplot as plt
# import matplotlib.pyplot.figure as figure
import numpy as np

coordinates = [(0, 0), (1, 1), (1, 2), (2, 3), (3, 4), (3, 5)]
xcoordinates =[]
ycoordinates = []


for coord in coordinates:
    xcoordinates.append(coord[0])
    ycoordinates.append(coord[1])


mapplot = plt.plot(xcoordinates,ycoordinates)
# map = plt.imread('map.jpg')
# mapplot.figure.figimage(map, 40, 40, alpha=.15, zorder=1)
plt.show()




