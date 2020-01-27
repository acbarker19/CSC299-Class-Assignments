# HW1-TheEntertainer.py
# January 22, 2020

# The Entertainer
# Composed by Scott Joplin
# Performed by Alec Barker

from music import *

####################
### Create Score ###
####################

the_entertainer_score = Score("The Entertainer - Easy", 180)   # Sets the title and the BPM

####################
### Create Parts ###
####################

treble_part = Part(HONKYTONK, 0)    # Plays the piano treble on channel 0
bass_part = Part(HONKYTONK, 1)      # Plays the piano bass on channel 1

######################
### Create Phrases ###
######################

treble_phrase_1 = Phrase()      # First treble phrase that plays once
treble_phrase_2 = Phrase()      # Second treble phrase that repeats
treble_phrase_3 = Phrase()      # Third treble phrase that is first ending
treble_phrase_4 = Phrase()      # Fourth treble phrase that is second ending
treble_phrase_repeat = Phrase() # A repeat of the second treble phrase

bass_phrase_1 = Phrase()        # First bass phrase that plays once
bass_phrase_2 = Phrase()        # Second bass phrase that repeats
bass_phrase_3 = Phrase()        # Third bass phrase that is first ending
bass_phrase_4 = Phrase()        # Fourth bass phrase that is second ending
bass_phrase_repeat = Phrase()   # A repeat of the second bass phrase

####################
### Measures 1-4 ###
### Treble/Bass  ###
####################

# Measure         One                                                           Two                       Three
treble_pitch_1 = [[D6, D5], [E6, E5], [C6, C5], [A6, A4], [B6, B4], [G5, G4],   D5, E5, C5, A4, B4, G4,   D4, E4, C4, A3, B3, A3, AF3,
# Measure         Four
                  G3, REST, [G5, D5, B4, G4], D4, DS4]
                  
# Measure         One                                                           Two                       Three
treble_dur_1 =   [EN,       EN,       EN,       QN,       EN,       QN,         EN, EN, EN, QN, EN, QN,   EN, EN, EN, QN, EN, EN, EN,
# Measure         Four
                  QN, QN,   QN,               EN, EN]

# Measure       One     Two                       Three                          Four
bass_pitch_1 = [REST,   D4, E4, C4, A3, B3, G3,   D3, E3, C3, A2, B2, A2, AF2,   G2, REST, [G2, G1], [G3, B3]]

# Measure       One     Two                       Three                          Four
bass_dur_1 =   [WN,     EN, EN, EN, QN, EN, QN,   EN, EN, EN, QN, EN, EN, EN,    QN, QN,   QN,       QN]

#########################
### Measures 5, 9, 13 ###
###    Treble/Bass    ###
#########################

# Measure         Five/Nine/Thirteen
treble_pitch_2 = [E4, C5, E4, C5, E4, C5]   

# Measure         Five/Nine/Thirteen
treble_dur_2 =   [EN, QN, EN, QN, EN, EN+HN]

# Measure       Five/Nine/Thirteen
bass_pitch_2 = [C3, [E3, G3], C3, [E3, BF3]]

# Measure       Five/Nine/Thirteen
bass_dur_2 =   [QN, QN,       QN, QN]

######################
### Measures 6, 14 ###
###  Treble/Bass   ###
######################

# Measure         Six/Fourteen
treble_pitch_3 = [REST, C5, D5, DS5]

# Measure         Six/Fourteen
treble_dur_3 =   [EN,   EN, EN, EN]

# Measure       Six/Fourteen
bass_pitch_3 = [F3, [A3, C4], E3, [G3, C4]]

# Measure       Six/Fourteen
bass_dur_3 =   [QN, QN,       QN, QN]

##########################
### Measures 7, 15, 19 ###
###    Treble/Bass     ###
##########################

# Measure         Seven/Fifteen/Nineteen
treble_pitch_4 = [E5, C5, D5, E5, B4, D5]

# Measure         Seven/Fifteen/Nineteen
treble_dur_4 =   [EN, EN, EN, QN, EN, QN]

