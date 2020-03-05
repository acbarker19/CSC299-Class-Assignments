#########################################################
### Barker_Bohemian_Rhapsody.py                       ###
### March 4, 2020                                     ###
###                                                   ###
### Bohemian Rhapsody                                 ###
### Composed by Freddie Mercury                       ###
### Arranged by Unknown                               ###
### Found at http://www.musiclassroom.com/partitions/ ###
###      Queen_BohemianRhapsody.pdf                   ###
### Performed by Alec Barker                          ###
#########################################################

from music import *

####################
### Create Score ###
####################

bohemian_rhapsody_score = Score("Bohemian Rhapsody", 72)   # Sets the
# title and the BPM

####################
### Create Parts ###
####################

pt_part = Part(PIANO, 0)           # Piano Treble
pth_part = Part(PIANO, 0)          # Piano Treble High Notes
pb_part = Part(PIANO, 0)           # Piano Bass
b_part = Part(BASS, 1)             # Bass Guitar
v_part = Part(SOPRANO_SAX, 2)      # Main Vocals
bv1_part = Part(HALO, 3)           # Backup Vocals 1
bv2_part = Part(VOICE, 3)          # Backup Vocals 2
g6_part = Part(ELECTRIC_GUITAR, 4) # Guitar 6
g7_part = Part(STEEL_GUITAR, 4)    # Guitar 7
dl_part = Part(0, 9)               # Drums Low Notes
dh_part = Part(0, 9)               # Drums High Notes
bt_part = Part(BELL, 9)            # Bell Tree

######################
### Create Phrases ###
######################

# Ballad
pt_b_phrase_1 = Phrase()
pt_b_phrase_2 = Phrase()
pt_b_phrase_3 = Phrase()

pth_b_phrase_1 = Phrase()
pth_b_phrase_2 = Phrase()
pth_b_phrase_3 = Phrase()

pb_b_phrase_1 = Phrase()
pb_b_phrase_2 = Phrase()
pb_b_phrase_3 = Phrase()

b_b_phrase_1 = Phrase()
b_b_phrase_2 = Phrase()
b_b_phrase_3 = Phrase()

v_b_phrase = Phrase(8)         # Starts on measure 17

bv1_b_phrase = Phrase(106)     # Starts on measure 42

bv2_b_phrase = Phrase(106)     # Starts on measure 42

bt_b_phrase = Phrase(86)       # Starts on measure 37
Mod.elongate(bt_b_phrase, 0.5) # Changes the speed to be 2x faster

g6_b_phrase = Phrase(106)      # Starts on measure 42

g7_b_phrase = Phrase(106)      # Starts on measure 42

dl_b_phrase = Phrase(32)       # Starts on measure 23

dh_b_phrase = Phrase(32)       # Starts on measure 23

##################################################################
### Each pitch and duration below is set to be one measure per ###
### line unless noted in a comment or the line is indented     ###
### further than the others, which indicates it is a           ###
### continuation of the previous line.                         ###
##################################################################

###############################################
### Measures 15, 16, 17, 21, 33, 34, 35, 39 ###
###               Piano, Bass               ###
###############################################

pt_b_pit_1 = [[D4, BF3], F3, BF3, D4, G4, F3, F4, F3]
pt_b_dur_1 = [EN,        EN, EN,  EN, EN, EN, EN, EN]
                       
pth_b_pit_1 = [REST, G5, F5]
pth_b_dur_1 = [HN,   QN, QN]

pb_b_pit_1 = [[BF2, BF1]]
pb_b_dur_1 = [WN]

b_b_pit_1 = [BF2]
b_b_dur_1 = [WN]
             
###############################
### Measures 18, 22, 36, 40 ###
###       Piano, Bass       ###
###############################

pt_b_pit_2 = [[D4, BF3], G3, BF3, D4, A4, G3, G4, G3]
pt_b_dur_2 = [EN,        EN, EN,  EN, EN, EN, EN, EN]
                       
pth_b_pit_2 = [REST, A5, G5]
pth_b_dur_2 = [HN,   QN, QN]

pb_b_pit_2 = [[G2, G1]]
pb_b_dur_2 = [WN]

