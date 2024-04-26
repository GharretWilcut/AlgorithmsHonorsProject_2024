import random
import math
#this is the basic delivery class I will probably change and add things to it
class delivery:
    def __init__(self, restaurant_loc,N_L):
        #restaurant location
        self.restaurant_loc = restaurant_loc
        self.wait = random.randint(0,15)
        self.reward = 0
        self.reward_ratio = {}
        self.route_to_restaurant_loc = 0
        self.driver_loc = 0
        self.dropoff(N_L)    
        #gets reward using the drop off time and then adds a random tip between 0 - 15
    def get_reward(self):
        self.reward = (math.log(1 + (self.dropoff_time)) + random.randint(0,15))
    def driver_location(self, loc):
        self.driver_loc = loc
            
    #route it takes the driver to go to the restaurant
    def route_to_restaurant_from_driver(self, wait):
        self.route_to_restaurant_loc = wait
            
    #route it takes the driver to get to the dropoff location
    def route_to_dropoff(self, wait):
        self.route_to_dropoff_loc = wait
        self.get_reward()
            
    #time it takes the driver to go to the restaurant
    def time_to_restaurant_from_driver(self, wait):
        self.time_to_restaurant = wait
            
    #time it takes the driver to get to the dropoff location
    def time_to_dropoff(self, wait):
        self.dropoff_time = wait
        
    #dropoff location
    def dropoff(self, N_L):
        g = random.randint(0,len(N_L))
        self.dropoff_loc =  N_L[g]
        
    def total_time(self):
        return self.wait + self.dropoff_time + self.time_to_restaurant
    
    def get_ratio(self,driver):
        self.reward_ratio[driver.init_location] = (self.reward / (driver.times[self.restaurant_loc] + self.dropoff_time))