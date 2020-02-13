from music import *
from random import *

heads = random() < 0.5   # has a 50/50 chance of true or false

if heads:
   note = Note(C4, HN)
else:
   note = Note(G4, HN)
   
Play.midi(note)