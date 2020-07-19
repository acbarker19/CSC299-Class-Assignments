# 06-02-1-Mozart.MusicalischesWurfelspiel.py
#
# This program generates an excerpt of Mozart's "Musikalisches Wurfelspiel" 
# (aka Mozart's Dice Game). It demonstrates how randomness may be sieved 
# (harnessed) to produce aesthetic results.  
# Making Music with Computers, pg. 157-159
# 
# See Schwanauer, S, and D Levitt. 1993. Appendix pg. 533-538
#
# The original has 16 measures with 11 choices per measure.  This excerpt is
# a simplified form.  In this excerpt, musical material is selected from this matrix:
#
# Dice  1     2    3     4    5   6    7    8     9    10   11   12   13   14   15   16
# --------------------------------------------------------------------------------------
#  2    96    22   141   41   105 #    11   30    70   121  26   9    112  49   #    #
#  3    32    6    128   63   #   46   134  81    117  #    126  #    174  #    #    #
#  4    69    95   158   13   153 55   #    24    66   #    15   #    #    #    145  #
#  5    40    17   113   85   161 2    159  100   90   176  #    34   67   160  #    #
#  6    148   74   #     45   #   97   #    107   25   #    #    125  #    #    #    #
#  7    104   157  27    167  154 68   118  91    #    71   #    29   #    #    23   #
#  8    152   60   171   #    #   133  21   #     #    155  57   175  43   168  89   #
#  9    119   #    114   50   140 86   169  #     120  88   #    166  51   #    #    #
# 10    98    142  42    #    75  129  62   #     #    #    #    82   137  38   #    #
# 11    #     87   165   61   135 47   #    33    #    #    31   #    144  59   173  #
# 12    54    130  10    103  28  37   #    5     #    #    108  #    #    #    44   #
#
# Columns represent alternatives for a measure.  The composer throws dice to select
# an alternative (choice) from first column.  Then, connects it with the choice from 
# second column, and so on.

from music import *
from random import *

# musical data structure
walzerteil = Part()     # contains a four-measure motif gnerated randomly from the
                        # matrix above
                            
###  measure 1 - create alternatives
# choice 96
pitches96     = [[C3, E5], C5, G4]
durations96   = [ EN,      EN, EN]
choice96 = Phrase()
choice96.addNoteList(pitches96, durations96)

# choice 32
pitches32     = [[C3, E3, G4], C5, E5]
durations32   = [ EN,          EN, EN]
choice32 = Phrase()
choice32.addNoteList(pitches32, durations32)

# choice 69
pitches69     = [[C3, E3, G5], E5, B4]
durations69   = [ EN,          EN, EN]
choice69 = Phrase()
choice69.addNoteList(pitches69, durations69)

# choice 40
pitches40     = [[C3, E3, C5], B4, C5, E5, G4, C5]
durations40   = [ SN,          SN, SN, SN, SN, SN]
choice40 = Phrase()
choice40.addNoteList(pitches40, durations40)

# choice 148
pitches148     = [[C6, E3, C3], B5, C6, G5, E5, C5]
durations148   = [ SN,          SN, SN, SN, SN, SN]
choice148 = Phrase()
choice148.addNoteList(pitches148, durations148)

# choice 104 18F-KB
pitches104   = [[C3, E5], D5, E5, G5, C6, G5]
durations104 = [SN,       SN, SN, SN, SN, SN]
choice104 = Phrase()
choice104.addNoteList(pitches104, durations104)

# choice 152 18F-JC
pitches152     = [G5, F5, E5, G5, D5, C5]
durations152   = [EN, SN, SN, SN, SN, SN]
choice152 = Phrase()
choice152.addNoteList(pitches152, durations152) 

# choice 119 19S-RB
pitches119     = [[E5, E3, C3], C5, G5, E5, C5, G5]
durations119   = [          .5, .5, .5, .5, .5, .5]
choice119 = Phrase()
choice119.addNoteList(pitches119, durations119)

#choice 98 18F-ZC
pitches98 = [C5, G4, E5]
durations98 = [EN, EN, EN]
choice98 = Phrase()
choice98.addNoteList(pitches98, durations98)

# choice 54  18F-STUDENT
pitches54      = [[E4, C5], [E4, C5], [E4, C5]]
durations54    = [   0.3,      0.3,      0.3]
choice54 = Phrase()
choice54.addNoteList(pitches54, durations54)
                            
#####  measure 2 - create alternatives

###################
### Alec Barker ###
### Measure 84  ###
###################

