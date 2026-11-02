# Removing Stars From a String

def remove_stars(s):
    stack = []

    for ch in s:
        if ch == '*':
            stack.pop()
        else:
            stack.append(ch)

    return ''.join(stack)


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


s = input()
jprint(remove_stars(s))