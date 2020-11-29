import pytest
import numpy as np
from src.files import read_system_of_lineq_from_file
from src.csr import CSRMatrix


def test_csr_mult_by_vector():
    matrix = [
        [2, 4, 5],
        [6, 2, 0],
        [1, 0, 8],
    ]
    vector = np.array([2, 4, 5])
    expected = np.array(matrix).dot(vector)

    csr_matrix = CSRMatrix(matrix)
    result = csr_matrix.mult(vector)

    assert (expected == result).all()
