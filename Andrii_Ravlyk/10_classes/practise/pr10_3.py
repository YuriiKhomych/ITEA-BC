'''3. Create base class `Vehicle` with main methods and attributes that share to other child classes.
Create 2-3 child classes. Create 2-3 methods and attributes in child classes.
Create 2-3 instances of each class and try to call each method.'''


class Vehicle:
     def __init__(self, manufacturer, radius):
        self.manufacturer= manufacturer
        self.radius = radius
     def move_vehicle(self):
         print (f"Move {self.manufacturer}")
class Car_vehicle(Vehicle):
    def __init__(self, manufacturer, radius, car_name):
        Vehicle.__init__(self, manufacturer, radius)
        self.season = car_name
    def get_diametr(self):
        return self.radius*2
class Byke_vehicle(Vehicle):
    def __init__(self, manufacturer, radius, bike_name, season):
        Vehicle.__init__(self, manufacturer, radius)
        self.season = bike_name
        self.season = season
    def get_count_vehicle(self):
        return 2

car_vehicle1 = Car_vehicle('Nokian', 10, 'Audi')
car_vehicle1.move_vehicle()
byke_vehicle1 = Byke_vehicle('Noname', '5', 'Comanche', 'winter')
print ('diametr', car_vehicle1.get_diametr())
print ('count_vehicle', byke_vehicle1.get_count_vehicle() )