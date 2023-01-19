# Itinerary
- [NCL Spring 2023 Registration](https://docs.google.com/forms/d/e/1FAIpQLSdjc3wOTnuduNyPofWMO77NVzpkuonWsBsODqYz1vcOsYtuNQ/viewform?usp=sf_link)
 - Activities
     - [HackTheBox](https://www.hackthebox.com/hacker/pricing)
     - [OverTheWire](https://overthewire.org/wargames/)
     - [DVWA](https://www.kali.org/tools/dvwa/)
 - Competitions
    - [DiceCTF](https://ctf.dicega.ng/) (Feb. 3-5th, 36 rating)
    - [PbCTF](https://ctftime.org/event/1763) (Feb. 18-20th, 36 rating)
    - [hxpCTF](https://2022.ctf.link/) (Mar. 10-12th, 100 rating)
    - [PlaidCTF](https://plaidctf.com/challenge) (April 8th, 100 rating)
- [Upcoming Conferences](https://www.northeastern.edu/graduate/blog/2019-tech-conferences/)
    - [RSA Conference](https://www.rsaconference.com/usa) (April 24-27th, CA)
    - [DefCon](https://defcon.org/) (April 11-14th, Nevada)
    - [Blackhat](https://www.blackhat.com/) (August 5-7th, Las Vegas)
- SGA:
 - Draft bill for ACM accounts (treasurer, vice president, sga rep., $20/each)

# Caesar and Ciphers
Encryption is the process of using a enciphering algorithm (called a cipher) to hide the
meaning of a message. Ciphers are two-way, there must be a way to encipher (hide) the 
message and to decipher (reveal) the message; though, the enciphering and deciphering 
process does not have to be the same. Often, the original unenciphered message is called
*plaintext* and the enciphered message is called the *ciphertext*.

The [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher) (aka shift cipher) is a
[classical](https://en.wikipedia.org/wiki/Classical_cipher) [monoalphabetic substitution cipher](https://en.wikipedia.org/wiki/Substitution_cipher). Fancy words, but that basically
means that the Caesar cipher belongs to a group of ciphers that uniquely replace each 
letter in the original message with a letter from the alphabet. The uniqueness of the 
mapping is important or else the ciphertext cannot be properly deciphered. For example, if 
you took the word "BEE" and mapped both 'B' and 'E' to 'Z', then you would get the 
ciphertext "ZZZ" and lose all meaning.

# Basic Attacks on Ciphers
[Cryptanalysis](https://en.wikipedia.org/wiki/Cryptanalysis) studies cryptographic systems
in hopes of breaking them. Although more modern ciphers are difficult to brute force, you
can still crack them by taking advantage of the mathematics behind them. For example,
the [birthday attack](https://en.wikipedia.org/wiki/Birthday_attack) can be used to generate
a hash used as digital signature that could be used to force a signed document.

In this exercise, you are given access to a cryptographic machine called the *mysterious
machine*. The mystery machine uses the caesar cipher algorithm, but you don't know what the
encryption key (the shift amount). Despite this, you will still be able to perform four
types of cryptoanalyic attacks on it. For each attack, write your solitions in *main.py* 
and only use the specified resources.

## Known Plaintext
Given both the original plaintext *"The best key lime pie is still up for debate"*
and the ciphertext *"MAX UXLM DXR EBFX IBX BL LMBEE NI YHK WXUTMX"*, deduce the encryption
key.

## Chosen Ciphertext
You gain temporary access to the *mysterious machine*. Use `mysterious_machine.decipher()`
to decipher any string of your choice. Your goal is to deduce the encryption key.

## Chosen Plaintext
You gain temporary access to the *mysterious machine*. Use `mysterious_machine.encipher()`
to encipher any string of your choice. Your goal is to deduce the encryption key.

## Ciphertext Only
Given only the ciphertext, determine the plaintext. You may not use the mysterious machine. Bonus: write a function that can brute force the solution without human 
intervention (without being read) via [letter frequency analysis](https://en.wikipedia.org/wiki/Letter_frequency). A pre-written letter frequency table can be found in 
`lfa.py`.

For modern ciphers this would take a long time if not be impossible, but remember that
[*most classical ciphers can be practically computed and solved by hand*](https://en.wikipedia.org/wiki/Classical_cipher).
