import math


def diagonal(a, b):
    return round(math.sqrt((a ** 2 + b ** 2)), 2)


def area(a, b):
    return a * b


def perimeter(a, b):
    return (a + b) * 2


def dictionary(a, b):
    return {'Diagonal': diagonal(a, b), 'Area': area(a, b), 'Perimeter': perimeter(a, b)}


if __name__ == '__main__':
    width = int(input('Width = '))
    length = int(input('Length = '))
    print("Diagonal = {} \nArea  = {} \nPerimeter = {} \nDictionary = {}".format(diagonal(width, length),
                                                                                 area(width, length),
                                                                                 perimeter(width, length),
                                                                                 dictionary(width, length)))
