#
# Rose Curves Demo
#

# Import the python module
import pyshiva as ps
import math, random

# Create a window with the title "Rose Curves"
w = ps.Window(title = "Rose Curves")

# Create 1000 squares with different colors
for i in range(1000):
    r = random.random()
    a = abs(math.cos(i))*0.5
    side_length = abs(math.sin(i))*50
    r = ps.Circle(0,0,radius = side_length,color = (r,abs(math.sin(i)),1,0.1),stroke_color = (0,0,0,0.8), stroke_thickness = 5.0)
    w.add(r) # Add the rectangles to the window.

k = 0.25
while w.is_open():
    x,y = ps.get_mouse_pos()
    t = w.s_since_open()*2 # Use a scaled time since program start as the parametric time value
    radius = abs(math.sin(w.s_since_open()))
    if radius < 0.01: # Every time the curve collapses...
        k = random.random() # Randomize the k value to change the type of the curve
    #k = float(x)/w.width
    #print k
    #print r.radius
    #k = 0.760935
    # Place every rectangle along a rose curve, offset by its index
    for (i,r) in enumerate(w): # Loop through every object in the window
        r.x = radius*math.cos(k*(t+i))*math.sin(t+i)*w.width/2+w.width/2
        r.y = radius*math.sin(k*(t+i))*math.sin(t+i)*w.height/2+w.height/2
        #print abs(10*math.sin(t))
        #r.width = 1.32303762436 #100000 #abs(100*math.sin(t))
        #r.height = 100000 #abs(100*math.sin(t))
        
    # Update the screen
    w.refresh()
