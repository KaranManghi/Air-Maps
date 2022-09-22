from functools import cache
from haversine import haversine, Unit

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
    
    @cache
    def getNeighbors(self, node, min_distance, max_distance):
        neighbors = []
        for n in self.nodes:
            if node != n:
                distance = n.getNauticalMiles(node)
                if distance > min_distance and distance < max_distance:
                    neighbors.append(n)
            
        return n

class Node:
    def __init__(self, lat, long, type, parent = None):
        self.lat = lat
        self.long = long
        self.type = type

        self.parent = parent

        self.g = 0
        self.h = 0
        self.f = 0

    def getNauticalMiles(self, node):
        source = (self.lat, self.long)
        dest = (node.lat, node.long)
        return haversine(source, dest, unit=Unit.NAUTICAL_MILES)
    
    def __eq__(self, node):
        return self.lat == node.lat and self.long == node.long
    

def navigate(source, des, graph):
    open_list = []
    closed_list = []

    open_list.append(source)

    min_distance = 5
    max_distance = 20
    delta_distance = 5

    while len(open_list) > 0:
        
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
                path.append((current.lat, current.long))
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
            for closed_child in closed_list:
                if child == closed_child:
                    continue
            
            # Create the f, g, and h values
            child.g = current_node.g + current_node.getNauticalMiles(child)
            child.h = child.getNauticalMiles(des)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)
            child.parent = current_node

 