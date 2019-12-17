# Practise
'''
1. Write a version of a palindrome recogniser that accepts a file name
from the sys.argv, reads each line, and prints the line to the screen if it
is a palindrome and write results to file like {source_name}/{result}.'''

import sys
sys.path.append("E:/Python/ITEA/ITEA-BC/Andrii_Ravlyk/8_files/practise/")
import argparse
import codecs


def get_file_name():
    parser = argparse.ArgumentParser(description='Files for test')
    parser.add_argument('file_name', type=str, help='Write filename')
    args = parser.parse_args(sys.argv[1:])
#   print(args.file_name)
    return args.file_name

print(get_file_name())

with codecs.open("E:/Python/ITEA/ITEA-BC/Andrii_Ravlyk/8_files/practise/"+get_file_name(), "r+", encoding='utf-8') as file_obj:
#   data = file_obj.read()
     new_list = []
     for line in file_obj.readlines():
         if line.lower().strip().replace(" ", "") == line[::-1].lower().strip().replace(" ", ""):
            new_list.append(line.strip() + "/" + "polindrom")
            print(line)
         else:
            new_list.append(line.strip() + "/" + "not_polindrom")
with open("E:/Python/ITEA/ITEA-BC/Andrii_Ravlyk/8_files/practise/output1.txt", "w") as file_obj2:
     for line2 in new_list:
        file_obj2.write(line2+"\n")
print("Final")
