x = input('Введите число: ')
z = len(x)
mn = 10
mx = 0

for i in range(z):
    if int(x[i]) < mn:
        mn = int(x[i])

    if int(x[i]) > mx:
        mx = int(x[i])

print('Минимальное число: %d' % mn)
print('Максимальное число: %d' % mx)
