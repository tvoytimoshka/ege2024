# Текстовый файл состоит не более чем из 106 символов 1, 2, 3, A, B, С. Определите максимальное количество идущих
# подряд символов, среди которых никакие две буквы и никакие две цифры не стоят рядом. Для выполнения этого задания
# следует написать программу.
with open("C:\\Users\\Владимир\\Downloads\\Telegram Desktop\\task6.txt") as file:
    f = file.readline()

count = 1
max_count = 0
for i in range(0, len(f)-1):
    if (f[i] in '123' and f[i+1] in 'ABC') or (f[i] in 'ABC' and f[i+1] in '123'):
        count += 1
        max_count = max(max_count, count)
    else:
        count = 1
print(max_count)