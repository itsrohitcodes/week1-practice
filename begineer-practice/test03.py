# Check if a number is a power of two

def is_power_of_two(n):
    # write your logic here
    if n < 1:
        return False

    while n % 2 == 0:
        n = n // 2

    return n == 1


if __name__ == "__main__":
    n = int(input().strip())
    print(is_power_of_two(n))