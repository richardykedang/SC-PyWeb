#Write a Python Program which iterates the integers from 1 - 20
# For multiples of 3 print "Fizz"
# For the multiples 5 print "Buzz"
# For number whinch are multiples 3 x 5 print "FizzBuzz"
# ouput = 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz

#solution

for fixxBuzz in range(1, 21):
    if fixxBuzz % 3 == 0 and fixxBuzz % 5 == 0:
        print("FIzzBUzz")
    elif fixxBuzz % 3 == 0:
        print("Fizz")
    elif fixxBuzz % 5 == 0:
        print("Buzz")
    else:
        print(fixxBuzz)