student_name = input("Enter student name: ")
marks = []

for _ in range(5):
    mark = int(input("Enter mark: "))
    marks.append(mark)

total_marks = sum(marks)
average_marks = total_marks / len(marks)
highest_mark = max(marks)
lowest_mark = min(marks)

passed = 0
failed = 0

for mark in marks:
    if mark >= 40:
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

print("\nStudent Name:", student_name)
print("Total Marks:", total_marks)
print("Average Marks:", f"{average_marks:.2f}")
print("Highest Mark:", highest_mark)
print("Lowest Mark:", lowest_mark)
print("Subjects Passed:", passed)
print("Subjects Failed:", failed)
print("Final Grade:", grade)

print("\nMarks greater than average:")
for mark in marks:
    if mark > average_marks:
        print(mark)