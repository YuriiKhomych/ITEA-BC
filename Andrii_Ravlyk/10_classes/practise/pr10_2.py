'''Create a Pets class that holds instances of dogs, cats;
this class is completely separate from the Dog or Cat classes.
In other words, the Dog or Cats classes does not inherit from the Pets class.
Then assign three dog and cat instances to an instance of the Pets class.'''

class Pets:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        pass


class Cat(Pets):
    __mice = 0

    def speak(self):
        print("Meow!")

class Dog(Pets):
    def speak(self):
        print("Woof!")


barsik = Cat(name="Barsik", age=3)
tom = Cat(name="Tom", age=5)
sharik = Dog(name="Sharik", age=5)

print(f"{barsik.name}, {tom.name}, {sharik.name}")