blocks = list(map(int, input().split()))
left = 0
right = len(blocks) - 1
max_water = 0
while (right - left) != 1:
    if blocks[left] < blocks[right]:
        water = blocks[left] * (right - left)
        left += 1
    else:
        water = blocks[right] * (right - left)
        right -= 1
    if water > max_water:
        max_water = water
print(max_water)