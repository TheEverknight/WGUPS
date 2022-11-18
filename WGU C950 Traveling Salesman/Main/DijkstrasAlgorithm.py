import heapq


# Algorithm to determine the shortest path.

# function takes the graph and the starting node. Sets the starting node to 0 distance, and predecessor to none.
# node has a min distance of MAX. 0 distance for the starting will determine each edge weight to its adjacent nodes.
# Ultimately this will function as Dijkstras Algorithm for shortest pathing

# 0(N^2)
class Algorithm(object):

    def __init__(self, graph, start_node):

        start_node.min_distance = 0
        start_node.predecessor = None
        unvisited = [i for i in graph.adjacency]
        # uses heapify to set the lowest as priority
        heapq.heapify(unvisited)
        # Function will continue to run until empty
        while len(unvisited):

            # Pops the smallest node and makes it the current node
            current = heapq.heappop(unvisited)
            current.visited = True

            # Searches through the current nodes list, making 'target' the adjacent node
            for target in graph.adjacency[current]:
                # while the adjacent node is has not been visited
                if target.visited == True:
                    continue
                weight = graph.GetWeight(current, target)
                # create edge weight with an adjacent node
                new_distance = current.min_distance + float(weight)

                # if new_distance is less than the adjacent node minimum distance, it assigns new_distance weight
                # to the adjance node's minimum_distance. Then sets the current node as predecessor.
                if new_distance < target.min_distance:
                    target.min_distance = new_distance
                    target.predecessor = current

            # Pops nodes
            while len(unvisited):
                heapq.heappop(unvisited)
            # new unvisited_list leaving out nodes marked visited.
            unvisited = [i for i in graph.adjacency if i.visited == False]
            heapq.heapify(unvisited)

    # function to find the calculate a semi-optimal route to a node.

    def Calculate(self, target_node):
        node = target_node
        while node is not None:
            node = node.predecessor
        return target_node
