"""    `string = AV is largest Analytics community of India`
4. Return first word from string.
result: `AV`"""

def find_first_word(i_str="AV is largest Analytics community of India"):
    import re
    match = re.search(r'\w+', i_str)
    print(match[0] if match else 'Not found')
    return match[0] if match else 'Not found'

#find_first_word()