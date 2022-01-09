fruits = ["apple", "Peach"]

for item in fruits:
    print(item)

# Mencari siapa yang paling tinggi
# input = 156 178 165 181 171
# output = 181


# spread into
student_height = input("INput List of student Height : ").split() # [156 178 165 181 171]
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
print(student_height)


#find max height
max_height = 0 #
for max in student_height: # mulai dari index[n] dari array student_height
    if max > max_height: # jika nilai max lebih besar dari max_height
        max_height = max # jika true ganti nilai max_height dengan nilai max
print(max_height)



