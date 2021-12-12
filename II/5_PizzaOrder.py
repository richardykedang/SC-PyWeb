# make pizza order with rules
# small pizza : 15
# Medium : 20
# Large : 25
# extra pperoni for small pizza : +2
# extra pperoni for medium or large pizza : +3
# extra cheese for any pizza : +1

#test case input:
# size : L
# add Peperoni : Y
# extra cheese : N

#output :
# your total bill is 28

#solution

print("Welcome to python pizza delivery")
size = input("what size do you want, L, M, or S").upper()
# print(f"size = {size}")
addPeperoni = input("Do you want Pepperoni ? ").upper()
extraCheese = input("Do you want extra cheese ? ").upper()
bill = 0
#size
if size == "L" :
    bill += 25
elif size == "M" :
    bill += 20
elif size == "S":
    bill += 15
#Peperoni
if addPeperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
# extracheese
if extraCheese == "Y":
    bill += 1

print(f"your total bill is {bill}")

