from pathlib import Path
import numpy as np
from problems.sphere import Sphere
from problems.ackley import Ackley
from problems.griewank import Griewank
from problems.rastrigin import Rastrigin
from problems.schwefel26 import Schwefel26
from problems.rosenbrock import Rosenbrock
from problems.trid import Trid
from problems.styblinski_tang import StyblinskiTang
from problems.levy import Levy
from problems.michalewicz import Michalewicz

# Your DE implementation (adjust import to your file name)
from algorithms.differential_evolution import DifferentialEvolution


SURNAME = "Goncalo"
DIMS = [10, 20, 30]
RUNS = 50

NP = 20
CR = 0.5
F = 0.6

def safe_float(x: float) -> float:
    """Ensure we never write NaN/Inf to the file."""
    if not np.isfinite(x):
        raise ValueError(f"Invalid fitness value produced: {x}")
    return float(x)

def main():
    out_dir = Path("results")
    out_dir.mkdir(exist_ok=True)

    problems = [
        ("Sphere", Sphere),
        ("Ackley", Ackley),
        ("Griewank", Griewank),
        ("Rastrigin", Rastrigin),
        ("Schwefel26", Schwefel26),
        ("Rosenbrock", Rosenbrock),
        ("Trid", Trid),
        ("StyblinskiTang", StyblinskiTang),
        ("Levy", Levy),
        ("Michalewicz", Michalewicz),
    ]

    for prob_name, prob_cls in problems:
        for d in DIMS:
            problem = prob_cls(d)
            maxFes = 3000 * d

            results = []
            for run in range(RUNS):
                de = DifferentialEvolution(NP=NP, CR=CR, F=F)
                sol = de.execute(problem, maxFes=maxFes)  # expects {"fitness": ..., "position": ...}
                best_f = safe_float(sol["fitness"])
                results.append(best_f)

            filename = out_dir / f"DE-{SURNAME}_{prob_name}D{d}.txt"

            # Write exactly 50 lines, one number per line
            with open(filename, "w", encoding="utf-8") as f:
                for val in results:
                    # good precision + always decimal point
                    f.write(f"{val:.23f}\n")

            print(f"[OK] wrote {filename} ({len(results)} lines)")

if __name__ == "__main__":
    main()