b_b_pit_2 = [G2]
b_b_dur_2 = [WN]

#############################
### Measures 19-20, 37-38 ###
###      Piano, Bass      ###
#############################

pt_b_pit_3 = [[EF4, C4], C4, EF4, G4, D5, C4, C5, C4,
              [G4, EF4], C4, EF4, G4, [A4, EF4, C4], EF4, F4, C5]
pt_b_dur_3 = [EN,        EN, EN,  EN, EN, EN, EN, EN,
              EN,        EN, EN,  EN, EN,            EN,  EN, EN]

pth_b_pit_3 = [REST, D6, C6,
               REST]
pth_b_dur_3 = [HN,   QN, QN,
               WN]
                 
pb_b_pit_3 = [[C3, C2],
              [C3, C2], [F3, F2]]
pb_b_dur_3 = [WN,
              HN,        HN]
              
b_b_pit_3 = [BF2,
             C3, F4]
b_b_dur_3 = [WN,
             HN, HN]

#############################
### Measures 23-27, 41-45 ###
###  Piano, Bass, Drums   ###
#############################

pt_b_pit_4 = [[G4, EF4], C4, EF4, G4, [EF4, B3], G4, [EF4, BF3], G4,
              [EF4, A3], A3, EF4, G4, [EF4, AF3], G4, [EF4, G3], G4,
              [G4, EF4], EF4, [EF5, BF4, G4], G4, [BF4, G4], EF4,
                  [F4, D4], BF3,
              [G4, EF4, C4], C4, EF4, G4, D5, C4, C5, C4,
              [AF4, F4], F4, [F5, C5, AF4], [C5, AF4, E4],
                  [C5, AF4, EF4], EF4, [C5, AF4, D4], D4]
pt_b_dur_4 = [EN] * 40

# Please Note: The square bracket on the right must be put on this
#              line to continue the variable assignment statement.
#              If you wish to have it on the next line, you must
#              put a \ at the end of the line so Python knows to
#              continue.
pth_b_pit_4 = [REST] * 3 + [   # 23-25
               REST, D6, C6,
               REST]
pth_b_dur_4 = [WN] * 3 + [     # 23-25
               HN,   QN, QN,
               WN]

pb_b_pit_4 = [[C3, C2], [B2, B1], [BF2, BF1],
              [A2, A1], [AF2, AF1], [G2, G1],
              [EF3, EF2], [D3, D2],
              [C3, C2],
              [F3, F2], [E3, E2], [EF3, EF2], [D3, D2]]
pb_b_dur_4 = [HN,        QN,       QN,
              HN,        QN,       QN,
              DHN,         QN,
              WN,
              DQN,       EN,       QN,         QN]

b_b_pit_4 = [C3, B2, BF2,
             A2, AF2, G2,
             EF3, D3,
             C3,
             F3,  E3, EF3, D3]
b_b_dur_4 = [HN, QN, QN,
             HN, QN,  QN,
             DHN, QN,
             WN,
             DQN, EN, QN,  QN]

dl_pattern = [BDR, SNR, BDR, BDR, SNR]

dl_b_pit_1 = [REST,
              SNR, REST] + dl_pattern + [   # 24-25
              BDR] + dl_pattern * 2         # 26-27
dl_b_dur_1 = [WN,
              QN,  DHN,
              QN,  QN,  EN,  EN,  QN,
              EN,  EN,  QN,  EN,  EN,  QN,
              QN,  QN,  EN,  EN,  QN]
             
dh_b_pit_1 = [REST] + [
              OHH] * 17 + [
              OHH] + [CHH] * 14 + [             # 25-26
              OHH, CHH, CHH] * 2
dh_b_dur_1 = [WN,
              QN] +         [0.1875] * 16 + [
              QN] +  [EN] * 14 + [              # 25-26
              QN,  EN,  EN] * 2

##########################
###   Measures 28-32   ###
### Piano, Bass, Drums ###
##########################

