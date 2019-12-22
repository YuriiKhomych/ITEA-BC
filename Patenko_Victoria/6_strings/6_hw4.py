import re

def split_strings(string):
    print(re.split(';|,| ', string))

my_string = 'asdf fjdk;afed,fjek,asdf,foo'
split_strings(my_string)