#Write a function `is_member()` that takes a value
#i.e. a number, string, etc) x and a list of values a,
#and returns True if x is a member of a, False otherwise.
#(Note that this is exactly what the `in` operator does, but
#for the sake of the exercise you should pretend Python
#id not have this operator.)

def is_member():
    list_a = input("Input a list of values: ").split()
    x = input("Input a number: ")
    if x in list_a:
        return True
    else:
        return False
