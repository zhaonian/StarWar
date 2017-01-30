# A Black_Hole is a Simulton; it updates by removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):
    radius = 10
    
    def __init__(self, x, y):   
        Simulton.__init__(self, x, y, 2*Black_Hole.radius, 2*Black_Hole.radius)
        
    def update(self, model):
        set_eaten = model.find(lambda b: isinstance(b, Prey) and self.contains(b.get_location()))
        for b in set_eaten:
            model.remove(b)
        return set_eaten

               
    def display(self, root_canvas):
        w = self.get_dimension()[0]
        h = self.get_dimension()[1]
        root_canvas.create_oval(self._x - w / 2, self._y - h / 2,
                               self._x + w / 2, self._y + h / 2,
                               fill = 'black')
        
 
    def contains(self, r):
        return self.distance(r) <= (self.get_dimension()[1])/2
    
    
    
    
    