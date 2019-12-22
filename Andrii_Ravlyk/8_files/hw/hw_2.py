'''
2. Create program that get [Text](https://www.python.org/dev/peps/pep-0008/#code-lay-out)
from file, find 5 most popular words and write result to file.'''

import re
with open("E:/Python/ITEA/ITEA-BC/Andrii_Ravlyk/8_files/hw/hw_text2.txt", "r+") as file_obj:
    data = file_obj.read()
    check = re.findall(r'\b\w+\b', data)
    print (check)
    n = 0
    res_dic = {}
    u_check = set(check)
    for i in u_check:
        n = 0
        for j in check:
            if i == j:
                n = n+1
        res_dic[i] = n
    print (res_dic)
    list_d = list(res_dic.items())
    list_d.sort(key=lambda i: i[1],reverse=True)
    n = len(list_d)
    ni = 1
    if n < 5:
        n = len(list_d)
    else:
        n = 5
    with open("E:/Python/ITEA/ITEA-BC/Andrii_Ravlyk/8_files/hw/hw_test2.txt", "w+") as file_obj2:
        for i in list_d:
            if ni > n:
                break
            print(i[0], ':', i[1])
            file_obj2.write(i[0] + ':'+ str(i[1])+"\n")
            ni = ni +1

