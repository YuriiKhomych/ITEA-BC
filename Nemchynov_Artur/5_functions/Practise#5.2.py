# 2. Define a function that computes the length of a
# given list or string. (It is true that Python has
# the len() function built in, but writing it yourself
# is nevertheless a good exercise.)

def lenght(string):
    summ = 0
    for i in string:
        summ = summ + 1
        return summ

print = lenght("string")
