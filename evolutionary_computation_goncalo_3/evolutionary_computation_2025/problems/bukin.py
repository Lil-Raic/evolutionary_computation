import numpy as np
from problems.problem import Problem

class Bukin(Problem):
    def __init__(self, d):
        lower = np.array([-15, -3])
        upper = np.array([-5, 3])
        super().__init__(d, lower, upper, "Bukin")

    def evaluate(self, x):
        x = np.array(x)
        return 100 * np.sqrt(np.abs(x[1] - 0.01 * x[0] ** 2)) + 0.01 * np.abs(x[0] + 10)

