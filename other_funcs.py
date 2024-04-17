import osmnx as ox
import random
import networkx as nx
from dijkstra_algorithm import dijkstra_algorithm
from dijkstra_algorithm import make_route
from dijkstra_algorithm import dijkstra_algorithm_driver
from driver import driver

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
            print(i.restaurant_loc)
            route = make_route(node_path, j.init_location,i.restaurant_loc)
            route.reverse()
            j.get_routes(route, i.restaurant_loc)
            j.get_times(route_times,i.restaurant_loc)
            j.get_ratio(i)


    


def graph_full_routes(deliveries):
    list_of_routes = []
    for i in range(len(deliveries)):
        list_of_routes.append(deliveries[i].route_to_restaurant_loc)
        list_of_routes.append(deliveries[i].route_to_dropoff_loc)
    return list_of_routes
    
    
    
    