# choice 84 20S-AB
pitches84     = [[C5,E3,C3], [G4,E3,C3], [E5,E3,C3], [C5,E3,C3], G5, E5]
durations84   = [ SN,         SN,         SN,         SN,        SN, SN]
choice84      = Phrase()
choice84.addNoteList(pitches84, durations84)

######################
### End of Measure ###
######################

# choice 22
pitches22     = [[E5, C3], C5, G4]
durations22   = [ EN,      EN, EN]
choice22 = Phrase()
choice22.addNoteList(pitches22, durations22)

# choice 6 (same as choice 32)
pitches6     = [[C3, E3, G4], C5, E5]
durations6   = [ EN,          EN, EN]
choice6 = Phrase()
choice6.addNoteList(pitches6, durations6)

# choice 95
pitches95     = [[G5, C3, E3], E5, C5]
durations95   = [ EN,          EN, EN]
choice95 = Phrase()
choice95.addNoteList(pitches95, durations95)

# choice 17
pitches17     = [[E3, G3, C5], G4, C5, E5, G4, C5]
durations17   = [ SN,          SN, SN, SN, SN, SN]
choice17 = Phrase()
choice17.addNoteList(pitches17, durations17)

# choice 74 
pitches74     = [[D5, E3, C2], B5, C5, G4, E4, C4]
durations74   = [ SN,          SN, SN, SN, SN, SN]
choice74 = Phrase() 
choice74.addNoteList(pitches74, durations74)

# choice 157 18F-IE
pitches157    = [[E5, C2],  D5,   E5,   G5,   C6,   G5]
durations157  = [    0.25, 0.25, 0.25, 0.25, 0.25, 0.25]
choice157 = Phrase()
choice157.addNoteList(pitches157, durations157)

#choice 60  18F-ZC
pitches60      = [G5, F5, E5, D5, C5]
durations60    = [QN, QN, QN, QN, QN]
choice60 = Phrase()
choice60.addNoteList(pitches60, durations60)

# choice 142  18F-MH
pitches142     = [[C3, E3, C5], G4, E5]
durations142   = [QN,           QN, QN]
choice142 = Phrase()
choice142.addNoteList(pitches142, durations142)

# choice 87  19S-DC
pitches87   = [[G5,E3,C3], C5, [E5,G3,C3]]
durations87 = [ EN,        EN,  EN ]
choice87 = Phrase()
choice87.addNoteList(pitches87, durations87)

# choice 130 18F-ML
pitches130     = [[E3,C4,C2], [E3,C4,C2], [E3,C4,C2] ]
durations130   = [  EN,        EN,         EN  ]
choice130 = Phrase()
choice130.addNoteList(pitches130, durations130)
                            
#####  measure 3 - create alternatives
# choice 141
pitches141     = [[B2, G3, D5], E5, F5, D5, [G2, C5], B4]
durations141   = [ SN,          SN, SN, SN,  SN,      SN]
choice141 = Phrase()
choice141.addNoteList(pitches141, durations141)

# choice 128
pitches128     = [[G2, B4], D4, G4]
durations128   = [ EN,      EN, EN]
choice128 = Phrase()
choice128.addNoteList(pitches128, durations128)

# choice 158
pitches158     = [[G2, B4], D5, B4, A4, G4]
durations158   = [ EN,      SN, SN, SN, SN]
choice158 = Phrase()
choice158.addNoteList(pitches158, durations158)
  
# choice 113
pitches113     = [[G3, B3, F5], D5, B4]
durations113   = [ EN,          EN, EN]
choice113 = Phrase()
choice113.addNoteList(pitches113, durations113)

# choice 27  18F-STUDENT
pitches27   = [[G3,B3,F5], E5, F5, D5, C5, B4]
durations27 = [        SN, SN, SN, SN, SN, SN]
choice27 = Phrase()
choice27.addNoteList(pitches27, durations27)

# choice 171
pitches171   = [[G2, G3, B4], C5, D5, E5, [B2, G3, F5], D5]
durations171 = [ SN,          SN, SN, SN,  SN,          SN]
choice171 = Phrase()
choice171.addNoteList(pitches171, durations171)

# choice 114  19S-TD
pitches114     = [[D5, B4, G3], [D5, B4, G3], [D5, B4, G3]]
durations114   = [1.0,      1.0,      1.0]
choice114 = Phrase()
choice114.addNoteList(pitches114, durations114)

