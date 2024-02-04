# Для какого наибольшего целого числа А формула:
# x&51 = 0 ∨ (x&41 = 0 → x&А = 0)
# тождественно истинна (т.е. принимает значение 1 при любом неотрицательном целом
# значении переменной x)?

for A in range(301):
    logic_flag = False
    for x in range(301):
        f = (x & 51 == 0) or (not (x & 41 == 0) or (x & A == 0))
        if not f:
            logic_flag = True
    if not logic_flag:
        print(A)