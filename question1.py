# Electricity Bill Calculator

# Input
customer_name = input()
units = float(input())

# First 100 Units = units * 2
# Next 100 Units = units * 3
# ABove 200 units = units * 5

# bill calculator
if units <= 100:
    total_bill = units * 2
elif units <= 200:
    total_bill = (100 * 2) + ((units - 100) * 3)
else:
    total_bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)

if total_bill > 1000:
    subcharge = total_bill * 0.05
    final_bill = subcharge + total_bill
else:
    surcharge = 0
    final_bill = total_bill

print(f"Customer Name: {customer_name}")
print(f"Units Consumed: {units}")
print(f"Electricity Charge: {total_bill}")
print(f"Surchagre: {surcharge}")
print(f"Final Bill: {final_bill}")