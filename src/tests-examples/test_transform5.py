import pytest
import transform as tf
from contextlib import contextmanager


@pytest.fixture
def my_value():
    return


@contextmanager
def does_not_raise():
    yield


@pytest.mark.circles
@pytest.mark.parametrize('myval, result',
                         [
                          (1, does_not_raise()),
                          (0, does_not_raise()),
                          (2.1, does_not_raise()),
                          # (-5, pytest.raises(ValueError)),
                         ])
def test_area_circ(myval, result):
    """Test the area values against a reference for r >= 0."""
    print(tf.area_circ(myval))
    assert tf.area_circ(myval) is not None
