from random import randrange
from functools import reduce


def union(a, x):
    a.add(x)
    return a


def reverse(a, x):
    a.insert(0, x)
    return a


def fun(value, *action):
    d_1 = {'sum': lambda a, x: a + x,
           'multiply': lambda a, x: a * x,
           'join': lambda a, x: 10 * a + x,
           'union': union,
           'reverse': reverse}

    d_2 = {'negated': lambda x: -x,
           'inverted': lambda x: 1 / x,
           'squared': lambda x: x * x}

    d_3 = {'odds': lambda x: x % 2 != 0,
           'evens': lambda x: x % 2 == 0,
           'simples': lambda x: x in {1, 2, 3, 5, 7}}

    d_start = {'sum': 0, 'multiply': 1, 'join': 0, 'union': set(), 'reverse': list()}

    return reduce(d_1[action[0]], map(d_2[action[1]], [value[j] for j in range(len(value)) if d_3[action[2]]]),
                  d_start[action[0]])


L = int(input('N: '))
seq = []

for i in range(L):
    seq.append(randrange(1, 10))

print(seq)

while True:
    actions = input('Action: ')
    actions = actions.split(' ')

    try:
        seq = fun(seq, *actions)
    except KeyError:
        print('Actions is not correct.\nTry again.')
    except IndexError:
        print('Action is too small.\nTry again.')
    else:
        break

print(seq)
