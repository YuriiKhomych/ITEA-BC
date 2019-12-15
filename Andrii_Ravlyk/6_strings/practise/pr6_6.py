"""
`string = AV is largest Analytics community of India`
6. Get two symbols of each word in string
result: `['AV', 'is', 'la', 'An', 'co', 'of', 'In']`
"""
def find_two_symb(i_str="AV is largest Analytics community of India"):
    import re
    match = re.findall(r'\b\w{2}', i_str)
#   print(match)
    return(match)

#find_two_symb()