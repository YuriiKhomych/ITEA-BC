# 1. Write a version of a palindrome recogniser that accepts a file name
# from the sys.argv, reads each line, and prints the line to the screen if it
# is a palindrome and write results to file like {source_name}/{result}.
import sys

def palindrome_from_file():
    with open('polindrome', 'r+') as file_obj:
        write_list = []
        for line in file_obj.readlines():
            for letter in range(len(line) // 2):
                if line[letter] != line[-2 - letter]:
                    result = False
                else:
                    result = True
            if result == True:
                print(f'{line[:-1:]} are palindrome?: {result}')
                write_list.append(f'{line[:-1:]} are palindrome?: {result}\n')
        file_obj.writelines(write_list)
     # return write_list

palindrome_from_file()

