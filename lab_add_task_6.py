from numpy import zeros, int64


N, M = int(input()), int(input())

array1 = zeros((N, M), int64)
array2 = array1.copy()
array_max = array2.copy()

for array in (array1, array2):
    for i in range(N * M):
        array[i // N, i % M] = int(input())
        array_max[i // N, i % M] = max(
            array_max[i // N, i % M],
            array[i // N, i % M]
        )

print(array_max)