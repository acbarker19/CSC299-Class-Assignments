# HW2_TheEntertainer_AlecBarker.py
# January 31, 2020

# The Entertainer
# Composed by Scott Joplin
# Arranged by Hiroshi Yamazami
# Found at https://www.free-scores.com/download-sheet-music.php?pdf=27429
# Performed by Alec Barker

from music import *

####################
### Create Score ###
####################

the_entertainer_score = Score("The Entertainer - Easy", 180)   # Sets the
# title and the BPM

####################
### Create Parts ###
####################

treble_part = Part(HONKYTONK, 0)    # Plays the piano treble on channel 0
bass_part = Part(HONKYTONK, 1)      # Plays the piano bass on channel 1
snare_part = Part(0, 9)             # Plays the snare drum on channel 9
bd_part = Part(0, 9)                # Plays the bass drum on channel 9
hh_part = Part(0, 9)                # Plays the high hat on channel 9

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

snare_phrase_1 = Phrase()       # First snare phrase that plays once
snare_phrase_2 = Phrase()       # Second snare drum phrase that repeats

bd_phrase_1 = Phrase()          # First bass drum phrase that plays once
bd_phrase_2 = Phrase()          # Second bass drum phrase that repeats

hh_phrase_1 = Phrase()          # First high hat drum phrase that plays once
hh_phrase_2 = Phrase()          # Second high hat drum phrase that repeats

####################
### Measures 1-4 ###
### Treble/Bass/ ###
###  Percussion  ###
####################

# Measure         One
treble_pitch_1 = [[D6, D5], [E6, E5], [C6, C5], [A6, A4], [B6, B4],
#                 One
                  [G5, G4],
#                 Two
                  D5, E5, C5, A4, B4, G4,
#                 Three
                  D4, E4, C4, A3, B3, A3, AF3,
#                 Four
                  G3, REST, [G5, D5, B4, G4], D4, DS4]
                  
# Measure         One
treble_dur_1 =   [EN,       EN,       EN,       QN,       EN,
#                 One
                  QN,
#                 Two
                  EN, EN, EN, QN, EN, QN,
#                 Three
                  EN, EN, EN, QN, EN, EN, EN,
#                 Four
                  QN, QN,   QN,               EN, EN]

# Measure       One
bass_pitch_1 = [REST,
#               Two
                D4, E4, C4, A3, B3, G3,
#               Three
                D3, E3, C3, A2, B2, A2, AF2,
#               Four
                G2, REST, [G2, G1], [G3, B3]]

# Measure       One
bass_dur_1 =   [WN,
#               Two
                EN, EN, EN, QN, EN, QN,
#               Three
                EN, EN, EN, QN, EN, EN, EN,
#               Four
                QN, QN,   QN,       QN]
                
# Measure        One-Four
snare_pitch_1 = [SNR, REST,  SNR, REST,  SNR, REST,  SNR, REST,
                 SNR, SNR, SNR]

# Measure        One-Four
snare_dur_1 =   [QN,  HN+QN, QN,  HN+QN, QN,  HN+QN, QN,  QN,
                 QN,  EN,  EN]

# Measure     One-Four
bd_pitch_1 = [BDR, REST,  BDR, REST,  BDR, REST,  BDR, REST, BDR,
              REST, BDR, BDR, BDR, BDR]

# Measure     One-Four
bd_dur_1 =   [QN,  HN+QN, QN,  HN+QN, QN,  HN+QN, QN,  QN,   QN,
              QN,   EN,  EN,  EN,  EN]

# Measure     One-Four
hh_pitch_1 = [REST] * 4

# Measure     One-Four
hh_dur_1 =   [WN] * 4

#########################
### Measures 5, 9, 13 ###
###   Treble/Bass/    ###
###    Percussion     ###
#########################

# Measure         Five/Nine/Thirteen
treble_pitch_2 = [E4, C5, E4, C5, E4, C5]   

# Measure         Five/Nine/Thirteen
treble_dur_2 =   [EN, QN, EN, QN, EN, EN+HN]

# Measure       Five/Nine/Thirteen
bass_pitch_2 = [C3, [E3, G3], C3, [E3, BF3]]

# Measure       Five/Nine/Thirteen
bass_dur_2 =   [QN, QN,       QN, QN]

# Measure        Five/Nine/Thirteen
snare_pitch_2 = [SNR, REST, SNR, REST, SNR]

# Measure        Five/Nine/Thirteen
snare_dur_2 =   [EN,  QN,   EN,  QN,   EN+HN]

