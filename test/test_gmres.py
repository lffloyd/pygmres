import pytest
import numpy as np
from scipy.sparse.linalg import gmres as scipy_gmres
from src.gmres import gmres

def test_gmres():
    A = np.array([
        [2, 4, 5],
        [6, 2, 9],
        [1, 0, 8],
    ])
    b = np.array([1, 8, 7])

    x_expected = scipy_gmres(A, b, atol="legacy")
    print(f'expected = {x_expected}')
    x = gmres(A, b).to_dense()
    print(f'actual = {x}')

    assert (x == x_expected).all()
