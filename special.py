# A Special is a Simulton; it updates by removing
#   any Hunter whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black PacMan with a radius of 40
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate





import simulton
import hunter
from PIL.ImageTk import PhotoImage
 
 
class Special(simulton.Simulton):
     
    def __init__(self, x, y):   
        self._image = PhotoImage(file = 'pac.jpg')
        simulton.Simulton.__init__(self, x, y, 40, 40)
         
    def update(self, model):
        eaten_set = model.find(lambda s : isinstance(s, hunter.Hunter) and self.contains(s.get_location()))
        for s in eaten_set:
            model.remove(s)
        return eaten_set
 
  
 
     
    def contains(self, r):
        return self.distance(r) <= self.get_dimension()[1]/2
 
                
    def display(self, root_canvas):
        root_canvas.create_image(self._x, self._y, image = self._image)
    
    





    