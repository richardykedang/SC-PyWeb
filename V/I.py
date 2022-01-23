#OOP / object oriented programming
#Tujuan
# mempermudah melakukan pengemangan program
#class - program karakter game
# di dalam class = atribut/property = value/, method / function = logic
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.y = age

    def run(self):
        return "run"

    def intro(self):
        print(f"hello my name is {self.name}, i'm {self.y} years old")


#objek
player1 = PlayerCharacter("cindy", 44)
print(player1.name) # expectation = print nama dari player 1
print(player1.run()) # expectation = jalankan fungsi run

player2 = PlayerCharacter("Tom", 21)
player2.attack = 50
print(player1.attack)
print(player2.attack)

#expectation
#"Hello my name is {name}, im {age} years old"
print(player1.intro())



