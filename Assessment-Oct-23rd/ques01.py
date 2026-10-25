# Calculate the Factorial of a Number Using Recursion

n = int(input())

def factorial(n):
    # Write your code here
    result = 1

    if n == 0 or n == 1:
        return 1

    for i in range(1, n+1):
        result *= i

    return result

print(factorial(n))