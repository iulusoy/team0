import unittest
import numpy as np
import transform as tf


class test_area_circ(unittest.TestCase):
    def test_area_circ(self):
        """Test the area values against a reference for r >= 0."""
        self.assertEqual(tf.area_circ(1), np.pi)
        self.assertEqual(tf.area_circ(0), 0)
        self.assertEqual(tf.area_circ(2.1), np.pi * 2.1**2)

    def test_values(self):
        """Make sure value errors are recognized for area_circ."""
        self.assertRaises(ValueError, tf.area_circ, -5)
