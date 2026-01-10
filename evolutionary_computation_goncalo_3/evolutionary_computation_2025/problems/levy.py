import numpy as np
from problems.problem import Problem

class Levy(Problem):
    def __init__(self, d):
        lower = np.full(d, -10)
        upper = np.full(d, 10)
        super().__init__(d, lower, upper, "Levy")

    def evaluate(self, x):
        x = np.array(x)
        w = 1 + (x - 1) / 4
        term1 = np.sin(np.pi * w[0]) ** 2
        term2 = np.sum((w[:-1] - 1) ** 2 * (1 + 10 * np.sin(np.pi * w[:-1] + 1) ** 2))
        term3 = (w[-1] - 1) ** 2 * (1 + np.sin(2 * np.pi * w[-1]) ** 2)
        return term1 + term2 + term3

