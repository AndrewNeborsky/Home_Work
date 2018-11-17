from json import loads, dumps

try:
    with open('date.json', 'rb') as f:
        header = f.read(4)
        s = f.read()
    FileIsFound = True
except FileNotFoundError:
    print('Файл не обнаружен.\nФайл будет перезаписан.')
    header = None
    s = {}
    FileIsFound = False


if FileIsFound and header == b'\xca\xfe\xba\xbe':
    s = loads(s.decode())

elif FileIsFound and header == b'\x8b\xad\xf0\x0d':
    s = bytearray(map(lambda x: 255 - x, s))
    s = loads(s.decode())

elif FileIsFound:
    print('Файл поврежден.\nФайл будет перезаписан.')
    s = {}

d = {input('Введите имя: '): {'age': int(input('Введите возраст: ')), 'profession': input('Введите профессию: ')}}
s.update(d)

if input('Нажмите Y если хотите, чтобы данные были зашифрованны: ') in {'Y', 'y'}:
    s = dumps(s, indent=4)
    s = bytearray(s.encode())

    s = bytearray(map(lambda x: 255 - x, s))

    with open('date.json', 'wb') as f:
        f.write(b'\x8b\xad\xf0\x0d' + s)
else:
    s = dumps(s, indent=4)
    s = s.encode()

    with open('date.json', 'wb') as f:
        f.write(b'\xca\xfe\xba\xbe' + s)
