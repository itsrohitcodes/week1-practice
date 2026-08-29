# QUESTION 05

# Function to calculate salary
def calculate_salary(basic_salary, bonus_percentage):
    bonus_amount = basic_salary * bonus_percentage / 100
    final_salary = basic_salary + bonus_amount

    return bonus_amount, final_salary

# Take input from the user
employee_name = input()
basic_salary = int(input())

special_bonus = input("Does the employee have a special bonus? ")

if special_bonus.strip().lower() == "yes":
    bonus_percentage = int(input())
else:
    bonus_percentage = 5

bonus_amount, final_salary = calculate_salary(basic_salary, bonus_percentage)

# Print the results
print(f"Employee Name: {employee_name}")
print(f"Basic Salary: {basic_salary}")
print(f"Bonus Percentage: {bonus_percentage}")
print(f"Bonus Amount: {bonus_amount}")
print(f"Final Salary: {final_salary}")