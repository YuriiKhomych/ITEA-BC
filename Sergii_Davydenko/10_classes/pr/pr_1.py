#
# Using the same Dog class, instantiate three new dogs, each with a different age and name.
# Then write a function called, get_biggest_number(), that takes any number of ages (* args)
# and returns the oldest one.Then output the age of the oldest dog like so:
#
# The oldest dog Sharik is 7 years old.

# Done 50% WHERE IS SHARIK

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


sharpey = Dog('Jack', 12)
taxa = Dog('Hot-dog', 5)
alabai = Dog('SQL', 20)
toy = Dog('Tanos', 4)

def get_biggest_number(*args):
    return max(args)

print(f'The oldest dog is {get_biggest_number(sharpey.age, toy.age, taxa.age, alabai.age)}')


# my_dog = [
#     sharpey('Jack', 12),
#     taxa('Hot-dog', 5),
#     alabai('SQL', 20),
#     toy('Tanos', 4),
# ]

# print(f'The oldest dog is {get_biggest_number(sharpey.age, sharpey.name, toy.age, toy.name, taxa.age, taxa.name, alabai.age, alabai.name)}')