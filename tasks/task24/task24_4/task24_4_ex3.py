# Текстовый файл состоит из символов A, B, C, D и O. Определите максимальное количество идущих подряд пар символов
# вида согласная + гласная в прилагаемом файле. Для выполнения этого задания следует написать программу.
with open("C:\\Users\\Владимир\\Downloads\\Telegram Desktop\\task6 (2).txt") as file:
    s = file.readline()

s = s.replace('BA', '1')
s = s.replace('BO', '1')
s = s.replace('CA', '1')
s = s.replace('CO', '1')
s = s.replace('DA', '1')
s = s.replace('DO', '1')
count = 0
max_c = 0
for i in range(0, len(s)):
    if s[i] == '1':
        count += 1
        max_c = max(max_c, count)
    else:
        count = 0
print(max_c)