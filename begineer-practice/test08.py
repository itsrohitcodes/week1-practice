# Convert number to Excel Column Title

def convert_to_column_title(columnNumber):
    # write your logic here
    result = ""

    while columnNumber > 0:
        columnNumber = columnNumber - 1
        remainder = columnNumber % 26
        result = chr(remainder + 65) + result
        columnNumber = columnNumber // 26

    return result


if __name__ == "__main__":
    columnNumber = int(input().strip())
    print(convert_to_column_title(columnNumber))