# Measure     Five/Nine/Thirteen
bd_pitch_2 = [BDR, BDR, BDR, BDR, BDR, BDR]

# Measure     Five/Nine/Thirteen
bd_dur_2 =   [EN,  QN,  EN,  QN,  EN,  EN+HN]

# Measure     Five/Nine/Thirteen
hh_pitch_2 = [REST, OHH, REST, OHH, REST, OHH]

# Measure     Five/Nine/Thirteen
hh_dur_2 =   [EN,   QN,  EN,   QN,  EN,   EN+HN]

######################
### Measures 6, 14 ###
###  Treble/Bass/  ###
###   Percussion   ###
######################

# Measure         Six/Fourteen
treble_pitch_3 = [REST, C5, D5, DS5]

# Measure         Six/Fourteen
treble_dur_3 =   [EN,   EN, EN, EN]

# Measure       Six/Fourteen
bass_pitch_3 = [F3, [A3, C4], E3, [G3, C4]]

# Measure       Six/Fourteen
bass_dur_3 =   [QN, QN,       QN, QN]

# Measure        Six/Fourteen
snare_pitch_3 = [REST, SNR, SNR, SNR]

# Measure        Six/Fourteen
snare_dur_3 =   [EN,   EN,  EN,  EN]

# Measure     Six/Fourteen
bd_pitch_3 = [REST, BDR, BDR, BDR]

# Measure     Six/Fourteen
bd_dur_3 =   [EN,   EN,  EN,  EN]

# Measure     Six/Fourteen
hh_pitch_3 = [REST]

# Measure     Six/Fourteen
hh_dur_3 =   [HN]

##########################
### Measures 7, 15, 19 ###
###    Treble/Bass/    ###
###     Percussion     ###
##########################

# Measure         Seven/Fifteen/Nineteen
treble_pitch_4 = [E5, C5, D5, E5, B4, D5]

# Measure         Seven/Fifteen/Nineteen
treble_dur_4 =   [EN, EN, EN, QN, EN, QN]

# Measure       Seven/Fifteen/Nineteen
bass_pitch_4 = [G2, [C3, E3], G2, [D3, F3]]

# Measure       Seven/Fifteen/Nineteen
bass_dur_4 =   [QN, QN,       QN, QN]

# Measure        Seven/Fifteen/Nineteen
snare_pitch_4 = [SNR, SNR, SNR, REST, SNR, SNR]

# Measure        Seven/Fifteen/Nineteen
snare_dur_4 =   [EN,  EN,  EN,  QN,   EN,  QN]

# Measure     Seven/Fifteen/Nineteen
bd_pitch_4 = [BDR, BDR, BDR, BDR, BDR, BDR]

# Measure     Seven/Fifteen/Nineteen
bd_dur_4 =   [EN,  EN,  EN,  QN,  EN,  QN]

# Measure     Seven/Fifteen/Nineteen
hh_pitch_4 = [REST,  OHH, REST]

# Measure     Seven/Fifteen/Nineteen
hh_dur_4 =   [EN+QN, QN,  EN+QN]

######################
### Measures 8, 20 ###
###  Treble Only/  ###
###   Percussion   ###
######################

# Measure         Eight/Twenty
treble_pitch_5 = [C5, REST, D4, DS4]

# Measure         Eight/Twenty
treble_dur_5 =   [HN, QN,   EN, EN]

# Measure        Eight/Twenty
snare_pitch_5 = [SNR, REST]

# Measure        Eight/Twenty
snare_dur_5 =   [HN,  HN]

# Measure     Eight/Twenty
bd_pitch_5 = [BDR, BDR, BDR, BDR]

# Measure     Eight/Twenty
bd_dur_5 =   [QN,  QN,  QN,  QN]

# Measure     Eight/Twenty
hh_pitch_5 = [REST, OHH, OHH, OHH]

# Measure     Eight/Twenty
hh_dur_5 =   [QN,   QN,  QN,  QN]

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

# Measure         Ten
treble_pitch_6 = [REST, A4, G4,
#                 Eleven
                  F4, A4, C5, E5, D5, C5, A4,
#                 Twelve
                  D5, REST, D4, DS4]

# Measure         Ten
treble_dur_6 =   [QN,   EN, EN,
#                 Eleven
                  EN, EN, EN, QN, EN, EN, EN,
#                 Twelve
                  HN, QN,   EN, EN]

