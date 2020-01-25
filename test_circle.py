"""
Tests for Circle Class
Author: Poompatai Puntitpong
"""

import math
import pytest
from circle import Circle

acceptable_float_difference = 1e-09

def float_equal(float_A, float_B):
    return abs(float_A - float_B) < acceptable_float_difference

def test_area():
    radius_value_array = [0, 2.5, 3.8, 10, 100.23, 987, 76538.234452]
    for radius_value in radius_value_array:
        test_circle = Circle(radius_value)
        assert float_equal(test_circle.area(), math.pi * (radius_value ** 2))

def test_perimeter():
    radius_value_array = [0, 2.5, 3.8, 10, 100.23, 987, 76538.234452]
    for radius_value in radius_value_array:
        test_circle = Circle(radius_value)
        assert float_equal(test_circle.perimeter(), 2 * math.pi * radius_value)

def test_wrong_type():
    radius_value_array = [{}, '123', []]
    for radius_value in radius_value_array:
        with pytest.raises(TypeError):
            test_circle = Circle(radius_value)

def test_negative_value():
    radius_value_array = [-1, -2, -96.2, -10800, -56678.74]
    for radius_value in radius_value_array:
        with pytest.raises(ValueError):
            test_circle = Circle(radius_value)  