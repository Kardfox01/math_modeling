from time import time


f = lambda x: 6 * (x**2) - 5 * x + 9
N = 10**5
results = {}

array_map = [i for i in range(N)]
start = time()
array_map = list(map(f, array_map))
results["map"] = time() - start

start = time()
array_include = [f(i) for i in range(N)]
results["include"] = time() - start

start = time()
array_for = []
for i in range(N):
    array_for.append(f(i))
results["For"] = time() - start

print("Fastest:", max(results, key=results.get), "with time", max(results.values()))