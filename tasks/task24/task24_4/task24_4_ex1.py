# Текстовый файл состоит не более чем из 10**6 символов X, Y и Z. Определите максимальную длину цепочки символов,
# состоящей из повторяющихся фрагментов XYZ. Цепочка должна начинаться с символа X и заканчиваться символом Z.
# Например, для строки ZZZXYZXYZXZZZ длина цепочки равна 6: XYZ+XYZ

with open("C:\\ЕГЭ ИНФОРМАТИКА\\project_python\\files\\filesdop\\task4 (2).txt") as file:
    s = file.readline()

count = 0
max_count = 0

s = s.replace('XYZ', '1')

for i in range(0, len(s)):
    if s[i] == '1':
        count += 1
        max_count = max(count, max_count)
    else:
        count = 0
print(max_count*3)