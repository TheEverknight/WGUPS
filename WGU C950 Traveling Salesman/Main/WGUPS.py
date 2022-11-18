# Joshua Ian Vaughn
# Data Structures and Algorithms II - C950
# 2-10-21

from ReadFiles import *
from DijkstrasAlgorithm import *



class WGUPS:
    def __init__(self):
        # trucks load are determine based project constraints. Each truck can hold up 16 units
        # Truck 1 has packages 13, 15, and 19 that can only be shipped together.
        # Truck 2 has packages that arrive at 9:05, and packages that can only be delivered by Truck 2
        # Truck 3 has the remaining packages with no constraints.
        self.truck1_load = [4, 11, 13, 14, 15, 16, 19, 20, 21, 23, 24, 34, 35, 39, 40]
        self.truck2_load = [3, 5, 6, 12, 17, 18, 28, 30, 31, 32, 36, 37, 38]
        self.truck3_load = [1, 2, 7, 8, 9, 10, 22, 25, 26, 27, 29, 33]
        self.total_distance = 0
        self.list_statuses = []
        self.delivered = []

    # method that delivers the packages.

    # 0(N^3)
    def delivery(self, truck, time):
        undelivered = []
        #set starting node
        start_node = (None, '4001 South 700 East')
        _smallest = None
        cost = 0
        _package = None

        # Loads trucks
        if truck.truck_id == 1:
            for i in self.truck1_load:
                truck.GetPackage(i)
        if truck.truck_id == 2:
            for i in self.truck2_load:
                truck.GetPackage(i)
        if truck.truck_id == 3:
            for i in self.truck3_load:
                truck.GetPackage(i)


        # Truck packages are appended.
        for i in truck.package_list.table:
            for j in i:
                undelivered.append((j, j.address))
        undelivered.append(start_node)

        # While the list is not empty
        while len(undelivered) != 0:
            # removes the new starting_node
            undelivered.remove(start_node)

            # Creates a new graph after each run through.
            graph = data.GetNodeGraph(Graph())

            # finds and returns  a node with a matching package address
            current = data.find_node(start_node[1])

            #  Shortest path's algorithm takes on a new graph and node.
            algorithm = Algorithm(graph, current)

            for i in undelivered:
                # Each run through, the package address is ran through shortest_path. Loops until a smallest is determined
                a = algorithm.Calculate(data.find_node(i[1]))

                # if smallest has not been determined, assign the first node as smallest along with its package
                # this is the first step after a package delivery.
                if _smallest is None:
                    _smallest = a
                    cost = _smallest.min_distance
                    _package = i[0]

                # if the new node is less than the smallest, new node becomes smallest and along with its package
                elif a.min_distance < _smallest.min_distance and a.address != _smallest.address:
                    _smallest = a
                    cost = _smallest.min_distance
                    _package = i[0]


                # this statement takes into affect whenever the user inputs a time that is appropriate to activate the
                # change in address. When the constraints are met, the current node will deleted from undelivered,
                # package will be modified, and the new address and package will be added to the list for later use.
                elif i[0].package_id == 9 and a.address == '300 State St' and i[0].to_minutes(time) >= 620:
                    print('ADDRESS CORRECTION @ 10:20am FOR PACKAGE', i[0].package_id, 'TO', a.address)
                    undelivered.remove((i[0], a.address))
                    _package = i[0]
                    _package.address = '410 S State St'
                    _smallest = data.find_node('410 S State St')
                    print('To new address ', _smallest.address)
                    undelivered.append((_package, _smallest.address))

            # Once all packages are delivered, the shortest distance to the hub from the last node will be found.
            # Final mileage for each truck will be added to the total.
            if len(undelivered) == 0:

                hub = algorithm.Calculate(data.find_node('4001 South 700 East'))
                truck.total_cost += hub.min_distance
                print(truck.truck_id,'returns to the hub with total distance travel', truck.total_cost)
                self.total_distance += truck.total_cost
                return

            # Once a smallest is founds. Adds distance traveled to the total, sets the timestamp to the package, marks it
            # as delivered, adds the package to delivered list, assigned the new start_node, and sets smallest as none.
            truck.total_cost += cost

            truck.SetTime(truck.total_cost)

            _package.SetTime(truck.total_cost)

            self.delivered.append(_package)

            _package.Deliver()

            start_node = (_package, _smallest.address)
            _smallest = None

# initiats WGU for later use
WGU = WGUPS()
