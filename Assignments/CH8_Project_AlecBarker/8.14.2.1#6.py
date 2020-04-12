# 8.14.2.1 #6
# Alec Barker

from gui import *
from music import *

"""
Not all of the GUI elements are functional with their intended purpose.
"""

"""
I am not able to test this due to AudioSamples throwing errors and exceptions on my PC, but I used print statements
of the volume variable and they seem correct to me.
"""

a = AudioSample(filename="Data Files\moondog.Bird_sLament.wav", volume=0)

# create display
d = Display("GUI Controls", 270, 200)

slider = 0
knob = 0

def testFunc():
   print("testFunc()")

def addSlider(x, y, height):
   global slider, knob
   slider = Rectangle(x, y, x + 4, y + height, Color.BLACK, True)
   d.add(slider)
   
   knob = Circle(x + 2, y, 5, Color.RED, True)
   d.add(knob)
   
def addTurnKnob(x, y, radius):
   turnKnob = Circle(x, y, radius, Color.RED, True)
   d.add(turnKnob)
   
def addButton(x, y, text, function):
   button = Button(text, function)
   d.add(button, x, y)

def moveKnob(x, y):
   global slider, knob
   if x >= slider.x - 3 and x <= slider.x + slider.getWidth() + 3 and y >= slider.y and y <= slider.y + slider.getHeight():
      d.move(knob, slider.x + 2, y)
      
      # change volume
      slider_percent = float(knob.y + 5 - slider.y) / float(slider.getHeight())
      volume = int(127 * slider_percent)
      a.setVolume(volume)

addSlider(25, 25, 100)
addTurnKnob(100, 100, 10)
addButton(150, 150, "TEST", testFunc)

d.onMouseDrag(moveKnob)