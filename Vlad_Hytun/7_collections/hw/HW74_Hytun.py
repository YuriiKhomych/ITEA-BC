#     # Dictionary
# 4. Favorite Numbers:
#     * Use a dictionary to store people’s favorite numbers.
#     * Think of five names, and use them as keys in your dictionary.
#     * Think of a favorite number for each person, and store each as a value in your dictionary.
#     * Print each person’s name and their favorite number.
#     * For even more fun, poll a few friends and get some actual data for your program.

favorite_numbers_dict = {
    "Vlad": "13",
    "Ksu": "26",
    "Katya": "15",
    "Den": "27",
    "Dad": "01",
}

for name, number in favorite_numbers_dict.items():
    print(f'One {name} like {number}')
