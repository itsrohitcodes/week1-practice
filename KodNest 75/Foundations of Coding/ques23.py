# Counting Bits

def count_bits(n):
    # Implement the function here ...
    lst = []
    for i in range(n + 1):
        count = 0
        while i > 0:
            count += i % 2
            i = i // 2

        lst.append(count)

    return lst


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
jprint(count_bits(n))