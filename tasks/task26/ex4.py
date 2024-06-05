with open("C:\\ЕГЭ ИНФОРМАТИКА\\project_python\\files\\26 (4).txt") as file:
    firstLine = file.readline().split()
    n = int(firstLine[0])
    m = int(firstLine[1])

    product = []  # Это продукты(товары), из нашего файла (!!ЭТО НЕ БИБЛИОТЕКА itertools!!)
    for i in range(n):
        line = file.readline().split()
        product.append((int(line[0]), str(line[1])))
    product.sort()

summa = 0  # эта сумма, которую потратим при нахождении максимального количества товаров ВНЕЗАВИСИМОСТИ ОТ ТИПА(A,B,C,D,E)
bigPurchase = []  # товары, которые были взяты при вычислении предыдущего шага.
productTypeA = []
for i in range(n):
    if summa + product[i][0] <= m:
        summa = summa + product[i][0]
        bigPurchase.append(product[i])
    else:
        if product[i][1] == 'A':
            productTypeA.append(product[i])

j = 0
for i in range(len(bigPurchase) - 1, - 1, -1):
    if bigPurchase[i][1] == 'A': continue

    if summa - bigPurchase[i][0] + productTypeA[j][0] <= m:
        summa = summa - bigPurchase[i][0] + productTypeA[j][0]
        bigPurchase[i] = productTypeA[j]
    else:
        break
    j += 1

count = 0
for i in range(len(bigPurchase)):
    if bigPurchase[i][1] == 'A':
        count += 1
print(count, m - summa)
