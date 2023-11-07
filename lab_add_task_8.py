from numpy import ndarray, int64

M, N = int(input()), int(input())

array = ndarray((M, N), int64)

for i in range(M * N):
    array[i // N, i % N] = int(input())

print(*[max(column) for column in zip(*array)])
