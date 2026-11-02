# Decode String

def decode_string(s):
    # Write your code here ...
    stack = []
    current = ""
    number = 0

    for ch in s:
        if ch.isdigit():
            number = number * 10 + int(ch)

        elif ch == '[':
            stack.append((current, number))
            current = ""
            number = 0

        elif ch == ']':
            previous, repeat = stack.pop()
            current = previous + current * repeat

        else:
            current += ch

    return current


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
jprint(decode_string(s))