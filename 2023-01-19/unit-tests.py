# Unit tests to make sure the Caesar algorithm was implemented correctly

import caesar

## ENCIPHERING ##

# Case 1: No rotation (nullop)
assert caesar.encipher("It's difficult to understand the lengths he'd go to remain short",0) == "IT'S DIFFICULT TO UNDERSTAND THE LENGTHS HE'D GO TO REMAIN SHORT"

# Case 2: Some rotation 1-25 (8)
assert caesar.encipher("The swirled lollipop had issues with the pop rock candy",8) == "BPM AEQZTML TWTTQXWX PIL QAACMA EQBP BPM XWX ZWKS KIVLG"

# Case 3: Rotation of 26 (nullop)
assert caesar.encipher("Is the museum visited by many people?",26) == "IS THE MUSEUM VISITED BY MANY PEOPLE?"


## DECIPHERING ##

# Case 4: Some rotation (17)
assert caesar.decipher("Nv nviv jkzcc mvip votzkvu", 17) == "WE WERE STILL VERY EXCITED"
