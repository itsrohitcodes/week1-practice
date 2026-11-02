# Merge Strings Alternately

def merge_alternately(word1, word2):
    # Write your code here ...
    result = ""

    for i in range(max(len(word1), len(word2))):
        if i < len(word1):
            result += word1[i]
        if i < len(word2):
            result += word2[i]

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


word1 = input()
word2 = input()

jprint(merge_alternately(word1, word2))