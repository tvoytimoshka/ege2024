# В файле содержится последовательность целых чисел.
# Элементы последовательности могут принимать целые значения от -10 000 до 10 000 включительно.
# Определите и запишите в ответе сначала количество пар элементов
# последовательности, в которых хотя бы одно число делится на 3,
# затем максимальную из сумм элементов таких пар.
# В данной задаче под парой подразумевается два идущих подряд элемента последовательности.


with open('C:\\temp\\17.txt') as file:
    numbers = [int(line) for line in file]

count = 0
max_summa = -200000000000
for i in range(len(numbers) - 1):  # i - index
    if (numbers[i] % 3 == 0) or (numbers[i + 1] % 3) == 0:
        count += 1
        max_summa = max(max_summa, numbers[i] + numbers[i+1])
print(count, max_summa)