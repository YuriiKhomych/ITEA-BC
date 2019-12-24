'''2. In English, the present participle is formed by adding the suffix -ing
    to the infinite form: go -> going. A simple set of heuristic rules can be
    given as follows:

    If the verb ends in e, drop the e and add ing (if not exception: be, see,
      flee, knee, etc.)
    If the verb ends in ie, change ie to y and add ing
    For words consisting of consonant-vowel-consonant, double the final letter
    before adding ing
    By default just add ing
    Your task in this exercise is to define a function make_ing_form() which
    given a verb in infinitive form returns its present participle form. Test
    your function with words such as lie, see, move and hug. However, you must
    not expect such simple rules to work for all cases.'''

def make_ing_form(verb):
    if verb[-1] == "e" and verb not in ("be", "see", "flee", "knee") and verb[-2:len(verb)] not in ("ie"):
        o_verb = verb[0:len(verb)-1]+"ing"
    elif verb[-1] not in ("a", "e", "i", "o", "u", "y") and verb[-2] in ("a", "e", "i", "o", "u", "y") \
            and verb[-3] not in ("a", "e", "i", "o", "u", "y"):
        o_verb = verb + verb[-1] +  "ing"
    elif verb[-2:len(verb)] in ("ie"):
        o_verb = verb[0:len(verb)-2] + "y" + "ing"
    else:
        o_verb = verb + "ing"

    return o_verb

#test lie, see, move and hug
#print ("lie", make_ing_form("lie"))
#print ("see", make_ing_form("see"))
#print ("move", make_ing_form("move"))
#print ("hug", make_ing_form("hug"))