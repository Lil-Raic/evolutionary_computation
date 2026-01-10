import numpy as np
from problems.problem import Problem

class StyblinskiTang(Problem):
    def __init__(self, d):
        lower = np.full(d, -5)
        upper = np.full(d, 5)
        super().__init__(d, lower, upper, "StyblinskiTang")

    def evaluate(self, x):
        x = np.array(x)
        return 0.5 * np.sum(x ** 4 - 16 * x ** 2 + 5 * x)
