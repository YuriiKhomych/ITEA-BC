''''Create decorator which print the execution time of function.
Use time or timeit module for it.

`import time`

`start = time.time()`

`end = time.time() - start`'''
import time
def my_decorator(my_function):
    def my_wrapped():
        start = time.time()
        my_function()
        end = time.time() - start
        print("Duration =", end)
    return my_wrapped
@my_decorator
def my_function():
    n = 0
    while n<=10000000:
        n += 1
    print ("Hi I am my_function")

my_function()