# Process Values Using next()

n = int(input())
quantities = list(map(int, input().split()))
k = int(input())

# Write your code here
it = iter(quantities)
total = 0

for i in range(min(k, n)):
    total += next(it)

print(total)