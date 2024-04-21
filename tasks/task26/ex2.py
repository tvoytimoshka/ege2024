# вторая вариация
with open("C:\\ЕГЭ ИНФОРМАТИКА\\project_python\\files\\26 (2).txt") as file:
    n = int(file.readline())

    trees = [0] * 100001

    for i in range(0, 100001):
        trees[i] = []

    for i in range(0, n):
        list = file.readline().split()
        trees[int(list[0])].append(int(list[1]))

for i in range(0, len(trees)):
    trees[i].sort()
stop = 0

for i in range(len(trees) - 1, -1, -1):
    for j in range(0, len(trees[i]) - 1):
        if trees[i][j + 1] - trees[i][j] == 14:
            print(i, trees[i][j] + 1)
            stop = 1
            break
    if stop == 1:
        break
