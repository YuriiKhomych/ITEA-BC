'''3. Write decorator that print function name before and after function execution.
`func.__name__`'''
def my_decorator(my_function):
    def my_wrapped():
        print("before", my_function.__name__)
        my_function()
        print("after", my_function.__name__)
    return my_wrapped
@my_decorator
def my_function():
    print ("Hi I am my_function")
my_function()