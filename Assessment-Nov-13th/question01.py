# Earliest Day to Pack Orders


def earliest_packing_day(ready_days, m, k):
    # Write your code here.
    if m * k > len(ready_days):
        return -1

    low, high = min(ready_days), max(ready_days)

    while low < high:
        mid = (low + high) // 2
        count = items = 0

        for x in ready_days:
            if x <= mid:
                items += 1
                if items == k:
                    count += 1
                    items = 0
            else:
                items = 0

        if count >= m:
            high = mid
        else:
            low = mid + 1

    return low


n, m, k = map(int, input().split())
ready_days = list(map(int, input().split()))
print(earliest_packing_day(ready_days, m, k))
