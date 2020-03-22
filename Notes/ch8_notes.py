from gui import *
from music import *

d = Display("First Display", 400, 400)

def f(display, x, y):
   c = Circle(x, y, 10)   # x, y, radius
   display.add(c)
   
   r = Rectangle(x-20, y-20, x+20, y+20) # left-top and right-bottom corners
   display.add(r)
   
   l = Line(x-40, y, x+40, y) # x, y of two points
   display.add(l)
   
   l1 = Line(x, y-40, x, y+40)
   display.add(l1)
   
f(d, 50, 50)
f(d, 150, 150)
f(d, 250, 250)

d.showMouseCoordinates()
d.hideMouseCoordinates()



d = Display("Simple Button Instrument", 270, 130)
pitch = A4

def startNote():         # function to start the note
   global pitch          # we use this global variable
   Play.noteOn(pitch)
   
def stopNote():          # function to stop the note
   global pitch          # we use this global variable
   Play.noteOff(pitch)   # stop the note
   
# next, create the button widgets and assign their callback functions
b1 = Button("On", startNote)
b2 = Button("Off", stopNote)

# finally, add buttons to the display
d.add(b1, 90, 30)
d.add(b2, 90, 65)