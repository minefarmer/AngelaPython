# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)  # [156, 178, 165, 171, 187]
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
# print(len(student_heights))  # 5
# print(sum(student_heights))  # 857

total_height = 0
for height in student_heights:
    total_height += height
print(total_height)  # 857

number_of_students = 0
for students in student_heights:
    number_of_students += 1
print(number_of_students)  # 5

average_height = round(total_height / number_of_students)
print(average_height)  # 171