import pytest
import numpy as np
import transform as tf


@pytest.fixture
def my_value():
    return


@pytest.mark.circles
@pytest.mark.parametrize('myval, result',
                         [
                          (1, np.pi),
                          (0, 0),
                          (2.1, np.pi * 2.1**2),
                          # (-5, pytest.raises(ValueError)),
                         ])
def test_area_circ(myval, result):
    """Test the area values against a reference for r >= 0."""
    print(tf.area_circ(myval))
    assert tf.area_circ(myval) == result


@pytest.mark.circles
def test_values():
    """Make sure value errors are recognized for area_circ."""
    with pytest.raises(ValueError):
        tf.area_circ(-5)