pt_b_pit_5 = [[F4, D4, BF3], [BF4, F4, D4], [D4, BF3], [AF4, D4, BF3],
              [G4, EF4], EF4, [EF5, BF4, G4], EF4, [F4, D4], D4,
                  [BF4, F4], D4,
              [G4, EF4], C4, [G4, EF4], C4, [EF4, CF4, AF3],
              [BF4, G4, EF4], EF4, G4, BF4,
              [C5, AF4], EF5, [BF4, G4], EF5, [A4, GF4], EF5,
                  [AF4, F4], EF5]
pt_b_dur_5 = [QN] * 4 + [
              EN] * 12 + [HN] + [             # 29-30
              EN] * 12                        # 31-32
              
pth_b_pit_5 = [REST,
               REST,
               REST,
               REST,
               REST]
pth_b_dur_5 = [WN,
               WN,
               HN,
               WN,
               WN]
               
pb_b_pit_5 = [[BF2, BF1]] * 12 + [
              [EF3, EF2], [D3, D2],
              [C3, C2], [AF2, AF1],
              [EF3, EF2]]                      # 31-32
pb_b_dur_5 = [EN, SN, SN] * 3 + [SN, SN, EN,
              HN,          HN,
              HN,        HN,
              HN+WN]                           # 31-32

b_b_pit_5 = [BF2] * 8 + [
             EF3, D3,
             C3, AF3,
             EF4,
             REST]
b_b_dur_5 = [QN+DEN, SN, DEN] + [SN] * 5 + [
             HN,  HN,
             HN, DQN+EN,
             HN,
             WN]
             
dl_b_pit_2 = [BDR, SNR, BDR, LTM] + [HFT] * 3 +       [LFT,
              BDR, SNR, BDR, BDR, BDR, SNR,
              BDR, BDR, SNR, BDR, REST,
              REST,
              REST]
dl_b_dur_2 = [QN,  QN,  EN,  EN] +  [(0.5 / 3)] * 3 + [EN,
              QN,  EN,  EN,  EN,  EN,  QN,
              EN,  EN,  QN,  QN,  QN,
              HN,
              WN]

dh_b_pit_2 = [CHH] * 5 +    [REST,
              OHH] + [CHH] * 6 + [
              OHH, CHH, CHH, OHH, REST,
              REST,
              REST]
dh_b_dur_2 = [EN] * 4 + [QN, QN,
              QN]  + [EN] * 6 + [
              QN,  EN,  EN,  QN,  QN,
              HN,
              WN]

###################
### Measure 46  ###
### Piano, Bass ###
###################

pt_b_pit_6 = [[D4, BF3, F3]] + [[F4, D4, BF3]] * 2 + [
                  [D4, BF3]] * 2 + [[AF4, D4, BF3]] * 3
pt_b_dur_6 = [DEN] +            [SN, DEN] * 2 + [
                                   SN, EN, EN+HN]

pb_b_pit_6 = [[BF2, BF1]] * 12
pb_b_dur_6 = [EN, SN, SN] * 3 + [SN, SN, EN+HN]

b_b_pit_6 = [BF2] * 12
b_b_dur_6 = [EN, SN, SN] * 3 + [ SN, SN, EN+HN]

######################
### Measures 33-46 ###
###   Drums Only   ###
######################

dl_b_pit_3 = [REST,
              REST] + dl_pattern + [                        # 34-35
              BDR] + dl_pattern + [
              BDR] + dl_pattern + [
              BDR] + dl_pattern + [
                  BDR] + dl_pattern * 3 + [                 # 38-41
              BDR, SNR, BDR, BDR, LTM, HFT, HFT, LFT] + \
              dl_pattern + [BDR] + dl_pattern + [BDR,       # 43-44
              BDR, BDR, BDR, BDR,
              BDR, BDR, SNR] + [LTM] * 11
dl_b_dur_3 = [WN,
              WN,
              QN,  QN,  EN,  EN,  QN] + [
              EN,  EN,  QN] * 5 + [EN,  EN,  EN,  EN] + [   # 36-38
              QN,  QN,  EN,  EN,  QN] * 2 + [               # 39-40
              QN,  EN,  EN,  QN,  QN,
              QN,  EN,  EN,  EN,  EN,  SN,  SN,  EN] + [
              QN,  QN,  EN,  EN,  EN,  EN] * 2 + [          # 43-44
              DQN, EN,  QN,  QN,
              EN,  EN,  EN] + [SN] * 8 + [0.125, 0.125, SN]

