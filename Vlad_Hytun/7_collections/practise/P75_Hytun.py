# 5. Rivers:
# Make a dictionary containing three major rivers and the country each river runs through.
# One key-value pair might be `'nile': 'egypt'`.
#     * Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
#     * Use a loop to print the name of each river included in the dictionary.
#     * Use a loop to print the name of each country included in the dictionary.

rivers_in_country = {
   'Dnipro': 'Ukraine',
   'Nile': 'Egypt',
   'Dynai': 'Romain',
}
for river, country in rivers_in_country.items():
    print(f'The {river} run through {country}')
for river in rivers_in_country.keys():
    print(f'The {river} included in rivers_in_country dict')
for country in rivers_in_country.values():
    print(f'The {country} included in rivers_in_country dict')



