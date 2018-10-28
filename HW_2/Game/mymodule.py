def print_field(field):
    print('    1   2   3\n  +---+---+---+')

    for i in range(3):
        print(i+1, '| %s |' % ' | '.join(field[i]))
        print('  +---+---+---+')


def check_range(x, y):
    if x > 2 or y > 2 or x < 0 or y < 0:
        return False
    else:
        return True


def check_location(field, x, y):
    if field[y][x] != ' ':
        return False
    else:
        return True


def make_turn(field, x, y, value):
    while not check_range(x, y) or not check_location(field, x, y):
        if not check_range(x, y):
            print('Данной ячейки не существует.\nВведите координаты другой ячейки: ')
            x = int(input(' x = ')) - 1
            y = int(input(' y = ')) - 1
        elif not check_location(field, x, y):
            print('Данная ячейка занята.\nВведите координаты другой ячейки: ')
            x = int(input(' x = ')) - 1
            y = int(input(' y = ')) - 1

    field[y][x] = value


def check_rows(v, sign):
    for i in range(3):
        if v[i][0] == v[i][1] == v[i][2] == sign:
            return True


def check_cols(v, sign):

    for i in range(3):
        if v[0][i] == v[1][i] == v[2][i] == sign:
            return True


def check_diagonals(v, sign):
    if v[0][0] == v[1][1] == v[2][2] == sign or v[0][2] == v[1][1] == v[2][0] == sign:
        return True


def check_field(field, value):
    if check_rows(field, value) or check_cols(field, value) or check_diagonals(field, value):
        return True
