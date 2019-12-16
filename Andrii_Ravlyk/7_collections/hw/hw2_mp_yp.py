'''2. My Pizzas, Your Pizzas:
Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
    * Add a new pizza to the original list.
    * Add a different pizza to the list friend_pizzas.
    * Prove that you have two separate lists.
    * Print the message, My favorite pizzas are:, and then use a for loop to print the first list.
    * Print the message, My friend’s favorite pizzas are:, and then use a for loop to print the second list.
    Make sure each new pizza is stored in the appropriate list.'''
my_pizza = ["margarita", "caprichoza", "neapolitana"]
friend_pizza = my_pizza[:]
my_pizza.append("diablo")
friend_pizza.append("calcone")
print(my_pizza)
print(friend_pizza)

print(f'My favorite pizzas are:')
for pizza in my_pizza:
    print (pizza)
print(f'My friend’s favorite pizzas are:')
for pizza in friend_pizza:
    print (pizza)