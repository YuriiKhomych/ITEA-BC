# Create a function that generate 10 random numbers from 1 to 100.
# Call this functions 100 times and append each result of function to file.

# Update With

import random


def sto():
    zero = 10
    rand_numb = []
    while zero != 0:
        with open('random.txt', 'w') as popular:
            popular.write(str(rand_numb))
            zero -= 1
            rand_numb.append(random.randint(0, 100))
    return rand_numb

if __name__ == '__main__':
    print(sto())
