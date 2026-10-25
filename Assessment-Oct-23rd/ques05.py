# Calculate the Area of Different Shapes

x = int(input())
y = int(input())

def area(x, y=0):
    # Write your code here
    if y == 0:
        return x * x
    else:
        return x * y

if y == 0:
    print(area(x))
else:
    print(area(x, y))