"""2. Define a function `is_palindrome()` that recognizes
palindromes (i.e. words that look the same written backwards).
For example, `is_palindrome("radar")` should `return True`."""

def is_palindrome(i_str = "radar"):
    return i_str == i_str[::-1]

# print(is_palindrome())
