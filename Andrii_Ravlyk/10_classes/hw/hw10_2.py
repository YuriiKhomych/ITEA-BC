'''2. Add a walk() method to Pets, Dog and Cats classes so that when you call the method on the Pets class,
each dog or cat instance assigned to the Pets class will walk().
Start by implementing the method in the same manner as the speak() method.
As for the method in the Pets class, you will need to iterate through the list of dogs, then call the method itself.'''

class Pets:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        pass
    def walk(self):
        print ('Walk')


class Cat(Pets):
    def __init__(self, name, age, hungry=True):
        Pets.__init__(self, name, age)
        self.hungry = hungry

    def speak(self):
        print("Meow!")

    def eat(self):
        self.hungry = False

class Dog(Pets):
    def __init__(self, name, age, hungry=True):
        Pets.__init__(self, name, age)
        self.hungry = hungry

    def speak(self):
        print("Woof!")

    def eat(self):
        self.hungry = False
#Test
barsik = Dog(name="Barsik", age=3)
pit = Dog(name="Pit", age=5)
tom = Cat(name="Tom", age=2)
pets = [barsik, pit, tom]
for pet in pets:
    print(pet.name)
    pet.walk()