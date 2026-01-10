import numpy as np
from problems.problem import Problem

class Michalewicz(Problem):
    def __init__(self, d):
        lower = np.full(d, 0)
        upper = np.full(d, np.pi)
        super().__init__(d, lower, upper, "Michalewicz")

    def evaluate(self, x):
        x = np.array(x)
        m = 10
        i = np.arange(1, len(x) + 1)
        return -np.sum(np.sin(x) * (np.sin(i * x ** 2 / np.pi)) ** (2 * m))

