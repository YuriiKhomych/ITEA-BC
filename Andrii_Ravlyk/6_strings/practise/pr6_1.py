"""1. Define a function `generate_n_chars()` that takes an
integer n and a character c and returns a string, n
characters long, consisting only of c:s. For example,
`generate_n_chars(5,"x")` should return the string "xxxxx".
(Python is unusual in that you can actually write an expression `5 * "x"`
that will evaluate to "xxxxx". For the sake of the exercise you should
ignore that the problem can be solved in this manner.)"""

def generate_n_chars(i_n = 2, i_str = "x"):
    if i_n < 1:
        i_n = 1
    res_st = ""
    for i in range(i_n):
        res_st = res_st + i_str
  #  print(res_st)
    return res_st

# generate_n_chars(i_n = 0, i_str = "x")