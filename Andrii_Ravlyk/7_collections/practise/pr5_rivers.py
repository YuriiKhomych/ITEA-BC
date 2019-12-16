'''5. Rivers:
Make a dictionary containing three major rivers and the country each river runs through.
One key-value pair might be `'nile': 'egypt'`.
    * Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
    * Use a loop to print the name of each river included in the dictionary.
    * Use a loop to print the name of each country included in the dictionary.'''

dict_rivers = {"nile":"egypt", "dnepr":"kyiv", "wisla":"poland"}
# Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
for key,value in dict_rivers.items():
    print(f'The {key.title()} runs through {value.title()}')
# Use a loop to print the name of each river included in the dictionary.
for key in dict_rivers.keys():
    print(f'{key.title()}')
# Use a loop to print the name of each country included in the dictionary
for value in dict_rivers.values():
    print(f'{value.title()}')