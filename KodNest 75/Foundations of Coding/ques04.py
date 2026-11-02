# Koko Eating Bananas

def min_eating_speed(piles, h):
    # Write your code here
    left = 1
    right = max(piles)

    while left < right:
        mid = (left + right) // 2
        hours = sum((p + mid - 1) // mid for p in piles)

        if hours <= h:
            right = mid
        else:
            left = mid + 1

    return left


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
piles = [ni() for _ in range(n)]
h = ni()

result = min_eating_speed(piles, h)

jprint(result)