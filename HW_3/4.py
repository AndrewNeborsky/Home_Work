from HW_3.Game_files.mymodule import print_field, check_field, make_turn, loader
from sys import exit
from pickle import dump

board, start_step = loader()

print_field(board)

for step in range(start_step, 9):
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

    try:
        input('Чтобы продолжить нажмите Enter\nЧтобы выйти из игры и сохранить прогресс нажмите Ctrl+D\n')
        # на windows ctrl+c не вызывает KeyboardInterrupt
    except EOFError:
        board = [','.join(row) for row in board]
        board = '\n'.join(board)
        with open('Game_files/Save.txt', 'wb') as f:
            dump(board.encode(), f)
        print('Прогресс сохранен')
        exit()

    if step > 3:
        if check_field(board, player):
            print('Победил игрок со знаком %s' % player)
            break

print('Игра завершена')
