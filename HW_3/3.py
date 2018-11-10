from json import loads, dumps

try:
    with open('date.json', 'rb') as f:
        code = f.read(4)
        s = f.read()
    FileIsFound = True
except FileNotFoundError:
    print('Файл не обнаружен.\nФайл будет перезаписан.')
    s = {}
    FileIsFound = False


if FileIsFound and code == b'\xca\xfe\xba\xbe':
    s = s.decode()
    s = loads(s)

elif FileIsFound and code == b'\x8b\xad\xf0\x0d':
    a = bytearray()
    for b in s:
        a.append(255 - b)

    s = a.decode()
    s = loads(s)

elif FileIsFound:
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
