from numpy import ndarray, sin, double


N = M = 5

A = ndarray((N, M), double)

for i in range(N):
    for j in range(M):
        number = sin(N * (i + 1) + M * (j + 1))
        A[i, j] = number if number > 0 else 0

print(A)