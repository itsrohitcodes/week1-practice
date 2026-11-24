# Check Increasing, Decreasing, or Neither

def jprint(x):
    if isinstance(x, bool):
        print("true" if x else "false")
    elif isinstance(x, list):
        def conv(v):
            if isinstance(v, bool):
                return "true" if v else "false"
            if isinstance(v, list):
                return "[" + ", ".join(conv(i) for i in v) + "]"
            return str(v)

        print("[" + ", ".join(conv(i) for i in x) + "]")
    else:
        print(x)


import sys

data = sys.stdin.read().split()
it = iter(data)

def ni():
    return int(next(it))

def ns():
    return next(it)

a = ni()
b = ni()
c = ni()

if a < b < c:
    print("Increasing")
elif a > b > c:
    print("Decreasing")
else:
    print("Neither")