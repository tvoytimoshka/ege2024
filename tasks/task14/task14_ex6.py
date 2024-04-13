alphabet = '0123456789abcdefghijklmnopq'
max_num = -10**11
for x in alphabet:
    value = int(f'123{x}24', 27) + int(f'{x}178', 27)
    if value % 26 == 0:
        max_num = max(max_num, value//26)
print(max_num)