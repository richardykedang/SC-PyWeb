#List / array fungsinya untuk menyimpan banyak objek
IndonesiaProv = ["Jakarta", "Bali", "Jawatimur"]
print(IndonesiaProv[0] )# Jakarta

#get last array // Jawatimur
print(IndonesiaProv[2])
print(IndonesiaProv[-1])

#add new single element from the last index
IndonesiaProv.append("Sumatera") # Jakarta", "Bali", "Jawatimur, Suatera
print(IndonesiaProv)

#add new multiple element from the last index
IndonesiaProv.extend(["Sulawesi", "DKI"])
print(IndonesiaProv)
