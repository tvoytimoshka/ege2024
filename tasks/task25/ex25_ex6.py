# Рассматриваются целые числа, принадлежащих числовому отрезку [485617; 529678], которые представляют собой
# произведение трёх различных простых делителей, оканчивающихся на одну и ту же цифру.
# В качестве ответа приведите все числа, разность максимального и минимального простых делителей которого меньше 100.
# Для каждого такого числа сначала запишите само число, а затем разность максимального и минимального простых делителей
def prostNum(num):
    for dev in range(2, int(num ** 0.5) + 1):
        if num % dev == 0:
            return False
    return True


for number in range(485617, 529678 + 1):
    simple_dev_list = []
    for devisor in range(2, int(number ** 0.5) + 1):
        if prostNum(devisor) == True and number % devisor == 0:
            simple_dev_list.append(devisor)

    if len(simple_dev_list) == 3:
        if str(simple_dev_list[0])[-1] == str(simple_dev_list[1])[-1] == str(simple_dev_list[2])[-1]:
            if simple_dev_list[0] * simple_dev_list[1] * simple_dev_list[2] == number:
                if max(simple_dev_list) - min(simple_dev_list) < 100:
                    print(number, max(simple_dev_list) - min(simple_dev_list))