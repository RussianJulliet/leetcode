string = str(input())
substring = []
k = 0
best = [1]
for i in string[:]:
    if string.index(i) == (len(string) - 1):
        k += 1
        best.append(k)
    if i in substring:
        best.append(k)
        # print(k)
        substring.clear()
        substring.append(i)
        k = 1
    if i not in substring and string.index(i) != (len(string) - 1):
        k += 1
        substring.append(i)
        # print(substring)
        # print(i, k)


print(max(best))

