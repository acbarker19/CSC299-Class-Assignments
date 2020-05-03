from music import *
from math import *
"""
print(sin(0))
print(sin(pi/2))
print(radians(90) == pi/2)
print(sin(radians(90)))
print(radians(180) == pi)
print(degrees(pi/2))
print(degrees(pi))



phr = Phrase()
density = 25.0 # higher for more notes in sine curve
cycle = int(2 * pi * density) # steps to traverse a complete cycle

# create one cycle of the sine curve at given density
for i in range(cycle):
   value = sin(i / density) # calculate the next sine value
   pitch = mapValue(value, -1.0, 1.0, C2, C8) # map to range C2-C8
   note = Note(pitch, TN)
   phr.addNote(note)
   
View.pianoRoll(phr) # so view them
Play.midi(phr) # and play them
"""


sineMelodyPhrase = Phrase()
density = 10.0
cycle = int(2 * pi * density)

for i in range(58):
   value = radians(i) * 1000
   print(value)
   pitch = mapValue(value, 0.0, 1000.0, C1, C9)
   duration = mapValue(value, 0.0, 1000.0, EN, 0.1)
   dynamic = mapValue(value, 0.0, 1000.0, PIANISSIMO, FORTISSIMO)
   panning = mapValue(value, 0.0, 1000.0, PAN_LEFT, PAN_RIGHT)
   
   note = Note(pitch, duration, dynamic, panning)
   sineMelodyPhrase.addNote(note)
   
View.pianoRoll(sineMelodyPhrase)
Play.midi(sineMelodyPhrase)