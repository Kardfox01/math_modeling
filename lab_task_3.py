def y1(x):
    part1 = ((x**3)**.5) / (x**3 + 3/x)
    part2 = (4 * x**7 - x**5)
    part3 = 80*((27 * x**4 + 12 * x**3 - 5 * x**2 + 10)**.5)

    return part1*part2 + part3

def y2(x):
    part1 = 3%2 + int(16.7 * 4.32)
    part2 = 14.5 + 31%12 - int(x**3.4)

    return part1 / part2

x = 3

print(y1(x))
print(y2(x))