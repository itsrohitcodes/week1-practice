# Count set bits in a number

def count_set_bits(n):
    # write your logic here
    count = 0

    while n > 0:
        count += n % 2
        n = n // 2

    return count


if __name__ == "__main__":
    n = int(input().strip())
    print(count_set_bits(n))