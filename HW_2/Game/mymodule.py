def board_draw(v):
    print('    1   2   3\n  +---+---+---+')

    for i in range(3):
        print(i+1, '|', v[0][i], '|', v[1][i], '|', v[2][i], '|')
        print('  +---+---+---+')


def win(v, sign):
    for i in range(3):
        if v[i][0] == v[i][1] == v[i][2] == sign:
            return True

    for i in range(3):
        if v[0][i] == v[1][i] == v[2][i] == sign:
            return True

    if v[0][0] == v[1][1] == v[2][2] == sign or v[0][2] == v[1][1] == v[2][0] == sign:
        return True


def check(a, b, v):
    while a > 2 or b > 2 or a < 0 or b < 0:
        print('Данной ячейки не существует.\nВведите координаты другой ячейки: ')
        a = int(input(' x = ')) - 1
        b = int(input(' y = ')) - 1

    while v[a][b] != ' ':
        print('Данная ячейка занята.\nВведите координаты другой ячейки: ')
        a = int(input(' x = ')) - 1
        b = int(input(' y = ')) - 1

    return a, b
