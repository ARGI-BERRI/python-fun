from numpy import e
from sympy import binomial
from scipy.special import factorial


def bernoulli(n: int, p: float, k: int) -> float:
    return binomial(n, k) * (p ** k) * (1 - p) ** (n - k)


def poisson(λ: int, k: int) -> float:
    return (λ ** k) / factorial(k) * e ** -λ
