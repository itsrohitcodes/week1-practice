# Process Data Read from a File.

# Write your code here
n = int(input())
scores = []

for i in range(n):
    score = int(input())

    scores.append(score)

total = 0

for score in scores:
    total += score

print(total)