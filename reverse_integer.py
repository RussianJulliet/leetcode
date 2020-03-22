x = int(input())
answer = 0
while x != 0:
    pop = x % 10
    x = x // 10
    answer = answer*10 + pop
print(answer)
