# Текстовый файл состоит не более чем из 106** символов X, Y и Z. Определите максимальное количество идущих подряд
# символов, среди которых символ Z встречается не более двух раз.

with open("C:\\ЕГЭ ИНФОРМАТИКА\\project_python\\files\\filesdop\\task3 (2).txt") as file:
    s = file.readline()

list = s.split('Z')
count = 0
max_count = 0
for i in range(0, len(list)-2):
    count = len(list[i]) + 1 + len(list[i+1]) + 1 + len(list[i+2])
    max_count = max(max_count, count)
print(max_count)
print(list)