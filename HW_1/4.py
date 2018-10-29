x = input('Введите строку: ')
z = len(x)
i = 0
p = True

while i <= z/2:  # как и во 2 второй задаче, лучше использовать for i in range(z // 2)
    if x[i] == x[z - i - 1]:  # здесь можно использовать запись проще: x[i] == x[-1 - i]
        i += 1
    else:
        p = False
        break

if p:
    print('Эта строка полинтром')
else:
    print('Эта строка не полинтром')
