from re import fullmatch

positive = ['dog', 'log', 'dock', 'lock']
negative = ['fog', 'block', 'locked']

for x in positive + negative:
    match = fullmatch('[d|l]o(g|ck)', x)
    if match:
        print(x, ' # match')
    else:
        print(x, ' # no match')
