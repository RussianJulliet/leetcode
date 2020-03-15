string = str(input())


def lengthOfLongestSubstring(string):
    if len(string) == 0:
        return 0
    chars = {}
    start_index, max_counter = 0, 0
    for i in range(len(string)):
    # заполняем словарь если встречаем символ впервые
        if string[i] not in chars:
            chars[string[i]] = i
        else:
            if chars[string[i]] < start_index:
                chars[string[i]] = i
                continue
            # обновление счетчика
            if i - start_index > max_counter:
                max_counter = i - start_index
            start_index = chars[string[i]] + 1
            chars[string[i]] = i
    # обновляем счетчик, если новый символ увеличил максимальную подпоследовательность
    if i - start_index + 1 > max_counter:
        max_counter = i - start_index + 1
    return max_counter


print(lengthOfLongestSubstring(string))