with open("C:\\ЕГЭ ИНФОРМАТИКА\\project_python\\files\\DpOpef2j6.txt") as file:
    N, K = [int(x) for x in file.readline().split()]
    details = []
    for i in range(1, N + 1):
        timeS, timeO = [int(x) for x in file.readline().split()]
        details.append((timeO, i, 'okr'))
        details.append((timeS, i, 'shlif'))
details.sort()
id_used = set()
lenta = [0] * (N + 1)
l = 1
count_shlif = 0
r = N
for time, id_, type_ in details:
    if id_ not in id_used:
        id_used.add(id_)
        if type_ == 'shlif':
            lenta[l] = id_
            l += 1
            count_shlif += 1
        else:
            lenta[r] = id_
            r -= 1
print(count_shlif, lenta[K])