# Create base class Vehicle with main methods and attributes that share to other child classes. # Done
# Create 2-3 child classes. # DOne
# Create 2-3 methods and attributes in child classes. # Done
# Create 2-3 instances of each class and try to call each method.

# Maybe Done

class Vehicle:

    def __init__(self, color, year, fuel, speed, model):
        self.color = color
        self.year = year
        self.fuel = fuel
        self.speed = speed
        self.model = model


    def car_speed(self):
        return f'The speed of {self.model} car is {self.speed} km/h'

    def what_fuel(self):
        return f'This {self.model} use {self.fuel}'

    def who_fust(self):
        return f'The fust car is {self.model} and the max speed is {self.speed}'


class Pontiac(Vehicle):
    def __init__(self, color, year, fuel, speed, model):
        super().__init__(color, year, fuel, speed, model)
        self.tank = 60

    def pon_tank(self):
        print(f'The tanks of {self.model} have {self.tank} litres')

    def who_fust(self):
        return self.speed


class Lamba(Vehicle):
    def speed(self):
        return self.model, self.speed


class Porsh(Vehicle):
    def speed(self):
        return self.model, self.speed


pontiac = Pontiac('Black', 2008, 'gas', 300, 'Pontiac G8 GXP')
lamba = Lamba('yellow', 1998, 'petrol', 450, 'Lambo V12')
porsh = Porsh('black', 1999, 'rocket fuel', 500, 'Porshe 911')

pontiac.pon_tank()
print(pontiac.car_speed())
print(lamba.what_fuel())
print(porsh.who_fust())
