from email import header
import sys
from turtle import color, width
sys.path.append('D:\\fhl\Air-Maps\\navigation\AStar.py')
from AStar import Node
from AStar import Graph
from AStar import navigate
import matplotlib.pyplot as plt
import csv

def findPath(source, des, graph):
    path = navigate(source, des, graph)
    return path

def buildGraph(csv_path):
    nodes = []
    with open(csv_path, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        header = True
        for row in reader:
            if header:
                header = False
            else:
                node = Node(int(row[0]), int(row[1]), row[2])
                nodes.append(node)

    return Graph(nodes)

def plotPath(path):
    xcoordinates =[]
    ycoordinates = []

    for node in path:
        xcoordinates.append(node.i)
        ycoordinates.append(node.j)
    
    print(xcoordinates)
    print(ycoordinates)
    plt.plot(xcoordinates, ycoordinates, color='green')
    plt.plot(xcoordinates, ycoordinates, 'o', color='red')

    map = plt.imread('navigation/map.jpg')
    plt.imshow(map)
    plt.show()

def Input():
    x = input("What is X co-ordinate?\n")
    y = input("What is Y co-ordinate?\n")

    return Node(int(x), int(y))

def main():
    csv_path = "data\\full_image_reduced.csv"
    graph = buildGraph(csv_path)

    auburn = Node(3190,3090)
    portAngeles = Node(1690,1660)
    sanDeFuca = Node(2690,1450)
    burley = Node(2670,2900)

    print("Enter the source of the route!")
    #source = Input()
    source = auburn

    print("Enter the destination of the route!")
    #dest = Input()
    dest = portAngeles

    path = findPath(source, dest, graph)

    for node in path:
        print(node)

    plotPath(path)


if __name__ == '__main__':
    main()


#3190,3090,Airport - Auburn

#1690,1660,Airport - Port Angeles

# 2690,1450,Airport - San De Fuca

#2670,2900,Airport - Burley
