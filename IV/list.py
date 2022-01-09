#mencri bilangan genap tertinggi
def highest_even(li):
    even = []
    for item in li:
        if item % 2 == 0:
            even.append(item) # even = [10,2, 4 , 8]
    return max(even) # 10

#main
print(highest_even([10,1,2,3,4,8])) # 10

# convert cent to dollars
# cents : 324
# Result : $3.24

def cent_to_dollar(cents):
    dollar_str = "Invalid Input"

    if len(cents) == 3 and cents.isnumeric():
        dollar_str = "$" + cents[0] + "." + cents[1:]
    return dollar_str

#main
cents = input("Enter 3 digits , please : ")
print(cent_to_dollar(cents))