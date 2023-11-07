from lab_task_1 import g


x0  = 0
y0  = 0
V0x = 10

points = [
    (
        t,
        x0 + V0x * t,
        y0 + V0x * t - ((g * t**2) / 2)
    ) for t in range(6)
]

print(*points, sep="\n")