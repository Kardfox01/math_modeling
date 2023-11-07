def fib(n):
    numbers = [0, 1]
    for _ in range(n - 2):
        numbers.append(
            numbers[-1] + numbers[-2]
        )

    return numbers[n - 1]

print(fib(10))