from HW_3.Game_files.mymodule import print_field, check_field, make_turn
from sys import exit
from pickle import dump, load
from os.path import isfile
from os import remove


def saver():
    try:
        input('\nЧтобы продолжить нажмите Enter\nЧтобы выйти из игры и сохранить прогресс нажмите Ctrl+D\n')
        # на windows ctrl+c не вызывает KeyboardInterrupt
    except EOFError:
        with open('Game_files/Save.txt', 'wb') as file:
            dump(board, file)
        print('Прогресс сохранен')
        exit()


board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
start_step = 0

if isfile('Game_files/Save.txt') and input('Найдено сохранение игры. Нажмите Y чтобы его загрузить: ') in {'Y', 'y'}:
    with open('Game_files/Save.txt', 'rb') as f:
        board = load(f)
    remove('Game_files/Save.txt')

    for i in range(2):
        for j in range(2):
            if board[i][j] != ' ':
                start_step += 1
elif isfile('Game_files/Save.txt'):
    remove('Game_files/Save.txt')

print_field(board)

for step in range(start_step, 9):
    if step % 2 == 0:
        player = 'X'
    else:
        player = 'O'

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

    saver()

print('Игра завершена')
