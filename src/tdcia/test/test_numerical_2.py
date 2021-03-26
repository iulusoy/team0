# this is an example for using requests in fixtures
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


# this is to demonstrate the request feature
# fixtures can request values from markers
@pytest.fixture()
def test_wfauto(init_obj, request):
    # request indicates that these
    # values will be taken from a marker
    marker = request.node.get_closest_marker("setval")
    # this requests the values set in the marker "setval"
    if marker == 'None':
        # missing marker - try what happens if the marker is not there
        print('Missing a marker for integrity of wave function object')
    else:
        print('Found markers {} {} {}'.format(marker.args[0], marker.args[1],
                                              marker.args[2]))
        wf = init_obj.init_array(marker.args[0], marker.args[1],
                                 marker.args[2])
        autocorr = init_obj.init_vector(marker.args[0],
                                        marker.args[2]**2 * marker.args[0])
    return wf, autocorr


@pytest.mark.setval(3, 3, 1.0)
def test_calc_auto(test_wfauto):
    """Test function to test calculation\
    of vector overlap."""
    assert np.array_equal(nl.calc_auto(test_wfauto[0]), test_wfauto[1])
