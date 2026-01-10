import numpy as np
from algorithms.algorithm import Algorithm


class RandomSearch(Algorithm):
    def __init__(self, isDebug=False):
        super().__init__(isDebug)

    def execute(self, problem, maxFes):
        best_solution = None
        best_fitness = float("inf")

        for i in range(1, maxFes + 1):
            candidate = problem.generate_random_solution()
            fitness = problem.evaluate(candidate)

            if fitness < best_fitness:
                best_fitness = fitness
                best_solution = candidate

                # Print whenever an improvement is found
                if self.isDebug:
                    print(f"{i}: x = {candidate} = {fitness}")

        return {"position": best_solution, "fitness": best_fitness}
