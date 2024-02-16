# ЕГЭ №2122
# Текстовый файл состоит из символов A, B, C, D и E.
#
# Определите в прилагаемом файле минимальное количество идущих подряд символов, среди которых символ A встречается 40
# раз.
#
# Для выполнения задания следует написать программу.
# for i in range(1, len(list)-target+1):
#     count = 0
#     for j in range(i, i + target - 1):
#         count += 1
#         count = count + len(list[j])
#     count += 1
#     min_count = min(min_count, count)

with open("C:\\Users\\Владимир\\Downloads\\Telegram Desktop\\taskege1.txt") as f:
    file = f.readline()

list = file.split("A")
target = 40
min_count = 10**10
count = 0
for j in range(1, target):
    count += 1
    count += len(list[j])
count += 1
print(count)
for i in range(target, len(list)-1):
    min_count = min(min_count, count)
    count -= len(list[i-target+1])
    count += len(list[i])
min_count = min(min_count, count)
print(min_count)