#choice42  18F-SS
pitches42 = [B4, C5, D5, B4, A4, G4] 
durations42 = [EN, EN, EN, EN, EN, EN]
choice42 = Phrase()
choice42.addNoteList(pitches42, durations42)

# choice 165 19S-KF
pitches165   = [[D5, B2], [B4, B2], G4]      # Treble and Bass piches are merged
durations165 = [ EN,       EN,      EN]
choice165 = Phrase()
choice165.addNoteList(pitches165, durations165)

# choice 10 19S-BG
pitches10   = [[G3, B4], A4, B4, C5, D5, B4]
durations10 = [SN,       SN, SN, SN, SN, SN]
choice10 = Phrase()
choice10.addNoteList(pitches10, durations10)
           
#####  measure 4 - create alternatives

###################
### Alec Barker ###
### Measure 156 ###
###################

# choice 156 20S-AB
pitches156     = [[C5,E3,C3], [G4,E3,C3], [E5,E3,C3], [C5,E3,C3], G5]
durations156   = [ SN,         SN,         SN,         SN,        EN]
choice156      = Phrase()
choice156.addNoteList(pitches156, durations156)

######################
### End of Measure ###
######################

# choice 41
pitches41     = [[C3, E3, C5], B4, C5, E5, G4]
durations41   = [ SN,          SN, SN, SN, EN]
choice41 = Phrase()
choice41.addNoteList(pitches41, durations41)

# choice 63
pitches63     = [[C3, E5], C5, B4, C5, G4]
durations63   = [ SN,      SN, SN, SN, EN]
choice63 = Phrase()
choice63.addNoteList(pitches63, durations63)

# choice 13
pitches13     = [[C5, G3, E3], G4, E4]
durations13   = [ EN,          EN, EN]
choice13 = Phrase()
choice13.addNoteList(pitches13, durations13)

# choice 85
pitches85     = [[E3, G3, C5], E5, B4]
durations85   = [ EN,          EN, EN]
choice85 = Phrase()
choice85.addNoteList(pitches85, durations85)

# choice 45 18F-KB
pitches45   = [[E3, G3, C5], B4, C5, G4, E4, C4]
durations45 = [SN, SN, SN, SN, SN, SN]
choice45 = Phrase()
choice45.addNoteList(pitches45, durations45)

# choice 167 18F-JC
pitches167    = [C5, C5, D5, E5]
durations167  = [EN, SN, SN, EN]
choice167 = Phrase()
choice167.addNoteList(pitches167, durations167)

#choice 50 18F-ZC
pitches50  = [C5, E5, C5,G4]
durations50 = [EN, SN, SN, EN]
choice50 = Phrase()
choice50.addNoteList(pitches50, durations50)

# choice 61  18F-STUDENT
pitches61     = [C5,  E5,  C5,  G4]
durations61   = [QN,  EN,  EN,  QN]
choice61 = Phrase()
choice61.addNoteList(pitches61, durations61)

# choice 103 
pitches103    = [[C4, G3, E3], E4, C4, A3, E3]
durations103  = [ SN,          SN, SN, SN, EN]
choice103 = Phrase() 
choice103.addNoteList(pitches103, durations103)

##### measure 5 - create alternatives
# choice 105 18F-IE
pitches105    = [[FF5, C2],   A5,   F5,   D5,   F5]
durations105  = [      0.5, 0.25, 0.25, 0.25, 0.25]
choice105 = Phrase()
choice105.addNoteList(pitches105, durations105)

#choice 153   19S-LK
pitches153   = [D5, A4, F5, D5, A5, F5]
durations153 = [SN, SN, SN, SN, SN, SN]
choice153 = Phrase()
choice153.addNoteList(pitches153, durations153)

# choice 161  18F-MH
pitches161     = [[C3, F4, C5], [C3, F4, C5], [C3, F4, C5]]
durations161   = [ EN,           EN,           EN ]
choice161 = Phrase()
choice161.addNoteList(pitches161, durations161)

# choice 154 18F-ML
pitches154     = [[D4,C3] , CS4, D4, FS4, A4, FS4]
durations154   = [ SN,      SN,  SN, SN,  SN, SN, ]
choice154 = Phrase()
choice154.addNoteList(pitches154, durations154)

# choice 140  18F-STUDENT
pitches140   = [[C3,FS3,A4], [C3,FS3,A4], D5, [C3,A3,FS5]]
durations140 = [         EN,          SN, SN,          EN]
choice140 = Phrase()
choice140.addNoteList(pitches140, durations140)

