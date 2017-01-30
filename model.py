import controller, sys
import model   #strange, but we need a reference to this module to pass this module to update
from special import Special
from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter


# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
cycle_counter = 0
running = False
one_step = False
clicked_object = 0
simultons = set()


#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(), controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global cycle_counter, simultons, running, one_step, clicked_object
    cycle_counter = 0
    running = False
    one_step = False
    clicked_object = 0
    simultons = set()


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#step just 1 update in the simulation
def step ():
    global running, one_step
    running = True
    one_step = True


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global clicked_object
    clicked_object = kind
#    print(str(kind))

#add the kind of remembered object to the simulation (or remove any objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x, y):
    if clicked_object == 'Remove':
        for s in find(lambda s : s.contains((x, y))):
            simultons.discard(s) 
            
    elif clicked_object == 0:
        print('No object selected!')                            

    else:
        print(clicked_object)
        simultons.add(eval(clicked_object + '(' + str(x)  + ','  + str(y) + ')'))


#add simulton s to the simulation
def add(s):
    global simultons
    simultons.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    global simultons
    simultons.discard(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    temp_set = set()
    for s in simultons:
        if p(s):
            temp_set.add(s)
    return temp_set


#call update for every simulton in the simulation
def update_all():
    global running, one_step
    if running:
        global cycle_counter
        cycle_counter += 1
        
        s_set = set(simultons)
        for s in s_set:
            if s in simultons: # start after step or stop
                s.update(model)
                
    if one_step:  # if press step after start
        running = False
        one_step = False
        


def display_all():
    for x in controller.the_canvas.find_all():
        controller.the_canvas.delete(x)
    
    for s in simultons:
        s.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(cycle_counter) + ' cycles/' + str(len(simultons)) + ' simultons')
