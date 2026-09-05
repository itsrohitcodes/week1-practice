# Check whether two strings are anagrams

def is_anagram(s, t):
    # write your logic here
    if len(s) != len(t):
        return False

    for char in s:
        if s.count(char) != t.count(char):
            return False
    return True


if __name__ == "__main__":
    s = input().strip()
    t = input().strip()
    print(is_anagram(s, t))