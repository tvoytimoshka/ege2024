with open("C:\\Users\\Владимир\\Downloads\\27880.txt") as file:
    firstLine = file.readline().split()
    s = int(firstLine[0])
    n = int(firstLine[1])
    users = [int(line) for line in file]
users.sort()
disk = []
for i in range(n):
    if sum(disk) + users[i] <= s:
        disk.append(users[i])
    else:
        break
disk = disk[:-1]
for i in range(len(users)-1, -1, -1):
    if sum(disk) + users[i] <= s:
        disk.append(users[i])
        break
print(len(disk), disk[-1])