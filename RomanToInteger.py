rom_number = input()
number = 0
i = 0
roman_dict = {'I': 1,
               'V': 5,
               'X': 10,
               'L': 50,
               'C': 100,
               'D': 500,
               'M': 1000}
while i < len(rom_number):
    if i != len(rom_number) - 1 and rom_number[i] == 'I' and rom_number[i + 1] == 'V':
        number = number + 4
        i += 2
    elif i != len(rom_number) - 1 and rom_number[i] == 'I' and rom_number[i + 1] == 'X':
        number = number + 9
        i += 2
    elif i != len(rom_number) - 1 and rom_number[i] == 'X' and rom_number[i + 1] == 'L':
        number = number + 40
        i += 2
    elif i != len(rom_number) - 1 and rom_number[i] == 'X' and rom_number[i + 1] == 'C':
        number = number + 90
        i += 2
    elif i != len(rom_number) - 1 and rom_number[i] == 'C' and rom_number[i + 1] == 'D':
        number = number + 400
        i += 2
    elif i != len(rom_number) - 1 and rom_number[i] == 'C' and rom_number[i + 1] == 'M':
        number = number + 900
        i += 2
    else:
        number = number + roman_dict[rom_number[i]]
        # print(number)
        i += 1
print(number)






