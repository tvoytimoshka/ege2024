from functools import lru_cache


def moves(situation):
    a, b = situation
    return ((a + 1, b),
            (a, b + 1),
            (a * 2, b),
            (a, b * 2))


@lru_cache(None)
def game(situation):
    if sum(situation) >= 77:  # Условие победы
        return 'w'

    if any(game(m) == 'w' for m in moves(situation)):
        return 'P1'
    if any(game(m) == 'P1' for m in moves(situation)):  # для 19 all -> any
        return 'B1'

    if any(game(m) == 'B1' for m in moves(situation)):
        return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in moves(situation)):
        return 'B2'


for s in range(1, 69 + 1):
    if game((7, s)) is not None:
        print(s, game((7, s)))
