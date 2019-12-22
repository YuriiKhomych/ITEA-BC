# The function `max()` and `max_of_three()` from previous exercises
# will only work for two and three numbers, respectively.
# But suppose we have a much larger number of numbers,
# or suppose we cannot tell in advance how many they are?
# Write a function max_in_list()
# that takes a list of numbers and returns the largest one.


list = [1, -7, 4, 5, 6, 7, 778]
def max_in_list(list):
    list.sort(reverse=True)
    return list[0]