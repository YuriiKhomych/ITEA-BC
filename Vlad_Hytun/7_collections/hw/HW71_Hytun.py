# 1. Order your favorite pizza:
#     * Create 3-4 lists with pizza ingredients groups (vegetables, meat_types...).
#     * Create list with predefined pizzas.
#     * Ask user what pizza he want (custom or predefined).
#     * Output variants of pizza or ingredient step by step
#     * Return result of ordered pizza

vegetables = ['paper', 'tomato', 'garlic']
meat_types = ['cow', 'pork', 'chicken']
dough_types = ['thick', 'think']
chees_types = ['parmesan', 'blue', 'chedder', 'mozarella']
predefined_pizzas = ['margarita', 'four_cheese', 'meat mix']

def pizza():
    custom_pizza = []
    pref_or_custom = input('Do you want predefined (Enter 1) pizza or custom (Enter 0)?: ')
    if int(pref_or_custom) == 1:
         pref_pizzas = input(f'What kind pizza do you want {predefined_pizzas}?: ')
         print(f'Good choice my friend: {pref_pizzas}')
    else:
        for dough in dough_types:
            choice_dough = input(f'Enter 1 if you want this one {dough}. Else 0')
            if int(choice_dough) == 1:
                custom_pizza.append(dough)
                break
            else:
                continue
        for veg in vegetables:
            choice_veg = input(f'Enter 1 if you want add this one {veg}. Else 0. "Quit" if you end')
            if choice_veg == 'Quit':
                break
            if int(choice_veg) == 1:
                custom_pizza.append(veg)
            else:
                continue
        for meat in meat_types:
            choice_meat = input(f'Enter 1 if you want add this one {meat}. Else 0. "Quit" if you end')
            if choice_meat == 'Quit':
                break
            if int(choice_meat) == 1:
                custom_pizza.append(meat)
            else:
                continue
        for cheese in chees_types:
            choice_cheese = input(f'Enter 1 if you want add this one {cheese}. Else 0. "Quit" if you end')
            if choice_cheese == 'Quit':
                break
            if int(choice_cheese) == 1:
                custom_pizza.append(cheese)
            else:
                continue
        print(f'Your custom pizza is: {custom_pizza}')

pizza()