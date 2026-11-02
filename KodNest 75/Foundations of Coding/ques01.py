# Kids with the Greatest Number of Chocolates

def kids_with_greatest_chocolates(chocolates, extraChocolates):
    lst = []
    maximum = max(chocolates)

    for i in range(len(chocolates)):
        if chocolates[i] + extraChocolates >= maximum:
            lst.append("true")
        else:
            lst.append("false")

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
chocolates = [ni() for _ in range(n)]
extraChocolates = ni()

jprint(kids_with_greatest_chocolates(chocolates, extraChocolates))