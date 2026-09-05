# Check for duplicate elements in an array

def contains_duplicate(nums):
    # write your logic here
    for num in nums:
        if nums.count(num) > 1:
            return True
    return False


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(contains_duplicate(nums))