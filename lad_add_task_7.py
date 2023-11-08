from random import randint as ri


def rand(n, array):
    while (rnd := ri(0, n)) in array: pass
    return rnd


print("Rnd", rand(7, [0, 2, 3, 4, 5]))