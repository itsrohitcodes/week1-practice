# QUESTION 01

# Take input from the user
customer_name = input()
units = int(input())

# Calculate electricity charge
if units <= 100:
    electricity_charge = units * 2
elif units <= 200:
    electricity_charge = (100 * 2) + (units - 100) * 3
else:
    electricity_charge = (100 * 2) + (100 * 3) + (units - 200) * 5

# Calculate surcharge
if electricity_charge >= 1000:
    surcharge = electricity_charge * 0.05
else:
    surcharge = 0

final_bill = electricity_charge + surcharge

# Print bill
print(f"Customer Name: {customer_name}")
print(f"Units Consumed: {units}")
print(f"Electricity Charge: {electricity_charge:.2f}")
print(f"Surcharge: {surcharge:.2f}")
print(f"Final Bill: {final_bill:.2f}")