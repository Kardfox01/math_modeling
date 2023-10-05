_n = int(input("n: ")) + 1
b1 = int(input("b1: "))
q = int(input("q: "))

print(*[b1 * q**(n - 1) for n in range(1, _n)])