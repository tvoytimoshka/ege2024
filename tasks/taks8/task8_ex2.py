# Вероника состовляет 3-буквенные коды из букв В Е Р О Н И К А, при чем буква В должна
# входить в код ровно один раз. Вероника записала алф. порядке и пронумеровала
# 1. ААВ
# 2. АВА
# 3. АВЕ
# На каком месте будет записан первый код ни одной А?

alphabet = sorted('вероника')
number = 1
for first_symbol in alphabet:
    for second_symbol in alphabet:
        for third_symbol in alphabet:
            word = first_symbol + second_symbol + third_symbol
            if word.count('в') == 1:
                print(number, word)
                number += 1