# 3. Write a function that takes a character (i.e. a
# string of length 1) and returns True if it is a vowel,
# False otherwise.

def is_vowel(character):
    vowels = ('a', 'e', 'i', 'o', 'u')
    if character not in vowels:
        return False
    return True

    print(is_vowel(("a"),("b")))