dh_b_pit_3 = [REST,
              REST,
              OHH] + [CHH] * 6 + [                   # 35
              CHH] * 8 + [
              CHH] * 8 + [
              OHH] + [CHH] * 6 + [
              OHH] + [CHH] * 6 + [
              OHH] + [CHH] * 7 + [                   # 40
              OHH, CHH, CHH, CHH, OHH, CHH, CHH,
              OHH, CHH, CHH, CHH, OHH, REST] + [
              OHH] + [CHH] * 6 + [
              OHH] + [CHH] * 6 + [
              OHH] * 4 + [                           # 45
              OHH, CHH, REST]
dh_b_dur_3 = [WN,
              WN,
              QN] + [EN] * 6 + [                     # 35
              EN] * 8 + [
              EN] * 8 + [
              QN] + [EN] * 6 + [
              QN] + [EN] * 6 + [
              EN] * 8 + [                            # 40
              EN] * 4 + [QN,  EN,  EN,
              EN,  EN,  EN,  EN,  QN,  QN,
              QN] + [EN] * 6 + [
              QN] + [EN] * 6 + [
              DQN, EN, QN, QN,                       # 45
              QN,  QN,  HN]

######################              
### Measures 17-47 ###
###  Vocals Only   ###
######################

v_b_pit = [D5, D5,     REST, BF4,
           C5, D5, D5,    REST, D5, D5,
           EF5, F5, EF5,   D5, C5,  REST, C5, D5,
           EF5, F5, EF5, D5, C5,    REST,                  # 20
           D5, D5,        REST, D5, F5,
           A5,  G5, G5, REST, G5,
           BF5, BF5, BF5, BF5, BF5, G5, EF5, D5,
           D5, C5,    REST,
           G5, G5,     F5, G5, AF5,                        # 25
           G5, REST, G5, G5,
           AF5, G5, G5, F5, F5, REST, BF4,
           BF4, F5, F5, G5, G5,  AF5, AF5, BF5, AF5,
           G5, REST, F5, G5, BF5, F5, G5,
           EF5, REST, BF4, BF4, CF5, DF5, CF5, DF5, CF5,   # 30
           BF4] + [
           REST] * 3 + [                                   # 32-34
           D5, D5,     REST, BF4,                          # 35
           C5, D5, D5,    REST,  D5,
           EF5, F5,  EF5, D5, C5,  REST, C5, D5,
           EF5, F5,  EF5, D5, D5, C5,    REST,
           D5, D5,     C5, BF4, C5, D5, REST, F5,
           A5,  G5, G5,  REST, F5, G5,                     # 40
           BF5, BF5, BF5, BF5, BF5, G5, EF5, D5,
           C5, C5,    REST,
           G5, G5,     F5, G5, AF5,
           G5,  REST,
           AF5, G5, G5, F5, F5,    REST, F5,               # 45
           BF4, F5, F5, G5, G5, AF5, AF5, AF5, BF5, AF5]
v_b_dur = [SN, DEN+HN, EN,   EN,
           EN, SN, SN+QN, DQN,  SN, SN,
           SN,  EN, SN+SN, EN, DEN, EN,   EN, EN,
           SN,  EN, EN,  EN, SN+QN, QN,                       # 20
           SN, DEN+QN+EN, EN,   EN, EN,
           DEN, SN, HN, EN,   EN,
           EN,  EN,  EN,  EN,  DEN, SN, DEN, SN,
           EN, EN+HN, QN,
           SN, DEN+HN, EN, SN, SN,                            # 25
           DHN, EN,   SN, SN,
           DEN, SN, EN, EN, QN, DEN,  SN,
           EN,  EN, EN, SN, DEN, EN,  EN,  SN,  DEN,
           EN, EN,   SN, SN, DQN, SN, SN,
           QN,  EN,   SN,  SN,  SN,  DEN, 0.33, 0.33, 0.34,   # 30
           HN] + [
           WN] * 3 + [                                        # 32-34
           SN, DEN+QN, DQN,  EN,                              # 35
           EN, SN, SN+QN, QN+EN, EN,
           DSN, DSN, EN,  EN, DEN, EN,   EN, EN,
           0.3, 0.3, 0.4, EN, SN, SN+QN, QN,
           SN, DEN+EN, SN, SN,  SN, SN, QN,   EN,
           DEN, SN, DQN, QN,   SN, SN,                        # 40
           EN,  EN,  EN,  SN,  QN,  SN, EN,  EN+SN,
           SN, EN+HN, QN,
           SN, DEN+HN, EN, SN, SN,
           DHN, QN,
           DEN, SN, SN, EN, SN+QN, DEN, SN,                   # 45
           EN,  EN, EN, EN, SN, SN,  EN,  EN,  SN,  SN]

