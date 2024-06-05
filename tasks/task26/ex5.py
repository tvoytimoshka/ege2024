with open("C:\\Users\\Владимир\\Downloads\\Telegram Desktop\\input26_02.txt") as file:
    n = int(file.readline())
    pixi = [0] * 100001

    for i in range(0, 100001):
        pixi[i] = []

    for i in range(0, n):
        list = file.readline().split()
        pixi[int(list[0])].append(int(list[1]))
for i in range(0, len(pixi)):
    pixi[i].sort()
stop = 0
for i in range(len(pixi)):
    for j in range(len(pixi[i])-1):
        if pixi[i][j+1] - pixi[i][j] == 3:
            print(i, pixi[i][-1]-1)
            stop = 1
            break
    if stop == 1:
        break
