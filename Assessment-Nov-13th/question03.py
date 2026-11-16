# First Unique ID


def first_unique_id(ids):
    # Write your code here.
    for i in ids:
        if ids.count(i) == 1:
            return i

    return -1


n = int(input())
ids = list(map(int, input().split()))
print(first_unique_id(ids))
