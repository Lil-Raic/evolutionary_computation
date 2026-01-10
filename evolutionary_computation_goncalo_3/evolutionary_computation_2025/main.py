from problems.sphere import Sphere
from problems.ackley import Ackley
from problems.griewank import Griewank
from problems.rastrigin import Rastrigin
from problems.schwefel26 import Schwefel26
from problems.rosenbrock import Rosenbrock
from problems.trid import Trid
from problems.bukin import Bukin
from problems.carrom_table import CarromTable
from problems.styblinski_tang import StyblinskiTang
from problems.levy import Levy
from problems.michalewicz import Michalewicz
from algorithms.hill_climbing import HillClimbing
from algorithms.statistics_utility import StatisticsUtility
from algorithms.improved_hill_climbing import ImprovedHillClimbing
from algorithms.differential_evolution import DifferentialEvolution


functions = [Sphere, Ackley, Griewank, Rastrigin, Schwefel26, Rosenbrock,
    Trid, CarromTable, StyblinskiTang, Levy, Michalewicz]

dimensions = [2, 5, 10]


if __name__ == "__main__":


    """
    print("----------------------------------\n")
    print("            Task 1 \n")
    print("----------------------------------\n\n")
    print("\n=== Sphere ===")
    
    problem = Sphere(d)
    algo = RandomSearch(isDebug=True)

    best = algo.execute(problem, maxFes)


    print("\n=== Best solution found ===")
    print("d = 2")
    print(f"x = {best['position']}")
    print(f"f(x) = {best['fitness']}")
    print("\n")
    print("d = 5")
    d = 5
    maxFes = 3000 * d

    problem = Sphere(d)
    algo = RandomSearch(isDebug=True)

    best = algo.execute(problem, maxFes)

    print("\n=== Best solution found ===")
    print(f"x = {best['position']}")
    print(f"f(x) = {best['fitness']}")
    print("\n")

    print("d = 10")
    d = 10
    maxFes = 3000 * d

    problem = Sphere(d)
    algo = RandomSearch(isDebug=True)

    best = algo.execute(problem, maxFes)

    print("\n=== Best solution found ===")
    print(f"x = {best['position']}")
    print(f"f(x) = {best['fitness']}")
    print("\n \n \n")

    print("\n=== Ackley ===")

    for d in [2, 5, 10]:
        print(f"\nd = {d}")
        maxFes = 3000 * d

        problem = Ackley(d)
        algo = RandomSearch(isDebug=True)

        best = algo.execute(problem, maxFes)

        print("\n=== Best solution found ===")
        print(f"x = {best['position']}")
        print(f"f(x) = {best['fitness']}")
        print("\n" + "-" * 50)

    print("\n=== Griewank ===")

    for d in [2, 5, 10]:
        print(f"\nd = {d}")
        maxFes = 3000 * d

        problem = Griewank(d)
        algo = RandomSearch(isDebug=True)

        best = algo.execute(problem, maxFes)

        print("\n=== Best solution found ===")
        print(f"x = {best['position']}")
        print(f"f(x) = {best['fitness']}")
        print("\n" + "-" * 50)


    print("\n=== Rastrigin ===")

    for d in [2, 5, 10]:
        print(f"\nd = {d}")
        maxFes = 3000 * d

        problem = Rastrigin(d)
        algo = RandomSearch(isDebug=True)

        best = algo.execute(problem, maxFes)

        print("\n=== Best solution found ===")
        print(f"x = {best['position']}")
        print(f"f(x) = {best['fitness']}")
        print("\n" + "-" * 50)

    print("\n=== Schwefel26 ===")

    for d in [2, 5, 10]:
        print(f"\nd = {d}")
        maxFes = 3000 * d

        problem = Schwefel26(d)
        algo = RandomSearch(isDebug=True)

        best = algo.execute(problem, maxFes)

        print("\n=== Best solution found ===")
        print(f"x = {best['position']}")
        print(f"f(x) = {best['fitness']}")
        print("\n" + "-" * 50)

    print("\n=== Rosenbrock ===")

    for d in [2, 5, 10]:
        print(f"\nd = {d}")
        maxFes = 3000 * d

        problem = Rosenbrock(d)
        algo = RandomSearch(isDebug=True)

        best = algo.execute(problem, maxFes)

        print("\n=== Best solution found ===")
        print(f"x = {best['position']}")
        print(f"f(x) = {best['fitness']}")
        print("\n" + "-" * 50)

    print("\n=== Trid ===")

    for d in [2]:
        print(f"\nd = {d}")
        maxFes = 3000 * d

        problem = Trid(d)
        algo = RandomSearch(isDebug=True)

        best = algo.execute(problem, maxFes)

        print("\n=== Best solution found ===")
        print(f"x = {best['position']}")
        print(f"f(x) = {best['fitness']}")
        print("\n" + "-" * 50)

    print("\n=== Bukin ===")

    for d in [2, 5, 10]:
        print(f"\nd = {d}")
        maxFes = 3000 * d

        problem = Bukin(d)
        algo = RandomSearch(isDebug=True)

        best = algo.execute(problem, maxFes)

        print("\n=== Best solution found ===")
        print(f"x = {best['position']}")
        print(f"f(x) = {best['fitness']}")
        print("\n" + "-" * 50)

    print("\n=== Carrom Table ===")

    for d in [2]:
        print(f"\nd = {d}")
        maxFes = 3000 * d

        problem = CarromTable(d)
        algo = RandomSearch(isDebug=True)

        best = algo.execute(problem, maxFes)

        print("\n=== Best solution found ===")
        print(f"x = {best['position']}")
        print(f"f(x) = {best['fitness']}")
        print("\n" + "-" * 50)

    print("\n=== Styblinski-Tang ===")

    for d in [2,5,10]:
        print(f"\nd = {d}")

        maxFes = 3000 * d

        problem = StyblinskiTang(d)
        algo = RandomSearch(isDebug=True)

        best = algo.execute(problem, maxFes)

        print("\n=== Best solution found ===")
        print(f"x = {best['position']}")
        print(f"f(x) = {best['fitness']}")
        print("\n" + "-" * 50)

    print("\n=== Levy ===")

    for d in [2, 5, 10]:
        print(f"\nd = {d}")

        maxFes = 3000 * d

        problem = Levy(d)
        algo = RandomSearch(isDebug=True)

        best = algo.execute(problem, maxFes)

        print("\n=== Best solution found ===")
        print(f"x = {best['position']}")
        print(f"f(x) = {best['fitness']}")
        print("\n" + "-" * 50)

    print("\n=== Michalewicz ===")

    for d in [2, 5, 10]:
        print(f"d = {d}")
        maxFes = 3000 * d

        problem = Michalewicz(d)
        algo = RandomSearch(isDebug=True)

        best = algo.execute(problem, maxFes)

        print("\n=== Best solution found ===")
        print(f"x = {best['position']}")
        print(f"f(x) = {best['fitness']}")
        print("\n" + "-" * 50 + "\n")
"""

    """
    print("----------------------------------\n")
    print("            Task 2 \n")
    print("----------------------------------\n\n")

    for func in functions:
        for d in dimensions:

            try:
                problem = func(d)
            except:
                if func.__name__ == "Bukin" and d != 2:
                    continue
                problem = func(d)

            print(f"\n=== {problem.name} | d = {d} ===")

            # ------------------------------
            # BASIC HILL CLIMBING RESULTS
            # ------------------------------
            basic_results = []

            for i in range(100):
                algo = HillClimbing(stepSize=0.01)
                sol = algo.execute(problem, maxFes=3000 * d)
                basic_results.append(sol["fitness"])

            basic_min = StatisticsUtility.get_min(basic_results)
            basic_avg = StatisticsUtility.get_average(basic_results)
            basic_std = StatisticsUtility.get_std(basic_results)

            # Print BASIC results
            print(f"Original - Min: {basic_min:.15f}, Average: {basic_avg:.15f}, Std: {basic_std:.15f}")

            # ------------------------------
            # IMPROVED HILL CLIMBING RESULTS
            # ------------------------------
            improved_results = []

            for i in range(100):
                algo = ImprovedHillClimbing(stepSize=0.1)
                sol = algo.execute(problem, maxFes=3000 * d)
                improved_results.append(sol["fitness"])

            improved_min = StatisticsUtility.get_min(improved_results)
            improved_avg = StatisticsUtility.get_average(improved_results)
            improved_std = StatisticsUtility.get_std(improved_results)

            # Print IMPROVED results
            print(f"Improved - Min: {improved_min:.15f}, Average: {improved_avg:.15f}, Std: {improved_std:.15f}")


    #Bukin
    problem = Bukin(2)
    d = 2

    print(f"\n=== {problem.name} | d = {d} ===")

    # ------------------------------
    # BASIC HILL CLIMBING RESULTS
    # ------------------------------
    basic_results = []

    for i in range(100):
        algo = HillClimbing(stepSize=0.01)
        sol = algo.execute(problem, maxFes=3000 * d)
        basic_results.append(sol["fitness"])

    basic_min = StatisticsUtility.get_min(basic_results)
    basic_avg = StatisticsUtility.get_average(basic_results)
    basic_std = StatisticsUtility.get_std(basic_results)

    # Print BASIC results
    print(f"Original - Min: {basic_min:.15f}, Average: {basic_avg:.15f}, Std: {basic_std:.15f}")

    # ------------------------------
    # IMPROVED HILL CLIMBING RESULTS
    # ------------------------------
    improved_results = []

    for i in range(100):
        algo = ImprovedHillClimbing(stepSize=0.1)
        sol = algo.execute(problem, maxFes=3000 * d)
        improved_results.append(sol["fitness"])

    improved_min = StatisticsUtility.get_min(improved_results)
    improved_avg = StatisticsUtility.get_average(improved_results)
    improved_std = StatisticsUtility.get_std(improved_results)

    # Print IMPROVED results
    print(f"Improved - Min: {improved_min:.15f}, Average: {improved_avg:.15f}, Std: {improved_std:.15f}")
"""

    print("----------------------------------\n")
    print("            Task 3 \n")
    print("----------------------------------\n\n")


    p = Sphere(10)
    de = DifferentialEvolution(NP=20, CR=0.5, F=0.6, isDebug=True)
    best = de.execute(p, maxFes=3000 * 10)
    print(best["fitness"])
