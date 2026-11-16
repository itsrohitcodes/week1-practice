# Longest Unique Segment


def longest_unique_segment(s):
    # Write your code here.
    longest = 0

    for i in range(len(s)):
        temp = ""

        for j in range(i, len(s)):
            if s[j] in temp:
                break

            temp += s[j]
            longest = max(longest, len(temp))

    return longest


s = input().strip()
print(longest_unique_segment(s))
