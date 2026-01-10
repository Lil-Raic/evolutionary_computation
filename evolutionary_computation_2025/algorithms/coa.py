import numpy as np
import math
from algorithms.algorithm import Algorithm


class CrayfishOptimizationAlgorithm(Algorithm):
    def __init__(self, pop_size=30):
        super().__init__()
        self.pop_size = pop_size

    def execute(self, problem, max_evals):
        """
        Executes the COA algorithm on the given problem.
        :param problem: An instance of the Problem class (from problems/problem.py)
        :param max_evals: Maximum number of function evaluations (e.g., 3000 * d)
        :return: The best fitness value found
        """
        # 1. Retrieve problem details using your project's attribute names
        dim = problem.d
        lb = problem.lower_bound
        ub = problem.upper_bound

        # 2. Initialize Population
        # Create random individuals within the bounds [lb, ub]
        X = np.random.uniform(lb, ub, (self.pop_size, dim))
        fitness = np.array([float('inf')] * self.pop_size)

        # 3. Evaluate Initial Population
        # We assume problem.evaluate(solution) returns a scalar fitness value
        fes = 0  # Function Evaluation Counter
        g_best_X = np.zeros(dim)
        g_best_fit = float('inf')

        for i in range(self.pop_size):
            # If bounds are scalar, clip works directly. If vectors, it works element-wise.
            X[i] = np.clip(X[i], lb, ub)

            # Evaluate using the problem class
            fitness[i] = problem.evaluate(X[i])
            fes += 1

            # Update Global Best
            if fitness[i] < g_best_fit:
                g_best_fit = fitness[i]
                g_best_X = X[i].copy()

            if fes >= max_evals:
                return g_best_fit

        # 4. Main Optimization Loop
        # COA Logic: Temperature regulation and Foraging

        # Approximate iterations remaining
        # Each loop processes 'pop_size' individuals
        t = 0

        while fes < max_evals:
            t += 1
            # Calculate max_iter dynamic to current progress
            max_iter = (max_evals) / self.pop_size

            # C2 decreases from 2 to 0
            C2 = 2 - (t / max_iter)
            if C2 < 0: C2 = 0

            # Temperature: Random between 20 and 35
            temp = np.random.rand() * 15 + 20

            for i in range(self.pop_size):
                if fes >= max_evals:
                    break

                X_new = X[i].copy()

                # --- PHASE 1: HEAT AVOIDANCE (Temp > 30) ---
                if temp > 30:
                    # Define "Cave" position (Exploitation/Interaction)
                    rand_idx = np.random.randint(self.pop_size)
                    X_cave = (g_best_X + X[rand_idx]) / 2

                    if np.random.rand() < 0.5:
                        # Retreat to cave (Exploration)
                        rand_vec = np.random.rand(dim)
                        X_new = X[i] + C2 * rand_vec * (X_cave - X[i])
                    else:
                        # Competition for cave (Exploitation)
                        z = np.random.randint(self.pop_size)
                        X_new = X[i] - X[z] + X_cave

                # --- PHASE 2: FORAGING (Temp <= 30) ---
                else:
                    # Food intake factor p
                    p = 2 * np.random.rand() * (1 - (t / max_iter))
                    # Food size factor Q
                    Q = C2 * np.random.rand()

                    if Q < 0.5:
                        # Food is small, attraction to food (Global Best)
                        X_new = X[i] + p * (g_best_X - X[i])
                    else:
                        # Food is big, tear it apart
                        X_new = X[i] + np.random.rand() * (g_best_X - X[i]) * math.exp(-1 / (Q + 1e-10))

                # Boundary Check
                X_new = np.clip(X_new, lb, ub)

                # Greedy Selection (Evaluate and compare)
                new_fit = problem.evaluate(X_new)
                fes += 1

                if new_fit < fitness[i]:
                    fitness[i] = new_fit
                    X[i] = X_new

                    # Update Global Best if needed
                    if new_fit < g_best_fit:
                        g_best_fit = new_fit
                        g_best_X = X_new.copy()

        return g_best_fit