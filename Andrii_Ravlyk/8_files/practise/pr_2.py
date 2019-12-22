'''2. Create a function that generate 10 random numbers from 1 to 100.
Call this functions 100 times and append each result of function to file.'''
import random
def gen_numbers():
    i=1
    a=""
    while i <= 10:
        a = a + str(random.randint(1, 100))+" "
        i+=1
    return a.rstrip()


with open("E:/Python/ITEA/ITEA-BC/Andrii_Ravlyk/8_files/practise/output2.txt", "w") as file_obj2:
    n = 1
    while n <= 100:
        file_obj2.write(gen_numbers() + "\n")
        n += 1
#     data = file_obj.read()
#     print(data.split("\n"))
#     file_obj.write(data * 20)
