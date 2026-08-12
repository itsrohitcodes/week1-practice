# Student marks and grade analyzer

student_name = input()
marks = []

for i in range(5):
    mark = int(input())
    marks.append(mark)

total_marks = sum(marks)
average_marks = total_marks / 5
highest_mark = max(marks)
lowest_mark = min(marks)
passed = 0
failed = 0

for i in marks:
    if i >= 40:
        passed += 1
    else:
        failed += 1

if average_marks >= 90:
    grade = "A"
elif average_marks >= 75:
    grade = "B"
elif average_marks >= 60:
    grade = "C"
elif average_marks >= 40:
    grade = "D"
else:
    grade = "F"

print("Student Name:", student_name)
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
print("Highest Mark:", highest_mark)
print("Lowest Mark:", lowest_mark)
print("Subjects Passed:", passed)
print("Subjects Failed:", failed)
print("Final Grade:", grade)

print("Marks greater than average:")
for mark in marks:
    if mark > average_marks:
        print(mark)