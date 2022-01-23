#Class method dan static method
class PlayerCharacters:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def adding_things1(num1, num2):
        return num1 + num2
    @classmethod
    def adding_things2(cls,num1, num2):
        return cls("Tommy", num1 + num2)

    #Enkapsulasi
    # kombinasi data dan fungsionalitas dalam sebuah unit sebagai bentuk menyembunyikan detail informasi
    def intro(self):
        print(f"hello my name is {self.name}, i'm {self.age} years old")


player1 = PlayerCharacters("cinfdy", 44)
#static method
player_1 = player1.adding_things1(1,3)
print(player1.age)

#class method
player_2 = PlayerCharacters.adding_things2(2,5)
print(player_2.age)

print(player1.intro())