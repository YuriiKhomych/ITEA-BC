# 4. Write decorator that collect result of each function into list.
import random


def my_decoration(func):
    def wrapper(a, b):
        results = []
        print(f'First ask')
        results.append(func(a, b))
        print(f'Second ask')
        results.append(func(a, b))
        print(f'Result of word two func is: {results}')
    return wrapper


@my_decoration
def some_print(a, b):
    # x = random.randint(0, 100)
    y = a + b
    return y


some_print(10, 33)