######################
###   Measure 37   ###
### Bell Tree Only ###       
######################
   
bt_b_pit = [REST, EF6, D6, C6, BF6]
bt_b_dur = [1.25,  EN,  EN, EN, EN]

#########################################
###          Measures 42-46           ###
### Guitar 6 & 7, Backup Vocals 1 & 2 ###
#########################################

g_b_pit = [A3, AF3, G3,
           EF4, D4,
           C4,
           F4,  E4, EF4, D4,
           BF3]
g_b_dur = [HN, QN,  QN,
           DHN, QN,
           WN,
           DQN, EN, QN,  QN,
           WN]
           
bv1_b_pit = [REST,
             [EF6, G5], [BF5, F5],
             [G5, EF5], REST,
             [A5, F5], REST,
             [C5, C4], [BF4, BF3], [EF5, EF4], [D5, D4], [G5, G4],
                  [F5, F4], [C6, C5], [BF5, BF4]]
bv1_b_dur = [WN,
             DHN,       QN,
             DHN,       QN,
             DHN,      QN,
             EN,       EN,         EN,         EN,       EN,
                  EN,       EN,       EN]

bv2_b_pit = [REST,
             REST,
             C4, C4, EF4, G4, D5, C5]
bv2_b_dur = [WN,
             WN,
             EN, EN, EN,  EN, QN, QN]

##########################
### Arrange Note Lists ###
##########################

# Piano Treble
pt_b_phrase_1.addNoteList(pt_b_pit_1, pt_b_dur_1) # 15
Mod.repeat(pt_b_phrase_1, 3)                      # 16-17
pt_b_phrase_1.addNoteList(pt_b_pit_2, pt_b_dur_2) # 18
pt_b_phrase_1.addNoteList(pt_b_pit_3, pt_b_dur_3) # 19-20
pt_b_phrase_1.addNoteList(pt_b_pit_1, pt_b_dur_1) # 21
pt_b_phrase_1.addNoteList(pt_b_pit_2, pt_b_dur_2) # 22
pt_b_phrase_1.addNoteList(pt_b_pit_4, pt_b_dur_4) # 23-27
pt_b_phrase_2 = pt_b_phrase_1.copy()              # 33-45(Copy 15-27)
pt_b_phrase_1.addNoteList(pt_b_pit_5, pt_b_dur_5) # 28-32
pt_b_phrase_3.addNoteList(pt_b_pit_6, pt_b_dur_6) # 46
Mod.append(pt_b_phrase_2, pt_b_phrase_3)          # Combines 2 and 3
Mod.crescendo(pt_b_phrase_1, 0, 122, 100, 100)    # Set volume
Mod.crescendo(pt_b_phrase_2, 0, 122, 100, 100)    # Set volume

