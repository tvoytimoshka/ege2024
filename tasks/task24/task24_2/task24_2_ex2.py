# Текстовый файл состоит из символов арабских цифр(0, 1, ...,9).

# Определите максимальное количество идущих подряд символов в прилагаемом файле, среди которых нет трёх символов 0,
# стоящих рядом. Для выполнения этого задания следует написать программу

with open("C:\\ЕГЭ ИНФОРМАТИКА\\project_python\\files\\filesdop\\task2 (2).txt") as file:
    f = file.readline()

count = 2
max_count = 0
for i in range(0, len(f) - 2):
    if f[i] == "0" and f[i+1] == "0" and f[i+2] == "0":
        count = 2
    else:
        count += 1
        max_count = max(max_count, count)


print(max_count)