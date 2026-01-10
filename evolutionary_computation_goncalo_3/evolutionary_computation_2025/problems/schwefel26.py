import numpy as np
from problems.problem import Problem

class Schwefel26(Problem):
    def __init__(self, d):
        lower = np.full(d, -500)
        upper = np.full(d, 500)
        super().__init__(d, lower, upper, "Schwefel26")

    def evaluate(self, x):
        x = np.array(x)
        sum_term = np.sum(x * np.sin(np.sqrt(np.abs(x))))
        return - sum_term
    #418.982887272433799807913601398 * len(x)