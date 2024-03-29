#
# Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
#
# — символ "?" означает ровно одну произвольную цифру;
#
# — символ "*" означает любую последовательность цифр произвольной длины; в том числе "*" может задавать и пустую
# последовательность.
#
# Например, маске 123*4?5 соответствуют числа 123405 и 12300405.
#
# Среди натуральных чисел, не превышающих 108, найдите все числа, соответствующие маске 1234*7, делящиеся на 141 без
# остатка.
#
# В ответе запишите в первом столбце таблицы все найденные числа в порядке возрастания, а во втором столбце —
# соответствующие им результаты деления эт их чисел на 14
from fnmatch import *

for i in range(141, 10**8+1, 141):
    if fnmatch(str(i), '1234*7'):
        print(i, i//141)