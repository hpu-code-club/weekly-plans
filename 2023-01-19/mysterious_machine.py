# BEWARE SPOOKY GHOSTS!!
#
#                      .-.
#         heehee      /aa \_
#                   __\-  / )                 .-.
#         .-.      (__/    /        haha    _/oo \
#       _/ ..\       /     \               ( \v  /__
#      ( \  u/__    /       \__             \/   ___)
#       \    \__)   \_.-._._   )  .-.       /     \
#       /     \             `-`  / ee\_    /       \_
#    __/       \               __\  o/ )   \_.-.__   )
#   (   _._.-._/     hoho     (___   \/           '-'
#    '-'                        /     \
#                             _/       \    teehee
#                            (   __.-._/

import caesar

KEY = 0b0101010 & 0x42 | 0x44 >> 2  # nothing scarier than bit math

def encipher(plaintext: str):
        return caesar.encipher(plaintext, KEY)

def decipher(ciphertext: str):
        return caesar.decipher(ciphertext, KEY)
