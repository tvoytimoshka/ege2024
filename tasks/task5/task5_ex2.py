# Автомат получает на вход пятизначное число. По этому числу строится новое число по следующим правилам.
# 1.Складываются отдельно первая, третья и пятая цифры, а ттакже вторая и четвёрая цифры.
# 2.Полученные два числа записываются друг за другом в порядке неубывания без разделителей.
# Пример. Исходное число: 63 179. Суммы: 6 + 1 + 9 = 16; 3 + 7 = 10. Результат: 1016.
# Укажите наименьшее число, при обработке которого автомат выдаёт результат 723

for i in range(10000, 100000):
    str_i = str(i)

    first_summa = int(str_i[0]) + int(str_i[2]) + int(str_i[4])
    second_summa = int(str_i[1]) + int(str_i[3])

    first_number = str( min(first_summa, second_summa) )
    second_number = str( max(first_summa, second_summa) )

    answer = first_number + second_number
    if answer == '723':
        print(i)
        break

# or

for n in range(10000, 99999 + 1):  # 123545 <- index?
    str_n = str(n)

    sum1 = int(str_n[0]) + int(str_n[2]) + int(str_n[4])
    sum2 = int(str_n[1]) + int(str_n[3])

    if min(sum2, sum1) == sum1:
        result = str(sum1) + str(sum2)
    else:
        result = str(sum2) + str(sum1)
    if int(result) == 723:
        print(n)
        break