# Measure       Ten
bass_pitch_6 = [F3, [A3, C4], E3, EF3,
#               Eleven
                D3, [FS3, A3], D3, [FS3, A3],
#               Twelve
                [G3, B3], G2, A2, B2]

# Measure       Ten
bass_dur_6 =   [QN, QN,       QN, QN,
#               Eleven
                QN, QN,        QN, QN,
#               Twelve
                QN,       QN, QN, QN]

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

# Measure       Sixteen
bass_pitch_7 = [[C3, E3], G2, [C3, E3], REST,
#               Seventeen
                C3, [E3, G3], BF2, [E3, G3],
#               Eighteen
                A2, [C3, E3], AS2, [C3, E3]]

# Measure       Sixteen
bass_dur_7 =   [QN,       QN, QN,       QN,
#               Seventeen
                QN, QN,       QN,  QN,
#               Eighteen
                QN, QN,       QN,  QN]

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

# Note won't accept two notes played together,
# so I had to create a NoteList below.

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

# Fades out the treble part at the end of the score
Mod.fadeOut(treble_phrase_4, 5)

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

##################################
### Add Notes to Snare Phrases ###
##################################

# Adds list of notes to phrase 1
snare_phrase_1.addNoteList(snare_pitch_1, snare_dur_1) # Measures 1-4

# Adds list of notes to phrase 2
snare_phrase_2.addNoteList(snare_pitch_2, snare_dur_2) # Measures 5
snare_phrase_2.addNoteList(snare_pitch_3, snare_dur_3) # Measure 6
snare_phrase_2.addNoteList(snare_pitch_4, snare_dur_4) # Measure 7
snare_phrase_2.addNoteList(snare_pitch_5, snare_dur_5) # Measure 8

# Add phrase that fades the snare in and out, as well as lower it an octave
snare_copy = snare_phrase_2.copy()
Mod.fadeOut(snare_copy, 5)
Mod.transpose(snare_copy, -12)
Mod.fadeIn(snare_phrase_1, 5)

######################################
### Add Notes to Bass Drum Phrases ###
######################################

# Adds list of notes to phrase 1
bd_phrase_1.addNoteList(bd_pitch_1, bd_dur_1) # Measures 1-4

# Adds list of notes to phrase 2
bd_phrase_2.addNoteList(bd_pitch_2, bd_dur_2) # Measure 5
bd_phrase_2.addNoteList(bd_pitch_3, bd_dur_3) # Measure 6
bd_phrase_2.addNoteList(bd_pitch_4, bd_dur_4) # Measure 7
bd_phrase_2.addNoteList(bd_pitch_5, bd_dur_5) # Measure 8

#####################################
### Add Notes to High Hat Phrases ###
#####################################

# Adds list of notes to phrase 1
hh_phrase_1.addNoteList(hh_pitch_1, hh_dur_1) # Measures 1-4

# Adds list of notes to phrase 2
hh_phrase_2.addNoteList(hh_pitch_2, hh_dur_2) # Measure 5
hh_phrase_2.addNoteList(hh_pitch_3, hh_dur_3) # Measure 6
hh_phrase_2.addNoteList(hh_pitch_4, hh_dur_4) # Measure 7
hh_phrase_2.addNoteList(hh_pitch_5, hh_dur_5) # Measure 8

# Adds phrase that randomizes the pitches of the high hat
hh_copy = hh_phrase_2.copy()
Mod.randomize(hh_copy, 5)

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

###############################
### Arrange Percussion Part ###
###############################

# Adds phrases to the percussion part
snare_part.addPhrase(snare_phrase_1)
snare_part.addPhrase(snare_phrase_2)
snare_part.addPhrase(snare_copy)

bd_part.addPhrase(bd_phrase_1)
bd_part.addPhrase(bd_phrase_2)

hh_part.addPhrase(hh_phrase_1)
hh_part.addPhrase(hh_phrase_2)
hh_part.addPhrase(hh_copy)

##########################
### Finish Arrangement ###
##########################

# Adds parts to the score
the_entertainer_score.addPart(treble_part)
the_entertainer_score.addPart(bass_part)
the_entertainer_score.addPart(snare_part)
the_entertainer_score.addPart(bd_part)
the_entertainer_score.addPart(hh_part)

# Writes to MIDI file
# Write.midi(the_entertainer_score, "the_entertainer.midi")

# Displays the notation
# View.notation(the_entertainer_score)

# Plays the song
Play.midi(the_entertainer_score)