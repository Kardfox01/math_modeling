number = int(input("Кол-ви чисел Фибоначчи: "))
fibonacci = [1, 1]

for i in range(number - 1):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

print(*fibonacci, sep=" ")