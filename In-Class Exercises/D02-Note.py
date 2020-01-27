# D02-Note.py
# Demonstrates how to play a single note.

from music import *

note = Note(BS3, WN+WN, 128, 0.5) # Note(note, length, volume{0-128}, left/center/right{0-1})
Play.midi(note)               # plays note