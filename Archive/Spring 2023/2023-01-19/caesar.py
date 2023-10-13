def encipher(plaintext: str, shift: int) -> str:
    return rotate(plaintext, shift)

def decipher(ciphertext: str, shift: int) -> str:
    return rotate(ciphertext, -shift)

def rotate(text: str, shift: int) -> str:
    shifted_text = ""

    for char in text.upper():
        if char.isalpha():
            shifted_char = (ord(char) - ord('A') + shift) % 26
            shifted_text += chr(shifted_char + ord('A'))
        else:
            shifted_text += char

    return shifted_text