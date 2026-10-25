# Calculate the Sum of Natural Numbers Using Recursion

n = int(input())

def sum_natural(n):
    # Write your code here
    total = 0
    
    for i in range(n + 1):
        total += i

    return total

print(sum_natural(n))