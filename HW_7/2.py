from re import fullmatch

positive = ['bar', 'car', 'far', 'war', '0ar', '$ar']
negative = ['bag', 'for', 'star', 'care']

for x in positive + negative:
    match = fullmatch('.ar', x)
    if match:
        print(x, ' # match')
    else:
        print(x, ' # no match')
