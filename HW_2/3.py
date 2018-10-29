from math import pow, acos, degrees

a = int(input('Введите длину первой стороны треугольника: '))
b = int(input('Введите длину второй стороны треугольника: '))
c = int(input('Введите длину третьей стороны треугольника: '))
print('\n\n')

if a + b < c or b + c < a or c + a < b:
    print('Треугольника с такими сторонами не существует')
else:
    # обычно pow не используется в Python таким образом, потому что для этого есть оператор x ** y
    ab = (pow(a, 2) + pow(b, 2) - pow(c, 2))/(2*a*b)
    bc = (pow(b, 2) + pow(c, 2) - pow(a, 2))/(2*b*c)
    # странно, что PyCharm не ругается здесь на PEP8, но вообще между операндами в бинарных операциях должен быть пробел
    # т.е. не 2*a*c, а 2 * a * c, то же самое касается +, -, /, //, %, **
    # но при этом пробел не ставится после унарных операций, например, унарного + или -: y = +x, y = -x
    ac = (pow(a, 2) + pow(c, 2) - pow(b, 2))/(2*a*c)

    print('Угол между первой и второй стороной треугольника равен %d градусов' % degrees(acos(ab)))
    print('Угол между второй и третьей стороной треугольника равен %d градусов' % degrees(acos(bc)))
    print('Угол между первой и третьей стороной треугольника равен %d градусов' % degrees(acos(ac)))
