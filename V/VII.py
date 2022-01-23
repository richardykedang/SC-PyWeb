#Polimorfisme

#Inheritance
#Penurunan sifat yang bisa dilakukan secara bertngkat-tingkat dengan mendefinisikan suatu
#kelas baru yang mewarisi sifat dari kelas lain yang sudah ada
#Contoh
class User(object):
    def sign_in(self):
        return 'Logged in'

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'atacking power is {self.power}')

class Archer(User):
    def __init__(self, name, arrow):
        self.name = name
        self.arrow = arrow

    def attack(self):
        print(f'atacking with arrows - arrows left =  {self.arrow}')


wizard1 = Wizard('Merlin', 60)
archer1 = Archer('Robbin', 30)

# def player_attack(char):
#     char.attack()

# player_attack(wizard1)
# player_attack(archer1)

# atau juga
for char in [wizard1, archer1]:
    char.attack()




