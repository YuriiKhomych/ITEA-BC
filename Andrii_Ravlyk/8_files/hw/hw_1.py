'''# HW

* Write test with 3-4 cases

1. According to Wikipedia, a semordnilap is a word or phrase that spells
a different word or phrase backwards. ("Semordnilap" is itself
"palindromes" spelled backwards.)
Write a semordnilap recogniser that accepts a file name (pointing to a list of words)
from the program arguments and finds
and prints all pairs of words that are semordnilaps to the screen.
For example, if "stressed" and "desserts" is part of the word list, the
the output should include the pair "stressed desserts". Note, by the way,
that each pair by itself forms a palindrome!'''


import sys
sys.path.append("E:/Python/ITEA/ITEA-BC/Andrii_Ravlyk/8_files/hw/")
import argparse
import codecs
import re


def get_file_name():
    parser = argparse.ArgumentParser(description='Files for test')
    parser.add_argument('file_name', type=str, help='Write filename')
    args = parser.parse_args(sys.argv[1:])
#   print(args.file_name)
    return args.file_name

with codecs.open("E:/Python/ITEA/ITEA-BC/Andrii_Ravlyk/8_files/hw/"+get_file_name(), "r+", encoding='utf-8') as file_obj:
    data = file_obj.read()
    check = re.findall(r'\b\w+\b', data)
    print (check)
    n = 0
    res_dic = {}
    u_check = set(check)
    print (u_check)
    with open("E:/Python/ITEA/ITEA-BC/Andrii_Ravlyk/8_files/hw/hw_test1.txt", "w+") as file_obj2:
        for s in  u_check:
            for l in check:
                if s[::-1] == l:
                    print (s, l, 'semordnilap')
                    file_obj2.write(s +' '+ l + ' semordnilap'  + "\n")
            break



