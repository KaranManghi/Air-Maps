from functools import cache
from math import dist

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
    
    
    def getNeighbors(self, node, min_distance, max_distance):
        neighbors = []
        for n in self.nodes:
            if node != n:
                distance = n.getEuclidianDistance(node)
                if distance > min_distance and distance < max_distance and n.type != 'Restricted':
                    neighbors.append(n)
            
        return neighbors

class Node:
    def __init__(self, i, j, type = None, parent = None):
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

    def __str__(self) -> str:
        return str((self.i, self.j, self.type))
    
    def __hash__(self) -> int:
        return hash(self.i) + hash(self.j)

def navigate(source, des, graph):
    open_set = set()
    closed_set = set()

    open_set.add(source)

    #50, 150, 600
    min_distance = 150
    delta_distance = 50

    while len(open_set) > 0:
        
        max_distance = 600

        # current Node
        current_node = open_set.pop()
        open_set.add(current_node)

        for item in open_set:
            if item.f < current_node.f:
                current_node = item
        
        # Pop current off open list, add to closed list
        open_set.remove(current_node)
        closed_set.add(current_node)

        # Found the goal
        if current_node == des:
            path = []
            current = current_node
            while current is not None:
                path.append(current)
                current = current.parent
            #return getUpdatedPath(path[::-1], des, graph) # Check for Restricted Zone Path
            return path[::-1]
        
        children = []

        while len(children) == 0:
            children = graph.getNeighbors(current_node, min_distance, max_distance)
            if len(children) > 0:
                break
            max_distance += delta_distance
        
        # Loop through children
        for child in children:

            # Child is on the closed list
            if child in closed_set:
                continue
            
            #if child is not on the open list
            if child not in open_set:
                child.g = current_node.g + current_node.getEuclidianDistance(child)
                child.h = child.getEuclidianDistance(des)
                child.f = child.g + child.h
                child.parent = current_node
                open_set.add(child)
            else:
            # Child is already in the open list
                if child.g > current_node.g + current_node.getEuclidianDistance(child):
                    child.g = current_node.g + current_node.getEuclidianDistance(child)
                    child.h = child.getEuclidianDistance(des)
                    child.f = child.g + child.h
                    child.parent = current_node
 

def getUpdatedPath(path, des, graph):
    no_flying_zone = set()

    for node in graph.nodes:
        if node.type == 'Restricted':
            no_flying_zone.add(node)
        
    index = 0

    while index < len(path) - 1:
        cur_node = path[index]
        next_node = path[index + 1]

        if isCrossingRestrictedZone(cur_node, next_node, no_flying_zone):
            print('Inside Restricted Zone!!')
            virtual_node = getVirtualNode(cur_node, next_node, des, no_flying_zone)
            path.insert(index + 1, virtual_node)
        else:
            index += 1    
    return path

def isCrossingRestrictedZone(cur_node, next_node, no_flying_zone):

    path_nodes = getPathNodes(cur_node, next_node)
    for n in path_nodes:
        if n in no_flying_zone:
            return True   
    return False

def getPathNodes(cur_node, next_node):
    points = []
    x1, y1 = cur_node.i, cur_node.j
    x2, y2 = next_node.i, next_node.j
    issteep = abs(y2-y1) > abs(x2-x1)
    if issteep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    rev = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        rev = True
    deltax = x2 - x1
    deltay = abs(y2-y1)
    error = int(deltax / 2)
    y = y1
    ystep = None
    if y1 < y2:
        ystep = 1
    else:
        ystep = -1
    for x in range(x1, x2 + 1):
        if issteep:
            points.append(Node(y, x))
        else:
            points.append(Node(x, y))
        error -= deltay
        if error < 0:
            y += ystep
            error += deltax
    # Reverse the list if the coordinates were reversed
    if rev:
        points.reverse()
    return points


def getVirtualNode(cur_node, next_node, des, no_flying_zone):
    delta = 60
    mid = Node((cur_node.i + next_node.i) // 2, (cur_node.j + next_node.j) // 2)

    best_node = None

    while best_node is None:

        best_distance = float('Infinity')

        left = Node(mid.i - delta, mid.j, 'Virtual', cur_node)
        right = Node(mid.i + delta, mid.j, 'Virtual', cur_node)
        top = Node(mid.i, mid.j + delta, 'Virtual', cur_node )
        bottom = Node(mid.i, mid.j - delta, 'Virtual', cur_node)

        if left.getEuclidianDistance(des) < best_distance and left not in no_flying_zone:
            best_node = left

        if right.getEuclidianDistance(des) < best_distance and right not in no_flying_zone:
            best_node = right

        if top.getEuclidianDistance(des) < best_distance and top not in no_flying_zone:
            best_node = top
        
        if bottom.getEuclidianDistance(des) < best_distance and bottom not in no_flying_zone:
            best_node = bottom
        
        delta += 10

        if best_node is not None:
            return best_node