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

seq = t.split('\n')
ctr = len(seq)//2


t = seq[ctr: len(seq)] + seq[0: ctr]

f = open('text.txt', 'w')
f.write('\n'.join(t))
f.close()
