'''6. Pets: Make several dictionaries, where the name of each dictionary is the name of a pet.
    * In each dictionary, include the kind of animal and the owner’s name.
    * Store these dictionaries in a list called pets.
    * Next, loop through your list and as you do print everything you know about each pet.'''

cats = {"cat1": "Mike"}
dogs = {"dog1": "Tom"}
pets = [cats, dogs]
for pet in pets:
    for key, value in pet.items():
        print (key.title() + " is the pet of", value)