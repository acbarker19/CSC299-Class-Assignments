from gui import *
from music import *
from math import sqrt

d = Display("First Display", 400, 400)

def f(display, x, y):
   c = Circle(x, y, 10)   # x, y, radius
   display.add(c)
   
   r = Rectangle(x-20, y-20, x+20, y+20) # left-top and right-bottom corners
   display.add(r)
   
   l = Line(x-40, y, x+40, y) # x, y of two points
   display.add(l)
   
   l1 = Line(x, y-40, x, y+40)
   display.add(l1)
   
f(d, 50, 50)
f(d, 150, 150)
f(d, 250, 250)

d.showMouseCoordinates()
d.hideMouseCoordinates()



d = Display("Simple Button Instrument", 270, 130)
pitch = A4

def startNote():         # function to start the note
   global pitch          # we use this global variable
   Play.noteOn(pitch)
   
def stopNote():          # function to stop the note
   global pitch          # we use this global variable
   Play.noteOff(pitch)   # stop the note
   
# next, create the button widgets and assign their callback functions
b1 = Button("On", startNote)
b2 = Button("Off", stopNote)

# finally, add buttons to the display
d.add(b1, 90, 30)
d.add(b2, 90, 65)



"""
FileNotFoundException occurs even though the file is in the folder.

# load audio sample
a = AudioSample("Data Files\moondog.Bird_sLament.wav")

# create display
d = Display("Continuous Pitch Instrument", 270, 200)

# set slider ranges (must be integers)
minFreq = 440 # frequency slider range
maxFreq = 880 # (440 Hz is A4, 880 Hz is A5)

minVol = 0 # volume slider range
maxVol = 127

# create labels
label1 = Label("Freq: " + str(minFreq) + " Hz") # set initial text
label2 = Label("Vol: " + str(maxVol))

# define callback functions (called every time the slider changes)
def setFrequency(freq): # function to change frequency
   global label1, a # label to update, and audio to adjust
   a.setFrequency(freq)
   label1.setText("Freq: " + str(freq) + " Hz") # update label

def setVolume(volume): # function to change volume
   global label2, a # label to update, and audio to adjust
   a.setVolume(volume)
   label2.setText("Vol: " + str(volume)) # update label

# next, create two slider widgets and assign their callback functions
#Slider(orientation, lower, upper, start, eventHandler)
slider1 = Slider(HORIZONTAL, minFreq, maxFreq, minFreq, setFrequency)
slider2 = Slider(HORIZONTAL, minVol, maxVol, maxVol, setVolume)

# add labels and sliders to display
d.add(label1, 40, 30)
d.add(slider1, 40, 60)
d.add(label2, 40, 120)
d.add(slider2, 40, 150)

# start the sound
a.loop()
"""


"""
AudioSample can play wav and aif audio formats.

a = AudioSample("Data Files\moondog.Bird_sLament.wav", C4, 100)

a.play()
a.play(start, size)
a.loop()
a.loop(times, start, size)
a.stop()
a.pause()
a.resume()
a.isPlaying()
a.setPitch(pitch)
a.getPitch()
a.setFrequency(freq)
a.getFrequency()
a.setVolume(volume
a.getVolume()
a.getFrameRate()
a.setPanning(panning)
a.getPanning()
"""


"""
MidiSequence can play midi audio formats.

m = MidiSequence("beat1.mid", C4, 100)

m.play()
m.loop()
m.stop()
m.pause()
m.resume()
m.isPlaying()
m.setPitch(pitch)
m.getPitch()
m.setTempo(tempo)
m.getTempo()
m.getDefaultTempo()
m.setVolume(volume)
m.getVolume()
"""



d1 = Display("Playing with Events", 200, 355)
c1 = d1.drawCircle(50, 100, 81, Color.ORANGE, False, 4)

def moveCircle(x, y):
   global c1, d1
   d1.move(c1, x, y)
   
b1 = Button("Move Circle", moveCircle(10, 30))
d1.add(b1, 25, 307)

b1.onMouseClick(moveCircle)



### initialize variables ######################
minPitch = C1 # instrument pitch range
maxPitch = C8

# create display
d = Display("Circle Instrument") # default dimensions (600 x 400)
d.setColor(Color(51, 204, 255)) # set background to turquoise

beginX = 0 # holds starting x coordinate for next circle
beginY = 0 # olds starting y coordinate

# maximum circle diameter - same as diagonal of display
maxDiameter = sqrt(d.getWidth()**2 + d.getHeight()**2) # calculate it

### define callback functions ######################
def beginCircle(x, y): # for when mouse is pressed
   global beginX, beginY
   beginX = x # remember new circle's coordinates
   beginY = y

