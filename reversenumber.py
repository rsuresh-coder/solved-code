def reverse_number(x: int) -> int:
    upper_limit = 2147483647
    lower_limit = -2147483648

    reverse = 0
    while x:
        digit = x % 10 #This may not work for negative numbers
        x = x // 10  # This also may not work for negative numbers

        # print(digit, x)
        if (reverse > upper_limit // 10) or (reverse == upper_limit // 10 and digit > upper_limit % 10):
            return 0

        if (reverse < lower_limit // 10) or (reverse == lower_limit // 10 and digit < lower_limit % 10):
            return 0

        reverse = reverse * 10 + digit

    return reverse

print(reverse_number(7463847412))
# print(reverse_number(-2463847412))
