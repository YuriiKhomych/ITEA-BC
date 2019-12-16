'''4. Person:
    * Use a dictionary to store information about a person you know.
    * Store their first name, last name, age, and the city in which they live.
    * You should have keys such as first_name, last_name, age, and city.
    * Print each piece of information stored in your dictionary.'''

my_dict = {"first_name":"Anna", "last name":"Lee", "age":"21", "city":"Kyiv"}
for key in my_dict.keys():
    print (f'{my_dict[key]}')

