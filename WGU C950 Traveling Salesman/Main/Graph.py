import sys

# Node class for each address.
# 0(N)
class Node(object):

    def __init__(self, address):
        self.address = address
        self.visited = False
        self.predecessor = None
        self.min_distance = sys.maxsize

    def __cmp__(self, other):
        return self.cmp(self.min_distance, other.min_distance)

    def __lt__(self, other):
        self_priority = self.min_distance
        other_priority = other.min_distance
        return self_priority < other_priority

# Graph to be used during shortest path algorithm. Adds node into the graph and creating adjacency_list for each node. Also
# created undirected edges. get_weight() used for later retrieval for edge weight.
# 0(N)

class Graph(object):
    def __init__(self):
        self._weight = {}
        self.reverse = {}
        self.adjacency = {}

    def AddNode(self, node):
        if node not in self.adjacency:
            self.adjacency[node] = []

    def AddEdge(self, start_node, target_node, weight):
        if weight != '':
            self._weight[start_node, target_node] = weight
            self._weight[(target_node, start_node)] = weight
            self.adjacency[start_node].append(target_node)


    def GetWeight(self, StartNode, EndNode):
            if self._weight[StartNode, EndNode]:
                weight = self._weight[StartNode, EndNode]
                return weight
            elif self._weight[EndNode, StartNode]:
                weight = self._weight[EndNode, StartNode]
                return weight