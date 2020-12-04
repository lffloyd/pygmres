import pytest
import numpy as np
from scipy.sparse.linalg import gmres as scipy_gmres
from src.gmres import gmres

def test_gmres():
    A = np.array([
        [2, 4, 0],
        [6, 2, 9],
        [1, 0, 8],
    ])
    b = np.array([1, 8, 7])

    x_expected, _ = scipy_gmres(A, b, atol="legacy")
    print(f'expected = {x_expected}, dtype = {x_expected.dtype}')
    x = gmres(A, b)
    print(f'actual = {x}, dtype = {x.dtype}')

    np.testing.assert_array_almost_equal(x, x_expected)
