s = str(input())
row = int(input())


def convert(s, row):
    lin = 0
    plt = 1
    answer = [""] * row
    for i in range(len(s)):
        answer[lin] += s[i]
        if row > 1:
            lin += plt
            if lin == 0 or lin == row - 1:
                plt *= -1
    outputStr = ""
    for j in range(row):
        outputStr += answer[j]
    return outputStr


print(convert(s, row))

    