# choice 75
pitches75   = [[C3, D5, FS5], [C3, D5, FS5], [C3, D5, FS5]]
durations75 = [ QN,            QN,            QN          ]
choice75 = Phrase()
choice75.addNoteList(pitches75, durations75)

# choice 135
pitches135     = [FS5, F5, D5, A5]
durations135   = [EN,  SN, SN, EN]
choice135 = Phrase()
choice135.addNoteList(pitches135, durations135)

# choice 28  18F-SS
pitches28 = [FS5, D5, C5, A5, FS5, D5]
durations28 = [EN, EN, EN, EN, EN, EN]
choice28 = Phrase()
choice28.addNoteList(pitches42, durations42)

##### measure 6 - create alternatives 

###################
### Alec Barker ###
### Measure 122 ###
###################

# choice 122 20S-AB      122 was listed as available, but I saw one already made when I came to post it here.
#                        Mine is different, so I'm leaving it here as another option.
pitches122     = [[G5, D3, B2], [FS5, D3, B2], [G5, D3, B2], [B5, D3, B2], [D5, D3, B2]]
durations122   = [ SN,           SN,            SN,           SN,           EN]
choice122      = Phrase()
choice122.addNoteList(pitches122, durations122)

######################
### End of Measure ###
######################

# choice 122 19S-AL
pitches122   = [[G5, B2, D3], FS5, [G5, B2, D3], B5, [D5, B2, D3]]
durations122 = [SN,            SN,       SN,     SN,     EN]
choice122 = Phrase()
choice122.addNoteList(pitches122, durations122)

# choice 46 19S-NM
pitches46     = [[G4, B3, D3], B4, G4, D4, B4]
durations46   = [ EN,          SN, SN, SN, SN]
choice46 = Phrase()
choice46.addNoteList(pitches46, durations46)

# choice 55 18F-KB
pitches55   = [[B2, D3, G5], B5, D5]
durations55 = [EN, EN, EN]
choice55 = Phrase()
choice55.addNoteList(pitches55, durations55)

#choice 2 18F-JC
pitches2      = [A4, FS4, G4, B4, G5]
durations2    = [EN, SN,  SN, SN, SN]
choice2   = Phrase()
choice2.addNoteList(pitches2,durations2)

#choice 97    19S-LM
pitches97   = [G5,  FS4, G5,  D5,  B4,  G4]
durations97 = [.25, .25, .25, .25, .25, .25]
choice97    = Phrase()
choice97.addNoteList(pitches97, durations97)

# choice 68    19S-LP
pitches68    = [[B2,G5], B5,  G5,  D5,  G5]
durations68  = [   .5  , .25, .25, .25, .25]
choice68     = Phrase()
choice68.addNoteList(pitches68, durations68)

# choice 133  19S-JP
pitches133    = [[D5, B2, G3], G5, D5, B4, D5]
durations133  = [ EN,          SN, SN, SN, SN]
choice133 = Phrase()
choice133.addNoteList(pitches133, durations133)

#choice 86  18F-STUDENT
pitches86    = [C5,  D5,  G5,  B5]
durations86  = [QN,  EN,  EN,  QN]
choice86 = Phrase()
choice86.addNoteList(pitches86, durations86)

# choice 129 
pitches129    = [[A4, D2, B2], G4, [FS4, D2, B2], G4, [D4, G3, B2]] 
durations129  = [ SN,          SN,   SN,          SN,  EN]
choice129 = Phrase() 
choice129.addNoteList(pitches129, durations129)

# choice 47 18F-IE
pitches47    = [[G5, B2, D3],   G5,   D5,  B5]
durations47  = [         0.5, 0.25, 0.25, 0.5]
choice47 = Phrase()
choice47.addNoteList(pitches47, durations47)

# choice 37  18F-ZC
pitches37      = [G5, B5, G5, D5, B4]
durations37    = [QN, QN, QN, QN, QN]
choice37 = Phrase()
choice37.addNoteList(pitches37, durations37)

##### measure 7 - create alternatives

# choice 11 19S-TP
pitches11   = [E5, C5, B4, A4, G4, FS4]
durations11 = [SN, SN, SN, SN, SN, SN]
choice11 = Phrase()
choice11.addNoteList(pitches11, durations11) 

# choice 134  18F-MH
pitches134     = [[C3, A4], E5, [D3, D5, B4], [A4, C5], [D2, G4, B4], [FS4, AS4]]
durations134   = [ EN,      EN,  EN,           EN,       EN,           EN   ]
choice134 = Phrase()
choice134.addNoteList(pitches134, durations134)

