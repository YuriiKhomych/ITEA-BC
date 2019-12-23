# . Define a function `max()` that takes two numbers as arguments
# and returns the largest of them. Use the if-then-else construct
# available in Python. (It is true that Python has the `max()` function
# built in, but writing it yourself is nevertheless a good exercise.)"""
def max_in_list(lst):
  max = 0
  for n in lst:
    if n > max:
      max = n
  return max

print(max_in_list([2,3,4,5,6,7,8,8,9,10]))
print(max_in_list([38,2,3,4]))
print(max_in_list([9,2,3,4,28]))