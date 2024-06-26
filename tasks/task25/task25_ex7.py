# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [224466; 664422], которые делятся на 5, 7 и 13 без остатка,
# при этом не кратны квадрату любого из перечисленных делителей и максимальный делитель не превышает 100 000.
# Делители 1 и само число не учитываются.
# Учитываются только те числа, максимальный делитель которых оканчивается на 19.
# В качестве результата работы программы приведите найденное число и максимальный делитель этого числа.
for number in range(224466, 664422 + 1):
    if number % 5 == 0 and number % 7 == 0 and number % 13 == 0:
        if number % 5 ** 2 != 0 and number % 7 ** 2 != 0 and number % 13 ** 2 != 0:
            max_num = -10 ** 10
            for dev in range(2, int(number ** 0.5) + 1):
                if number % dev == 0:
                    max_num = max(max_num, dev, number//dev)
                    if dev != number//dev:
                        max_num = max(max_num, dev, number // dev)
            if ((max_num % 100) == 19) and max_num < 100000:
                print(number, max_num)
