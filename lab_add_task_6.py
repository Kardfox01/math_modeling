def pow(a, n):
    for _ in range(n - 1):
        a *= a

    return a

print(pow(5, 2))