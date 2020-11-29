import numpy as np
from src.arnoldi import arnoldi_iteration
from src.csr import CSRMatrix


def gmres(A, b):
    A_csr = CSRMatrix(A)
    x = np.random.rand(1, len(b))

    for n in range(len(b)):
        Qn, hn = arnoldi_iteration(A, b, n)
        y = minimize(Qn, hn, b)
        x[n] = Qn.mult(y)

    return x


def minimize(Qn, hn, b):
    return np.random.rand(1, len(b))
