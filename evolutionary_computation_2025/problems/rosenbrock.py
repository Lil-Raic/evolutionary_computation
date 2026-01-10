import numpy as np
from problems.problem import Problem

class Rosenbrock(Problem):
    def __init__(self, d):
        lower = np.full(d, -5)
        upper = np.full(d, 10)
        super().__init__(d, lower, upper, "Rosenbrock")

    def evaluate(self, x):
        x = np.array(x)
        return np.sum(100 * (x[1:] - x[:-1] ** 2) ** 2 + (1 - x[:-1]) ** 2)
