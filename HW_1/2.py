L = int(input('Введите количество чисел: '))
s = 0

for i in range(L):
    a = input('Число №%d: ' % (i+1))
    a = int(a)

    if a % 3 == 0:
        s += a

print('Сумма чисел делящихся на 3 равна: %d' % s)
