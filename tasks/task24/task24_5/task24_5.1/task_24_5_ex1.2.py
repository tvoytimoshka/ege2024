# 2 программа решения

f = open("C:\\ЕГЭ ИНФОРМАТИКА\\project_python\\files\\filesdop\\task9.txt")
count = 0
list = [0] * 150

for s in f.readlines():
    count += 1
    if count == 162:
        for i in range(0, len(s)):
            list[ord(s[i])] += 1

char = ''
mx = 0
for i in range(0, 150):
    if list[i] > mx:
        mx = list[i]
        char = chr(i)
print(char)

file = open("C:\\ЕГЭ ИНФОРМАТИКА\\project_python\\files\\filesdop\\task9.txt")
count_k = file.read()
print(count_k.count('K'))
