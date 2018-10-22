import string

f = open('text.txt', 'r')
t = f.read()
f.close()

print('Текст в файле: \n%s' % t, '\n')

words = len(t.split())
print('Количество слов в файле:', words)

print('Буквы, их количество в файле: \n')

seq = list(t.lower())
i = 0

while i < len(seq):
    num = seq.count(seq[i])
    for j in range(len(seq) - 1, i - 1, -1):
        if seq[i] == seq[j] and i != j:
            del seq[j]
    if seq[i] == '\n' or seq[i] == ' ' or seq[i] == '.' or seq[i] == ',' or seq[i] == "'":
        del seq[i]
    else:
        print('%s: ' % seq[i], num)
    i += 1

ctr = len(t)//2

f = open('text.txt', 'w')
f.write(t[ctr: len(t)] + t[0: ctr])
f.close()
