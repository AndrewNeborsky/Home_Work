from HW_2.Game.mymodule import print_field, check_field, make_turn

board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

print_field(board)

step = 0

while step < 9:
    if step % 2 == 0:
        player = 'x'
    else:
        player = '0'

    print('Сейчас ходит игрок со знаком %s' % player)
    x = int(input('Введите координаты хода: \n x = ')) - 1
    y = int(input(' y = ')) - 1

    make_turn(board, x, y, player)

    print('\n' * 50)
    print_field(board)

    if step > 3:
        if check_field(board, player):
            print('Победил игрок со знаком %s' % player)
            break

    step += 1

print('Игра завершена')
