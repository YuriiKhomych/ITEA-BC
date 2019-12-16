'''3. Buffet:
A buffet-style restaurant offers only five basic foods.
Think of five simple foods, and store them in a tuple.
    * Use a for loop to print each food the restaurant offers.
    * Try to modify one of the items, and make sure that Python rejects the change.
    * The restaurant changes its menu, replacing two of the items with different foods.
    * Add a block of code that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.
    * Use slicing for get last two items of foods.
    * Use slicing for get every second item of food.
    * Reverse your food order.'''
foods = ("tea", "salat1", "salat2", "salat3", "salat4" )
# Use a for loop to print each food the restaurant offers.
for food in foods:
    print(food)
# Try to modify one of the items, and make sure that Python rejects the change.
try:
    foods[1] = "ffff"
except Exception:
    print("Don't try change tuple")
# Add a block of code that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.
foods = ("tea", "salat1", "salat2", "salat5", "salat6")
for food in foods:
    print (food)
# Use slicing for get last two items of foods.
print(foods[-2:])
# Use slicing for get every second item of food.
print(foods[1::2])
# Reverse your food order.
r_foods = [i for i in foods]
r_foods.reverse()
print(r_foods)
# or
print (foods[::-1])
