import numpy as np

###################################################################
def rastrigin(x):
    """
    Rastrigin function.

    Parameters:
    - x: Input vector (numpy array).

    Returns:
    - Value of the Rastrigin function at the given point.
    """
    A = 10
    n = len(x)
    return A * n + np.sum(x**2 - A * np.cos(2 * np.pi * x))

###################################################################
def ackley(x):
    """
    Ackley function.

    Parameters:
    - x: Input vector (numpy array).

    Returns:
    - Value of the Ackley function at the given point.
    """
    a = 20
    b = 0.2
    c = 2 * np.pi

    term1 = -a * np.exp(-b * np.sqrt(np.sum(x**2) / len(x)))
    term2 = -np.exp(np.sum(np.cos(c * x) / len(x)))

    return term1 + term2 + a + np.exp(1)

###################################################################
def rosenbrock(x):
    """
    Rosenbrock function.

    Parameters:
    - x: Input vector (numpy array).

    Returns:
    - Value of the Rosenbrock function at the given point.
    """
    return np.sum(100 * (x[1:] - x[:-1]**2)**2 + (1 - x[:-1])**2)

###################################################################

