# Successful Pairs of Spells and Potions

def successful_pairs(spells, potions, success):
    # Write your code here ...
    result = []

    for spell in spells:
        count = 0
        for potion in potions:
            if spell * potion >= success:
                count += 1

        result.append(count)

    return result


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
spells = [ni() for _ in range(n)]

m = ni()
potions = [ni() for _ in range(m)]

success = ni()

jprint(successful_pairs(spells, potions, success))