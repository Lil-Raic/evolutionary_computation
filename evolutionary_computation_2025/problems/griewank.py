import numpy as np
from problems.problem import Problem

class Griewank(Problem):
    def __init__(self, d):
        lower = np.array([-600.0 for _ in range(d)])
        upper = np.array([600.0 for _ in range(d)])
        super().__init__(d, lower, upper, "Griewank")

    def evaluate(self, x):
        x = np.array(x)
        sum_term = np.sum(x**2) / 4000.0
        prod_term = np.prod(np.cos(x / np.sqrt(np.arange(1, len(x) + 1))))
        return sum_term - prod_term + 1
