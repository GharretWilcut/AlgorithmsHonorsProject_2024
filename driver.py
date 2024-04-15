import other_funcs
import random
class driver:
    def __init__(self,N_L):
        self.age = random.randint(0,10000)
        self.get_location(N_L)
    def get_location(self,N_L):
        g = random.randint(0,len(N_L))
        self.init_location = N_L[g]
    
    