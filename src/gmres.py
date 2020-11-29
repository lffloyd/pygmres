import numpy as np
from src.arnoldi import arnoldi_iteration
from src.csr import multiply_matrix, parse_csr

def gmres(A, b):
    x = np.random.rand(1, len(b))

    for n in range(len(b)):
        Qn, hn = arnoldi_iteration(A, b, n)
        y = minimize(Qn, hn, b)
        x[n] = multiply_matrix(Qn, np.array([y]))[0]

    return x


def minimize(Qn, hn, b):
    return np.random.rand(1, len(b))
