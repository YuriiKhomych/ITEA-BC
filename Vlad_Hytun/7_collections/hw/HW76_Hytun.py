# 6. Pets: Make several dictionaries, where the name of each dictionary is the name of a pet.
#     * In each dictionary, include the kind of animal and the owner’s name.
#     * Store these dictionaries in a list called pets.
#     * Next, loop through your list and as you do print everything you know about each pet.

Leo = {
    'kind': 'cat',
    'owner': 'Den'
}

Shelli = {
    'kind': 'dog',
    'owner': 'Kat'
}

Kaiser = {
    'kind': 'Big dog',
    'owner': 'Mam'
}

pets_list = [Leo, Shelli, Kaiser]

for pet in pets_list:
    print(pet)