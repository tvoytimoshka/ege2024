# Сколько анаграмм можно составить из слова “Параллелепипед”?
# Анаграммой называется произвольное слово, полученное из данного слова перестановкой букв

from functools import lru_cache


@lru_cache(None)
def count_anagramms(alphabet):
    if len(alphabet) <= 1:
        return 1
    else:
        count = 0
        unic_chars = set(alphabet)
        for char in unic_chars:
            remaining_word = alphabet.replace(char, '', 1)
            count += count_anagramms(remaining_word)
        return count


print(count_anagramms('параллелепипед'))
