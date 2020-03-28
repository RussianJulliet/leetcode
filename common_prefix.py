strs = list(input().split())


def common_prefix(strs):
    if len(strs) == 0:
        return ""
    for i in range(len(strs[0])):
        c = strs[0][i]
        for j in range(len(strs)):
            if i == len(strs[j]) or strs[j][i] != c:
                return strs[0][:i]


print(common_prefix(strs))
