'''1. Write a program that maps a list of words into a list
of integers representing the lengths of the correponding words.'''

def convert_list_to_len(i_list=['aa','bbbbbb','ggg', 'hfghf']):
    o_str = []
    for i in i_list:
        o_str.append(i.__len__())

#    print(o_str)
    return o_str

#convert_list_to_len(i_list=['aa','bb','ggg', 'hfghf'])
