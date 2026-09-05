# Find the Majority Element in an array

def majority_element(nums):
    # write your logic here
    for num in nums:
        if nums.count(num) > len(nums) // 2:
            return num


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(majority_element(nums))