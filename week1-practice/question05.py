# Employee Salary Calculator using a Default Arguments

def calculate_salary(basic_salary, bonus_percentage=5):
    bonus_amount = basic_salary * bonus_percentage / 100
    final_salary = basic_salary + bonus_amount

    return bonus_amount, final_salary


employee_name = input()
basic_salary = int(input())

special_bonus = input()

if special_bonus == "yes" or special_bonus == "Yes" or special_bonus == "Yes":
    bonus_percentage = int(input())
    bonus_amount, final_salary = calculate_salary(basic_salary, bonus_percentage)
else:
    bonus_percentage = 5
    bonus_amount, final_salary = calculate_salary(basic_salary)

print("Employee Name:", employee_name)
print("Basic Salary:", basic_salary)
print("Bonus Percentage:", bonus_percentage)
print("Bonus Amount:", bonus_amount)
print("Final Salary:", final_salary)