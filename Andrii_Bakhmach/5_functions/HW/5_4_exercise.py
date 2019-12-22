# Define a function `sum()` and a function `multiply()` that
# sums and multiplies (respectively) all the numbers in a list
# of numbers. For example, `sum([1, 2, 3, 4])` should return 10,
# and `multiply([1, 2, 3, 4])` should return `24`.
import sys


def res_sum(list_a):
    total_sum = 0
    for item in list_a:
        total_sum += item
    return total_sum


def res_multiplication(list_a):
    total_mult = 0
    for item in list_a:
        total_mult *= item
    return total_mult
