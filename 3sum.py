nums = list(map(int, input().split()))


def three_sum(nums):
    dict = {}
    set = []
    answer = []
    for i in range(len(nums)):
        dict[nums[i]] = i
    for k in range(len(nums)):
        c = -nums[k]
        for i in range(k + 1, len(nums)):
            comlement = c - nums[i]
            # print(-c, nums[i], comlement)
            if (comlement in dict) and (dict.get(comlement) > i) and (dict.get(comlement) > k)\
                    and (-c not in set or nums[i] not in set or comlement not in set):
                answer.append([-c, nums[i], comlement])
                set.append(-c)
                set.append(nums[i])
                set.append(comlement)
    if not answer:
        print("no answer")
    else:
        print(answer)


three_sum(nums)