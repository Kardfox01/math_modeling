import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from numpy import sin, cos


def star_update(frame):
    area = np.linspace(-25, 25, 100)
    x = 12*cos(area) + 8*cos(1.5*area)
    y = 12*sin(area) - 8*sin(1.5*area)

    star.set_data(
        x*cos(frame) - y*sin(frame),
        y*cos(frame) + x*sin(frame)
    )


figure, ax = plt.subplots()

star, = plt.plot([], [], "y")

ax.set_xlim(-26, 26)
ax.set_ylim(-26, 26)

star_animation = FuncAnimation(
    figure,
    star_update,
    frames=np.linspace(-25, 25, 500),
    interval=10
)

plt.axis("equal")
plt.show()