'''6. Return list of domains from list of emails.'''
import re
def get_list_domain (i_list = ["aff@mail.ru", "gjgjg@i.ua", "hkhjhkh@apple.com"]):
    list_domain = []
    for i in i_list:
        match = re.search(r'@',i)
        list_domain.append(i[match.start()+1:])
#   print(list_domain)
    return(list_domain)

get_list_domain()
