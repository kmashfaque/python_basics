import numpy as np

# x = [1, 2, 3, 4, 5]

# y = np.array(x)
# print(y)

# z = np.arange(1, 5)
# print(z)

# arr = []

# for i in range(1, 5):
#     value = int(input("Enter your number: "))
#     arr.append(value)
# print(np.array(arr))
# print(arr.ndim)


# arr = np.array([[1, 2, 3, 5], [5, 6, 7, 8]])
# print(arr.ndim)

kanto = [5, 5, 5]
weigth = [10, 20, 30]


def dot_product(kanto, weigth):
    z = 0
    for x, y in zip(kanto, weigth):
        z += x*y
    return z


val = dot_product(kanto, weigth)
print(val)


x = np.array([5, 5, 5])

y = np.array([10, 20, 30])

res = np.dot(x, y)
print(res)
