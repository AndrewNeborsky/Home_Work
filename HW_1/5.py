x1 = input('Введите первую строку: ')
x2 = input('Введите вторую строку: ')
z1 = len(x1)
z2 = len(x2)

i = 0
j = 0
p = True

while j < z1:
    while i < z2:
        if x2[i] == x1[j]:
            j += 1
            i += 1
        else:
            if j < (z1 - 1):
                j += 1
            else:
                p = False
                break
    break

if p:
    print('Вторая строка является частью первой строки')
else:
    print('Вторая строка не является частью первой строки')
