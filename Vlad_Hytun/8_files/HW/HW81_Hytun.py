# 1. According to Wikipedia, a semordnilap is a word or phrase that spells
# a different word or phrase backwards. ("Semordnilap" is itself
# "palindromes" spelled backwards.)
# Write a semordnilap recogniser that accepts a file name (pointing to a list of words)
# from the program arguments and finds
# and prints all pairs of words that are semordnilaps to the screen.
# For example, if "stressed" and "desserts" is part of the word list, the
# the output should include the pair "stressed desserts". Note, by the way,
# that each pair by itself forms a palindrome!
import codecs
import re
filename = 'polindrome frases.txt'

def semordnilap(filename):
    with codecs.open(filename, 'r', encoding='utf-8') as file_obj:
        cashe_data = file_obj.readlines()
       # print(cashe_data)
    with codecs.open(f'{filename}_check.', 'w+', encoding='utf-8') as file_obj2:
        # print(cashe_data)
        # print(cashe_data2)
        for line in cashe_data:
            if line.strip().replace(' ', '').lower()[:len(line.strip().replace(' ', ''))//2] !=\
                    line.strip().replace(' ', '').lower()[:len(line.strip().replace(' ', ''))//2:-1]:
                # print(f'{line.rstrip()} --- It is NOT semordnilap!')
                file_obj2.writelines(f'{line.rstrip()} --- It is NOT semordnilap!\n')
            else:
                # print(f'{line.rstrip()} --- It is semordnilap!')
                file_obj2.writelines(f'{line.rstrip()} --- It is semordnilap!\n')


semordnilap(filename)
