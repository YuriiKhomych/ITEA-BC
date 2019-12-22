"""3. Define a function `overlapping()` that takes two lists and
returns True if they have at least one member in common,
False otherwise. You may use your `is_member()` function,
or the in operator, but for the sake of the exercise,
you should (also) write it using two nested for-loops."""
def overlapping(list1, list2):
    a = False
    for i in list1:
        if a == False:
            for j in list2:
                if i == j:
                    a = True
                    break
        else:
            break
    return a

# print(overlapping(["e","k"],["c","d","b"]))
