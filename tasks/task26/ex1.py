# первая вариация
with open('C:\\ЕГЭ ИНФОРМАТИКА\\project_python\\files\\26.txt') as file:
    firstLine = file.readline().split()
    s = int(firstLine[0])
    n = int(firstLine[1])
    users = [int(line) for line in file]

# сортируем список users
users.sort()
disk = []
for i in range(n):
    if sum(disk) + users[i] <= s:
        disk.append(users[i])
    else:
        break
disk = disk[:-1]  # удаляем последний элемент
for i in range(len(users) - 1, -1, -1):
    if sum(disk) + users[i] <= s:
        disk.append(users[i])
        break
print(len(disk), disk[-1])