import numpy as np
from numpy.linalg import lstsq
from src.arnoldi import arnoldi_iteration
from src.csr import CSRMatrix


def generate_e(n):
    arr = [0] * (n+1)
    arr[0] = 1
    return np.array(arr)


def gmres(A, b, max_iter=50, min_residual=1e-8):
    A_csr = CSRMatrix(A)

    Q_values = []
    y = np.random.rand(1, len(b))

    for n in range(max_iter):
        Qn, hn = arnoldi_iteration(A_csr, b, n)
        Q_values.append(Qn)

        y = minimize(Qn, hn, b)

        rn = calculate_residual(hn, b, y, n)
        if rn < min_residual:
            return CSRMatrix(Qn).mult(y)

    return CSRMatrix(Q_values[:-1]).mult(y)


def calculate_residual(hn, b, y, n):
    e1 = generate_e(n)
    b_norm = np.linalg.norm(b)
    return np.linalg.norm(hn.dot(y) - (b_norm*e1)) / b_norm


def minimize(hn, b, n):
    e1 = generate_e(n)
    b_norm = np.linalg.norm(b)
    negated_b_norm = np.negative(b_norm)
    negated_hn = np.negative(hn)
    return lstsq(negated_hn, negated_b_norm * e1)
