import other_funcs
import random
class driver:
    def __init__(self,N_L):
        self.age = random.randint(0,10000)
        self.get_location(N_L)
        self.routes ={}
        self.times = []
        self.reward_ratios = {}
    def get_location(self,N_L):
        g = random.randint(0,len(N_L))
        self.init_location = N_L[g]
    
    def get_routes(self,route,delivery_set):
        self.routes[delivery_set] = route
    
    def get_times(self,times,delivery_set):
        self.times.append({delivery_set : int(times[delivery_set])})
    
    def get_ratio(self,deliveries):
        self.reward_ratios[deliveries.restaurant_loc] = (deliveries.reward / (self.times[deliveries.restaurant_loc] + deliveries.dropoff_time))