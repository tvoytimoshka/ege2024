# Текстовый файл состоит не более чем из 10**6 символов арабских цифр (0, 1, ...,9).
# Определите максимальное количество идущих подряд нечётных цифр, расположенных в неубывающем порядке.
# Для выполнения этого задания следует написать программу.

with open("C:\\Users\\Владимир\\Downloads\\Telegram Desktop\\task5.txt") as f:
    file = f.readline()

count = 1
max_count = -1213
for i in range(0, len(file) - 1):
    if file[i] <= file[i+1] and file[i] in '13579' and file[i+1] in '13579':
        count += 1
        max_count = max(max_count, count)
    else:
        count = 1
print(max(count, max_count))