# choice 159 18F-ML
pitches159     = [[E4,C3], G4, [D4,D3], C4, [B3,D2], A3]
durations159   = [ SN,     SN,  SN,     SN,  SN,     SN]
choice159 = Phrase()
choice159.addNoteList(pitches159, durations159)

#choice 118  18F-STUDENT
pitches118   = [[C3,E5], A5, [D3,G5], B5, [D2,FS5], A5]
durations118 = [     SN, SN,      SN, SN,       SN, SN]
choice118 = Phrase()
choice118.addNoteList(pitches118, durations118)

# choice 21 19S-BS
pitches21     = [[C5,C3], E5, [G5,D3], D5, [A4,D2], FS5]
durations21   = [ SN,     SN,  SN,     SN,  SN,     SN]
choice21 = Phrase()
choice21.addNoteList(pitches21, durations21)

# choice 169
pitches169     = [E5, G5, D5, G5, A4, FS5]
durations169   = [SN, SN, SN, SN, SN, SN ]
choice169 = Phrase()
choice169.addNoteList(pitches169, durations169)

# choice 62  18F-SS
pitches62 = [E5, C5, B4, G4, A4, FS4]
durations62 = [EN, EN, EN, EN, EN, EN]
choice62 = Phrase()
choice62.addNoteList(pitches62, durations62)

##### measure 8 - create alternatives
# choice 30
pitches30     = [[C5,G4,E4,C4,C2]]
durations30   = [ DQN ]
choice30 = Phrase()
choice30.addNoteList(pitches30, durations30)

# choice 81
pitches81     = [[C2,C5,G4,E4,C4], [G2,B4], [C2,E4,C5]]
durations81   = [ SN,               SN,      QN ]
choice81 = Phrase()
choice81.addNoteList(pitches81, durations81)

# choice 24
pitches24     = [[C2,C5,G4,E4,C4], [G2,B4], [C2,E4,C5]]
durations24   = [ SN,               SN,      QN]
choice24 = Phrase()
choice24.addNoteList(pitches24, durations24)

# choice 100
pitches100     = [[C2,C5,G4,E4,C4], [G2,B4], [C2,E4,C5]]
durations100   = [ SN,               SN,      QN ]
choice100 = Phrase()
choice100.addNoteList(pitches100, durations100)

# choice 107     19S-PZ
pitches107     = [[G5,D5,B4,G4], REST]
durations107   = [ 1,            .5]
choice107 = Phrase()
choice107.addNoteList(pitches107, durations107)

# choice 91 19S-RB
pitches91     = [[G5,D5,B4,G4,G2], [B3,G3], [G3,F3], [FS3,E3], [E3,D3]]
durations91   = [ 1,                .5,      .5,      .5,       .5]
choice91 = Phrase()
choice91.addNoteList(pitches91, durations91)

# choice 33  19S-DC
pitches33   = [[G4,B4,D5,G5,G2], [G3,B3], [G3,F3], [FS3,E3], [E3,D3]]
durations33 = [ EN,               SN,      SN,      SN,       SN]
choice33 = Phrase()
choice33.addNoteList(pitches33, durations33)

# choice 5
pitches5     = [[C2,C5,G4,E4,C4], [G2,B4], [C2,E4,C5]]
durations5   = [ SN,               SN,      QN]
choice5 = Phrase()
choice5.addNoteList(pitches5, durations5)

##### measure 9 - create alternatives

# choice 70 19S-NM
pitches70     = [[FS4,D3], A4, FS4, [D4,C3], FS4]
durations70   = [ EN,      SN, SN,   SN,     SN]
choice70 = Phrase()
choice70.addNoteList(pitches70, durations70)

# choice 117   19S-LM
pitches117   = [D5,  A4,  D5,  FS5, A5,  F5]
durations117 = [.25, .25, .25, .25, .25, .25]
choice117    = Phrase()
choice117.addNoteList(pitches117, durations117)

# choice 66    19S-LP
pitches66    = [[D3,A3,FS5], [D3,FS3,A5], [C3,D3,FS5]]
durations66  = [ .5,          .5,          .5]
choice66     = Phrase()
choice66.addNoteList(pitches66, durations66)

# choice 90  19S-JP
pitches90     = [[C3,A3,FS5], A5, D6, A5, FS5, A5]
durations90   = [ SN,         SN, SN, SN,  SN, SN]
choice90 = Phrase()
choice90.addNoteList(pitches90, durations90)  

