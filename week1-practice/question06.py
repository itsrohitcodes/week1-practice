# Function-Based Number List Analyzer

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


# Take input from user
numbers = input()
numbers = numbers.split()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

# Call the function
total, average, highest, lowest, even_count, odd_count = analyze_numbers(numbers)

# Display results
print("Sum of Numbers:", total)
print("Average:", average)
print("Highest Number:", highest)
print("Lowest Number:", lowest)
print("Even Number Count:", even_count)
print("Odd Number Count:", odd_count)

# Find numbers above average
above_average = numbers_above_average(numbers, average)

print("Numbers Above Average:", above_average)