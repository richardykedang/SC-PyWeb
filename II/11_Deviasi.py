from math import *

n = int(input("\nBanyaknya Data : "))
data = []
jumlah = 0

for i in range(n):
    print(i) # index ke 0 - 4
    temp = float(input("masukan data ke - %d: " %(i + 1)))
    print(temp)# "12.0, 78.0"
    data.append(temp) # [12.0, 78.0] i0 + i1 + 12 ...in
    print(data)
    jumlah += data[i]
    print(jumlah)
    rata2 = jumlah / n
    print(rata2)

print("Data yang dimasukan (%d data) adalah : " %(n), list(data))
print("Hasil Nilai rata2 : %0.2f" % rata2 )




