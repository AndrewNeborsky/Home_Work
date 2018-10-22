from HW_2.Game.mymodule import board_draw, win, check


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

    x, y = check(x, y, board)

    board[x][y] = player

    print('\n' * 50)
    board_draw(board)

    if step > 3:
        if win(board, player):
            print('Победил игрок со знаком %s' % player)
            break

    step += 1

print('Игра завершена')
