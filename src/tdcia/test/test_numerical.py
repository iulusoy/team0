import pytest
import numpy as np
import numerical as nl


class build_wf:
    def __init__(self, dim1, dim2, myval):
        self.dim1 = dim1
        self.dim2 = dim2
        self.myval = myval

    def init_array(self):
        arr = np.ones((self.dim1,self.dim2), dtype=complex)
        return arr*self.myval

    def init_vector(self):
        arr = np.ones((self.dim1), dtype=complex)
        return arr*self.myval


@pytest.fixture
def test_wf():
    obj = build_wf(3, 3, 1.0)
    return obj.init_array()


@pytest.fixture
def ref_auto():
    obj = build_wf(3, 0, 3.0)
    return obj.init_vector()


def test_calc_auto(test_wf, ref_auto):
    """Test function to test calculation\
    of vector overlap."""
    assert np.array_equal(nl.calc_auto(test_wf), ref_auto)