# Measure       Seven/Fifteen/Nineteen
bass_pitch_4 = [G2, [C3, E3], G2, [D3, F3]]

# Measure       Seven/Fifteen/Nineteen
bass_dur_4 =   [QN, QN,       QN, QN]

######################
### Measures 8, 20 ###
###  Treble Only   ###
######################

# Measure         Eight/Twenty
treble_pitch_5 = [C5, REST, D4, DS4]

# Measure         Eight/Twenty
treble_dur_5 =   [HN, QN,   EN, EN]

#################
### Measure 8 ###
### Bass Only ###
#################

# Measure       Eight
bass_pitch_5 = [C3, [E3, G3], [E3, G3], [G3, B3]]

# Measure       Eight
bass_dur_5 =   [QN, QN,       QN,       QN]

######################
### Measures 10-12 ###
###  Treble/Bass   ###
######################

# Measure         Ten             Eleven                        Twelve
treble_pitch_6 = [REST, A4, G4,   F4, A4, C5, E5, D5, C5, A4,   D5, REST, D4, DS4]

# Measure         Ten             Eleven                        Twelve
treble_dur_6 =   [QN,   EN, EN,   EN, EN, EN, QN, EN, EN, EN,   HN, QN,   EN, EN]

# Measure       Ten                      Eleven                          Twelve
bass_pitch_6 = [F3, [A3, C4], E3, EF3,   D3, [FS3, A3], D3, [FS3, A3],   [G3, B3], G2, A2, B2]

# Measure       Ten                      Eleven                          Twelve
bass_dur_6 =   [QN, QN,       QN, QN,    QN, QN,        QN, QN,          QN,       QN, QN, QN]

###################
### Measure 16  ###
### Treble Only ###
###################

# Measure         Sixteen
treble_pitch_7 = [C5, REST, C5, D5]

# Measure         Sixteen
treble_dur_7 =   [HN, QN,   EN, EN]

######################
### Measures 16-18 ###
###   Bass Only    ###
######################

# Measure       Sixteen                         Seventeen                      Eighteen
bass_pitch_7 = [[C3, E3], G2, [C3, E3], REST,   C3, [E3, G3], BF2, [E3, G3],   A2, [C3, E3], AS2, [C3, E3]]

# Measure       Sixteen                         Seventeen                      Eighteen
bass_dur_7 =   [QN,       QN, QN,       QN,     QN, QN,       QN,  QN,         QN, QN,       QN,  QN]

######################
### Measure 17, 18 ###
###  Treble Only   ###
######################

# Measure         Seventeen/Eighteen
treble_pitch_8 = [E5, C5, D5, E5, C5, D5, C5]

# Measure         Seventeen/Eighteen
treble_dur_8 =   [EN, EN, EN, QN, EN, EN, EN]

##################
### Measure 20 ###
### Bass Only  ###
##################

# Measure       Twenty
bass_pitch_8 = [[C3, E3], G2, A2, C3]

# Measure       Twenty
bass_dur_8 =   [QN,       QN, QN, QN]

###################
### Measure 21  ###
### Treble/Bass ###
###################

# Measure         Twenty-One
treble_end_note = Note(C5, HN)

# Note won't accept two notes played together, so I had to create a NoteList below.

# Measure       Twenty-One
bass_pitch_9 = [[C3, E3]]

# Measure       Twenty-One
bass_dur_9 =   [HN]

###################################
### Add Notes to Treble Phrases ###
###################################

# Adds list of notes to phrase 1
treble_phrase_1.addNoteList(treble_pitch_1, treble_dur_1) # Measures 1-4

