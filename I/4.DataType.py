# String
# print("hello")
#get first element of the string
# print("hello"[0])

# number
# int & float
print(type(2+4)) # int 6
print(type(2-4)) # int -2
print(type(2/4))# float 0.5
print(type(2*4))# int 8
print(type(20+1.1))# float 21.1

# bilangan berpangkat
print(1 + 2**3) # 1 + 2^3 = 1 + 2*2*2 = 9
# modulus atau sisa pembagian
print(7 % 4)  # 3
print(6 % 4) # 2
print(8 % 4) # 0

# Math function
import math
print(round(2.5)) # 2 pembulatan kebawah
print(math.ceil(2.5)) # 3 pembulatan ke atas
print(math.floor(2.9)) # 2 pembulatan kebawah

# operator precendence = prosedur mana yg harus diutamakan dahulu
print(2+3*4) # 20 & 14
# () ,*, /, +, -,

presedence = (20 - 3) + 2 ** 2
print(presedence)

# assigmnet operator =
some_value = 5
# some_value = some_value + 2
some_value += 2 # 7
# some_value -= 2 # 3

print(some_value) # 7


# string
uname = 'superUser'
password = 'superPwd'
print(f"Username = {uname} password = {password}")
longstring = '''
WOW
0 0
___
'''
print(longstring)

# concat
first_name = 'ucup'
last_name = 'ganteng'
fullname = first_name + last_name #ucupganteng
fullname_concat = first_name +' '+last_name
print(fullname)
print(fullname_concat)

#escape string
# case
#wheater = "It's "kind of "sunny"
# wheater = "It's "kind of "sunny"
wheater = "\t It\'s \"kind of \"sunny\n hope you hv a good day"
print(wheater)

# formated string
username = "jony"
age = 11
# print('hi' + ' '+ username + 'you are' + str(age))
print(f'hi {username} you are {age}')

selfish = 'me me me'
_selfish = 'testing'
          #01234567
print(selfish[4]) # e

#[start:end]
print(_selfish[0:2]) # te

number = '012345678'
        # 012345678
print(number[0:5:2])# 0 2 4 6 8
print(number[-1])
print(number[::-1])

# built in function
quote = 'to be or not to be'

print(quote.upper()) #capital letters
print(len(quote)) #18
print(quote.find('be'))
print(quote.replace('be','me'))
print(quote) #to be or not to be, sifatnya immutable/tdk bisa di replace kecuali di assign ke new variable

# datetime
import datetime
now = datetime.datetime.now()
nows = datetime.datetime.now()
print(now.day)
birth_year = input('what year you were born ?')
print(type(birth_year))
age = now.year - int(birth_year)
print(age)

# password checker program
# case
# ('jay')
#('secret')
#print({username}, your {******} is {6} letter long)
print('*'*2) # **

uname = input('Please input username : ')
pwd = input('Please input password : ')
pwd_length = len(pwd)
hidden = '*' * pwd_length

print(f'{uname}, your {hidden} is {pwd_length} letter long')

# list
tokopedia = ['notebook', 'sunglasses', 3]
print(tokopedia[1])

#list slicing
print(tokopedia[0::2]) # 'notebook', 3

matrix = [
    [1,5,1],
    [0,1,0],
    [1,0,1]
]

print(matrix[1][2]) # 0

basket = [
    "banana",
    ["Apples",["Oranges"], "Blueberries"]
    ]
print(basket[1][1][0])
print(basket[1][2])




