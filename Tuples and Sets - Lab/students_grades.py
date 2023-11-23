number_of_students = int(input())
students_info = {}

for line in range(number_of_students):
    name, grade = input().split()
    if name not in students_info:
        students_info[name] = []
    students_info[name].append(float(grade))

for names, grades in students_info.items():
    student_grade = ' '.join([f"{grade:.2f}" for grade in grades])
    average_grade = sum(grades)/len(grades)
    print(f"{names} -> {student_grade} (avg: {average_grade:.2f})")