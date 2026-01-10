import numpy as np
from problems.problem import Problem

class Rastrigin(Problem):
    def __init__(self, d):
        lower = np.full(d, -5.12)
        upper = np.full(d, 5.12)
        super().__init__(d, lower, upper, "Rastrigin")

    def evaluate(self, x):
        x = np.array(x)
        A = 10
        return A * len(x) + np.sum(x**2 - A * np.cos(2 * np.pi * x))
