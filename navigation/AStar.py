from functools import cache
from math import dist

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
    
    @cache
    def getNeighbors(self, node, min_distance, max_distance):
        neighbors = []
        for n in self.nodes:
            if node != n:
                distance = n.getEuclidianDistance(node)
                if distance > min_distance and distance < max_distance:
                    neighbors.append(n)
            
        return n

class Node:
    def __init__(self, i, j, type, parent = None):
        self.i = i
        self.j = j
        self.type = type

        self.parent = parent

        self.g = 0
        self.h = 0
        self.f = 0

    def getEuclidianDistance(self, node):
        source = (self.i, self.j)
        dest = (node.i, node.j)
        return dist(source, dest)
    
    def __eq__(self, node):
        return self.i == node.i and self.j == node.j
    

def navigate(source, des, graph):
    open_list = []
    closed_list = []

    open_list.append(source)

    min_distance = 5
    delta_distance = 5

    while len(open_list) > 0:
        
        max_distance = 20

        # current Node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index
        
        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == des:
            path = []
            current = current_node
            while current is not None:
                path.append((current.i, current.j))
                current = current.parent
            return path[::-1] # Return reversed path
        

        children = []

        while len(children) == 0:
            children = graph.getNeighbors(current_node, min_distance, max_distance)
            if len(children) > 0:
                break
            max_distance += delta_distance
        
        # Loop through children
        for child in children:

            # Child is on the closed list
            if child in closed_list:
                continue
            
            #if child is not on the open list
            if child not in open_list:
                child.g = current_node.g + current_node.getEuclidianDistance(child)
                child.h = child.getEuclidianDistance(des)
                child.f = child.g + child.h
                child.parent = current_node
                open_list.append(child)
            else:
            # Child is already in the open list
                if child.g > current_node.g + current_node.getEuclidianDistance(child):
                    child.g = current_node.g + current_node.getEuclidianDistance(child)
                    child.h = child.getEuclidianDistance(des)
                    child.f = child.g + child.h
                    child.parent = current_node
 