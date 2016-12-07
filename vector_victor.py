import math


class ShapeError(Exception):
    pass


def shape(vector_list):
    if type(vector_list[0]) == list:
        matrix_size = tuple([len(vector_list), len(vector_list[0])])
        return matrix_size
    else:
        l = list(vector_list)
        return (len(l), )


def vector_add(m, n):
    if len(m) == len(n):
        return [x + y for x, y in zip(m, n)]
    else:
        raise ShapeError(Exception)


def vector_sub(m, n):
    if len(m) == len(n):
        return [x - y for x, y in zip(m, n)]
    else:
        raise ShapeError(Exception)


def vector_sum(*args):
    if len(set([shape(x) for x in args])) == 1:
        return [sum(x) for x in zip(*args)]
    else:
        raise ShapeError(Exception)


def dot(m, n):
    if len(m) == len(n):
        return sum([x * y for x, y in zip(m, n)])
    else:
        raise ShapeError(Exception)


def vector_multiply(m, mult):
    return [x * mult for x in m]


def vector_mean(*args):
    return [sum(x)/(len(x)) for x in zip(*args)]


def magnitude(m):
    return math.sqrt(sum(i**2 for i in m))
