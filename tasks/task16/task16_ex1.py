# f(1) = 5; f(2) = 5;
# f(n) = 5 * f(n - 1) - 4 * f(n - 2) при n > 2
# Чему равно значение функции f(13)?

def f(n):
    if n == 1:
        return 5
    if n == 2:
        return 5
    return 5 * f(n - 1) - 4 * f(n - 2)


print(f(13))
