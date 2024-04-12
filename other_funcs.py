import osmnx as ox
import random
import networkx as nx
from dijkstra_algorithm import dijkstra_algorithm
from dijkstra_algorithm import make_route
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

def find_shortest_driver_non_dikstra(G,deliveries,drivers):
    poss_routes = []
    poss_times = []
    remaining_deliveries = len(deliveries)
    # need these to get the correct size of the 2d arrays
    for i in range(len(deliveries)):
        col = []
        for j in range(len(drivers)):
            col.append(0)
        poss_routes.append(col)

    for i in range(len(deliveries)):
        col = []
        for j in range(len(drivers)):
            col.append(0)
        poss_times.append(col)
    #fills the arrays with the routes and time it takes on those paths
    for i in range(len(deliveries)):
        for j in range(len(drivers)):
            poss_routes[i][j] = ox.shortest_path(G, drivers[j],deliveries[i].restaurant_loc, weight="travel_time")
            poss_times[i][j] = nx.shortest_path_length(G, drivers[j],deliveries[i].restaurant_loc, weight="travel_time")
    min = 100000000000
    skip_i = []
    skip_j = []
    delivery_min = 0
    driver_min = 0
    #finds the shortest routes for the drivers to restaurants
    while (remaining_deliveries > 0):
        #checks every spot on the 2d array
        min = 100000000000
        delivery_min = 0
        driver_min = 0
        for i in range(len(deliveries)):
            for j in range(len(drivers)):
                #makes sure the delivery or driver is not already taken this is an attempt at a time saving measure
                if i not in skip_i and j not in skip_j:
                    # checks if the current time is less than or equal to min if so makes min the new time
                    if poss_times[i][j] <= min:
                        min = poss_times[i][j]
                        # these are needed to at the end of checking the min it will make the skip_j and skip_i have the now taken delivery and driver
                        delivery_min = i
                        driver_min = j
                
        #adds the coordinates to the list to skip for later iterations        
        skip_i.append(delivery_min)
        skip_j.append(driver_min)
        
        #stores the lowest available delivery times along with the routes and driver starting location
        deliveries[delivery_min].driver_location(drivers[driver_min])
        deliveries[delivery_min].route_to_restaurant_from_driver(poss_routes[delivery_min][driver_min])
        deliveries[delivery_min].time_to_restaurant_from_driver(poss_times[delivery_min][driver_min])

        #decrements remaining_deliveries to stop the while loop
        remaining_deliveries = remaining_deliveries - 1


def graph_full_routes(deliveries):
    list_of_routes = []
    for i in range(len(deliveries)):
        list_of_routes.append(deliveries[i].route_to_restaurant_loc)
        list_of_routes.append(deliveries[i].route_to_dropoff_loc)
    return list_of_routes
    