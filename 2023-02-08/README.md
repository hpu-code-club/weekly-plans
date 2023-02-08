# Password Cracking

# Tools
1. hashid - calculates hash type (most to least likely)
2. hashcat - password cracker
3. rcrack - rainbow table

# Challenges
1. Brute-force attack with rockyou.txt (`hashcat -a 0 -m 0 hashes.txt ~/wordlists/rockyou.txt`
2. Mask attack with known stem (`hashcat -a 3 -m 0 hashes.txt SKY-HQNT-?d?d?d?d`)
3. Brute-force attack with [custom pokemon wordlist](https://raw.githubusercontent.com/cervoise/pentest-scripts/master/password-cracking/wordlists/pokemon-list-en.txt) (`hashcat -a -m 0 hashes.txt ~/wordlists/pokemon-list-en.txt`)
