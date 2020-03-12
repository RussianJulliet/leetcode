#hash_table
numList = list(map(int, input().split()))
target = int(input())
answer = []
dict = {}
for i in range(len(numList)):
    dict[numList[i]] = i
for i in range(len(numList)):
    comlement = target - numList[i]
    if (comlement in dict) and (dict.get(comlement) != i):
        answer = [i, dict.get(comlement)]
if not answer:
    print("no answer")
else:
    print(answer)

