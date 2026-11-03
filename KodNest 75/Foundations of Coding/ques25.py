# Minimum Flips to Make A OR B Equal to C

def min_flips(a, b, c):
    # Implement the function here ...
    flips = 0

    while a > 0 or b > 0 or c > 0:
        x, y, z = a % 2, b % 2, c % 2

        if z == 1 and x == 0 and y == 0:
            flips += 1
        elif z == 0:
            flips += x + y

        a //= 2
        b //= 2
        c //= 2

    return flips


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

jprint(min_flips(a, b, c))