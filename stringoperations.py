s = "  Hello Python 123 World  "

print("Original String :", s)

# Length
print("Length :", len(s))

# Uppercase
print("Upper :", s.upper())

# Lowercase
print("Lower :", s.lower())

# Capitalize
print("Capitalize :", s.capitalize())

# Title
print("Title :", s.title())

# Swap Case
print("Swapcase :", s.swapcase())

# Strip Spaces
print("Strip :", s.strip())

# Left Strip
print("Lstrip :", s.lstrip())

# Right Strip
print("Rstrip :", s.rstrip())

# Replace
print("Replace :", s.replace("Python", "Java"))

# Split
print("Split :", s.split())

# Join
words = s.split()
print("Join :", "-".join(words))

# Find
print("Find 'Python' :", s.find("Python"))

# Index
print("Index 'World' :", s.index("World"))

# Count
print("Count of 'o' :", s.count("o"))

# Startswith
print("Startswith '  He' :", s.startswith("  He"))

# Endswith
print("Endswith '  ' :", s.endswith("  "))

# isalpha
print("isalpha :", s.isalpha())

# isdigit
print("isdigit :", s.isdigit())

# isalnum
print("isalnum :", s.isalnum())

# islower
print("islower :", s.islower())

# isupper
print("isupper :", s.isupper())

# istitle
print("istitle :", s.istitle())

# isspace
print("isspace :", s.isspace())

# Center
print("Center :", s.center(40, "*"))

# Left Justify
print("Ljust :", s.ljust(40, "-"))

# Right Justify
print("Rjust :", s.rjust(40, "-"))

# Zero Fill
num = "123"
print("Zfill :", num.zfill(8))

# Encode
print("Encode :", s.encode())

# Reverse
print("Reverse :", s[::-1])

# Count Vowels
vowels = 0
for ch in s.lower():
    if ch in "aeiou":
        vowels += 1
print("Vowels :", vowels)

# Count Consonants
consonants = 0
for ch in s.lower():
    if ch.isalpha() and ch not in "aeiou":
        consonants += 1
print("Consonants :", consonants)

# Count Digits
digits = 0
for ch in s:
    if ch.isdigit():
        digits += 1
print("Digits :", digits)

# Count Spaces
spaces = 0
for ch in s:
    if ch == " ":
        spaces += 1
print("Spaces :", spaces)

# Remove Spaces
print("Without Spaces :", s.replace(" ", ""))

# Frequency of Characters
print("\nCharacter Frequency:")
for ch in sorted(set(s)):
    print(repr(ch), ":", s.count(ch))

# Sort Characters
print("\nSorted Characters :", "".join(sorted(s)))

# Remove Duplicate Characters
result = ""
for ch in s:
    if ch not in result:
        result += ch
print("Without Duplicates :", result)

# Palindrome Check
temp = s.strip().lower()
if temp == temp[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")