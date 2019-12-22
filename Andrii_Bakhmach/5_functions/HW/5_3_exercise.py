# Write a function that takes a character (i.e. a
#string of length 1) and returns True if it is a vowel,
#False otherwise.

def character_detector(char):
    char = char.lower()
    if char in "aeiou":
        return True
    else:
        return False