# Adds list of notes to phrase 2
treble_phrase_2.addNoteList(treble_pitch_2, treble_dur_2) # Measure 5
treble_phrase_2.addNoteList(treble_pitch_3, treble_dur_3) # Measure 6
treble_phrase_2.addNoteList(treble_pitch_4, treble_dur_4) # Measure 7
treble_phrase_2.addNoteList(treble_pitch_5, treble_dur_5) # Measure 8
treble_phrase_2.addNoteList(treble_pitch_2, treble_dur_2) # Measure 9
treble_phrase_2.addNoteList(treble_pitch_6, treble_dur_6) # Measures 10-12
treble_phrase_2.addNoteList(treble_pitch_2, treble_dur_2) # Measure 13
treble_phrase_2.addNoteList(treble_pitch_3, treble_dur_3) # Measure 14
treble_phrase_2.addNoteList(treble_pitch_4, treble_dur_4) # Measure 15
treble_phrase_2.addNoteList(treble_pitch_7, treble_dur_7) # Measure 16
treble_phrase_2.addNoteList(treble_pitch_8, treble_dur_8) # Measure 17
treble_phrase_2.addNoteList(treble_pitch_8, treble_dur_8) # Measure 18
treble_phrase_2.addNoteList(treble_pitch_4, treble_dur_4) # Measure 19

# Adds list of notes to phrase 3
treble_phrase_3.addNoteList(treble_pitch_5, treble_dur_5) # Measure 20

# Adds the end note to phrase 4
treble_phrase_4.addNote(treble_end_note)                  # Measure 21

# Repeats phrase 2
treble_phrase_repeat = treble_phrase_2.copy()             # Measures 5-19

#################################
### Add Notes to Bass Phrases ###
#################################

# Adds list of notes to phrase 1
bass_phrase_1.addNoteList(bass_pitch_1, bass_dur_1) # Measures 1-4

# Adds list of notes to phrase 2
bass_phrase_2.addNoteList(bass_pitch_2, bass_dur_2) # Measure 5
bass_phrase_2.addNoteList(bass_pitch_3, bass_dur_3) # Measure 6
bass_phrase_2.addNoteList(bass_pitch_4, bass_dur_4) # Measure 7
bass_phrase_2.addNoteList(bass_pitch_5, bass_dur_5) # Measure 8
bass_phrase_2.addNoteList(bass_pitch_2, bass_dur_2) # Measure 9
bass_phrase_2.addNoteList(bass_pitch_6, bass_dur_6) # Measures 10-12
bass_phrase_2.addNoteList(bass_pitch_2, bass_dur_2) # Measure 13
bass_phrase_2.addNoteList(bass_pitch_3, bass_dur_3) # Measure 14
bass_phrase_2.addNoteList(bass_pitch_4, bass_dur_4) # Measure 15
bass_phrase_2.addNoteList(bass_pitch_7, bass_dur_7) # Measures 16-18
bass_phrase_2.addNoteList(bass_pitch_4, bass_dur_4) # Measure 19

# Adds list of notes to phrase 3
bass_phrase_3.addNoteList(bass_pitch_8, bass_dur_8) # Measure 20

# Adds the end note to phrase 4
bass_phrase_4.addNoteList(bass_pitch_9, bass_dur_9) # Measure 21

# Repeats phrase 2
bass_phrase_repeat = bass_phrase_2.copy()           # Measures 5-19

###########################
### Arrange Treble Part ###
###########################

# Adds phrases to the treble part
treble_part.addPhrase(treble_phrase_1)
treble_part.addPhrase(treble_phrase_2)
treble_part.addPhrase(treble_phrase_3)
treble_part.addPhrase(treble_phrase_repeat)
treble_part.addPhrase(treble_phrase_4)

#########################
### Arrange Bass Part ###
#########################

# Adds phrases to the bass part
bass_part.addPhrase(bass_phrase_1)
bass_part.addPhrase(bass_phrase_2)
bass_part.addPhrase(bass_phrase_3)
bass_part.addPhrase(bass_phrase_repeat)
bass_part.addPhrase(bass_phrase_4)

##########################
### Finish Arrangement ###
##########################

# Adds parts to the score
the_entertainer_score.addPart(treble_part)
the_entertainer_score.addPart(bass_part)

# Writes to MIDI file
Write.midi(the_entertainer_score, "the_entertainer.midi")

# Plays the song
Play.midi(the_entertainer_score)