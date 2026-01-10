import numpy as np
from problems.problem import Problem

class Trid(Problem):
    def __init__(self, d):
        lower = np.full(d, - d ** 2)
        upper = np.full(d, d ** 2)
        super().__init__(d, lower, upper, "Trid")

    def evaluate(self, x):
        x = np.array(x)
        return np.sum((x - 1) ** 2) - np.sum(x[:-1] * x[1:])
