'''1. Order your favorite pizza:
    * Create 3-4 lists with pizza ingredients groups (vegetables, meat_types...).
    * Create list with predefined pizzas.
    * Ask user what pizza he want (custom or predefined).
    * Output variants of pizza or ingredient step by step
    * Return result of ordered pizza'''

ingredients = ["tomato", "salami", "cheese", "basil"]
my_pizza = ["margarita", "caprichoza", "neapolitana"]
type_pizza = input("What pizza do you want custom or predefined print 'C' for custom or 'P' for predefined ? =")
while True:
    if type_pizza == "P":
        name_pizza = input("What pizza do you want 'm' - margarita, 'c' - caprichoza, 'n' - neapolitana  ? =")
        if name_pizza == 'm':
            name_pizza = "margarita"
        elif  name_pizza == 'c':
            name_pizza = "caprichoza"
        else:
            name_pizza = "neapolitana"
        print (f'Your pizza is {name_pizza}')
        break
    elif type_pizza == "C":
        user_ing = []
        for ingr in ingredients:
            add_ingr = input ("Do you want " + ingr + " 'y' or 'n' ? = ")
            if add_ingr == "y":
                user_ing.append(ingr)
        print (f'Your custom pizza with {user_ing}')
        break