x = input('Введите строку: ')
z = len(x)
i = 0
p = True

while i <= z/2:
    if x[i] == x[z - i - 1]:
        i += 1
    else:
        p = False
        break

if p:
    print('Эта строка полинтром')
else:
    print('Эта строка не полинтром')
