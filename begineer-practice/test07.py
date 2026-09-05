# Find the Unique Element in an array

def find_single_number(nums):
    # write your logic here
    for num in nums:
        if nums.count(num) == 1:
            return num


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(find_single_number(nums))