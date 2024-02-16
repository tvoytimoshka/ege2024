# Текстовый файл состоит из символов A, B, C, D и E.
#
# Определите в прилагаемом файле максимальное количество идущих подряд символов, среди которых символ A встречается
# не более 101 раз.
#
# Для выполнения задания следует написать программу.
with open("C:\\Users\\Владимир\\Downloads\\Telegram Desktop\\task.txt") as f:
    file = f.readline()


a = file.split('A')
t = 101
count = 0
max_count = 0
for j in range(0, t + 1):
    count += len(a[j])
    if t != j:
        count += 1
print(count)
for i in range(t + 1, len(a)):
    max_count = max(max_count, count)
    count -= len(a[i-t-1])
    count += len(a[i])
max_count = max(max_count, count)
print(max_count)