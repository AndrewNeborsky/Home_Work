from string import ascii_lowercase

f = open('text.txt', 'r')
t = f.read()
f.close()

print('Текст в файле: \n%s' % t, '\n')

words = len(t.split())
print('Количество слов в файле:', words, '\n')

print('Буквы, их количество в файле: ')

seq = list(t.lower())

for i in range(len(ascii_lowercase)):
    num = seq.count(ascii_lowercase[i])

    if num != 0:
        print('%s: ' % ascii_lowercase[i], num)

ctr = len(t)//2

f = open('text.txt', 'w')
f.write(t[ctr: len(t)] + t[0: ctr])
f.close()
