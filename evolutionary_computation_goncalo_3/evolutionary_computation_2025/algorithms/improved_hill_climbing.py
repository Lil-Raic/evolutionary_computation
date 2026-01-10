import numpy as np
from algorithms.algorithm import Algorithm


class ImprovedHillClimbing(Algorithm):
    def __init__(self, stepSize=0.1, increaseFactor=1.2, decreaseFactor=0.5, minStep=1e-6):
        super().__init__(isDebug=False)
        self.stepSize = stepSize
        self.increaseFactor = increaseFactor
        self.decreaseFactor = decreaseFactor
        self.minStep = minStep

    def execute(self, problem, maxFes):
        d = problem.d

        # Initial solution
        current = problem.generate_random_solution()
        current_f = problem.evaluate(current)
        fes = 1

        step = self.stepSize

        while fes < maxFes and step > self.minStep:
            improved = False
            best_neighbor = current
            best_f = current_f

            # Generate 2*d neighbors
            for i in range(d):
                # +step
                x1 = np.copy(current)
                x1[i] += step
                x1[i] = np.clip(x1[i], problem.lower_bound[i], problem.upper_bound[i])
                f1 = problem.evaluate(x1)
                fes += 1

                # -step
                x2 = np.copy(current)
                x2[i] -= step
                x2[i] = np.clip(x2[i], problem.lower_bound[i], problem.upper_bound[i])
                f2 = problem.evaluate(x2)
                fes += 1

                # Evaluate best of these two
                if f1 < best_f:
                    best_neighbor, best_f = x1, f1
                    improved = True
                if f2 < best_f:
                    best_neighbor, best_f = x2, f2
                    improved = True

                if fes >= maxFes:
                    break

            if improved:
                current = best_neighbor
                current_f = best_f
                step *= self.increaseFactor   # increase step size
            else:
                step *= self.decreaseFactor   # reduce step size

        return {"position": current, "fitness": current_f}
