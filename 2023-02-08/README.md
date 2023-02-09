# Password Cracking

# Tools
1. hashid - calculates hash type (most to least likely)
2. hashcat - password cracker
3. rcrack - rainbow table

# Challenges
1. Dictionary attack with rockyou.txt (`hashcat -a 0 -m 0 hashes.txt ~/wordlists/rockyou.txt`
2. Mask attack with known stem (`hashcat -a 3 -m 0 hashes.txt SKY-HQNT-?d?d?d?d`)
3. Brute-force attack with [custom pokemon wordlist](https://raw.githubusercontent.com/cervoise/pentest-scripts/master/password-cracking/wordlists/pokemon-list-en.txt) (`hashcat -a 0 -m 0 hashes.txt ~/wordlists/pokemon-list-en.txt`)
4. Ophcrack [XP rainbow table lookup](https://ophcrack.sourceforge.io/tables.php)
5. Dictionary attack with [custom Law and Order SVU Episode Title wordlist](https://github.com/ais047/CyberSec-Publicc/blob/master/wordlists/law-and-order-svu-episode-titles.txt) (`hashcat -a 0 -m 0 hashes.txt ~/wordlists/law-and-order-svu-episode-titles.txt)
