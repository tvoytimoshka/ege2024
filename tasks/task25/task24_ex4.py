# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [25317; 51237],
# числа, которые имеют хотя бы 6 различных простых делителей.
# Делители 1 и само число не учитываются.
# Для каждого найденного числа запишите найденное число и максимальный простой делитель этого числа.
from math import sqrt
for num in range(25317, 51237 + 1):
    if int(sqrt(num)) ** 2 == num:
        divisor_list = []
        for divisor in range(2, int(sqrt(num)) + 1):
            if num % divisor == 0:
                divisor_list.append(divisor)
                divisor_bro = num // divisor
                if divisor != divisor_bro:
                    divisor_list.append(divisor_bro)
        if len(divisor_list) == 6:
            divisor_list.sort()
            print(num, max(divisor_list))
