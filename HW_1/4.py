x = input('Введите строку: ')
z = len(x)
p = True

for i in range(z // 2):
    if x[i] != x[- i - 1]:
        p = False
        break

if p:
    print('Эта строка полинтром')
else:
    print('Эта строка не полинтром')
