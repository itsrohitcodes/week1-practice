# Determine If Two Strings Are Close

def close_strings(word1, word2):
    # Write your code here ...
    if len(word1) != len(word2):
        return False

    count1 = [0] * 26
    count2 = [0] * 26

    for ch in word1:
        index = ord(ch) - ord('a')
        count1[index] += 1

    for ch in word2:
        index = ord(ch) - ord('a')
        count2[index] += 1

    for i in range(26):
        if (count1[i] == 0 and count2[i] != 0) or \
           (count1[i] != 0 and count2[i] == 0):
            return False

    count1.sort()
    count2.sort()

    if count1 == count2:
        return True
    else:
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


word1 = input()
word2 = input()

jprint(close_strings(word1, word2))