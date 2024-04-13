# coding=utf-8
# Назовём делитель, не равной единице и самому числу.
# Найдите все натуральные числа, принадлежащие отрезку
# [106732567; 152673836] и имеющие ровно три делителя. Для каждого
# найденного числа запишите в ответе само число и его наибольший
# делитель. Найденные числа расположите в порядке возрастания.

# Три разных делителя имеют только(!) простые числа в 4 степени.


# 1. Функция get_simple_nums(num_start, num_end):
#    - Создается пустое множество result для хранения найденных простых чисел.
#    - Создается список prime размером n + 1, заполненный значениями True. Этот список будет
#    использоваться для отметки составных чисел.
#    - Цикл for odd_num in range(3, num_end + 1, 2) перебирает нечетные числа от 3 до num_end:
#      - Если prime[odd_num] равно False, значит число odd_num уже помечено как составное, и
#      цикл переходит к следующей итерации.
#      - Если odd_num больше num_start, то число odd_num добавляется в множество result.
#      - Цикл j in range(odd_num * odd_num, num_end + 1, odd_num) помечает все числа, кратные odd_num,
#      как составные, начиная с odd_num * odd_num.
#    - Функция возвращает отсортированный список найденных простых чисел.
#
# 2. Переменные start и end задают диапазон чисел, в котором будут искаться простые числа.
#
# 3. Переменные num_start и num_end вычисляются как 25% от a и b соответственно, округленные вниз и вверх.


def get_simple_nums(num_start, num_end):
    result = set()
    prime = [True] * (num_end + 1)
    for odd_num in range(3, num_end + 1, 2):
        if not prime[odd_num]:
            continue
        if odd_num > num_start:
            result.add(odd_num)
        for j in range(odd_num * odd_num, num_end + 1, odd_num):
            prime[j] = False
    return sorted(list(result))


start = 106732567
end = 152673836
num_start = int(start ** 0.25)
num_end = int(end ** 0.25) + 1


list_simple = get_simple_nums(num_start, num_end)
for numer in list_simple:
    print(numer ** 4, numer ** 3)