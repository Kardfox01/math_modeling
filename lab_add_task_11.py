number = int(input())
denominators = set()

for i in range(1, number):
    sum = 0
    for n in range(1, i):
        if i % n == 0:
            sum += n

        if i == sum:
            denominators.add(i)

print(*sorted(denominators), sep=" ")
