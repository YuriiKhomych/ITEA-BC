# Create a Pets class that holds instances of dogs, cats; this class is completely separate from the Dog or Cat classes.
# In other words, the Dog or Cats classes does not inherit from the Pets class.
# Then assign three dog and cat instances to an instance of the Pets class.

# Done


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

class Dog:
    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age

    def descriptions(self):
        return self.age, self.name, self.breed

    def my_dogs(self):
        return f'The TPC Dogs is: {self.breed} name - {self.name} age -{self.age}'

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

    def description(self):
        return self.name, self.age, self.breed

    def my_cats(self):
        return f'The TPC Cats is: {self.breed} name - {self.name} age -{self.age}'

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
name_pets.my_dogs()
name_pets.my_cats()
