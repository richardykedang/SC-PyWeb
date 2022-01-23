#Given the bellow class

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Expectation
#Print out : "The oldest cat is x years old.."[3,7,2] -> max?

# 1 Instance the cat object with 3 cat
peanut = Cat("Peanut", 3)
garfiled = Cat("Garfield", 7)
snicker = Cat("snickers", 1)
# 2. Create function that finds the oldest cat
#finds the oldest cat
def get_oldest_cat(*args):
    return max(args)
# 3 Print out "The oldest cat is x years old
print(f"The oldest cat is {get_oldest_cat(peanut.age, garfiled.age, snicker.age)} years old")