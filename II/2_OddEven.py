# modulus
#  7 % 3 = 1 / 3 + 3 + 1
#  7 % 2 = 1 / 2 + 2 + 2 + 1
# 6 % 2 = 0 / 2 + 2 + 2

print(7 % 3)
print(6 % 2)

# user Provide your number
#  cek input == genap ? genap : ganjil

Number = int(input("Provide your number : "))

if Number % 2 == 0 :
    print(f"{Number} is genap")
else:
    print(f"{Number} is ganjil")

# pengecekan 1 to N
# Please Enter any Maximum Number : 10
# output : 1,3,5,7,9

num = int(input("Please Enter any Maximum Number :"))

for x in range(1, num): #1,2,3,4,5 - 10
    if x % 2 == 0: # apakah 1 % 2 tdk sama dengan 0 /1,3,5 - 10
        print(x)
    # else:
    #     print(f"ganjil {x}")


# for, while, do while
# #  C#, javascript, php
# for(x = 1; x < 10; x++) {
#     if (x % 2 != 0 ) {
#         print(x)
#     }
# }

