with open("C:\\Users\\Владимир\\Downloads\\ege-inf-stat30032022-402-26.txt") as input_file:
    total_particles = int(input_file.readline())
    rows = [set() for _ in range(10001)]  # Создаем список множеств для каждого ряда
    for _ in range(total_particles):
        row, position = map(int, input_file.readline().split())
        rows[row].add(position)  # Добавляем позицию частицы в соответствующий ряд

    max_odd_points = 0  # Максимальное количество светлых точек в нечетных позициях
    max_odd_points_row = 0  # Номер ряда с максимальным количеством светлых точек в нечетных позициях
    for row_num in range(10001):
        odd_points_count = 0  # Счетчик светлых точек в нечетных позициях для текущего ряда
        for pos in rows[row_num]:
            if pos % 2 == 1:  # Проверяем, является ли позиция нечетной
                odd_points_count += 1
        if odd_points_count > max_odd_points:
            max_odd_points = odd_points_count
            max_odd_points_row = row_num
    print(max_odd_points, max_odd_points_row)
print(len(rows[995]), rows[995])