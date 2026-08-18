def calculate_salary(basic_salary, bonus_percentage=5):
    bonus_amount = basic_salary * bonus_percentage / 100
    final_salary = basic_salary + bonus_amount

    return bonus_amount, final_salary


employee_name = input("Enter employee name: ")
basic_salary = int(input("Enter basic salary: "))

special_bonus = input("Does the employee have a special bonus? ")

if special_bonus.strip().lower() == "yes":
    bonus_percentage = int(input("Enter bonus percentage: "))
    bonus_amount, final_salary = calculate_salary(
        basic_salary, bonus_percentage
    )
else:
    bonus_percentage = 5
    bonus_amount, final_salary = calculate_salary(basic_salary)

print("\nEmployee Name:", employee_name)
print("Basic Salary:", basic_salary)
print("Bonus Percentage:", bonus_percentage)
print("Bonus Amount:", bonus_amount)
print("Final Salary:", final_salary)