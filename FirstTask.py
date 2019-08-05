def diagonal(a, b):
    import math
    return round(math.sqrt((a ** 2 + b ** 2)), 2)


def area(a, b):
    return a * b


def perimeter(a, b):
    return a + b


width = int(input('Ширина прямоугольника = '))
length = int(input('Длина прямоугольника = '))
print('Диагональ = {} \nПлощадь  = {} \nПериметр = {}'.format(diagonal(width, length),
      area(width, length), perimeter(width, length)))
