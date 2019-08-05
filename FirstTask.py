import math


def diagonal(a, b):
    return round(math.sqrt((a ** 2 + b ** 2)), 2)


def area(a, b):
    return a * b


def perimeter(a, b):
    return a + b


if __name__ == '__main__':
    width = int(input('Width = '))
    length = int(input('Length = '))
    print("Diagonal = {} \nArea  = {} \nPerimeter = {}".format(diagonal(width, length),
                                                               area(width, length), perimeter(width, length)))