# choice 25  19S-TP                                                                              
pitches25   = [D4, FS4, A4, D5, FS5, A5]
durations25 = [SN, SN,  SN, SN, SN,  SN]
choice25 = Phrase()
choice25.addNoteList(pitches25, durations25)

# choice 120 19S-BS
pitches120     = [[D6,FS3,D3], A5, FS5, [D5,FS3,C3], A4]
durations120   = [ EN,         SN, SN,   SN,         SN]
choice120 = Phrase()
choice120.addNoteList(pitches120, durations120)


##### measure 10 - create alternatives

# choice 121 19S-RB
pitches121     = [[G5,G3,B2], B5, G5, D5]
durations121   = [ 1,         .5, .5,  1]
choice121 = Phrase()
choice121.addNoteList(pitches121, durations121)

# choice 176
pitches176   = [[B3,D3,A5], G5, B5, G5, [D5,B3,D3], G5]
durations176 = [ SN,        SN, SN, SN,  SN,        SN]
choice176 = Phrase()
choice176.addNoteList(pitches176, durations176)

# choice 71  19S-TD
pitches71     = [[G5,D3,B2], [B5,D3,B2], [D6,D3,B2], [B5,D3,B2], [G5,D3,B2]]
durations71   = [0.5,         0.5,        0.5,        0.5,        1.0]
choice71 = Phrase()
choice71.addNoteList(pitches71, durations71)

# choice 155 19S-KF              # Treble and Bass piches are merged
pitches155   = [[G5,D3,B2], [B5,D3,B2], [G5,D3,B2], [D5,D3,B2], B4, G4]
durations155 = [ SN,         SN,         SN,         SN,        SN, SN]
choice155 = Phrase()
choice155.addNoteList(pitches155, durations155)

# choice 88 19S-BG
pitches88   = [[D3,B2,G5], D5, G5, B5, [D3,B2,G5], D5]
durations88 = [ SN,        SN, SN, SN,  SN,        SN]
choice88 = Phrase()
choice88.addNoteList(pitches88, durations88)


##### measure 11 - create alternatives

# choice 26  19S-TD
pitches26     = [[C3,E5,C5], [E3,E5,C5], [F3,E5,C5], [E3,E5,C5], [C4,E5,C5], [C3,E5,C5]]
durations26   = [ 0.5,        0.5,        0.5,        0.5,        0.5,        0.5]
choice26 = Phrase()
choice26.addNoteList(pitches26, durations26)

# choice 126 19S-KF               # Treble and Bass piches are merged
pitches126   = [[C5, E3], [G4,E3], [C5,E3], [E5,E3], [G5,E3], [E5,C5,C3]]     
durations126 = [ SN,       SN,      SN,      SN,      SN,      SN]
choice126 = Phrase()
choice126.addNoteList(pitches126, durations126)

# choice 15 19S-BG
pitches15   = [[G3,C3,E5], G5, E5, [E3,C3,C5]]
durations15 = [ EN,        SN, SN,  EN]
choice15 = Phrase()
choice15.addNoteList(pitches15, durations15)

# choice 57   19S-LK
pitches57   = [E5, C5, G4]
durations57 = [EN, EN, EN]
choice57 = Phrase()
choice57.addNoteList(pitches57, durations57)

# choice 31
pitches31   = [[C3,G3,E5], C5, G4, [C3,G3,E5]]
durations31 = [ SN,        SN, EN,  EN         ]
choice31 = Phrase()
choice31.addNoteList(pitches31, durations31)

# choice 108 19S-AL
pitches108  =  [[E5,G3,C3], G5, [C6,E3,C3]]
durations108 = [ EN,        EN,  EN]
choice108 = Phrase()
choice108.addNoteList(pitches108, durations108)   

##### measure 12 - create alternatives

###################
### Alec Barker ###
### Measure 56  ###
###################

# choice 56 20S-AB
pitches56     = [[D5, G3, G2], [B4, G3, G2], [G4, G3, G2], G3]
durations56   = [ SN,           SN,           EN,          EN]
choice56      = Phrase()
choice56.addNoteList(pitches56, durations56)

######################
### End of Measure ###
######################

# choice 9  19S-LK
pitches9   = [[E5,C5], [D5,B4], REST]
durations9 = [ EN,      EN,     EN ]
choice9 = Phrase()
choice9.addNoteList(pitches9, durations9)

# choice 34 19S-AL
pitches34 =   [[E5,G3], C5, D5, B4, G4]
durations34 = [ SN,     SN, SN, SN, SN]
choice34 = Phrase()
choice34.addNoteList(pitches34, durations34) 

