# Две логические функции заданы выражениями:
# F1=(x → y)≡(w ∨ ¬z)
# F2=(x → y)∧(¬w ≡ z)
# Дан частично заполненный фрагмент, содержащий неповторяющиеся строки таблицы истинности обеих функций.
# Определите, какому столбцу таблицы истинности соответствует каждая из переменных w, x, y, z.
from itertools import product

print('x y z w f1 f2')
for x, y, z, w in product([0, 1], repeat=4):
    f1 = (not x or y) == (w or not z)
    f2 = (not x or y) and (not w == z)
    print(x, y, z, w, f1, f2)

# Проверка
x = 0
z = 1
y = 0
w = 0
f1 = (not x or y) == (w or not z)
f2 = (not x or y) and (not w == z)
print(f1, f2)
