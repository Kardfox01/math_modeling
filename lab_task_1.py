from numpy import array, random
from random import randint as ri


N = int(input())

array1 = array([ri(0, 100) for _ in range(N)])
array2 = array([ri(0, 100) for _ in range(N)])
array3 = array([ri(0, 100) for _ in range(N)])

maximum = max(
    max(array1),
    max(array2),
    max(array3)
)

sum_array1 = sum(array1)
sum_array2 = sum(array2)
sum_array3 = sum(array3)

print(maximum)
print(
    sum_array1,
    sum_array2,
    sum_array3,
    sep=", "
)