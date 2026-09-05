# Find the Digital Root of a number

def add_digits(num):
    # write your logic here
    while num >= 10:
        total = 0

        while num > 0:
            digit = num % 10
            total += digit
            num = num // 10

        num = total
    return num


if __name__ == "__main__":
    num = int(input().strip())
    print(add_digits(num))