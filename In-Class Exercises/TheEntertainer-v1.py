# TheEntertainer-v1.py
# January 17, 2020

from music import *

### define the data structures
theEntertainerScore = Score("The Entertainer - Easy", 140)   # sets the title and the BPM

pianoPart = Part(PIANO, 0)   # plays the piano on channel 0

melodyPhrase = Phrase()   # hold the melody

### creates musical data
# melody
melodyPitch1 =    [[D6, D5], [E6, E5], [C6, C5], [A6, A4], [B6, B4], [G5, G4],
                   D5, E5, C5, A4, B4, G4,   D4, E4, C4, A3, B3, A3, AF3,
                   G3, REST, [G5, D5, B4, G4], D4, DS4,
                   E4, C5, E4, C5, E4, C5,   REST, C5, D5, DS5,
                   E5, C5, D5, E5, B4, D5,   C5]
melodyDuration1 = [EN,       EN,       EN,       QN,       EN,       QN,
                   EN, EN, EN, QN, EN, QN,   EN, EN, EN, QN, EN, EN, EN,
                   QN, QN,   QN,               EN, EN,
                   EN, QN, EN, QN, EN, HN,   EN,   EN, EN, EN,
                   EN, EN, EN, QN, EN, QN,   HN]

melodyPhrase.addNoteList(melodyPitch1, melodyDuration1)   # add list of notes to phrase
pianoPart.addPhrase(melodyPhrase)   # add phrase to part
theEntertainerScore.addPart(pianoPart)   # add part to score

Play.midi(theEntertainerScore)