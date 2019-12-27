'''1. Add for each class (Dog, Cat, etc.) attribute `is_hungry = True`
Then add a method called eat() which changes the value of `is_hungry` to `False` when called.
Create three instance of each class and call `eat` method.'''
class Pets:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        pass


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

barsik = Cat(name="Barsik", age=3)
print ( barsik.name, barsik.hungry,  barsik.eat())
pit = Dog(name="Pit", age=5)
print ( pit.name,pit.hungry,  pit.eat())