def endCircleAndPlayNote(endX, endY): # for when mouse is released
   global beginX, beginY, d, maxDiameter, minPitch, maxPitch
   # calculate circle parameters
   # first, calculate distance between begin and end points
   diameter = sqrt( (beginX-endX)**2 + (beginY-endY)**2 )
   diameter = int(diameter) # in pixels - make it an integer
   radius = diameter/2 # get radius
   centerX = (beginX + endX)/2 # circle center is halfway between...
   centerY = (beginY + endY)/2 # ...begin and end points
   
   # draw circle with yellow color, unfilled, 3 pixels thick
   d.drawCircle(centerX, centerY, radius, Color.YELLOW, False, 3)
   
   # create note
   pitch = mapScale(diameter, 0, maxDiameter, minPitch, maxPitch, MAJOR_SCALE)

   # invert pitch (larger diameter, lower pitch)
   pitch = maxPitch - pitch
   
   # and play note
   Play.note(pitch, 0, 5000) # start immediately, hold for 5 secs

def clearOnSpacebar(key): # for when a key is pressed
   global d
   
   # if they pressed space, clear display and stop the music
   if key == VK_SPACE:
      d.removeAll() # remove all shapes
      Play.allNotesOff() # stop all notes

### assign callback functions to display event handlers
######################
d.onMouseDown(beginCircle)
d.onMouseUp(endCircleAndPlayNote)
d.onKeyDown(clearOnSpacebar)



Play.setInstrument(PIANO) # set desired MIDI instrument (0-127)

# load piano image and create display with appropriate size
pianoIcon = Icon("Data Files\iPianoOctave.png") # image for complete piano
display = Display("iPiano", pianoIcon.getWidth(), pianoIcon.getHeight())

display.add(pianoIcon) # place image at top-left corner

# load icons for pressed piano keys
cDownIcon = Icon("Data Files\iPianoWhiteLeftDown.png") # C
cSharpDownIcon = Icon("Data Files\iPianoBlackDown.png") # C sharp
dDownIcon = Icon("Data Files\iPianoWhiteCenterDown.png") # D
# ...continue loading icons for additional piano keys

# remember which keys are currently pressed
keysPressed = []

#####################################################################
# define callback functions
def beginNote(key):
   """This function will be called when a computer key is pressed.
   It starts the corresponding note, if the key is pressed for
    the first time (i.e., counteracts the key-repeat function of
   computer keyboards).
   """
   global display # display surface to add icons
   global keysPressed # list to remember which keys are pressed
   
   print "Key pressed is " + str(key) # show which key was pressed
   
   if key == VK_Z and key not in keysPressed:
      display.add(cDownIcon, 0, 1) # "press" this piano key
      Play.noteOn(C4) # play corresponding note
      keysPressed.append(VK_Z) # avoid key-repeat
   elif key == VK_S and key not in keysPressed:
      display.add(cSharpDownIcon, 45, 1) # "press" this piano key
      Play.noteOn(CS4) # play corresponding note
      keysPressed.append(VK_S) # avoid key-repeat
   elif key == VK_X and key not in keysPressed:
      display.add(dDownIcon, 76, 1) # "press" this piano key
      Play.noteOn(D4) # play corresponding note
      keysPressed.append(VK_X) # avoid key-repeat
   
   #...continue adding elif's for additional piano keys

def endNote(key):
   """This function will be called when a computer key is released.
   It stops the corresponding note.
   """
   
   global display # display surface to add icons
   global keysPressed # list to remember which keys are pressed
   
   if key == VK_Z:
      display.remove(cDownIcon) # "release" this piano key
      Play.noteOff(C4) # stop corresponding note
      keysPressed.remove(VK_Z) # and forget key
   elif key == VK_S:
      display.remove(cSharpDownIcon) # "release" this piano key
      Play.noteOff(CS4) # stop corresponding note
      keysPressed.remove(VK_S) # and forget key
   elif key == VK_X:
      display.remove(dDownIcon) # "release" this piano key
      Play.noteOff(D4) # stop corresponding note
      keysPressed.remove(VK_X) # and forget key
   
   #...continue adding elif's for additional piano keys

#####################################################################
# associate callback functions with GUI events
display.onKeyDown(beginNote)
display.onKeyUp(endNote)



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

# lists of virtual keys and pitches corresponding to above piano keys
virtualKeys = [VK_Z, VK_S, VK_X, VK_D, VK_C, VK_V]
pitches = [C4, CS4, D4, DS4, E4, F4]

# create list of display positions for downKey icons
#
# NOTE: This as hardcoded – they depend on the used images!
#
iconLeftXCoordinates = [0, 45, 76, 138, 150, 223]

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