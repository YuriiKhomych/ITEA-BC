'''1. The third person singular verb form in English is distinguished
    by the suffix -s, which is added to the stem of the infinitive form:
    run -> runs. A simple set of rules can be given as follows:

    If the verb ends in y, remove it and add ies
    If the verb ends in o, ch, s, sh, x or z, add es
    By default just add s
    Your task in this exercise is to define a function make_3sg_form()
    which given a verb in infinitive form returns its third person singular
    form. Test your function with words like try, brush, run and fix.
    Note however that the rules must be regarded as heuristic, in the
    sense that you must not expect them to work for all cases. Tip: Check
    out the string method endswith().'''
def make_3sg_form(verb):
    if verb[-1] == "y":
        o_verb = verb[0:len(verb)-1]+"ies"
    elif verb[-1] in ("o", "s", "x", "z"):
        o_verb = verb + "es"
    elif verb[-2:len(verb)] in ("ch", "sh"):
        o_verb = verb + "es"
    else:
        o_verb = verb + "s"
    return o_verb

#test brush, run and fix
#print ("try", make_3sg_form("try"))
#print ("brush", make_3sg_form("brush"))
#print ("run", make_3sg_form("run"))
#print ("fix", make_3sg_form("fix"))
#test_1 = (make_3sg_form("try"))
#print ("try", test_1.endswith('ies'))
#test_2 = (make_3sg_form("try"))
#print ("brush", test_2.endswith('es'))
#test_3 = (make_3sg_form("run"))
#print ("run", test_3.endswith('s'))
#test_4 = (make_3sg_form("fix"))
#print ("fix", test_4.endswith('es'))