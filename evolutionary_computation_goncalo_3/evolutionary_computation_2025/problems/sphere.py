import numpy as np
from problems.problem import Problem


class Sphere(Problem):
    def __init__(self, d):
        lower = np.array([-100 if i % 2 == 0 else -10 for i in range(d)])
        upper = np.array([100 if i % 2 == 0 else 10 for i in range(d)])
        super().__init__(d, lower, upper, "Sphere")

    def evaluate(self, x):
        x = np.array(x)
        return np.sum(x ** 2)
