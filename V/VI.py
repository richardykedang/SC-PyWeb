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

class Archer(User):
    def __init__(self, name, arrow):
        self.name = name
        self.arrow = arrow

class Tes():
    def tes():
        return "tes"

wizard1 = Wizard('Merlin', 100)
archer1 = Archer('Robin', 50)
print(wizard1.sign_in())
print(archer1.sign_in())

#pembuktioan apakah kelas turunan
print(isinstance(wizard1,User))
print(isinstance(wizard1,Tes))
print(isinstance(wizard1, object))
