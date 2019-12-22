# Add a walk() method to Pets, Dog and Cats classes so that when you call the method on the Pets class, # Done
# each dog or cat instance assigned to the Pets class will walk().  # Done
# Start by implementing the method in the same manner as the speak() method.  # Done
# As for the method in the Pets class, you will need to iterate through the list of dogs, then call the method itself.

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

    def walk(self):
        for dog in self.dogs:
            print(f'{dog.walk()}')

    def sound(self):
        for cat in self.cats:
            print(f'{cat.sound()}')



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
        self.is_hungry = False

    def walk(self):
        return f'The {self.name} is wolk now'

    def sound(self):
        return f'The {self.name} says guf-guf'

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
        self.is_hungry = True

    def description(self):
        return self.name, self.age, self.breed

    def my_cats(self):
        return f'The TPC Cats is: {self.breed} name - {self.name} age -{self.age}'

    def eat(self):
        self.is_hungry = False

    def walk(self):
        return f'The {self.name} is wolk now '

    def sound(self):
        return f'The {self.name} says miay-miyau'

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
name_pets.walk()
name_pets.sound()
