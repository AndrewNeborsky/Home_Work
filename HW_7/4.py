from re import fullmatch

seq = ['1', '-23', '1231231', '456.789', 'hello!']

for x in seq:
    match = fullmatch(r'[+\-]?(\d+)(\.\d+)?', x)
    if match:
        print('x =', x, ' # match')
    else:
        print('x =', x, ' # no match')
