import numpy as np
from problems.problem import Problem

class CarromTable(Problem):
    def __init__(self, d):
        lower = np.full(d, -10)
        upper = np.full(d, 10)
        super().__init__(d, lower, upper, "CarromTable")

    def evaluate(self, x):
        x = np.array(x)
        term1 = np.cos(x[0]) ** 2 * np.cos(x[1]) ** 2
        term2 = np.exp(2 * abs(1 - np.sqrt(x[0] ** 2 + x[1] ** 2) / np.pi))
        return - (1 / 30) * term1 * term2

