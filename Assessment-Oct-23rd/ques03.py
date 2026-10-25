# Student Marks Calculator

total_marks = int(input())
marks = int(input())

def add_marks(marks):
    # Write your code here
    global total_marks
    total_marks = total_marks + marks

add_marks (marks)
print(total_marks)