from music import *

# arpeggioPattern = [0, 2, 4, 5, 7, 9, 11]   # major scale
arpeggioPattern = [0, 2, 3, 5, 7, 8, 10]   # minor scale
duration = TN

rootPitch = input("Enter root note (e.g., C4): ")
repetitions = input("Enter how many times you want to repeat the arpeggio: ")

arpeggioPhrase = Phrase(0.0)

for interval in arpeggioPattern:
   pitch = rootPitch + interval
   n = Note(pitch, duration)
   arpeggioPhrase.addNote(n)
   
Mod.repeat(arpeggioPhrase, repetitions)

lastPitch = rootPitch + arpeggioPattern[0]
n = Note(lastPitch, duration * 4)
arpeggioPhrase.addNote(n)

Play.midi(arpeggioPhrase)