#
# Rose Curves Demo
#

# Import the python module
import pyshiva as ps
import math, random

# Create a window with the title "Rose Curves"
w = ps.Window(title = "Rose Curves")

all_rects = list()

# Create 1000 squares with different colors
for i in range(1000):
    r = random.random()
    a = abs(math.cos(i))*0.5
    side_length = abs(math.sin(i))*50
    r = ps.Rect(0,0,side_length,side_length,(r,math.sin(i),math.cos(i),a))
    w.add(r) # Add the rectangles to the window...
    all_rects.append(r) # and keep track of them with a list

k = 0.25
while w.is_open():
    x,y = ps.get_mouse_pos()
    k = float(x)/w.width # Set the curve type based on the x position of the mouse
    print k
    t = w.s_since_open()*2 # Use a scaled time since program start as the parametric time value
    radius = abs(math.sin(w.s_since_open()))
    #if radius < 0.01: # Every time the curve collapses...
    #    k = random.random() # Randomize the k value to change the type of the curve
    # Place every rectangle along a rose curve, offset by its index
    for (i,r) in enumerate(all_rects):
        r.x = radius*math.cos(k*(t+i))*math.sin(t+i)*w.width/2+w.width/2
        r.y = radius*math.sin(k*(t+i))*math.sin(t+i)*w.height/2+w.height/2

    # Update the screen
    w.refresh()