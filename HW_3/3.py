from json import loads, dumps

try:
    with open('date.json', 'rb') as f:
        s = f.read()
    FileIsFound = True
except FileNotFoundError:
    print('Файл не обнаружен.\nФайл будет перезаписан.')
    s = {}
    FileIsFound = False


if FileIsFound and s[:4] == b'\xca\xfe\xba\xbe':
    s = bytearray(s)
    del s[:4]

    s = s.decode()
    s = loads(s)

elif FileIsFound and s[:4] == b'\x8b\xad\xf0\x0d':
    s = bytearray(s)
    del s[:4]
    
    a = bytearray()
    for b in s:
        a.append(255 - b)

    s = a.decode()
    s = loads(s)

elif FileIsFound and s[0] != '{':
    print('Файл поврежден.\nФайл будет перезаписан.')
    s = {}


d = {input('Введите имя: '): {'age': int(input('Введите возраст: ')), 'profession': input('Введите профессию: ')}}
s.update(d)

if input('Нажмите Y если хотите, чтобы данные были зашифрованны: ') in {'Y', 'y'}:
    s = dumps(s, indent=4)
    s = bytearray(s.encode())

    a = bytearray()
    for b in s:
        a.append(255 - b)

    with open('date.json', 'wb') as f:
        f.write(b'\x8b\xad\xf0\x0d' + a)
else:
    s = dumps(s, indent=4)
    s = s.encode()

    with open('date.json', 'wb') as f:
        f.write(b'\xca\xfe\xba\xbe' + s)
