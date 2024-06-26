# Логическая функция F задаётся выражением (x ∧ ¬y) ∨ (y ≡ z) ∨ w.
# Дан частично заполненный фрагмент, содержащий неповторяющиеся строки таблицы истинности функции F.
# Определите, какому столбцу таблицы истинности соответствует каждая из переменных x, y, z, w.

from itertools import product

print('x y z w f')
for x, y, z, w in product([0, 1], repeat=4):
    f = (x and not y) or (y == z) or w
    if f:
        print(x, y, z, w, f)