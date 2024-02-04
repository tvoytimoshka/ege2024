# Текстовый файл состоит из символов P, Q, R и S. Определите максимальное количество идущих подряд символов в
# прилагаемом файле, среди которых нет идущих подряд символов P. Для выполнения этого задания следует написать
# программу.
with open("C:\\ЕГЭ ИНФОРМАТИКА\\project_python\\files\\filesdop\\task1.txt") as file:
    f = file.readline()

count = 1
max_count = 0
for i in range(0, len(f)-1):
    if f[i] == 'P' and f[i+1] == 'P':
        count = 1
    else:
        count += 1
        max_count = max(max_count, count)
print(max_count)