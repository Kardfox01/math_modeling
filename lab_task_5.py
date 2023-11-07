from numpy import pi


CIRCLE    = 0
RECTANGLE = 1
TRIANGLE  = 2


def square(type, **kwargs):
    if type == CIRCLE:
        return pi * kwargs["r"]**2
    elif type == RECTANGLE:
        return kwargs["a"] * kwargs["b"]
    elif type == TRIANGLE:
        return (kwargs["a"] * kwargs["h"]) / 2



print(
    square(CIRCLE, r=5),
    square(RECTANGLE, a=5, b=5),
    square(TRIANGLE, a=5, h=5),
)