s = str(input())
max_str = " "
max_len = 0


def is_palindrom(left, right, max_len, max_str):
    l, r = left, right
    while (l >= 0 and r < len(s) and s[r] == s[l]):
        l -= 1
        r += 1
    if l - r + 1 > max_len:
        max_len = l - r + 1
        max_str = s[l + 1: r]
    return max_len, max_str


def palindrom(s):
    if len(s) == 0:
        return ""
    for i in range(len(s)):
        max_len, max_str = is_palindrom(i, i, max_len, max_str)
        max_len, max_str = is_palindrom(i, i + 1, max_len, max_str)
    return max_str

print(palindrom(s))
