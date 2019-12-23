# Define a function `overlapping()` that takes two lists and
# returns True if they have at least one member in common,
# False otherwise. You may use your `is_member()` function,
# or the in operator, but for the sake of the exercise,
# you should (also) write it using two nested for-loops

def overlapping():
    list_1 = input("Please, input list of numbers: ").split()
    list_2 = input("Please, input list of numbers: ").split()
    for i in list_1:
        for z in list_2:
            if z == i:
                return True
            else:
                return False