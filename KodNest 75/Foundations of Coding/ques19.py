# Guess Number Higher or Lower

def guess_number(n):
    # Write your code here ...
    pick = 6
    left = 1
    right = n

    while left <= right:
        mid = left + (right - left) // 2

        if mid == pick:
            return mid
        elif mid < pick:
            left = mid + 1
        else:
            right = mid - 1

    return -1


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
jprint(guess_number(n))