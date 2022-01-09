#Tambah
def Tambah(n1, n2):
    # print("ini fungsi tambah")
    return n1 + n2
#Kurang
def Kurang(n1, n2):
    # print("ini fungsi Kurang")
    kurang = n1 - n2
    return kurang
#Kali
def Kali(n1, n2):
    # print("ini fungsi Kali")
    return n1 * n2
#Bagi
def Bagi(n1, n2):
    # print("ini fungsi Bagi")
    return n1/n2
# operation
operation = {
    "+" : Tambah,
    "-" : Kurang,
    "/" : Bagi,
    "*" : Kali
}

# main

num1 = int(input("Masukan Bilangan Pertama : "))
num2 = int(input("Masukan Bilangan Kedua : "))

#looping dictionary/object
for symbol in operation:
    print(symbol)

    operation_symbol = input("pick an operation from line above : ").strip() # +
    calculation_function = operation[operation_symbol] # cari data dalam dict operation yang operation symbolnya = +
    answer = calculation_function(num1, num2) # cek fungsi tambah, kemudian jalankan fungsi tambah
    print(f"{num1} {operation_symbol} {num2} = {answer}") # 1 + 2 = 3





#
