with open("C:\\ЕГЭ ИНФОРМАТИКА\\project_python\\files\\dkNLDfUaG.txt") as file:
    n = int(file.readline())
    clients = []
    for s in file:
        startTime, fullTime, windowNum = [int(x) for x in s.split()]
        clients += [[startTime, fullTime, windowNum]]
clients.sort()
print(clients)
queue = [[], []]
yesService = 0
noService = 0
for startTime, fullTime, windowNum in clients:
    queue[0] = [x for x in queue[0] if x > startTime]
    queue[1] = [x for x in queue[1] if x > startTime]
    if windowNum == 1 or (windowNum == 0 and len(queue[0]) <= len(queue[1])):
        if len(queue[0]) >= 14:
            noService += 1
            continue
        if len(queue[0]) == 0:
            queue[0] += [startTime + fullTime]
        else:
            queue[0] += [max(queue[0]) + fullTime]
    else:
        if len(queue[1]) >= 14:
            noService += 1
            continue
        yesService += 1
        if len(queue[1]) == 0:
            queue[1] += [startTime + fullTime]
        else:
            queue[1] += [max(queue[1]) + fullTime]
print(yesService, noService)