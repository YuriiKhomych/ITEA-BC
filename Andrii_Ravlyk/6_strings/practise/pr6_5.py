"""    `string = AV is largest Analytics community of India`
5. Return last word from string.
result: `India`
"""
def find_last_word(i_str="AV is largest Analytics community of India"):
    import re
    match = re.findall(r'\w+', i_str)
#   print(match[-1])
    return match[-1]

#find_last_word()