def min(arg, *args, value_to_key=None, **kwargs):

    # в ф-ию min может передаваться:
    #     _одно или больше значений (первое значение записывается в переменную arg, остальные в кортеж args)
    #     _функция value_to_key
    #     _словарь

    if value_to_key is None:
        value_to_key = lambda x: x

    # строки 7 - 8: проводится присваивание переменной value_to_key значение анонимной функции,
    # котрая возвращает полученное значение, если значение этой переменной не задано.

    # строки 25 - 32: проводится проверка: переданно ли в функцию min больше одного значения:
    # если да, то:
    #     1. все значения кроме первого присваиваются перемменной values ввиде кортежа
    #     2. переменным min_value и min_key присваиваются значение arg и значение ф-ии value_to_key(arg) соответственно
    #     3. переменной has_initial_value присваивается значение True (данная переменная обозначает присвоение значения
    #        переменным min_value и min_key)
    # если нет, то:
    #     1. переменной value присаивается значение arg
    #     2. переменным min_value и min_key присваиваются значение None
    #     3. переменной has_initial_value присваивается значение False

    if len(args) > 0:
        values = args
        min_value, min_key = arg, value_to_key(arg)
        has_initial_value = True
    else:
        values = arg
        min_value, min_key = None, None
        has_initial_value = False

    # строка 38: проводится присваивание переменной value_key_pairs кортежа, состоящего из еще одного кордежа,
    # который имеет вид (value, value_to_key(value)); т.е. если переменная value = (1, 2, 3, 4), а функция
    # value_to_key = lambda x: -x, то переменная value_key_pairs будет иметь вид: ((1, -1), (2, -2), (3, -3), (4, -4))

    value_key_pairs = tuple(map(lambda x: (x, value_to_key(x)), values))

    # строка 50: проводится цикл по значениям кортежа value_key_pairs. В этом цикле проводится поиск значения min_key
    # строки 51 - 61: проводится проверка: были ли пременным min_value и min_key присвоены значения:
    # если да, то:
    #     1. проводится сравнение переменной min_key со значением (key) ф-ии value_to_key
    #       взятое из кортежа value_key_pairs. Если min_key > key, то значению min_key присваивается значение key,
    #       а min_value -- значение соответствующее ключу key
    # если нет, то:
    #     1. значению min_key присваивается значение key, а min_value -- значение соответствующее ключу key
    #     2. переменной has_initial_value присваивается значение True

    for value, key in value_key_pairs:
        if has_initial_value:
            if key < min_key:
                min_value, min_key = value, key
        else:
            min_value, min_key = value, key
            has_initial_value = True

    # строки 64 - 67: если в функцию min не было пререданно
    # ни одного значения (в этом случае переменная has_initial_value = False),
    # то идет поиск ключа 'default' в словаре kwargs:
    # если он там есть то функция min возвращает значение соответствующее этому ключу,
    # а если его нет, то возвращается ошибка

    if not has_initial_value:
        if 'default' in kwargs:
            return kwargs['default']
        raise ValueError('arg is an empty sequence')

    # сторока 71 возвращает найденное значение min_value

    return min_value


empty_sequence = tuple()
value_sequence = 3, 1, 2
x, y, z = value_sequence

print(min(x, y, z))  # result: 1
print(min(value_sequence))  # result: 1

print(min(x, y, z, value_to_key=lambda v: -v))  # result: 3
print(min(value_sequence, value_to_key=lambda v: -v))  # result: 3

print(min(x, y, z, default=0xE0F))  # result: 1
print(min(value_sequence, default=0xE0F))  # result: 1
print(min(empty_sequence, default=0xE0F))  # result: 3599

# print(min(empty_sequence))  # error!
