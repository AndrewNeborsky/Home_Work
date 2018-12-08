from re import sub

x = 'The dog trotted forward with a short, sharp bark, and the keeper lifted his face suddenly and saw her.'
x = sub('[T|t]he |an? ', '', x)
print(x)
