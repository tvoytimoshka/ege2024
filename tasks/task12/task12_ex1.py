# Известно, что исходная строка A содержала больше 44 цифр, первая из которых— ноль, а остальные— единицы и двойки.
# После выполнения данной программы получилась строка B, сумма цифр которой оказалась простым числом.
# Чему равна наименьшая возможная сумма цифр в строке A?

def prostoe_Chislo(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


min_num = 10 ** 10
for x in range(100):
    for y in range(100):
        s = '0' + '1' * x + '2' * y
        if len(s) > 44:
            while ('01' in s) or ('02' in s):
                s = s.replace('02', '1110', 1)
                s = s.replace('01', '220', 1)
            if prostoe_Chislo(s.count('1') + s.count('2') * 2):
                min_num = min(min_num, x + 2 * y)
print(min_num)
