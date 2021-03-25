import pytest
import numpy as np
import numerical as nl


class build_wf:
    def __init__(self):
        pass

    def init_array(self, dim1, dim2, myval):
        arr = np.ones((dim1, dim2), dtype=complex)
        return arr*myval

    def init_vector(self, dim1, myval):
        arr = np.ones((dim1), dtype=complex)
        return arr*myval


@pytest.fixture(scope='module')
def init_obj():
    obj = build_wf()
    return obj


@pytest.fixture
def test_wfauto(init_obj):
    wf = init_obj.init_array(3, 3, 1.0)
    autocorr = init_obj.init_vector(3, 3.0)
    return wf, autocorr


def test_calc_auto(test_wfauto):
    """Test function to test calculation\
    of vector overlap."""
    assert np.array_equal(nl.calc_auto(test_wfauto[0]), test_wfauto[1])
