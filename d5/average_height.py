#Input a Python list of student heights 
sum = 0
students = 0

student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    sum += student_heights[n]
    students += 1

average_height = sum / students

print(f"Total height: {sum}")
print(f"Number of students: {students}")
print(f"Average height: {average_height.__round__()}")

