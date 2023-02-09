# What is Password "Cracking"?
If you were to hack someone's computer and steal the passwords from the Windows [Security Account Manager](https://en.wikipedia.org/wiki/Security_Account_Manager) (SAM),
you would probably be disappointed to find out that all you got was the password hash, a seemingly random series of letters and numbers (e.g. 
`aad3c435b514a4eeaad3b935b51304fe:c46b9e588fa0d112de6f59fd6d58eae3`). 
Because it is unsafe to store passwords in plaintext (due to hacking!), people don't store passwords -- they stored [password hashes](https://auth0.com/blog/hashing-passwords-one-way-road-to-security/). 
A *hash* is the product of putting data through a [hashing algorithm](https://www.okta.com/identity-101/hashing-algorithms/) like MD5 or SHA256. The most important
properties of a hashing algorithm is that they are:
1. Unique - every possible input will yield a distinct hash
2. Uniformly random - even the slightest variation in even one million letters will drastically change the *entire* hash
3. Consistent - every password will always have the same hash
4. One-way - unlike encrypted data, hashed data cannot be "unhashed". 

# Cracking Password Hashes
So if hashes are one-way algorithms, then how can you "crack" a password?  Take advantage of principles 1 and 3: the uniqueness and consistency of hashes, we could run
every possible password through the hashing algorithm and when we find a matching hash, we'll know we've found the original passsword.

Although brute-forcing is a valid technique, it's not the best approach. Using some basic combinatorics, we can determine how many possible passwords we could have to
generate to find someone's password. Let's say we know someone's passwords is 7 letters long and includes lowercase letters (26 chars), uppercase letters, (26 chars),
numbers (10 chars), and symbols (32 chars). This means that number of possible passwords is 7 to the 94th power, or about
27,492,596,703,964,827,506,775,644,239,221,895,731,006,665,580,707,234,238,573,173,859,460,696,305,424,849. Assuming you could just 100 trillion passwords per second
(which is *really* generous), it would take you 8.7e60 years to guess all the possible combinations.

So clearly brute-force is not the best approach. Luckily, there's better ways.
Would you wager that someone's password is more likely to be "pZU%c$7rGG3" or "qwerty123"? We know passwords are more common than others. So what if we just took a list
of all the most common passwords and tried that? This is called a [*dictionary attack*](https://en.wikipedia.org/wiki/Dictionary_attack) and is a great way to crack
passwords. The most common password cracking wordlist is [rockyou.txt](https://dekisoft.com/rockyou-txt-gz-password-list-download/), which is a list of ~14 million
passwords leaked from [a real life breach](https://www.computerworld.com/article/2522045/rockyou-hack-exposes-names--passwords-of-30m-accounts.html).

Another good approach is called a mask attack. If you know part of someone's password, you can brute force the rest. For example, if I know someone's password is their
birthday and they were born in July, then there's a fair chance that their password is "July" followed by four digits. Passing the expression `July?d?d?d?d` to HashCat
would try every combination from `July1111` to `July9999`. For more modes, visit the [HashCat Wiki](https://hashcat.net/wiki/).

# Common Tools for Cracking
- [HashCat](https://www.kali.org/tools/hashcat/) and [John The Ripper](https://www.kali.org/tools/john/#john) are tools for directly cracking passwords with a variety of
attack modes
- [RainbowCrack](https://www.kali.org/tools/rainbowcrack/#rcrack) and [OphCrack](https://www.kali.org/tools/ophcrack/) are [rainbow table](https://www.csoonline.com/article/3623195/rainbow-tables-explained-how-they-work-and-why-theyre-mostly-obsolete.html) tools to instantly crack known hashes. OphCrack is Windows-specific (LM and
NT hashes)
- [HashID](https://www.kali.org/tools/hashid/) is a tool for identifying over 175 types of hashes. Native John formatting support

IyBDaGFsbGVuZ2VzCjEuIERpY3Rpb25hcnkgYXR0YWNrIHdpdGggcm9ja3lvdS50eHQgKGBoYXNoY2F0IC1hIDAgLW0gMCBoYXNoZXMudHh0IH4vd29yZGxpc3RzL3JvY2t5b3UudHh0YAoyLiBNYXNrIGF0dGFjayB3aXRoIGtub3duIHN0ZW0gKGBoYXNoY2F0IC1hIDMgLW0gMCBoYXNoZXMudHh0IFNLWS1IUU5ULT9kP2Q/ZD9kYCkKMy4gQnJ1dGUtZm9yY2UgYXR0YWNrIHdpdGggW2N1c3RvbSBwb2tlbW9uIHdvcmRsaXN0XShodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vY2Vydm9pc2UvcGVudGVzdC1zY3JpcHRzL21hc3Rlci9wYXNzd29yZC1jcmFja2luZy93b3JkbGlzdHMvcG9rZW1vbi1saXN0LWVuLnR4dCkgKGBoYXNoY2F0IC1hIDAgLW0gMCBoYXNoZXMudHh0IH4vd29yZGxpc3RzL3Bva2Vtb24tbGlzdC1lbi50eHRgKQo0LiBPcGhjcmFjayBbWFAgcmFpbmJvdyB0YWJsZSBsb29rdXBdKGh0dHBzOi8vb3BoY3JhY2suc291cmNlZm9yZ2UuaW8vdGFibGVzLnBocCkKNS4gRGljdGlvbmFyeSBhdHRhY2sgd2l0aCBbY3VzdG9tIExhdyBhbmQgT3JkZXIgU1ZVIEVwaXNvZGUgVGl0bGUgd29yZGxpc3RdKGh0dHBzOi8vZ2l0aHViLmNvbS9haXMwNDcvQ3liZXJTZWMtUHVibGljYy9ibG9iL21hc3Rlci93b3JkbGlzdHMvbGF3LWFuZC1vcmRlci1zdnUtZXBpc29kZS10aXRsZXMudHh0KSAoYGhhc2hjYXQgLWEgMCAtbSAwIGhhc2hlcy50eHQgfi93b3JkbGlzdHMvbGF3LWFuZC1vcmRlci1zdnUtZXBpc29kZS10aXRsZXMudHh0KQ==
