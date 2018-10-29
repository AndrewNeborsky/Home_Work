L = input('Введите количество чисел: ')
i = 0
s = 0

while i < int(L):  # Лучше использовать for i in range(L)
    a = input('Число №%d: ' % (i+1))
    a = int(a)

    if a % 3 == 0:
        s += a

    i += 1

print('Сумма чисел делящихся на 3 равна: %d' % s)
