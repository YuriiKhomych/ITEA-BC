'''4. Favorite Numbers:
    * Use a dictionary to store people’s favorite numbers.
    * Think of five names, and use them as keys in your dictionary.
    * Think of a favorite number for each person, and store each as a value in your dictionary.
    * Print each person’s name and their favorite number.
    * For even more fun, poll a few friends and get some actual data for your program.'''

fav_numb = {"Tom": "2","Tim": "1","Mark": "3", "Eva": "6", "Anna": "8"}
for key, value in fav_numb.items():
    print(key, value)
