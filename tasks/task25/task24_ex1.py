# Маска числа — это последовательность цифр, в которой могут встречаться специальные символы «?» и «*».
# Символ «?» означает ровно одну произвольную цифру, символ «*» означает произвольную (в том числе пустую)
# последовательность цифр.
#
#
# Пример.
# Маске 123*4?5 соответствуют числа 123405 и 12376415.
#
# Найдите все натуральные числа, не превышающие 10**10, которые соответствуют маске 1?2655*8 и при этом без остатка
# делятся на 4173.
#
# В ответе запишите все найденные числа в порядке возрастания.
# В порядке возрастания.
# 10000000000
# 19265599998
alphabet = '0123456789'
number = 1026558
if number % 4173 == 0:
    print(number)
print(10**10)
for x in alphabet:
    for y in alphabet:
        number = int(f'1{x}2655{y}8')
        if number % 4173 == 0:
            print(number)

for x in alphabet:
    for y in alphabet:
        for i in alphabet:
            number = int(f'1{x}2655{y}{i}8')
            if number % 4173 == 0:
                print(number)
for x in alphabet:
    for y in alphabet:
        for i in alphabet:
            for z in alphabet:
                number = int(f'1{x}2655{y}{i}{z}8')
                if number % 4173 == 0:
                    print(number)
for x in alphabet:
    for y in alphabet:
        for i in alphabet:
            for z in alphabet:
                for d in alphabet:
                    number = int(f'1{x}2655{y}{i}{z}{d}8')
                    if number % 4173 == 0:
                        print(number)