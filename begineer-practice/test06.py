# Determine whether a number is happy

def is_happy_number(n):
    # write your logic here
    while n != 1 and n != 4:
        total = 0

        while n > 0:
            digit = n % 10
            total += digit * digit
            n = n // 10

        n = total
    return n == 1


if __name__ == "__main__":
    n = int(input().strip())
    print(is_happy_number(n))