print("Welcome to the ROller Coaster")
height = int(input("what's is your height in cm : ")) #110
age = int(input("what's your age : ")) #19
bill = 0

if height > 120:
    print("You can ride the roller coaster")
    if age < 12: # 0 - 11
        bill = 5
        print("please pay 5")
    elif age < 18: # 12 - 18
        bill = 7
        print("please pay 7")
    elif age >= 44 and age <= 55:
        print("Everything is free")
    else: # 19 - N
        bill = 12
        print("Please pay 12")
    photo = input("Do you want a photo taken ? Y or N ")
    if photo == "Y" or photo == "y":
        # bill = bill + 3 # 10
        bill += 3
        print(f"your bill is {bill}")
    else:
        print(f"your bill is {bill}")
else:
    print("Sorry you hv to grow taller")

