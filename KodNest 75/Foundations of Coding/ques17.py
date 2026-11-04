# Find Peak Element

# Write your code here
def findPeakElement(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return left


n = int(input())

nums = list(map(int, input().split()))

result = findPeakElement(nums)

print(result)