import osmnx as ox
import random
import networkx as nx
import heapq
from dijkstra_algorithm import dijkstra_algorithm
from dijkstra_algorithm import make_route
from dijkstra_algorithm import dijkstra_algorithm_driver
from driver import driver
from test_object import poss_order

def find_node(restaurants, G):
        restaurant_nodes = []
        for i in range(len(restaurants)):
                add = ox.distance.nearest_nodes(G, X=float(restaurants[i][15]), Y=float(restaurants[i][14]))
                restaurant_nodes.append(add)
        return restaurant_nodes

def random_restaurant_locations(rows,num_of_orders):
    lst = []
    restaurants = []
    for i in range(num_of_orders):
        lst.append(random.randint(0, len(rows) - 1))
    for i in lst:
        if (rows[i][14] != "" and rows[i][15] != ""):
            restaurants.append(rows[i])
    return restaurants

def get_random_node(node_list,num):
    random_nodes = []
    for i in range(num):
        j = random.randint(0,len(node_list))
        random_nodes.append(node_list[j])
    return random_nodes

def get_drop_off_points(node_list,num,deliveries):
    points = []
    points = get_random_node(node_list,num)
    for i in range(num):
        deliveries[i].dropoff(points[i])
        
def get_driver_points(N_L,num_of_drivers):
    points = []
    points = get_random_node(N_L,num_of_drivers)
    return points

def find_routes_for_res_to_dropoff(G,list_of_deliveries):
    for i in list_of_deliveries:
        node_path,route_times = dijkstra_algorithm(G, i.restaurant_loc,i.dropoff_loc)
        i.time_to_dropoff(route_times[i.dropoff_loc])
        route = make_route(node_path,i.restaurant_loc,i.dropoff_loc)
        route.reverse()
        i.route_to_dropoff(route)

def find_shortest_driver_dikstra(G,list_of_deliveries,drivers,delivery_set):
    for j in drivers:
        node_path, route_times = dijkstra_algorithm_driver(G,j.init_location,delivery_set)
        for i in list_of_deliveries:
            route = make_route(node_path, j.init_location,i.restaurant_loc)
            route.reverse()
            j.get_routes(route, i.restaurant_loc)
            j.get_times(route_times,i.restaurant_loc)
            j.get_ratio(i)
            i.get_ratio(j)
    #sorts them by age largest to smallest thats why there is a negative
    heap_driver = []
    copy_deliveries = []
    copy_deliveries.extend(list_of_deliveries)
    for i in drivers:
        heapq.heappush(heap_driver,(-(i.age), i))
    for i in drivers:    
        oldest_driver = heapq.heappop(heap_driver)
        max = 0
        for i in copy_deliveries:
            if max < i.reward_ratio[oldest_driver[1].init_location] / oldest_driver[1].times[i.restaurant_loc]:
                max = i.reward_ratio[oldest_driver[1].init_location] / oldest_driver[1].times[i.restaurant_loc]
        for i in copy_deliveries:
            if max == i.reward_ratio[oldest_driver[1].init_location] / oldest_driver[1].times[i.restaurant_loc]:
                i.route_to_restaurant_from_driver(oldest_driver[1].routes[i.restaurant_loc])
                i.time_to_restaurant_from_driver(oldest_driver[1].times[i.restaurant_loc])
                copy_deliveries.remove(i)
                break

def graph_full_routes(deliveries):
    list_of_routes = []
    for i in range(len(deliveries)):
        if deliveries[i].route_to_restaurant_loc != 0:
            list_of_routes.append(deliveries[i].route_to_restaurant_loc)
            list_of_routes.append(deliveries[i].route_to_dropoff_loc)
    return list_of_routes
    
    
def find_shortest_driver_dikstra_rest_heap(G,list_of_deliveries,drivers,delivery_set):
    for j in drivers:
        node_path, route_times = dijkstra_algorithm_driver(G,j.init_location,delivery_set)
        for i in list_of_deliveries:
            route = make_route(node_path, j.init_location,i.restaurant_loc)
            route.reverse()
            j.get_routes(route, i.restaurant_loc)
            j.get_times(route_times,i.restaurant_loc)
            j.get_ratio(i)
            i.get_ratio(j)
    #sorts them by age largest to smallest thats why there is a negative
    copy_deliveries = []
    copy_deliveries.extend(list_of_deliveries)
    heap_driver = []
    heap_deliveries = []
    already_picked = {}
    picked_more_than_once = ()

    # gets highest aged driver 
    for i in drivers:
        heapq.heappush(heap_driver,(-(i.age), i))
    for i in drivers:
        oldest_driver = heapq.heappop(heap_driver)
        #gets the highest reward ratio for said driver clears the heap for the next run
        heap_deliveries = []
        for j in copy_deliveries:
            heapq.heappush(heap_deliveries,(- j.reward_ratio[oldest_driver[1].init_location], j))
        oldest_driver[1].restaurant_heap(heap_deliveries)
    #filling the heap back up
    for i in drivers:
        heapq.heappush(heap_driver,(-(i.age), i))
    for i in drivers:
        oldest_driver = heapq.heappop(heap_driver)
        first = heapq.heappop(oldest_driver[1].restaurants)
        p = poss_order(first[1],oldest_driver[1])
        #just make a list of poss_order objects and iterate through that for unique restaurants 
        if first[1].restaurant_loc not in already_picked and first[1] not in picked_more_than_once:
            already_picked[first[1].restaurant_loc] = (first[1],oldest_driver[1])
        elif first[1].restaurant_loc in already_picked:
            del already_picked[first[1].restaurant_loc]
            picked_more_than_once.append(first[1], oldest_driver[1])
        else:
            picked_more_than_once.append(first[1], oldest_driver[1])

    taken = []
    for i in already_picked:
        already_picked[i].route_to_restaurant_from_driver(i[0].routes[i.restaurant_loc])
        already_picked[i].time_to_restaurant_from_driver(i[0].times[i.restaurant_loc])
        taken.append(already_picked[i])
        already_picked.remove(already_picked[i])
        

        if i[1][1] not in taken:
            i[1][1].route_to_restaurant_from_driver(i[0].routes[i[1][1].restaurant_loc])
            i[1][1].time_to_restaurant_from_driver(i[0].times[i[1][1].restaurant_loc])
            picked_more_than_once.remove(i[1][1])
            taken.append(i[1][1])
        if i[1][1] in taken:
            b = True
            while b:
                next = heapq.heappop(i[0].restaurants)
                if next not in taken:
                    i[1][1].route_to_restaurant_from_driver(i[0].routes[i[1][1].restaurant_loc])
                    i[1][1].time_to_restaurant_from_driver(i[0].times[i[1][1].restaurant_loc])
                    picked_more_than_once.remove(i[1][1])
                    taken.append(i[1][1])
                    b = False