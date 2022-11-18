import csv
from Graph import *
from hashTable import *

PackageData = 'Assets/CSV_Files/_WGUPSPackageFile.csv'
DistanceData = 'Assets/CSV_Files/_WGUPSDistanceTable.csv'
AddressData = 'Assets/CSV_Files/_WGUPSAddressTable.csv'

PackageTable = HashTable()
DistanceTable = [[]]


class Data(object):
    def __init__(self):
        self._graph = Graph()

    # Gather all all rows from the CSV file
    # 0(N)
    def ReadData(self, file):
        csv_data = []
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            # next(csv_reader, None)
            for row in csv_reader:
                csv_data.append(row)
        return csv_data

    # Uses to DistanceTable.csv file to add edges to edges list for easier retrieval when adding edge weights
    # 0(N^2)
    def GetNodeGraph(self, graph):
        edges = []
        global node
        global node2
        data = self.ReadData(DistanceData)
        for row in data:
            graph.AddNode(Node(row[1]))
        for row in data:
            for i in range(3, len(row)):  # Starts at 3. Only need distances
                if row[i] != '':
                    edges.append((row[1], data[i - 3][1],
                                  float(row[i - 1])))  # data[i-3][1] gets each connected street vertex
        # Without creating new Node objects, edges list was used to compare nodes from the adjacency list, add the compared
        # nodes to the add_edge() and add their appropriate weight.Returns graph for later use.
        for j in edges:
            for i in graph.adjacency:
                if i.address == j[0]:
                    node = i
                if i.address == j[1]:
                    node2 = i
            graph.AddEdge(node, node2, j[2])
            graph.AddEdge(node2, node, j[2])

        self._graph = graph
        return graph

    # Help finding a node that belong to the adjacency list as to avoid creating new Node objects.
    # 0(N)
    def find_node(self, address):
        for i in self._graph.adjacency:
            if i.address == address:
                return i


# creates object for later use
data = Data()
