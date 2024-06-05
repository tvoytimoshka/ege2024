def f(x, A):
    return not (x in P) or (not ((x in Q) and not (x in A)))


P = [i / 10 for i in range(130 * 10, (171 * 10) + 1)]
Q = [i / 10 for i in range(150 * 10, (185 * 10) + 1)]
A = set()
for x in [i / 10 for i in range(100 * 10, (200 * 10) + 1)]:
    if not f(x, A):
        A.add(x)
print(sorted(A))
