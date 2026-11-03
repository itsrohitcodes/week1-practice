# Domino and Tromino Tiling

def num_tilings(n):
    # Implement the function here ...
    MOD = 10 ** 9 + 7

    if n <= 2:
        return n

    a, b, c = 1, 1, 2

    for i in range(3, n + 1):
        a, b, c = b, c, (2 * c + a) % MOD

    return c


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
jprint(num_tilings(n))