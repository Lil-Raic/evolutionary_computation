import numpy as np
from algorithms.algorithm import Algorithm

class HillClimbing(Algorithm):
    def __init__(self, stepSize=0.1, isDebug=False):
        super().__init__(isDebug)
        self.stepSize = stepSize

    def execute(self, problem, maxFes):
        d = problem.d

        # Start with a random solution
        current = problem.generate_random_solution()
        current_fitness = problem.evaluate(current)
        fes = 1  # Fitness evaluations counter

        if self.isDebug:
            print(f"Start: x = {current}, f = {current_fitness}")

        while fes < maxFes:
            best_neighbor = current
            best_fit = current_fitness
            improved = False

            # Generate 2*d neighbors
            for i in range(d):
                # +step size
                x_plus = current.copy()
                x_plus[i] += self.stepSize
                x_plus[i] = np.clip(x_plus[i], problem.lower_bound[i], problem.upper_bound[i])
                f_plus = problem.evaluate(x_plus)

                # -step size
                x_minus = current.copy()
                x_minus[i] -= self.stepSize
                x_minus[i] = np.clip(x_minus[i], problem.lower_bound[i], problem.upper_bound[i])
                f_minus = problem.evaluate(x_minus)

                fes += 2

                # Pick best among {current, x_plus, x_minus}
                if f_plus < best_fit:
                    best_fit = f_plus
                    best_neighbor = x_plus.copy()
                    improved = True

                if f_minus < best_fit:
                    best_fit = f_minus
                    best_neighbor = x_minus.copy()
                    improved = True

            # If no improvement found → stop
            if not improved:
                break

            current = best_neighbor
            current_fitness = best_fit

            if self.isDebug:
                print(f"Improved: x = {current}, f = {current_fitness}")

        return {"position": current, "fitness": current_fitness}

