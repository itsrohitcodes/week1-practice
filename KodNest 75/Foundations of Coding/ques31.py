# Product of Array Except Self

def product_except_self(nums):
    # Write your code here ...
    result = []

    for i in range(len(nums)):
        product = 1

        for j in range(len(nums)):
            if i != j:
                product *= nums[j]

        result.append(product)

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


import sys
data = sys.stdin.read().split()
it = iter(data)

def ni():
    return int(next(it))

def ns():
    return next(it)


n = ni()
nums = [ni() for _ in range(n)]

jprint(product_except_self(nums))