from numpy import linspace


def revlinspace(start, stop, num):
    for i in linspace(start, stop, num): yield i
    for i in linspace(stop, start, num): yield i