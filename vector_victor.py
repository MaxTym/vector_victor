import math

class ShapeError(Exception):
    pass

def shape(vector_list):
    l = list(vector_list)
    return (len(l), )

def vector_add(self, other):
    if len(self) == len(other):
        return [x + y for x, y in zip(self, other)]
    else:
        raise ShapeError(Exception)

def vector_sub(self, other):
    if len(self) == len(other):
        return [x - y for x, y in zip(self, other)]
    else:
        raise ShapeError(Exception)

def vector_sum(*args):
    if len(set([shape(x) for x in args])) == 1:
        return [sum(x) for x in zip(*args)]
    else:
        raise ShapeError(Exception)

def dot(self, other):
    if len(self) == len(other):
        return sum([x * y for x, y in zip(self, other)])
    else:
        raise ShapeError(Exception)

def vector_multiply(self, mult):
    return [x * mult for x in self]

def vector_mean(*args):
    return [sum(x)/float(len(args)) for x in zip(*args)]

def magnitude(self):
    return math.sqrt(sum(i**2 for i in self))
