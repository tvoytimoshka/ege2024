# Текстовый файл состоит не более чем из 106 символов арабских цифр (0, 1, ...,9).
# Определите максимальное количество идущих подряд цифр, среди которых каждые две соседние различны.
# Для выполнения этого задания следует написать программу.


with open('/home/george/Рабочий стол/task4.txt') as f:
    file = f.readline()

count = 1
max_count = 0

for i in range(0, len(file) - 1):
    if file[i] != file[i + 1]:
        count += 1
        max_count = max(max_count, count)
    else:
        count = 1
print(max_count)