# choice 125 19S-NM
pitches125     = [[G4,G3], E4, [D4,G2], D4, G3]
durations125   = [ SN,     SN,  SN,     SN, EN]
choice125 = Phrase()
choice125.addNoteList(pitches125, durations125)

# choice 29   19S-LM
pitches29   = [B4,  D5,  G5,  D5,  B4]
durations29 = [.25, .25, .25, .25, .5]
choice29    = Phrase()
choice29.addNoteList(pitches29, durations29)

# choice 175   19S-LP
pitches175    = [[G3,E5], C5, [G2,B4], D5,  G5]
durations175  = [  .25,   .25,   .25,  .25, .5]
choice175     = Phrase()
choice175.addNoteList(pitches175, durations175)

# choice 166  19S-JP
pitches166     = [[G3,B3,D5], B5, G5, D5, B4]
durations166   = [ SN,        SN, SN, SN, EN]
choice166 = Phrase()
choice166.addNoteList(pitches166, durations166)

# choice 82   19S-TP
pitches82   = [D5, B4, G4, G5]
durations82 = [SN, SN, EN, EN]
choice82 = Phrase()
choice82.addNoteList(pitches82, durations82)

##### measure 13 - create alternatives

# choice 112 19S-BS
pitches112     = [[E5,E3,C3], G3, [C5,E3,C3], G3, [G4,E3,C3], G3]
durations112   = [ SN,        SN,  SN,        SN,  SN,        SN]
choice112 = Phrase()
choice112.addNoteList(pitches112, durations112)

# choice 174 19S-KF        # Treble and Bass piches are merged
pitches174   = [[E3,C3,G4], [G3,G4], [E3,C3,C5], [G3,C5], [E3,C3,E5], [G3,E5]]
durations174 = [ SN,         SN,      SN,         SN,      SN,         SN]
choice174 = Phrase()
choice174.addNoteList(pitches174, durations174)

# choice 67      19S-PZ
pitches67     = [C5, B4, C5, E5, G4, C5]
durations67   = [.25, .25, .25, .25, .25, .25]
choice67 = Phrase()
choice67.addNoteList(pitches67, durations67)

# choice 43  19S-TD
pitches43     = [[G5,C3,E3],  [F5,C3,E3], [E5,C3,E3], D5,  C5]
durations43   = [ 1.0,         0.5,        0.5,       0.5, 0.5]
choice43 = Phrase()
choice43.addNoteList(pitches43, durations43)

# choice 51 19S-KF               # Treble and Bass piches are merged
pitches51   = [[C5,E3,C3], [G4,E3,C3], [E5,E3,C3], [C5,E3,C3], G5, E5]
durations51 = [ SN,         SN,         SN,         SN,        SN, SN]
choice51 = Phrase()
choice51.addNoteList(pitches51, durations51)

# choice 144   19S-LP
pitches144    = [[C3,E3,G5], G3, [C3,E3,C5], G3, [C3,E3,E5], G3]
durations144  = [ .25,       .25, .25,       .25, .25,       .25]
choice144     = Phrase()
choice144.addNoteList(pitches144, durations144)

##### measure 14 - create alternatives

# choice 49 19S-BG
pitches49   = [[C3,E3,E5], G3, [C3,E3,C5], G3, [C3,E3,G4], G3]
durations49 = [SN,         SN,  SN,        SN, SN,         SN]
choice49 = Phrase()
choice49.addNoteList(pitches49, durations49)

# choice 160  19S-JP
pitches160   = [[C3,E3,C5], B4, C5, E5, G4, [C3,E3,C5]]
durations160 = [ SN,        SN, SN, SN, SN,  SN         ]
choice160 = Phrase()
choice160.addNoteList(pitches160, durations160)

# choice 168   19S-LP
pitches168    = [[C3,E3,G5], F5,  E5, [E3,G3,D5], C5]
durations168  = [   .5,      .25, .25,   .25,     .25]
choice168     = Phrase()
choice168.addNoteList(pitches168, durations168)

#choice 38    19S-LK
pitches38 =   [C5, G4, E5]
durations38 = [EN, EN, EN] 
choice38 = Phrase()
choice38.addNoteList(pitches38, durations38)

#choice 59    19S-LK
pitches59 =   [G5, C5, E5]
durations59 = [EN, EN, EN]
choice59 = Phrase()
choice59.addNoteList(pitches59, durations59)

##### measure 15 - create alternatives

