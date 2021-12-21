# create random list to choose who will pay the bill use random module
# input : Jon, Danny, James
# output : Jon will be pay the bills

import random

name = input("Please provide the names with comma separator : ")
print(name) # Jon Danny James
print(name[1]) # o
#split into array
names = name.split(" ")
print(names[1]) # Danny
# names.append("Sumatera")
print(names)


#get total number of list
numItem = len(names)
print(numItem) # 3

#generate random  number between 0 to i
randomChoice = random.randint(0, numItem - 1)
print(randomChoice)

#person who will pay
PersonWhoWillPay = names[randomChoice]
print(PersonWhoWillPay)
print(f"{PersonWhoWillPay} will pays the bill")




