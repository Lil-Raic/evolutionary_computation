import numpy as np
from algorithms.algorithm import Algorithm


class DifferentialEvolution(Algorithm):
    """
    Differential Evolution (DE) - rand/1/bin strategy (minimization).
    Params (as in the assignment):
      NP >= 4
      CR in [0, 1]
      F  in [0, 2]
    """

    def __init__(self, NP=20, CR=0.5, F=0.6, isDebug=False, seed=None):
        super().__init__(isDebug)

        if NP < 4:
            raise ValueError("NP must be >= 4 for DE rand/1/bin.")
        if not (0.0 <= CR <= 1.0):
            raise ValueError("CR must be in [0, 1].")
        if not (0.0 <= F <= 2.0):
            raise ValueError("F must be in [0, 2].")

        self.NP = NP
        self.CR = CR
        self.F = F
        self.rng = np.random.default_rng(seed)

    def execute(self, problem, maxFes):
        d = problem.d
        lb = np.asarray(problem.lower_bound, dtype=float)
        ub = np.asarray(problem.upper_bound, dtype=float)
        rng = self.rng

        # ----------------------------
        # 1) Initialize population
        # ----------------------------
        pop = rng.uniform(lb, ub, size=(self.NP, d))
        fitness = np.empty(self.NP, dtype=float)

        for i in range(self.NP):
            fitness[i] = float(problem.evaluate(pop[i]))

        fes = self.NP  # already evaluated NP solutions

        if self.isDebug:
            best_idx = int(np.argmin(fitness))
            print(f"Init best f = {fitness[best_idx]}")

        # ----------------------------
        # 2) Main loop until maxFes
        # ----------------------------
        while fes < maxFes:
            for i in range(self.NP):
                if fes >= maxFes:
                    break

                # Pick random a, b, c all distinct and != i
                idxs = np.arange(self.NP)
                idxs = idxs[idxs != i]
                a, b, c = rng.choice(idxs, size=3, replace=False)

                xa, xb, xc = pop[a], pop[b], pop[c]

                # Mutation: v = xa + F * (xb - xc)
                v = xa + self.F * (xb - xc)
                v = np.clip(v, lb, ub)

                # Binomial crossover (ensure at least one component from v)
                R = rng.integers(0, d)
                cross = rng.random(d) < self.CR
                cross[R] = True

                y = np.where(cross, v, pop[i])
                y = np.clip(y, lb, ub)

                # Selection
                fy = float(problem.evaluate(y))
                fes += 1

                if fy <= fitness[i]:
                    pop[i] = y
                    fitness[i] = fy

                    if self.isDebug:
                        print(f"fes={fes}: improved i={i}, f={fy}")

        # ----------------------------
        # 3) Return best solution
        # ----------------------------
        best_idx = int(np.argmin(fitness))
        return {"position": pop[best_idx].copy(), "fitness": float(fitness[best_idx])}
