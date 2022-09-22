import sys
sys.path.append('C:\Air-Maps\navigation\AStar.py')
from AStar import Node
from AStar import Graph
from AStar import navigate


node1 = Node(0,0,'airport', None)
node2 = Node(0,1,'airport', None)
node3 = Node(0,2,'nofly', None)
node4 = Node(0,3,'airport', None)
node5 = Node(1,0,'airport', None)
node6 = Node(1,1,'nofly', None)
node7 = Node(1,2,'airport', None)
node8 = Node(1,3,'airport', None)
node9 = Node(2,0,'lake', None)
node10 = Node(2,1,'lake', None)
node11 = Node(2,2,'airport', None)
node12 = Node(2,3,'airport', None)
node13 = Node(3,1,'lake', None)
node14 = Node(3,2,'airport', None)
node15 = Node(3,3,'airport', None)
node16 = Node(3,4,'city', None)
node17 = Node(3,5,'airport', None)
nodes = node1, node2, node3, node4, node5, node6, node7, node8, node9, node10, node11, node12, node13, node14, node15, node16, node17
graph = Graph(nodes)


print(navigate(node1, node17, graph))


