# Equal Row and Column Pairs

# Write your code here
def equal(grid):
    n = len(grid)
    count = 0

    for row in grid:
        for col in range(n):
            equal = True

            for i in range(n):
                if row[i] != grid[i][col]:
                    equal = False
                    break

            if equal:
                count += 1

    return count


n = int(input())
grid = []

for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

result = equal(grid)

print(result)