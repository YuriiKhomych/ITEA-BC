# 4. Person:
#     * Use a dictionary to store information about a person you know.
#     * Store their first name, last name, age, and the city in which they live.
#     * You should have keys such as first_name, last_name, age, and city.
#     * Print each piece of information stored in your dictionary.

persona = {
    'first_name': 'Denis',
    'last_name': 'Kornienko',
    'age': 37,
    'city': 'Kiev'
}

print(persona)
for key, values in persona.items():
    print(f'{key} : {values}')