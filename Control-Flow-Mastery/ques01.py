# Skipping Even Numbers

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


maxNumber = ni()

for i in range(maxNumber + 1):
    if i % 2 != 0:
        print(i)