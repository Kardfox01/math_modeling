from random import randint as ri
from time import sleep, time


M, N = ri(0, 5), ri(0, 5)
print("M", M, "N", N)

start = time()

for i in range(0, M):
    for j in range(0, N):
        sleep(1)
        print("j", j)
    sleep(1)
    print("i", i)

stop = time()

print("Theoretical", M * (N + 1), "Real", stop - start)