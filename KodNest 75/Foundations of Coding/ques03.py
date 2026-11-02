# Greatest Common Prefix Pattern

def gcd_of_strings(str1, str2):
    # Write your code here ...
    for i in range(min(len(str1), len(str2)), 0, -1):
        s = str1[:i]
        if str1 == s * (len(str1) // len(s)) and str2 == s * (len(str2) // len(s)):
            return s

    return ""


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


str1 = input()
str2 = input()

jprint(gcd_of_strings(str1, str2))