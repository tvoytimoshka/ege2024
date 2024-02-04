# Текстовый файл состоит не более, чем из 106 символов из набора A, B, С. Найдите максимальное количество идущих пар
# символов AC или AB. Искомая подстрока может включать только пары AB, только пары AC или содержать одновременно как
# пары AC, так и пары AB.

with open("C:\\ЕГЭ ИНФОРМАТИКА\\project_python\\files\\filesdop\\task5 (2).txt") as file:
    s = file.readline()

s = s.replace('AB', '1')
s = s.replace('AC', '1')
count = 0
max_count = 0
for i in range(0, len(s)):
    if s[i] == '1':
        count += 1
        max_count = max(max_count, count)
    else:
        count = 0
print(max_count)