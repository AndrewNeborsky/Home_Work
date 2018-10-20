from HW_2.Game.mymodule import board_draw, win


board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
board_draw(board)

step = 0
player = 'x'

while step < 9:
    if step % 2 == 0:
        player = 'x'
    else:
        player = '0'

    print('Сейчас ходит игрок со знаком %s' % player)
    x = int(input('Введите координаты хода: \n x = ')) - 1
    y = int(input(' y = ')) - 1

    if x > 2 or y > 2:
        print('Данной ячейки не существует.\nВведите координаты другой ячейки: ')
        x = int(input(' x = ')) - 1
        y = int(input(' y = ')) - 1

    while board[x][y] != ' ':
        print('Данная ячейка занята.\nВведите координаты другой ячейки: ')
        x = int(input(' x = ')) - 1
        y = int(input(' y = ')) - 1

    board[x][y] = player

    print('\n' * 50)
    board_draw(board)

    if step > 3:
        if win(board, player):
            print('Победил игрок со знаком %s' % player)
            break

    step += 1

print('Игра завершена')
