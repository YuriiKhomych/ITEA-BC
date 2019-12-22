# 5. Glossary:
# A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
#     * Think of five programming words you’ve learned about in the previous chapters.
#     * Use these words as the keys in your glossary, and store their meanings as values.
#     * Print each word and its meaning as neatly formatted output.
#     * You might print the word followed by a colon and then its meaning,
#     or print the word on one line and then print its meaning indented on a second line.
#     * Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

python_dictionary = {
    'list': 'list of items',
    'dict': 'dictionary with key and value',
    'variable': 'it is var in program',
    'function': 'A function is a block of organized, reusable code that is used to perform a specific task.',
    'class': 'A prototype of a programmable object defined by a programmer with a set of attributes '
             '(variables and methods) that describe this object. Access to attributes and methods is through a point',
}

for key, description in python_dictionary.items():
    print(f'{key} is means: \n\t{description}')