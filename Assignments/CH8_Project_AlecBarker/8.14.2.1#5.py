# 8.14.2.1 #5
# Alec Barker

from gui import *
from music import *

"""
I am not able to test this due to AudioSamples throwing errors and exceptions on my PC, but I used print statements
of the volume variable and they seem correct to me.
"""

a = AudioSample(filename="Data Files\moondog.Bird_sLament.wav", volume=0)

# create display
d = Display("Slider", 270, 200)

slider = Rectangle(16, 20, 20, 150, Color.BLACK, True)
d.add(slider)

knob = Circle(slider.x + 2, slider.y, 5, Color.RED, True)
d.add(knob)

def moveKnob(x, y):
   global slider, knob
   if x >= slider.x - 3 and x <= slider.x + slider.getWidth() + 3 and y >= slider.y and y <= slider.y + slider.getHeight():
      d.move(knob, slider.x + 2, y)
      
      # change volume
      slider_percent = float(knob.y + 5 - slider.y) / float(slider.getHeight())
      volume = int(127 * slider_percent)
      a.setVolume(volume)

d.onMouseDrag(moveKnob)