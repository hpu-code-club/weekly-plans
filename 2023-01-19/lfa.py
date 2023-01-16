from typing import Dict

# TODO: FINISH SKELETON
#
# Of course, you could just brute force all 26 possible keys of the mysterious machine
# and read them all until you found one that made sense; but that's only possible because
# the key space is so small. Reading all the possible deciphered texts for a key space
# in the thousands is exhausting, and in the millions is impossible. Instead, you can use
# letter frequency analysis to filter the most likely candidates and read those.
#
# If you've ever played Scrabble or Wheel of Fortune, you know some letters are more 
# common than others in the English language. 'E' being the most common. Using this fact,
# you can statistically generate the most likely deciphered texts based on the similarity of the
# frequency of letters in said deciphered text vs the English language.


# A mapping of each letter to their frequency in the English alphabet (out of 1.0) from
# "Views for Multilevel Database Security," IEEE Transactions on Software 
# Engineering 13 (2), pp. 129-140 (Feb. 1987).
ENGLISH_MODEL = {
    'a':0.080, 'b':0.015, 'c':0.030, 'd':0.040, 'e':0.130, 'f':0.020, 'g':0.015,
    'h':0.060, 'i':0.065, 'j':0.005, 'k':0.005, 'l':0.035, 'm':0.030, 'n':0.070,
    'o':0.080, 'p':0.020, 'q':0.002, 'r':0.065, 's':0.060, 't':0.090, 'u':0.030,
    'v':0.010, 'w':0.015, 'x':0.005, 'y':0.020, 'z':0.002,  
}
