# 8.14.2.1 #4
# Alec Barker

from gui import *
from music import *

# create display
d = Display("Slider", 270, 200)

slider = Rectangle(16, 10, 20, 150, Color.BLACK, True)
d.add(slider)

knob = Circle(slider.x + 2, slider.y, 5, Color.RED, True)
d.add(knob)

def moveKnob(x, y):
   global slider, knob
   if x >= slider.x - 3 and x <= slider.x + slider.getWidth() + 3 and y >= slider.y and y <= slider.y + slider.getHeight():
      d.move(knob, slider.x + 2, y)

d.onMouseDrag(moveKnob)