# input(masukan tinggi badan : 115)
# if tinggi badan >= 115 ? Youc can ride : sorry you hv to grow taller
# if (tinggi badan = true) , if age < 12? pay 5, age <= 18 ? 7, else pay 12

print("Welcome to the ROller Coaster")
height = int(input("what's is your height in cm : ")) #110
age = int(input("what's your age : ")) #18

if height >= 115: # int >= int
    print("you can ride the roller coaster")
    if age < 12 : # 1 - 11
        print("Please pay 5")
    elif age <= 18 : # 12 - 18
        print("Please pay 7")
    elif age <= 30 : # 19 - 30
        print("Please pay 10")
    else: # 19 - xxx
        print("Please pay 12")

else:
    print("Sorry you hv to grow taller")

#  case 1 = height 110
