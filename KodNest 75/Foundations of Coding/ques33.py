# Reverse Vowels of a String

def reverse_vowels(s):
    # Write your code here
    vowels = "aeiouAEIOU"
    v = [i for i in s if i in vowels]
    result = ""

    for i in s:
        if i in vowels:
            result += v.pop()
        else:
            result += i

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


s = input()
jprint(reverse_vowels(s))