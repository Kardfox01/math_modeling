# взял энергию при средней точке нахождения тела
from constants_from_less_3 import g


def energy(m, h, V):
    E = m * V**2
    E /= 2
    E += m * g * h

    return E