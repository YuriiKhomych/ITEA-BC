'''Write decorator that collect result of each function into list'''
def my_decorator(my_function):
    def my_wrapped(x,y):
        result_list = []
        result_list.append(my_function(x,y))
        print(result_list)
    return my_wrapped
@my_decorator
def my_function(x,y):
    return x+y
#Test
my_function(2,3)
