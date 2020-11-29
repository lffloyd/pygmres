import pytest
import numpy as np
from src.files import read_system_of_lineq_from_file

def test_read_system_of_lineq_from_file():
    A_expected = np.array([
        [2, 4, 5],
        [6, 2, 9],
        [1, 0, 8],
    ])
    b_expected = np.array([1, 8, 7])

    filename = "resources/mtx1.mtx"
    A, b = read_system_of_lineq_from_file(filename)
    assert (A == A_expected).all()
    assert (b == b_expected).all()
