import os
from algorithms.coa import CrayfishOptimizationAlgorithm
# Import your specific problem classes
# (Based on the file list you uploaded in 'problems/')
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


def run_experiment():
    # Configuration
    algorithm_acronym = "COA"
    surname = "Ravber"  # Change this to your actual surname
    dims = [10, 20, 30]
    runs = 50
    output_dir = "results"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # List of problem classes to execute
    problem_classes = [
        Sphere, Ackley, Griewank, Rastrigin, Schwefel26,
        Rosenbrock, Trid, StyblinskiTang, Levy, Michalewicz
    ]

    print(f"Starting {algorithm_acronym} Experiment...")

    for ProblemClass in problem_classes:
        # Get the name of the class for the filename
        prob_name = ProblemClass.__name__
        # Note: If your class names don't match the required filename format
        # perfectly, you might need a manual mapping string.

        for d in dims:
            print(f"Running {prob_name} (D={d})...")

            results = []

            # Initialize problem instance
            # We assume your Problem classes take dimension as the first argument
            # e.g., Sphere(d)
            problem_instance = ProblemClass(d)

            # Max FES for this dimension
            max_fes = 3000 * d

            for r in range(runs):
                # Create algorithm instance
                optimizer = CrayfishOptimizationAlgorithm(pop_size=30)

                # Execute logic
                best_fitness = optimizer.execute(problem_instance, max_fes)
                results.append(best_fitness)

            # Save results
            filename = f"{algorithm_acronym}-{surname}_{prob_name}D{d}.txt"
            filepath = os.path.join(output_dir, filename)

            with open(filepath, "w") as f:
                for res in results:
                    f.write(f"{res}\n")

            print(f"  -> Saved {filename}")


if __name__ == "__main__":
    run_experiment()