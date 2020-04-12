from gui import *
from random import *
from music import *

# 8.6.2
d = Display("Chapter 8 Discussion - Exercise 8.6.2", 270, 130)

pitch = A4
pitch2 = G5

def startNote():                     # function to start the note
   global pitch                      # we use this global variable
   Play.setInstrument(PIANO)
   Play.noteOn(pitch)                # play the note
   
def stopNote():                      # function to stop the note
   global pitch                      # we use this global variable
   Play.noteOff(pitch)               # stop the note
   
def startNote2():
   global pitch2
   Play.setInstrument(randint(1, 127))   # all instruments except piano
   Play.noteOn(pitch2)
   
def stopNote2():
   global pitch2
   Play.noteOff(pitch2)
   
# next, create the button widgets and assign their callback functions
b1 = Button("Pitch 1 On", startNote)
b2 = Button("Pitch 1 Off", stopNote)
b3 = Button("Pitch 2 On", startNote2)
b4 = Button("Pitch 2 Off", stopNote2)

# finally, add buttons to the display
d.add(b1, 40, 30)
d.add(b2, 40, 65)
d.add(b3, 130, 30)
d.add(b4, 130, 65)

"""
I started this exercise by following the instruction and code samples found earlier
in the chapter to create the buttons that play a note. Since this exercise wanted
you to build upon the existing program, I decided to keep the same style of
architecture that uses global variables instead of creating a single function with
parameters. Therefore, there are startNote2 and stopNote2 functions, as well as a
pitch2 variable that is called via global. For my enhancement, I used randomness
again to play a random instrument every time the user presses the pitch 2 button. The
only instrument that is excluded is the piano, which is covered by the pitch 1
button. I was having fun just choosing a second instrument, and I went through a
number of them before I thought of the idea of randomizing it. I accomplished this
by simply adding a randint into the setInstrument function in the startNote2 function.
I think this exercise is good for adding buttons and seeing how they can use notes
for interaction. The only thing that I thought of is changing the duration of notes.
Looking at the Play documentation page for Jython, it seems like the programmer can't
set the duration unless they use Play.note(), which I don't think allows stopping via
noteOff(). Maybe include duration in some way the next time around.
"""