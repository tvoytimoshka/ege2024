# P = [12, 62]
# Q = [32, 92]
# Какова НАИМЕНЬШАЯ возможная длинна интервала A, что формула
# not (not (x in A) and (x in q)) or (x in P)
# тождественно истинна, принимает значение 1. При любом значении X
def f(x, A):
    return not (not (x in A) and (x in Q)) or (x in P)


P = [i / 10 for i in range(12 * 10, 62 * 10 + 1)]
Q = [i / 10 for i in range(32 * 10, 92 * 10 + 1)]
A = set()


for x in [i / 10 for i in range(5 * 10, 100 * 10 + 1)]:
    if not f(x, A):
        A.add(x)

print(sorted(A))

# A = (62, 92]
# Длинна интервалла = 92 - 62 = 30