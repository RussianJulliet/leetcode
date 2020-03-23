numb_str = input()
MAXINT = 2147483647
MININT = -2147483648
MAXDIV10 = MAXINT // 10
MINDIV10 = MININT // 10 + 1

def is_digit(c):
    return (ord(c) >= ord('0')) and (ord(c) <= ord('9'))


def atoi(string):
    i, k = 0, 0
    mul = 1
    number = 0
    for c in string:
        if is_digit(c):
            break
        elif c == '-':
            mul *= -1
            # i += 1
        elif c == '+':
            i += 1
        elif c != ' ':
            return 0
        i += 1
    # print(string[i:])
    for c in string[i:]:
        if not is_digit(c):
            break
        digit = mul * (ord(c) - ord('0'))
        # print(digit)
        if number > MAXDIV10 or (number == MAXDIV10 and digit > 7):
            return MAXINT
        if number < MINDIV10 or (number == MINDIV10 and digit == -9):
            return MININT
        number = number * 10 + digit
    return number


print(atoi(numb_str))





