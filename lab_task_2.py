from numpy import array


def prod(arr: array):
    acc = 1
    for number in arr:
        acc *= number

    return acc

arr = array((1, 2, 3))
print(prod(arr))