integer = int(input())
rom_n = ''
i = 0
thousands = integer // 1000
hundreds = integer // 100 % 10
decades = integer // 10 % 10
units = integer % 10
# print(thousands, hundreds, decades, units)
for i in range(thousands):
    rom_n = 'M' + rom_n
if hundreds == 9:
    rom_n += 'CM'
elif hundreds == 4:
    rom_n += 'CD'
elif hundreds >= 5:
    rom_n += 'D'
    for i in range(hundreds - 5):
        rom_n += 'C'
else:
    for i in range(hundreds):
        rom_n += 'C'
if decades == 9:
    rom_n += 'XC'
elif decades == 4:
    rom_n += 'XL'
elif decades >= 5:
    rom_n += 'L'
    for i in range (decades - 5):
        rom_n += 'X'
else:
    for i in range(decades):
        rom_n += 'X'
if units == 9:
    rom_n += 'IX'
elif units == 4:
    rom_n += 'IV'
elif units >= 5:
    rom_n += 'V'
    for i in range (units - 5):
        rom_n += 'I'
else:
    for i in range(units):
        rom_n += 'I'
print(rom_n)

