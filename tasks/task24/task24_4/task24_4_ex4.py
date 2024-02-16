# Текстовый файл состоит не более чем из 10**6 символов X, Y и Z. Определите максимальную длину цепочки вида
# XYZXYZXYZ... (составленной из фрагментов XYZ, последний фрагмент может быть неполным). Для выполнения этого задания
# следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.
# x % 3 = 0
# y % 3 = 1
# z % 3 = 2
with open("C:\\ЕГЭ ИНФОРМАТИКА\\project_python\\files\\filesdop\\task7.txt") as file:
    s = file.readline()

count = 0
max_count = 0

for i in range(0, len(s)):
    if (s[i] == 'X' and count % 3 == 0) or (s[i] == 'Y' and count % 3 == 1) or (s[i] == 'Z' and count % 3 == 2):
        count += 1
        max_count = max(count, max_count)
    else:
        if s[i] == 'X': count = 1
        else: count = 0
print(max_count)