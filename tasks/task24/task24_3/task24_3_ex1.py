# Текстовый файл состоит не более чем из 106 символов X, Y и Z. Определите максимальное количество идущих подряд
# символов, среди которых символ Z встречается не более одного раза.

with open("C:\\Users\\Владимир\\Downloads\\Telegram Desktop\\task3 (2).txt") as file:
    s = file.readline()

list = s.split('Z')
count = 0
max_count = 0
for i in range(0, len(list)-1):
    count = len(list[i]) + 1 + len(list[i+1])
    max_count = max(max_count, count)
print(max_count)