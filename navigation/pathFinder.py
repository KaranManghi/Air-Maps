from email import header
import sys
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
    nodes = tuple()
    with open(csv_path, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            node = Node(row[0], row[1], row[2])
            nodes.append(node)

    return Graph(nodes)

def plotPath(path):
    xcoordinates =[]
    ycoordinates = []

    for node in path:
        xcoordinates.append(node.x)
        ycoordinates.append(node.y)
    
    plt.plot(xcoordinates, ycoordinates)
    map = plt.imread('navigation/map.jpg')
    plt.imshow(map)
    plt.show()

def Input():
    x = input("What is X co-ordinate?")
    y = input("What is Y co-ordinate?")

    return Node(int(x), int(y))

def main():
    csv_path = ""
    graph = buildGraph(csv_path)

    print("Enter the source of the route!")
    source = Input()

    print("Enter the destination of the route!")
    dest = Input()

    path = findPath(source, dest, graph)

    plotPath(path)

if __name__ == 'main':
    main()