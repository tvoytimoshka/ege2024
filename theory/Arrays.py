# Тема 3
# Списки - упорядоченный изменяемый набор объектов произвольных типов,
# пронумерованных от 0. Они используются для хранения и работы с данными.

num = [9, 3, 4, 2, 4, 5, 1, 4, 5]

# Для вывода каждого элемента используем его порядковый номер в списке

print(num[0])  # покажет первое число(9)
print(num[4])  # покажет пятое число(4)
print(num[6])  # покажет седьмое число(1)
# Можно вывести тот или иной элемент с помощью его индеса с конца
print(num[-1])  # покажет 5
# Можно вывести сразу весь список
print(num)  # Покажет [9, 3, 4, 2, 4, 5, 1, 4, 5]

# Списки можно создавать с помощью генератора списков. Такой
# способ схож с циклом for, но компактнее.

# Пример с циклом for:
a = []
for a in 'ПРИВЕТ!':
    a.append(a)

# Компактный вариант:
a = []
a = [a for i in 'ПРИВЕТ!']
print(a)

# Методы работы со списком.

# list.append(x) - добавление элемента x в конец списка
a = [1, 2]
a.append(9)
print(a)  # Покажет 1, 2, 9

# list.insert(y, x) - y: Индекс вставляемого элемента. x: Сам вставляемый элемент
a.insert(0, 2)

a = [1, 2]
a.insert(0, 2)
print(a)  # Покажет 2, 1, 2

# list.remove(x) - удаляет первый элемент в списке list, который равен
# значению x
a = [1, 2, 1]
a.remove(1)
print(a)  # выведет 2, 1

# list.pop(y) - удаление элемента попорядковому номеру(индексу)
a = [1, 2, 1]
a.pop(0)
print(a)  # выведет 2, 1

# list.count(x) - возвращает количество элементов со значением x в списке
a = [1, 2, 1, 3]
b = a.count(1)
print(b)  # выведет два числа '1' в списке

# list.sort() - сортировка списка. По умолчанию - по возрастанию.
a = [3, 1, 2]
a.sort()
print(a)  # выведет 1, 2, 3

# list.reverse() - переворачивает список.
a = [2, 1, 3]
a.reverse()
print(a)  # выведет 3, 1, 2

# list.clear() - очищает список полностью.
a = [2, 2, 5, 1, 7]
a.clear()
print(a)  # выведет []
