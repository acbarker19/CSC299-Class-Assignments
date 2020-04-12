# 8.14.2.1 #1
# Alec Barker

from gui import *
from music import *

Play.setInstrument(PIANO) # set desired MIDI instrument (0–127)

# load piano image and create display with appropriate size
pianoIcon = Icon("Data Files\iPianoOctave.png") # image for complete piano
d = Display("iPiano", pianoIcon.getWidth(), pianoIcon.getHeight())
d.add(pianoIcon) # place image at top-left corner

# NOTE: The following loads a partial list of icons for pressed piano
# keys, and associates them (via parallel lists) with the
# virtual keys corresponding to those piano keys and the corresponding
# pitches. These lists should be expanded to cover the whole octave
# (or more).

# load icons for pressed piano keys
# (continue loading icons for additional piano keys)
downKeyIcons = [] # holds all down piano-key icons
downKeyIcons.append(Icon("Data Files\iPianoWhiteLeftDown.png")) # C
downKeyIcons.append(Icon("Data Files\iPianoBlackDown.png")) # C sharp
downKeyIcons.append(Icon("Data Files\iPianoWhiteCenterDown.png")) # D
downKeyIcons.append(Icon("Data Files\iPianoBlackDown.png")) # D sharp
downKeyIcons.append(Icon("Data Files\iPianoWhiteRightDown.png")) # E
downKeyIcons.append(Icon("Data Files\iPianoWhiteLeftDown.png")) # F
downKeyIcons.append(Icon("Data Files\iPianoBlackDown.png")) # F sharp
downKeyIcons.append(Icon("Data Files\iPianoWhiteCenterDown.png")) # G
downKeyIcons.append(Icon("Data Files\iPianoBlackDown.png")) # G sharp
downKeyIcons.append(Icon("Data Files\iPianoWhiteCenterDown.png")) # A
downKeyIcons.append(Icon("Data Files\iPianoBlackDown.png")) # A sharp
downKeyIcons.append(Icon("Data Files\iPianoWhiteRightDown.png")) # B

# lists of virtual keys and pitches corresponding to above piano keys
virtualKeys = [VK_Z, VK_S, VK_X, VK_D, VK_C, VK_V, VK_G, VK_B, VK_H, VK_N, VK_J, VK_M]
pitches = [C4, CS4, D4, DS4, E4, F4, FS4, G4, GS4, A4, AS4, B4]

# create list of display positions for downKey icons
#
# NOTE: This as hardcoded – they depend on the used images!
#
iconLeftXCoordinates = [0, 45, 76, 138, 150, 223, 268, 298, 350, 372, 434, 446]

keysPressed = [] # holds which keys are currently pressed

#####################################################################
# define callback functions
def beginNote( key ):
   """Called when a computer key is pressed. Implements the
   corresponding piano key press (i.e., adds key-down icon on
   display, and starts note). Also, counteracts the key-repeat
   function of computer keyboards.
   """
   # loop through all known virtual keys
   for i in range(len(virtualKeys)):
      # if this is a known key (and NOT already pressed)
      if key == virtualKeys[i] and key not in keysPressed:
         # "press" this piano key (by adding pressed key icon)
         d.add(downKeyIcons[i], iconLeftXCoordinates[i], 0)
         Play.noteOn(pitches[i]) # play corresponding note
         keysPressed.append(key) # avoid key-repeat

def endNote( key ):
   """Called when a computer key is released. Implements the
   corresponding piano key release (i.e., removes key-down icon,
   and stops note).
   """
   # loop through known virtual keys
   for i in range(len(virtualKeys)):
      # if this is a known key (we can assume it is already pressed)
      if key == virtualKeys[i]:
         # "release" this piano key (by removing pressed key icon)
         d.remove( downKeyIcons[i] )
         Play.noteOff( pitches[i] ) # stop corresponding note
         keysPressed.remove( key ) # and forget key

#####################################################################
# associate callback functions with GUI events
d.onKeyDown(beginNote)
d.onKeyUp(endNote)