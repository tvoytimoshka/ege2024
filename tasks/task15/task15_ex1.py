# Для какого наименьшего целого неотрицательного числа А выражение
# (x + 2y < A) v (y > x) v (x > 30)
# тождественно истинно, т.е. принимает значение 1 при любых целых неотрицательных х и у?

for A in range(301):
    logic_flag = False
    for x in range(301):
        for y in range(301):
            f = (x + 2 * y < A) or (y > x) or (x > 30)
            if not f:
                logic_flag = True
    if not logic_flag:
        print(A)
