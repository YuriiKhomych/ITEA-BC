# In English, the present participle is formed by adding the suffix -ing
# to the infinite form: go -> going. A simple set of heuristic rules can
# be given as follows: If the verb ends in e, drop the e and add ing
# (if not exception: be, see, flee, knee, etc.)

# If the verb ends in ie, change ie to y and add ing For words consisting of consonant-vowel-consonant,
# double the final letter before adding ing By default just add ing Your task in
# this exercise is to define a function make_ing_form() which given a verb in
# infinitive form returns its present participle form.

# Test your function with words such as lie, see, move and hug.
# However, you must not expect such simple rules to work for all cases.

# Done + test
from hw_3 import my_timer


# my_file = 'text_file/test.txt'
my_excaption = 'be, see, flee, knee'

@my_timer
def participle(my_file):
    text = open(my_file)
    words = text.read().lower().split()
    text.close()
    part_word = []
    for word in words:
        len_word = len(word)
        if word not in my_excaption:
            if word.endswith('ie'):
                part_word.append(str(word)[:(len_word - 2)] + 'y' + 'ing')
            elif word.endswith('e'):
                part_word.append(str(word)[:(len_word - 1)] + 'ing')
    return part_word

# print(participle(my_file))