# First Occurrence Index Finder

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


n = ni()
m = ni()

lst = [ni() for i in range(m)]

found = False

for i in range(m):
    if lst[i] == n:
        print(i)
        found = True
        break

if not found:
    print(-1)