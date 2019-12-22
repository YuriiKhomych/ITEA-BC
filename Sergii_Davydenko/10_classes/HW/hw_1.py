# Add for each class (Dog, Cat, etc.) attribute `is_hungry = True` # Done
# Then add a method called eat() which changes the value of `is_hungry` to `False` when called.
# Create three instance of each class and call `eat` method.

# Create a Pets class that holds instances of dogs, cats; this class is completely separate from the Dog or Cat classes.
# In other words, the Dog or Cats classes does not inherit from the Pets class.
# Then assign three dog and cat instances to an instance of the Pets class.

# Maybe Done


class Pets:
    dogs = []
    cats = []

    def __init__(self, dogs, cats):
        self.dogs = dogs
        self.cats = cats

    def my_dogs(self):
        for dog in self.dogs:
            print(dog.my_dogs())

    def my_cats(self):
        for cat in self.cats:
            print(cat.my_cats())

    def eat(self):
        for dog in self.dogs:
            if dog.is_hungry == False:
                print(f'Some dogs hungry - {dog.is_hungry == False}')
            else:
                print(f'All dogs full - {dog.is_hungry}')

        for cat in self.cats:
            if cat.is_hungry == False:
                print(f'Some cats hungry {cat.is_hungry == False}')
            else:
                print(f'All cats full - {cat.is_hungry}')


class Dog:

    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age
        self.is_hungry = True

    def descriptions(self):
        return self.age, self.name, self.breed

    def my_dogs(self):
        return f'The TPC Dogs is: {self.breed} name - {self.name} age -{self.age}'

    def eat(self):
        return self.is_hungry == False

class Taxa(Dog):
    def guf(self):
        return f'{self.breed}, {self.name}, {self.age}'

class Rassel(Dog):
    def guf(self):
        return f'{self.breed}, {self.name}, {self.age}'


class Cat:

    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age
        self.is_hungry = False

    def description(self):
        return self.name, self.age, self.breed

    def my_cats(self):
        return f'The TPC Cats is: {self.breed} name - {self.name} age -{self.age}'

    def eat(self):
        return self.is_hungry == False

class Bengal(Cat):
    def miay(self):
        return f'{self.breed}, {self.name}, {self.age}'

class Bombay(Cat):
    def miay(self):
        return f'{self.breed}, {self.name}, {self.age}'


my_dog = [
    Taxa('taxa', 'Hot-dog', 12),
    Rassel('rassel', 'Lucky', 10),
]

my_cat = [
    Bengal('Bengal cat', 'Tomas', 9),
    Bombay('Bombay cat', 'Jerry', 6),
]


name_pets = Pets(my_dog, my_cat)
# name_pets.my_dogs()
# name_pets.my_cats()

print(name_pets.eat())

# def eat(self):
#     for dog in self.dogs:
#         for cat in self.cats:
#             if dog.is_hungry == False | cat.is_hungry == False:
#                 print(f'Some dogs hungry - {dog.is_hungry} \nSome cats hungry {cat.is_hungry}')
#             else:
#                 print(f'All pets full - {dog.is_hungry}')





