import other_funcs
import random
class driver:
    def __init__(self,N_L):
        self.age = random.randint(0,10000)
        self.get_location(N_L)
        self.routes ={}
        self.times = {}
        self.reward_ratios = {}
        self.restaurants = []
    def get_location(self,N_L):
        g = random.randint(0,len(N_L))
        self.init_location = N_L[g]
    
    def get_routes(self,route,restaurant_loc):
        self.routes[restaurant_loc] = route
    
    def get_times(self,times,restaurant_loc):
        self.times[restaurant_loc] = int(times[restaurant_loc])
    
    def get_ratio(self,deliveries):
        self.reward_ratios[deliveries.restaurant_loc] = (deliveries.reward / (self.times[deliveries.restaurant_loc] + deliveries.dropoff_time))
    def restaurant_heap(self,heap):
        self.restaurants = heap