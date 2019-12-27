'''1. Using the same Dog class, instantiate three new dogs, each with a different age and name.
Then write a function called, get_biggest_number(), that takes any number of ages (*args)
and returns the oldest one. Then output the age of the oldest dog like so:
`The oldest dog Sharik is 7 years old.`'''

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
def get_biggest_number(*numbers):
    return max(numbers)

philo = Dog(name="Philo", age=5)
mikey = Dog(name="Mikey", age=6)
tim = Dog(name="Tim", age=7)
max_old = get_biggest_number(philo.age, mikey.age, tim.age)
if philo.age == max_old:
    print (f"The oldest dog {philo.name} is {max_old} years old")
elif mikey.age == max_old:
    print (f"The oldest dog {mikey.name} is {max_old} years old")
else:
    print(f"The oldest dog {tim.name} is {max_old} years old")