numb = int(input())


def palindrom(n):
    if n < 0 or n % 10 == 0 and n != 0:
        return 0
    else:
        half = 0
        while n > half:
            half = half * 10 + n % 10
            n //= 10
        return n == half or n == half // 10


print(palindrom(numb))