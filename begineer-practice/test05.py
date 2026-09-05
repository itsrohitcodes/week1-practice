# Check if two string are Isomorphic

def are_isomorphic(s, t):
    # write your logic here
    if len(s) != len(t):
        return False

    a = {}
    b = {}

    for i in range(len(s)):
        if a.get(s[i]) != t[i] or b.get(t[i]) != s[i]:
            if s[i] in a or t[i] in b:
                return False
            a[s[i]] = t[i]
            b[t[i]] = s[i]

    return True


if __name__ == "__main__":
    s = input().strip()
    t = input().strip()
    print(are_isomorphic(s, t))