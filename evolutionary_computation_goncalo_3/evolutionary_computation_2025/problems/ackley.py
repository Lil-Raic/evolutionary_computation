import numpy as np
from problems.problem import Problem

class Ackley(Problem):
    def __init__(self, d):
        lower = np.full(d, -32.768)
        upper = np.full(d, 32.768)
        super().__init__(d, lower, upper, "Ackley")

    def evaluate(self, x):
        x = np.array(x)
        a, b, c = 20, 0.2, 2 * np.pi
        sum_sq = np.mean(x ** 2)
        sum_cos = np.mean(np.cos(c * x))
        return -a * np.exp(-b * np.sqrt(sum_sq)) - np.exp(sum_cos) + a + np.e
