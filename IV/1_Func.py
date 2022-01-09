# # Fungsi
# # membuat fungsi cost
# def nama_fungsix():
#     #return "Hello World"
#     print ("Hello World")

# # main
# # x = nama_fungsix()
# # print(x)

# # print(nama_fungsix())

# # kalau pakai print
# nama_fungsix()

# # parameter atau argument
# # total  = price * amount
# def cost(price, amount):
#     total  = price * amount
#     #return price * amount
#     return total

# # main
# print(cost(5000, 2))

# # combine input
# def prime_checker(number):
#     #print ("parameter exist")
# #flag
#     is_prime = True
# #logic find prime number
#     for i in range(2, number): # looping range 2 s/d 10
#         print(i) # 2- 10
#         if number % i == 0: # Jika 10 % i
#             is_prime = False
# #validasi
#     if is_prime:
#         print("It's prime number")
#     else:
#         print("Not Prime Number")

# #main
# n = int(input("Check number : "))
# prime_checker(n)


# jika inputan ada isinya print parameter, jika tidak retrun not valid input
def formated_name(f_name, last_name):
    # validasi false
    tes = ["", "@"] # tes = ""@
    for x in tes:
        # print(tes)
        if f_name == x or last_name == x:
            return "You didnt provide valid input"
        formated_fname = f_name.title() # mr
        formated_lname = last_name.title() # Tono
        return f"Result : {formated_fname} {formated_lname}"

#main
fisrt = (input("what's is your first name : "))
last = (input("what's is your last name : "))
# print(formated_name(input("what's is your first name : "), input("what's is your last name : ")))
print(formated_name(fisrt,last))








