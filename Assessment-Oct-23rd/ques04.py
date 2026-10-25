# Simple Calculator Using Function Overloading

a = int(input())
b = int(input())
c = int(input())

def add(a, b, c=0):
    # Write your code here
    if c == 0:
        return a + b
    else:
        return a + b + c

if c == 0:
    print(add(a, b))
else:
    print(add(a, b, c))