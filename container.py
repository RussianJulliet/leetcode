list = list(map(int, input().split()))
dict = {}
max_water = 0
for x in list:
    dict[x] = list.index(x)
for i in range(len(list)):
    for j in range(i + 1, len(list)):
        water = min(list[i], list[j]) * (j - i)
        # print(water)
        if water > max_water:
            max_water = water
print(max_water)
