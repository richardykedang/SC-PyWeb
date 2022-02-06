class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking'

class Simon(Cat):
    def sing(self, sound):
        return f'{sound}'

class Sally(Cat):
    def sing(self, sound):
        return f'{sound}'

class tes(Cat):
    def sings(self, sound):
        return f'{sound}'
#1 Add another cat
class Suzy(Cat):
    def sing(self, sound):
        return f'{sound}'
#2 create list of all the pets (create 3 cat instances from above)
my_cats = [Simon('Simon', 4), Sally('Sally', 21), Suzy('Suzy',1), tes('Tes',3)]

#3 Instantiate the pet class with all your cat use variable my_pets
my_pets = Pets(my_cats)

#4 output all of the cats singing using my_pets instance
my_pets.walk()

