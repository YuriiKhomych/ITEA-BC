'''2. Write a function find_longest_word() that takes
a list of words and returns the length of the longest one.'''

#import sys
#sys.path.append("E:/Python/ITEA/ITEA-BC/Andrii_Ravlyk/6_strings/hw")
#print(sys.path)
from hw6_1 import convert_list_to_len

def find_longest_word(i_list=['aa','byyyyyyyybbb','ggg', 'hfghf']):

    l_world = convert_list_to_len(i_list)
    l_world.sort()
#   print(l_world[-1])
    return l_world[-1]

#find_longest_word()
