import math
import pytest
import numpy as np

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

TOL = 1e-7


# -----------------------------
# Sphere
# -----------------------------
def test_sphere():
    for d in [2, 5, 10]:
        p = Sphere(d)
        x_star = [0.0] * d
        f = p.evaluate(x_star)
        assert abs(f - 0.0) < TOL


# -----------------------------
# Ackley
# -----------------------------
def test_ackley():
    for d in [2, 5, 10]:
        p = Ackley(d)
        x_star = [0.0] * d
        f = p.evaluate(x_star)
        assert abs(f - 0.0) < TOL


# -----------------------------
# Griewank
# -----------------------------
def test_griewank():
    for d in [2, 5, 10]:
        p = Griewank(d)
        x_star = [0.0] * d
        f = p.evaluate(x_star)
        assert abs(f - 0.0) < TOL


# -----------------------------
# Rastrigin
# -----------------------------
def test_rastrigin():
    for d in [2, 5, 10]:
        p = Rastrigin(d)
        x_star = [0.0] * d
        f = p.evaluate(x_star)
        assert abs(f - 0.0) < TOL


# -----------------------------
# Rosenbrock
# -----------------------------
def test_rosenbrock():
    for d in [2, 5, 10]:
        p = Rosenbrock(d)
        x_star = [1.0] * d
        f = p.evaluate(x_star)
        assert abs(f - 0.0) < TOL


# -----------------------------
# Schwefel26
# -----------------------------
def test_schwefel26():
    for d in [2, 5, 10]:
        p = Schwefel26(d)
        x_star = [420.9687] * d
        expected = -418.9829 * d
        f = p.evaluate(x_star)
        assert abs(f - expected) < 1e-3  # Schwefel has larger rounding errors


# -----------------------------
# Trid
# -----------------------------
def test_trid():
    for d in [2, 5, 10]:
        p = Trid(d)
        x_star = [i * (d + 1 - i) for i in range(1, d + 1)]
        expected = -d * (d + 4) * (d - 1) / 6
        f = p.evaluate(x_star)
        assert abs(f - expected) < 1e-6


# -----------------------------
# Bukin N.6
# -----------------------------
def test_bukin():
    p = Bukin(2)
    x_star = [-10.0, 1.0]
    f = p.evaluate(x_star)
    assert abs(f - 0.0) < TOL


# -----------------------------
# Carrom Table
# -----------------------------
def test_carrom_table():
    p = CarromTable(2)
    x_star = [9.646168, -9.646168]
    expected = -24.1568155
    f = p.evaluate(x_star)
    assert abs(f - expected) < 1e-5


# -----------------------------
# Styblinski–Tang
# -----------------------------
def test_styblinski_tang():
    for d in [2, 5, 10]:
        p = StyblinskiTang(d)
        x_star = [-2.90353401818596] * d
        expected = -39.16616570377142 * d
        f = p.evaluate(x_star)
        assert abs(f - expected) < 1e-6


# -----------------------------
# Levy
# -----------------------------
def test_levy():
    for d in [2, 5, 10]:
        p = Levy(d)
        x_star = [1.0] * d
        f = p.evaluate(x_star)
        assert abs(f - 0.0) < TOL


# -----------------------------
# Michalewicz
# -----------------------------
def test_michalewicz_d2():
    p = Michalewicz(2)
    x_star = [2.202906, math.pi / 2]
    expected = -1.8013034
    f = p.evaluate(x_star)
    assert abs(f - expected) < 1e-5


def test_michalewicz_d5():
    p = Michalewicz(5)
    x_star = [2.202906, math.pi / 2, 1.284992, 1.923058, 1.720470]
    expected = -4.6876582
    f = p.evaluate(x_star)
    assert abs(f - expected) < 1e-5


def test_michalewicz_d10():
    p = Michalewicz(10)
    x_star = [2.202906, math.pi / 2, 1.284992, 1.923058, 1.720470,
              math.pi / 2, 1.454414, 1.756087, 1.655717, math.pi / 2]
    expected = -9.6601517
    f = p.evaluate(x_star)
    assert abs(f - expected) < 1e-5
