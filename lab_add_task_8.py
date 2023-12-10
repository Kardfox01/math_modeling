import matplotlib.pyplot as plt
import numpy as np


def stairs(N):
    x, y = [0], [0]
    for _ in range(N):
        x.append(x[-1])
        y.append(y[-1] + 5)

        x.append(x[-1] + 5)
        y.append(y[-1])

    x.append(x[-1])
    y.append(0)

    x.append(0)
    y.append(0)

    plt.axis("equal")
    plt.plot(x, y)
    plt.show()

stairs(10)