# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


from PIL.ImageTk import PhotoImage
from prey import Prey

import random

class Floater(Prey): # inherit prey
    def __init__(self, x, y):   
        self._image = PhotoImage(file = 'ufo.gif')
        Prey.__init__(self, x, y, self._image.width(), self._image.height(), 0, 5)
        self.randomize_angle()

        
    def update(self, model):
        if random.randrange(0,10) / 10 <= 0.3: # 30% time changed
            if (self.get_speed() + random.randrange(0, 10) / 10 - 0.5) >= 0.3:
                if (self.get_speed() + random.randrange(0, 10) / 10 - 0.5) <= 0.7:
                    new_speed = (self.get_speed() + random.randrange(0, 10) / 10 - 0.5)
                else:
                    new_speed = 7
            else:
                new_speed = 3            
            self.set_velocity(new_speed, self.get_angle() + random.randrange(0, 10) / 10 - 0.5)
        self.move()
 

    def display(self,root_canvas):
        root_canvas.create_image(self._x, self._y, image = self._image)
