n = input('Введите число: ')
n = int(n)
x = []

for i in range(2, n):
    x.append(i)

i = 0

while i < len(x):
    j = i + 1
    while j < len(x):
        if x[j] % x[i] == 0:
            del x[j]
        else:
            j += 1
    i += 1

print('Все простые числа меньше %d: ' % n, x)
