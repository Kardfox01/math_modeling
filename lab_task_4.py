from numpy import linspace, double


def parabola(a, b, N):
    return [x**2 for x in linspace(a + 1, b, N, double)]

print(parabola(-5, 5, 20))