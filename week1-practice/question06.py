def analyze_numbers(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    highest = max(numbers)
    lowest = min(numbers)

    even_count = 0
    odd_count = 0

    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return total, average, highest, lowest, even_count, odd_count

def numbers_above_average(numbers, average):
    result = []

    for num in numbers:
        if num > average:
            result.append(num)

    return result


numbers = [int(num) for num in input().split()]

total, average, highest, lowest, even_count, odd_count = analyze_numbers(numbers)

print(f"Sum of Numbers: {total}")
print(f"Average: {average:.2f}")
print(f"Highest Number: {highest}")
print(f"Lowest Number: {lowest}")
print(f"Even Number Count: {even_count}")
print(f"Odd Number Count: {odd_count}")

above_average = numbers_above_average(numbers, average)
print(f"Numbers Above Average: {above_average}")