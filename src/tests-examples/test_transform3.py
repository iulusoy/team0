import pytest
import numpy as np
import transform as tf


@pytest.mark.circles
@pytest.mark.parametrize('myinput, myref',
                         [(1, np.pi),
                          (0, 0),
                          (2.1, np.pi * 2.1**2),
                          # (-5, pytest.raises(ValueError)),
                          ])
def test_area_circ(myinput, myref):
    """Test the area values against a reference for r >= 0."""
    print(myinput)
    assert tf.area_circ(myinput) == myref


@pytest.mark.circles
def test_values():
    """Make sure value errors are recognized for area_circ."""
    with pytest.raises(ValueError):
        tf.area_circ(-5)
