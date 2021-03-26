# this is an example for using parametrizing fixtures
import pytest
import numpy as np
import numerical as nl


class build_wf:
    def __init__(self):
        pass

    def init_array(self, dim1, dim2, myval):
        arr = np.ones((dim1, dim2), dtype=complex)
        return arr * myval

    def init_vector(self, dim1, myval):
        arr = np.ones((dim1), dtype=complex)
        return arr * myval


@pytest.fixture(scope='module')
def init_obj():
    obj = build_wf()
    return obj


# this is to demonstrate parametrizing fixtures
@pytest.fixture(params=[(3, 3, 1.0), (3, 3, 2.0)], ids=['test one', 'test two'])
def myfixture(request):
    return request.param


@pytest.fixture()
def test_wfauto(init_obj, myfixture):
    # this will get both the instance of the class from init_obj
    # and the values set in myfixture
    # it will run as many times as there are parameters in
    # myfixture, in this case twice, once for each set tuple
    print(myfixture, myfixture[0])
    wf = init_obj.init_array(myfixture[0], myfixture[1],
                             myfixture[2])
    autocorr = init_obj.init_vector(myfixture[0],
                                    myfixture[2]**2 * myfixture[0])
    return wf, autocorr


def test_calc_auto(test_wfauto):
    """Test function to test calculation\
    of vector overlap."""
    assert np.array_equal(nl.calc_auto(test_wfauto[0]), test_wfauto[1])
