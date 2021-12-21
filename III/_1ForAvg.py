#Menghitung tinggi rata2 dari setiap anak
# input = 156 178 165 171 181
# output = Totalinput / n

# spread into array
student_height = input("input List of student Height : ").split()
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
    print(student_height[n]) # 0 - 4

print(student_height)

#find length array
number_of_student = len(student_height)
print(number_of_student) #5
print(type(student_height))

# number_of_student = 0
# for student in student_height:
#     print(f"student = {student}")
#     number_of_student += 1 # number_of_student = number_of_student + student
# print(number_of_student)

#find total sum
total_height = sum(student_height)

print(total_height)

# total_height = 0
# for height in student_height:
#     total_height += height
# print(total_height)

#find avg
avg_height = round(total_height / number_of_student)
print(avg_height)



