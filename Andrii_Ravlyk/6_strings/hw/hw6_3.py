'''3. Write a function filter_long_words() that takes a list
of words and an integer n and returns the list of words that
are longer than n.'''

def filter_long_words(i_list = ['aa','bbbbbb','ggg', 'hfghf'], n = 3):
    o_list = []
    for i in i_list:
        if len(i) > n:
            o_list.append(i)
#    print(o_list)
    return o_list

#filter_long_words()