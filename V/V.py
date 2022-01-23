#Method lainnya
#Method __str__() akan di panggil ketika sebuah instan dari kelas yang bersangkutan
#di konversikan menjadi string atau ketika di jadikan parameter untuk fungsi print()
#contoh
class Segitiga:
    def __init__(self, a, t):
        self.alas = a
        self.tinggi = t

#buat instan
a = Segitiga(10,10)
b = Segitiga(20, 10)

print(a)
print(b)

#solusi convert hexa to string
class Segitiga:
    def __init__(self, a, t):
        self.alas = a
        self.tinggi = t

    def __str__(self):
        luas = 0.5 * self.alas * self.tinggi
        return f'segitiga (alas = {self.alas} tinggi = {self.tinggi} luas = {luas})'

#buat instan
a = Segitiga(10,10)
b = Segitiga(20, 10)

print(a)
print(b)

#Method __len__()
# Ia adalah sebuah method yang akan di panggil ketika sebuah objek atau instan
#di jadikan parameter untuk fungsi bawaan python len()
#Contoh
class siswa:
    def __init__(self):
        self.__list_siswa = []

    def tambah_siswa(self, siswa):
        self.__list_siswa.append(siswa)

    def __len__(self):
        return len(self.__list_siswa)

    def  __getitem__(self, position):
        return self.__list_siswa[position]

group1 = siswa()
group1.tambah_siswa('Huda')
group1.tambah_siswa('Joni')
group1.tambah_siswa('Joni')
print(len(group1)) # 2

#Method __getitem__()
#Fungsi __getitem adalah sebuah fungsi yang akan dipanggil ketika sebuah instan dari kelas yang kita buat
#dipanggil menggunakan indeks yang diapit dengan kurung siku[]

print(group1[0])
