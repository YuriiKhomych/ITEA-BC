# 3. Write decorator that print function name before and after function execution.
# `func.__name__`

def my_decorator(func):
    def wrapper():
        print(f'Before run {func.__name__}')
        func()
        print(f'After run {func.__name__}')
    return wrapper


def say_wee():
    print(f'Yes, it is function for decor')

say_wee = my_decorator(say_wee)

say_wee()