import caesar

KEY = 0b0101010 & 0x42 | 0x44 >> 2

def encipher(plaintext: str):
        return caesar.encipher(plaintext, KEY)

def decipher(ciphertext: str):
        return caesar.decipher(ciphertext, KEY)