# Program Payroll
class Programmer:

    salary = 100000
    monthly_bonus = 500

    def __init__(self, name, umur, address, phone, programming_languages):
        self.name = name
        self.umur = umur
        self.address = address
        self.phone = phone
        self.programming_languages = programming_languages

class Assistant:
    salary = 5000
    monthly_bonus = 200

    def __init__(self, name, umur, address, phone, bilingual):
        self.name = name
        self.umur = umur
        self.address = address
        self.phone = phone
        self.bilingual = bilingual

#Program

# Funtion that prints the montly salary of each other
# and total amount

def calculate_payroll(employees):

    total = 0

    print("\n====================Welcome to our Payroll System =====================\n")

    #Iterate over the list of instance to calculate
    #and display the month salary of each salary
    #and add monthly salary to the total for this month

    for employe in employees:
        salary = round(employe.salary /12, 2) + employe.monthly_bonus
        print(employe.name.capitalize() + " 's salary is: $" + str(salary))
        total += salary

    #Display total
    print("\n The total payroll this motnh will be : $", total)

# Instances (employe)
jack = Programmer("Jack", 45, "Dahlia", "123-456", ["Python", "Java"])
isabel = Programmer("Isabel", 40, "Cempaka", "123-456", ["Javascript"])
nora = Assistant("Nora", 23, "Melati", "654-34", True)

#List instance
employees = [jack, isabel, nora]

#Fucntion call - Passing the list of instnces as argument
calculate_payroll(employees)

