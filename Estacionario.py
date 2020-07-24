import numpy as np
import seaborn as sns
import random
import matplotlib.pyplot as plt


def estacionario(P, n):
    Pn = P
    for i in range(0, n):
        Pn = np.dot(P, Pn)
    return Pn


P = np.array([(0.7, 0.2, 0.1),
              (0.2, 0.75, 0.05),
              (0.1, 0.1, 0.8)])

print(P)
