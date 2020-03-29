strs = list(input().split())


def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""
    min_len = 2147483647
    for i in strs:
        min_len = min(min_len, len(i))
    low = 1
    high = min_len
    while low <= high:
        middle = (low + high) // 2
        if isCommonPrefix(strs, middle):
            low = middle + 1
        else:
            high = middle - 1
    return strs[0][:(low + high)//2]


def isCommonPrefix(strs, len):
    # print(type(len))
    str1 = strs[0][:len]
    # print(str1)
    for i in strs:
        if not i.startswith(str1):
            return False
    return True


print(longestCommonPrefix(strs))
