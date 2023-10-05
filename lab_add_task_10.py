number = int(input("Число: "))

for i in range(2, int(number**.5) + 1):
    while (number % i == 0):
        print(i, end=" ")
        number //= i

if (number != 1):
    print(number)