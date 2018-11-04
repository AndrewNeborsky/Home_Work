from random import randrange
from functools import reduce


def reverse(a, x):
    a.insert(0, x)
    return a


def fun(value, action):
    d = {'sum': reduce(lambda a, x: a + x, value),
         'multiply': reduce(lambda a, x: a * x, value),
         'join': reduce(lambda a, x: 10 * a + x, value, 0),
         'union': set(value),
         'reverse': reduce(reverse, value, list()),
         'negated': map(lambda x: -x, value),
         'inverted': map(lambda x: 1 / x, value),
         'squared': map(lambda x: x * x, value),
         'odds': filter(lambda x: x % 2 != 0, value),
         'evens': filter(lambda x: x % 2 == 0, value),
         'simples': filter(lambda x: x in {1, 2, 3, 5, 7}, value)}

    return d[action]


L = int(input('N: '))
seq = []
for i in range(L):
    seq.append(randrange(1, 10))

print(seq)

actions = input('Action: ')
actions = actions.split(' ')

seq = list(fun(seq, actions[2]))
seq = list(fun(seq, actions[1]))
seq = fun(seq, actions[0])

print(seq)
