from gui import *
from random import *
from music import *

# Exercise 8.4.1 #2
d = Display("Chapter 8 Discussion - Exercise 8.4.1 #2", 1000, 1000)
num_shapes = 1000

def get_random_color():
   # get random color (RGB)
   red = randint(0, 255) # random R(0-255)
   green = randint(0, 255) # random G (0-255)
   blue = randint(0, 255) # random B (0-255)
   color = Color(red, green, blue) # build color from random RGB
   return color

def draw_shape(display, x, y):
   c = Circle(x, y, 10, get_random_color())
   display.add(c)
   
   r = Rectangle(x-20, y-20, x+20, y+20, get_random_color())
   display.add(r)
   
   l = Line(x-40, y, x+40, y, get_random_color())
   display.add(l)
   
   l1 = Line(x, y-40, x, y+40, get_random_color())
   display.add(l1)
   
for i in range(num_shapes):
   # get random position and radius
   x = randint(0, d.getWidth()-1)    # x may be anywhere on display
   y = randint(0, d.getHeight()-1)   # y may be anywhere on display
   draw_shape(d, x, y)
   
"""
For this exercise, I followed the instructions and given code on how to create
the complex shape, and I did the additional step that was mentioned to put the
shape in its own function with relative coordinates. This made it easier once I
read the instructions for exercise 8.4.1 #2 since we need to draw the shape
multiple times. I also was able to follow the code that the book used for
drawing multiple circles to get the random x and y coordinate generator and the
random RGB value generator, which is my enhancement. I chose this enhancement
because it is fairly simple but adds a bit of color and diversity to the
repeating shapes. Without the color, they sometimes blend together and are hard
to distinguish. I used the code the book uses for the random repeated circles,
put it in its own function, and I call it for each part of the complex shape so
its not all the same color. I think this exercise is pretty good for a first
GUI drawing in python. I feel like the book didn't cover the random library very
well, so some students might be a little confused unless they just copy the code.
Maybe include a refresher about random and randint with the exercise in the future.
"""