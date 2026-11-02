# Find the Difference of Two Arrays

def find_difference(nums1, nums2):
    # Write your code here ...
    first = []
    second = []

    for num in nums1:
        if num not in nums2 and num not in first:
            first.append(num)

    for num in nums2:
        if num not in nums1 and num not in second:
            second.append(num)

    return [first, second]


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
nums1 = [ni() for _ in range(n)]
m = ni()
nums2 = [ni() for _ in range(m)]

result = find_difference(nums1, nums2)
jprint(result)