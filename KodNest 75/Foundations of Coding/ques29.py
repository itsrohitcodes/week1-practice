# String Compression

def compress(chars):
    # Write your code here ...
    result = []
    i = 0

    while i < len(chars):
        count = 1

        while i + 1 < len(chars) and chars[i] == chars[i+1]:
            count += 1
            i += 1

        result.append(chars[i])

        if count > 1:
            result.append(str(count))

        i += 1

    chars[:] = result

    return len(chars)


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
chars = [ns() for i in range(n)]

jprint(compress(chars))