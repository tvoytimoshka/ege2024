with open("C:\\ЕГЭ ИНФОРМАТИКА\\project_python\\files\\26 (3).txt") as file:
    n = int(file.readline())
    boxes = [int(line) for line in file]
boxes.sort(reverse=True)

count = 1
last_box = boxes[0]

for i in range(0, len(boxes)):
    if last_box - boxes[i] >= 3:
        count += 1
        last_box = boxes[i]
print(count, last_box)
