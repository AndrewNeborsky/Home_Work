from random import randrange

z = randrange(1, 11)
print('Было загаданно число в промежутке [1, 10]. Поробуйте отгадать его.')
p = int(input('И это число: '))

while z != p:
    print('Не угадал.\nПопробуй снова.')
    p = int(input('И это число: '))

print('Урррааа!!! Ты угадал')
