# Can Place Flowers

def can_place_flowers(flowerbed, n):
    # Write your code here ...
    if n == 0:
        return True

    for i in range(len(flowerbed)):
        if flowerbed[i] == 0:
            left = (i == 0) or (flowerbed[i-1] == 0)
            right = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

            if left and right:
                flowerbed[i] = 1
                n -= 1

                if n == 0:
                    return True

    return False


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


m = ni()
flowerbed = [ni() for _ in range(m)]
n = ni()

jprint(can_place_flowers(flowerbed, n))