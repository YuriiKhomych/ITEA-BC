# 2. Create a function that generate 10 random numbers from 1 to 100.
# Call this functions 100 times and append each result of function to file.
import random

def ten_from_hundred(count_line):
    def create_line():
        list_num = []
        while len(list_num) < 10:
            num = random.randint(1, count_line)
            list_num.append(num)
        return list_num

    with open('Ten_in_hundred.txt', 'w+') as file:
        for num in range(count_line):
            file.writelines(f'{create_line()}\n')

ten_from_hundred(100)
