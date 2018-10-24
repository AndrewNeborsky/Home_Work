def min(arg, *args, key=None, **kwargs):  # определение функции min

    if args:  # если кортеж args имеет хоть один компонент, то:
        flag = False  # переменной flag задается значение False
        iterable = args  # переменной iterable пресваиваются значения args
        if key is None:  # если переменная key пуста, то:
            vmin, kmin = arg, arg  # переменным vmin и kmin пресваивается значение arg
        else:  # в противном случае, если переменная key не пуста, то:
            vmin, kmin = arg, key(arg)  # переменной vmin присваевается значение arg, а переменной kmin -- key(arg)
    else:  # в противном случае, если кортеж args не имеет компонентов, то:
        flag = True  # переменной flag задается значение True
        iterable = arg  # переменной iterable пресваиваются значения arg
        vmin, kmin = None, None  # переменным vmin и kmin становятся пустыми

    if key is None:  # если перременная key пуста, то:
        iterable = map(lambda x: (x, x), iterable)  # при помощи функции map и анонимной функции lambda
        # переменной iterable присваевается map объект, содержащий кортеж из 2 объектов iterable
    else:  # в противном случае, если перременная key не пуста, то:
        iterable = map(lambda x: (x, key(x)), iterable)  # при помощи функции map и анонимной функции lambda
        # переменной iterable присваевается map объект, содержащий кортеж (iterable, key(iterable))

    for v, k in iterable:  # создается цикл по значением iterable
        if flag:  # если переменная flag равна True, то:
            vmin, kmin = v, k  # переменной vmin присваевается значение v, а переменной kmin -- k
            flag = False  # переменной flag задается значение False
        else:  # в противном случае, если переменная flag не равна True(т.е. равна False), то:
            if k < kmin:  # если значение k меньше значения kmin, то
                vmin, kmin = v, k  # переменной vmin присваевается значение v, а переменной kmin -- k

    if flag:  # если переменная flag равна True, то:
        if 'default' in kwargs:  # если сторока 'default' является ключоь в словаре kwargs, то:
            return kwargs['default']  # возвращается значение которое находится в словаре kwargs под ключем 'default'
        raise ValueError('arg is an empty sequence')  # в противном случае, вывести сообщение об ошибке

    return vmin  # возвращается значение vmin


empty_sequence = tuple()
value_sequence = 3, 1, 2
x, y, z = value_sequence

print(min(x, y, z))  # result: 1
print(min(value_sequence))  # result: 1

print(min(x, y, z, key=lambda v: -v))  # result: 3
print(min(value_sequence, key=lambda v: -v))  # result: 3

print(min(x, y, z, default=0xE0F))  # result: 1
print(min(value_sequence, default=0xE0F))  # result: 1
print(min(empty_sequence, default=0xE0F))  # result: 3599

print(min(empty_sequence))  # error!
