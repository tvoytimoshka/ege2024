# Алгоритм вычисления функций F(n) и G(n), где n – натуральное число, задан следующими соотношениями:
# F(n) = 1 , если n ≥ 3210,
# G(n) = n, если n < 10.
# F(n) = F(n+3) + 7, если n<3210,
# G(n) = G(n–3) + 5, если n ≥ 10.
# Чему равно значение выражения F(15) – G(3000)

import sys

sys.setrecursionlimit(4000)


def f(n):
    if n >= 3210:
        return 1
    return f(n + 3) + 7


def g(n):
    if n < 10:
        return n
    return g(n - 3) + 5


print(f(15) - g(3000))