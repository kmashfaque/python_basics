import functools
import operator
lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# value = iter(lis)

# for value in value:
#     print(value)

# def func(a, b):
#     return a+b


# res = functools.reduce(func, lis)
# res1 = functools.reduce(lambda a, b: a+b, lis)

# print(res)
# print(res1)

# res2 = functools.reduce(operator.add, lis)
# res3 = functools.reduce(operator.mul, lis)
# print(res2)
# print(res3)


# implementation of reduce function
def reduce(func, iterable, initializer=None):
    it = iter(iterable)

    if initializer == None:
        value = next(it)

    else:
        value = initializer

    for element in it:
        print(element)
        value = func(value, element)

    return value


res2 = reduce(lambda x, y: x+y, lis, None)
# print(res2)
