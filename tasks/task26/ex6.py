with open("C:\\ЕГЭ ИНФОРМАТИКА\\project_python\\files\\26 (5).txt") as file:
    n = file.readline()
    numbers = set()
    for i in file:
        i = int(i)
        numbers.add(i)
    numbers_chet = []
    for i in numbers:
        if i % 2 == 0:
            numbers_chet.append(i)
    count = 0
    max_arith = 0
    for i in range(len(numbers_chet)-1):
        for j in range(i+1, len(numbers_chet)):
            if ((numbers_chet[i] + numbers_chet[j]) // 2) in numbers:
                count += 1
                max_arith = max(max_arith, ((numbers_chet[i] + numbers_chet[j]) // 2))
print(count, max_arith)
