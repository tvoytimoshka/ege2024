# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите максимальное количество идущих подряд символов, среди которых ровно по одному разу встречаются буквы X и Y.
with open("C:\\Users\\Владимир\\Downloads\\qJ8bde_Gx.txt") as file:
    s = file.readline()
l = 0
r = -1
m = 0
k = 0
k_x = k_y = 0
while r < len(s):
    while k_x <= 1 and k_y <= 1:
        r += 1
        if r == len(s): break
        if s[r] == 'X':
            k_x += 1
        if s[r] == 'Y':
            k_y += 1
        if k_x == 1 and k_y == 1:
            m = max(m, r-l+1)
    while not(k_x <= 1 and k_y <= 1):
        if s[l] == 'X':
            k_x -= 1
        if s[l] == 'Y':
            k_y -= 1
        l += 1
    m = max(m, r-l+1)
print(m)