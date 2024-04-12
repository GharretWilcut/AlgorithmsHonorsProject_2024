import sys
from minheap import MinHeap
import heapq

def make_route(prev_nodes,start_node,end_node):
    found = False
    route = []
    route.append(int(end_node))
    previous_node = int(prev_nodes[end_node])
    while not found:
        if previous_node == start_node:
            route.append(int(previous_node))
            found = True
        else:
            route.append(int(previous_node))
            previous_node = prev_nodes[previous_node]
    return route

def dijkstra_algorithm(graph, initial,end):
    visited = {initial: 0}
    h = [(0, initial)]
    path = {}

    nodes = list(graph.nodes)[None:None:None]

    while nodes and h:
        current_weight, min_node = heapq.heappop(h)
        try:
            while min_node not in nodes:
                current_weight, min_node = heapq.heappop(h)
        except IndexError:
            break

        nodes.remove(min_node)

        for v in graph.edges(min_node):
            i = v[1]
            weight = current_weight + graph.get_edge_data(min_node, i)[0]['travel_time']
            if i not in visited or weight < visited[i]:
                visited[i] = weight
                heapq.heappush(h, (weight, i))
                path[i] = min_node
                if (min_node == end):
                    return path , visited

    return path, visited