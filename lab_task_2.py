from lab_task_1 import g, h, k
import numpy as np


_h = 100
alpha = np.pi / 3
beta = 30

V =  g * _h * np.tan(beta)**2
V /= 2 * np.cos(alpha)**2 * (1 - np.tan(beta) * np.tan(alpha))
V =  V ** .5

# ----

T = 200
E = 300

N =  2 / (np.pi**.5)
N *= h / (k * T)**1.5
N *= np.e**(-E / (k * T))
N *= E**(T / 2)

print(V, N)