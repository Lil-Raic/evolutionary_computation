from abc import ABC, abstractmethod
import numpy as np


class Problem(ABC):
    def __init__(self, d, lower_bound, upper_bound, name):
        self.d = d
        self.lower_bound = np.array(lower_bound)
        self.upper_bound = np.array(upper_bound)
        self.name = name

    @abstractmethod
    def evaluate(self, x):
        pass

    def generate_random_solution(self):
        return np.random.uniform(self.lower_bound, self.upper_bound)
