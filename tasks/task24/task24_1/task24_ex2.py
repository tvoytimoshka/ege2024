with open('/home/george/Рабочий стол/task2.txt') as f:
    file = f.readline()

count = 1
max_count = 0
for i in range(0, len(file)):
    if file[i] == 'B':
        count += 1
        max_count = max(count, max_count)
    else:
        count = 1
print(max_count)