# 3. Buffet:
# A buffet-style restaurant offers only five basic foods.
# Think of five simple foods, and store them in a tuple.
#     * Use a for loop to print each food the restaurant offers.
#     * Try to modify one of the items, and make sure that Python rejects the change.
#     * The restaurant changes its menu, replacing two of the items with different foods.
#     * Add a block of code that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.
#     * Use slicing for get last two items of foods.
#     * Use slicing for get every second item of food.
#     * Reverse your food order.

basic_foods = ('borsch', 'soop', 'beef', 'burger', 'hamburger')
for food in basic_foods:
    print(food)
# basic_foods[1] = 'pasta'
basic_foods = ('borsch', 'ice-cream', 'pasta', 'burger', 'hamburger')

print(basic_foods[-2::])
print(basic_foods[0::2])
# basic_foods.reverse()
