# Текстовый файл 24-157.txt состоит не более чем из 106 символов и содержит только заглавные буквы латинского
# алфавита (ABC…Z). Определите символ, который чаще всего встречается в файле между двумя одинаковыми символами.
# Например, в тексте CCBAABABCBC есть комбинации ABA, BAB, BCB и CBC. Чаще всего – 2 раза – между двумя одинаковыми
# символами стоит B, в ответе для этого случая надо написать B2 (без пробелов и других разделителей). Если таких
# символов несколько, выведите тот, который стоит раньше в алфавите.

with open("C:\\Users\\Владимир\\Downloads\\Telegram Desktop\\task8.txt") as file:
    s = file.readline()
list = [0] * 150

for i in range(0, len(s) - 2):
    if s[i] == s[i + 2]:
        list[ord(s[i + 1])] += 1  # ord переводит условный символ A в 65(то есть A в Unicode)
char = ''
mx = 0
for i in range(0, 150):  # 150 - из-за длины списка 150
    if list[i] > mx:
        mx = list[i]
        char = chr(i)  # chr переводит индекс буквы(Unicode) в буквы
print(char, mx)