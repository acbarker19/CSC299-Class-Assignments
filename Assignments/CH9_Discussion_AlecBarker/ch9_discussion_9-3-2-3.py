from osc import *
from music import *

###### server program ######
###### create an OSC input object ######
oscIn = OscIn( 57110 ) # receive incoming messages on port 57110

def simple(message):
   print "Hello world!"

# Takes in a message and a set of arguments. It attempts to find the sum of all the arguments.
def sum_of_args(message):
   print("\r\nSum of Arguments:")   
   args = message.getArguments()
   
   try:
      if len(args) == 0:
         print("There were no arguments")
      else:
         total = 0
         
         for i in range(len(args)):
            total += int(args[i])
         
         print(total)
   except:
      print("The arguments were not number values.")

def complete(message):
   OSCaddress = message.getAddress()
   args = message.getArguments()
   
   # print OSC message time and address
   print "\nOSC Event:"
   print "OSC In - Address:", OSCaddress,
   
   # also, print message arguments (if any), all on a single line
   for i in range( len(args) ):
      print ", Argument " + str(i) + ": " + str(args[i]),
   print

###### now, associate above functions with OSC addresses ######
# callback function for incoming OSC address "/helloWorld"
oscIn.onInput("/helloWorld", simple)

oscIn.onInput("/sum", sum_of_args)

# callback function for all incoming OSC addresses
# (specify that as "/.*")
oscIn.onInput("/.*", complete)



###### client program ######
###### create an OSC output object ######

# where to send outgoing OSC messages - you may replace "localhost"
# with the IP address of a receiving computer (e.g., "192.168.1.223")
oscOut = OscOut( "localhost", 57110 ) # use port 57110

###### that's it - now, send some test OSC messages ######
# send a "/helloWorld" message without arguments
oscOut.sendMessage("/helloWorld")

# send a "/itsFullOfStars" message with an integer, a float,
# a string, and a boolean argument
oscOut.sendMessage("/itsFullOfStars", 1, 2.35, "wow!", True)

# tests the sum of various arguments
oscOut.sendMessage("/sum")
oscOut.sendMessage("/sum", 1, "abc", 5.5, 9)
oscOut.sendMessage("/sum", 1, 7, 5.5, 9)