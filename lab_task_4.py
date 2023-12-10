import matplotlib.pyplot as plt
import numpy as np


# Я понятия не имею, как это сделать с meshgrid и формулами перевода

ф = np.arange(0, 8*np.pi, .01)

def spiral(b=.19):
    r = np.exp(b*ф)

    plt.polar(ф, r)
    plt.show()

def arch_spiral(k=1):
    r = k*ф

    plt.polar(ф, r)
    plt.show()

def rod_spiral(k=1):
    r = k / np.sqrt(ф)

    plt.polar(ф, r)
    plt.show()

def rose(k=.1):
    r = np.sin(k*ф)

    plt.polar(ф, r)
    plt.show()

spiral()
arch_spiral()
rod_spiral()
rose()