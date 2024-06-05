def sum_s(n):
    count = 0
    for i in n:
        count += int(i)
    return count


for n in range(1, 1000):
    s = '7' + '1' * (n + 1) + '2' * (n + 2) + '3' * (n + 3)
    while '71' in s or '72' in s or '73' in s:
        if '71' in s:
            s = s.replace('71', '227', 1)
        if '72' in s:
            s = s.replace('72', '37', 1)
        if '73' in s:
            s = s.replace('73', '17', 1)
    if sum_s(s) == 9*n:
        print(n)