# Piano Treble High Notes
pth_b_phrase_1.addNoteList(pth_b_pit_1, pth_b_dur_1) # 15
Mod.repeat(pth_b_phrase_1, 3)                        # 16-17
pth_b_phrase_1.addNoteList(pth_b_pit_2, pth_b_dur_2) # 18
pth_b_phrase_1.addNoteList(pth_b_pit_3, pth_b_dur_3) # 19-20
pth_b_phrase_1.addNoteList(pth_b_pit_1, pth_b_dur_1) # 21
pth_b_phrase_1.addNoteList(pth_b_pit_2, pth_b_dur_2) # 22
pth_b_phrase_1.addNoteList(pth_b_pit_4, pth_b_dur_4) # 23-27
pth_b_phrase_2 = pth_b_phrase_1.copy()               # 33-45(Copy 15-27)
pth_b_phrase_1.addNoteList(pth_b_pit_5, pth_b_dur_5) # 28-32
Mod.crescendo(pth_b_phrase_1, 0, 122, 100, 100)      # Set volume
Mod.crescendo(pth_b_phrase_2, 0, 122, 100, 100)      # Set volume

# Piano Bass
pb_b_phrase_1.addNoteList(pb_b_pit_1, pb_b_dur_1)  # 15
Mod.repeat(pb_b_phrase_1, 3)                       # 16-17
pb_b_phrase_1.addNoteList(pb_b_pit_2, pb_b_dur_2)  # 18
pb_b_phrase_1.addNoteList(pb_b_pit_3, pb_b_dur_3)  # 19-20
pb_b_phrase_1.addNoteList(pb_b_pit_1, pb_b_dur_1)  # 21
pb_b_phrase_1.addNoteList(pb_b_pit_2, pb_b_dur_2)  # 22
pb_b_phrase_1.addNoteList(pb_b_pit_4, pb_b_dur_4)  # 23-27
pb_b_phrase_2 = pb_b_phrase_1.copy()               # 33-45(Copy 15-27)
pb_b_phrase_1.addNoteList(pb_b_pit_5, pb_b_dur_5)  # 28-32
pb_b_phrase_3.addNoteList(pb_b_pit_6 , pb_b_dur_6) # 46
Mod.append(pb_b_phrase_2, pb_b_phrase_3)           # Combines 2 and 3
Mod.crescendo(pb_b_phrase_1, 0, 122, 100, 100)     # Set volume
Mod.crescendo(pb_b_phrase_2, 0, 122, 100, 100)     # Set volume

# Piano Bass Accents
Mod.accent(pb_b_phrase_1, 4, [0, 4, 8, 12, 16, 20, 22, 24, 28, 32,
      34, 45, 36, 38, 39, 40, 43, 44, 48, 49.5, 50, 51, 52, 53, 54,
      55, 56, 58, 60, 62, 64], 1000) 
Mod.accent(pb_b_phrase_2, 4, [0, 4, 8, 12, 16, 20, 22, 24, 28, 32,
      34, 45, 36, 38, 39, 40, 43, 44, 48, 49.5, 50, 51, 52, 53, 54,
      55], 1000)

# Bass Guitar
b_b_phrase_1.addNoteList(b_b_pit_1, b_b_dur_1) # 15
Mod.repeat(b_b_phrase_1, 3)                    # 16-17
b_b_phrase_1.addNoteList(b_b_pit_2, b_b_dur_2) # 18
b_b_phrase_1.addNoteList(b_b_pit_3, b_b_dur_3) # 19-20
b_b_phrase_1.addNoteList(b_b_pit_1, b_b_dur_1) # 21
b_b_phrase_1.addNoteList(b_b_pit_2, b_b_dur_2) # 22
b_b_phrase_1.addNoteList(b_b_pit_4, b_b_dur_4) # 23-27
b_b_phrase_2 = b_b_phrase_1.copy()             # 33-45(Copy 15-27)
b_b_phrase_1.addNoteList(b_b_pit_5, b_b_dur_5) # 28-32
b_b_phrase_3.addNoteList(b_b_pit_6, b_b_dur_6) # 46
Mod.append(b_b_phrase_2, b_b_phrase_3)         # Combines 2 and 3
Mod.crescendo(b_b_phrase_1, 0, 122, 127, 127)  # Set volume
Mod.crescendo(b_b_phrase_2, 0, 122, 127, 127)  # Set volume

# Main Vocals
v_b_phrase.addNoteList(v_b_pit, v_b_dur)    # 15-46
v_b_phrase.addNote(G5, HN)                  # 47
Mod.crescendo(v_b_phrase, 0, 122, 105, 105) # Set volume
Mod.crescendo(v_b_phrase, 123, 125, 105, 0) # Set volume

