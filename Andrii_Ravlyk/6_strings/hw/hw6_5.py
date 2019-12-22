''''li = ["+380971236789", "+380809123232", "99999x9999"]
5. Check that mobile phone number is valid.'''
import re
def check_mob_num(i_list = ["+380971236789", "+380809123232", "99999x9999"]):
    check = ""
    o_res ={}
    for i in i_list:
        if len(i) == 13 and i[0:4] == "+380" and  re.findall(r'\D+', i[4:]) == []:
            check = "valid"
        else:
            check = "not_valid"
        o_res[i] = check
#   print (o_res)
    return (o_res)

# check_mob_num()