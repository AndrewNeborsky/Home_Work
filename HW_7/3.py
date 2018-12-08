from re import fullmatch

positive = ['rock', 'core', 'roar', 'doors', 'looolz']
negative = ['hog', 'rack', 'shock', 'pocket']

for x in positive + negative:
    match = fullmatch('.o+.{2}', x)
    if match:
        print(x, ' # match')
    else:
        print(x, ' # no match')