# Backup Vocals 1
bv1_b_phrase.addNoteList(bv1_b_pit, bv1_b_dur) # 42-46
bv1_b_phrase.addNoteList([[EF6, G5]], [DHN])   # 47
Mod.crescendo(bv1_b_phrase, 0, 122, 50, 50)    # Set volume
Mod.crescendo(bv1_b_phrase, 123, 125.5, 50, 0) # Set volume

# Backup Vocals 2
bv2_b_phrase.addNoteList(bv2_b_pit, bv2_b_dur) # 42-46
Mod.crescendo(bv2_b_phrase, 0, 122, 75, 75)    # Set volume

# Bell Tree
bt_b_phrase.addNoteList(bt_b_pit, bt_b_dur)  # 37
Mod.crescendo(bt_b_phrase, 0, 122, 105, 105) # Set volume

# Guitar 6
g6_b_phrase.addNoteList(g_b_pit, g_b_dur)  # 42-46
Mod.crescendo(g6_b_phrase, 0, 122, 90, 90) # Set volume

# Guitar 7
g7_b_phrase.addNoteList(g_b_pit, g_b_dur)    # 42-46
Mod.crescendo(g7_b_phrase, 0, 122, 127, 127) # Set volume

# Drums High Notes
dl_b_phrase.addNoteList(dl_b_pit_1, dl_b_dur_1) # 23-27
dl_b_phrase.addNoteList(dl_b_pit_2, dl_b_dur_2) # 28-32
dl_b_phrase.addNoteList(dl_b_pit_3, dl_b_dur_3) # 33-46
Mod.crescendo(dl_b_phrase, 0, 122, 100, 100)    # Set volume

# Drums Low Notes
dh_b_phrase.addNoteList(dh_b_pit_1, dh_b_dur_1) # 23-27
dh_b_phrase.addNoteList(dh_b_pit_2, dh_b_dur_2) # 27-32
dh_b_phrase.addNoteList(dh_b_pit_3, dh_b_dur_3) # 33-46
Mod.crescendo(dh_b_phrase, 0, 122, 100, 100)    # Set volume

#####################
### Arrange Parts ###
#####################

# Ballad
pt_part.addPhrase(pt_b_phrase_1)
pt_part.addPhrase(pt_b_phrase_2)

pth_part.addPhrase(pth_b_phrase_1)
pth_part.addPhrase(pth_b_phrase_2)

pb_part.addPhrase(pb_b_phrase_1)
pb_part.addPhrase(pb_b_phrase_2)

b_part.addPhrase(b_b_phrase_1)
b_part.addPhrase(b_b_phrase_2)

v_part.addPhrase(v_b_phrase)

bv1_part.addPhrase(bv1_b_phrase)

bv2_part.addPhrase(bv2_b_phrase)

bt_part.addPhrase(bt_b_phrase)

g6_part.addPhrase(g6_b_phrase)

g7_part.addPhrase(g6_b_phrase)

dl_part.addPhrase(dl_b_phrase)

dh_part.addPhrase(dh_b_phrase)

#####################
### Arrange Score ###
#####################

bohemian_rhapsody_score.addPart(pt_part)
bohemian_rhapsody_score.addPart(pth_part)
bohemian_rhapsody_score.addPart(pb_part)
bohemian_rhapsody_score.addPart(b_part)
bohemian_rhapsody_score.addPart(v_part)
bohemian_rhapsody_score.addPart(bv1_part)
bohemian_rhapsody_score.addPart(bv2_part)
bohemian_rhapsody_score.addPart(bt_part)
bohemian_rhapsody_score.addPart(g6_part)
bohemian_rhapsody_score.addPart(g7_part)
bohemian_rhapsody_score.addPart(dl_part)
bohemian_rhapsody_score.addPart(dh_part)

# Writes to MIDI file
Write.midi(bohemian_rhapsody_score, "barker_bohemian_rhapsody.midi")

# Displays the notation
View.notation(bohemian_rhapsody_score)

Play.midi(bohemian_rhapsody_score)