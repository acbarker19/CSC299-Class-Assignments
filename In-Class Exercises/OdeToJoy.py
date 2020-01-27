# D02-Note.py
# Demonstrates how to play a single note.

from music import *

phr = Phrase()    # create an empty phrase
phr.setInstrument(BIRD)
phr.setTempo(150)

pitches =   [E4, E4, F4, G4,   G4, F4, E4, D4,   C4, C4, D4, E4,   E4, D4, D4]
durations = [EN, EN, EN, EN,   EN, EN, EN, EN,   EN, EN, EN, EN,   EN, EN, QN]

phr.addNoteList(pitches, durations)
# phr.addNoteList(pitches, durations) # plays twice

Play.midi(phr)