###################
### Alec Barker ###
### Measure 72  ###
###################

# choice 72
pitches72     = [[F5, F3], [E5, F3], [D5, F3], [C5, F3], [B4, G3], [D5, G3]]
durations72   = [ SN,       SN,       SN,       SN,       SN,       SN]
choice72      = Phrase()
choice72.addNoteList(pitches72, durations72)

######################
### End of Measure ###
######################

# choice 145  19S-JP
pitches145   = [[F3,D5], F5, A4, D5, B4, [G3,D5]]
durations145 = [ SN,     SN, SN, SN, SN,  SN     ]
choice145 = Phrase()
choice145.addNoteList(pitches145, durations145)

# choice 23 19S-RB
pitches23     = [[F5,F3], [E5,E3], [D5,D3], [E5,E3], [F5,F3], [G5,G3]]
durations23   = [ .25,     .25,     .25,     .25,     .25,     .25]
choice23 = Phrase()
choice23.addNoteList(pitches23, durations23)

# choice 89 19S-RB
pitches89     = [[G5, F3], [E5, E3], [D5, D3], [G5, G3]]
durations89   = [     .25,      .25,        1,        1]
choice89 = Phrase()
choice89.addNoteList(pitches89, durations89)

# choice 173 19S-BG
pitches173   = [[F3, F5], A5, A4, [G3, B4], D5]
durations173 = [SN,       SN, EN,  SN,      SN]
choice173 = Phrase()
choice173.addNoteList(pitches173, durations173)

# choice 44  19S-TD
pitches44     = [[A4,F3], [F5,F3], [D4,F3], [A4,G3], [B4,G3]]
durations44   = [1.0,      0.5,     0.5,     0.5,     0.5]
choice44 = Phrase()
choice44.addNoteList(pitches44, durations44)

##### measure 16 - create alternatives



##### Use for testing your measure before you add it
test = Phrase()
test.addNoteList(pitches13, durations13)

##### roll the dice!!!
## In the sheet music table measures equal columns
measure1 = choice([choice96, choice32, choice69, choice40, choice148, choice104, 
                   choice152, choice119, choice98, choice54])
measure2 = choice([choice84, choice22, choice6, choice95, choice17, choice74, choice157, 
                   choice60, choice142, choice87, choice130])
measure3 = choice([choice141, choice128, choice158, choice113, choice27, choice171, 
                   choice114, choice42, choice165, choice10])
measure4 = choice([choice156, choice41, choice63, choice13, choice85, choice45, choice167, 
                    choice50, choice61, choice103])
measure5 = choice([choice105, choice153, choice161, choice154, choice140, choice75, choice135, 
                    choice28])
measure6 = choice([choice122, choice46, choice55, choice2, choice97, choice68, choice133, choice86, 
                    choice129, choice47, choice37])
measure7 = choice([choice11, choice134, choice159, choice118, choice21, choice169, choice62])
measure8 = choice([choice30, choice81, choice24, choice100, choice107, choice91, choice33,
                    choice5])
measure9 = choice([choice70, choice117, choice66, choice90, choice25, choice120])
measure10 = choice([choice121, choice176, choice71, choice155, choice88])
measure11 = choice([choice26, choice126, choice15, choice57, choice31, choice108])
measure12 = choice([choice56, choice9, choice34, choice125, choice29, choice175, choice166, choice82])
measure13 = choice([choice112, choice174, choice67, choice43, choice51, choice144])
measure14 = choice([choice49, choice160, choice168, choice38, choice59])
measure15 = choice([choice72, choice145, choice23, choice89, choice173, choice44])
# measure16 = choice([])

##### connect the random measure into a waltz excerpt
# walzerteil.addPhrase(test)          # used to test measures
walzerteil.addPhrase(measure1)
walzerteil.addPhrase(measure2)
walzerteil.addPhrase(measure3)
walzerteil.addPhrase(measure4)
walzerteil.addPhrase(measure5)
walzerteil.addPhrase(measure6)
walzerteil.addPhrase(measure7)
walzerteil.addPhrase(measure8)
walzerteil.addPhrase(measure9)
walzerteil.addPhrase(measure10)
walzerteil.addPhrase(measure11)
walzerteil.addPhrase(measure12)
walzerteil.addPhrase(measure13)
walzerteil.addPhrase(measure14)
walzerteil.addPhrase(measure15)
# walzerteil.addPhrase(measure16)

### view and play randomly generated waltz exerpt
# View.sketch(walzerteil)
Play.midi(walzerteil)