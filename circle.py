"""
Manatal python Exercise 1: Object Oriented Programming
Author: Poompatai Puntitpong
"""

import numbers
import math

class Circle:

    def __init__(self, radius):
        if not isinstance(radius, numbers.Number):
            raise TypeError('Radius must be a number')
        if radius < 0:
            raise ValueError('Radius must not be negative')
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2* math.pi * self.radius