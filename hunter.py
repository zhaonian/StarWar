# A Hunter is both a Mobile_Simulton and Pulsator: it updates
#   like a Pulsator, but it moves (either in a straight line
#   or in pursuit of Prey) and displays as a Pulsator.

from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from prey import Prey
from math import atan2


class Hunter(Pulsator,Mobile_Simulton): #inherit pulsator
    in_range = 200   
    
    def __init__(self, x, y):   
        Pulsator.__init__(self, x, y)
        w, h = self.get_dimension()
        Mobile_Simulton.__init__(self, x, y, w, h, 0, 5)
        self.randomize_angle()
        
        
    def update(self, model):
        eaten_set = Pulsator.update(self, model)
        _range  = model.find(lambda x : isinstance(x, Prey) and self.distance(x.get_location()) <= Hunter.in_range)
        eat_list = []
        if len(_range) != 0:
            for s in _range:
                eat_list.append((self.distance(s.get_location()), s))
            d, chosen_eat = sorted(eat_list)[0]
            x, y   = chosen_eat.get_location()
            sim_x, sim_y = self.get_location()
            self.set_angle(atan2(y - sim_y, x - sim_x))
        self.move()
        return eaten_set
        
