'''`string = 'asdf fjdk;afed,fjek,asdf,foo' # String has multiple delimiters (";",","," ").`
4. Split words by delimiters.'''
import re

def split_string(i_str =  'asdf fjdk;afed,fjek,asdf,foo'):
    o_str = re.split(r';|,|\s', i_str)
#   print (o_str)
    return (o_str)
#split_string()