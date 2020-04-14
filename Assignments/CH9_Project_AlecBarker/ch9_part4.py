from gui import *
from music import *
from osc import *

# This program runs with the "OSC Controller" app by Adam Katz found on the Google Play Store
# I am using the first slider on the first tab and the first 3 buttons on the fourth tab

pitch = D3
volume = 25

def complete(message):
   global pitch
   global volume   

   command = message.getAddress().split("/")
   
   if "gridButton" in str(command[2]):
      if command[2] == "gridButton1":
         pitch = G4
      elif command[2] == "gridButton2":
         pitch = A5
      elif command[2] == "gridButton3":
         pitch = C4
      
      note = Note(pitch, HN, volume)
      Play.midi(note)
   elif "slider" in str(command[2]):
      args = message.getArguments()   
   
      if command[2] == "slider1":
         volume = int(args[0] * 100)
         print(volume)

oscIn = OscIn(57110)
oscIn.onInput("/.*", complete)