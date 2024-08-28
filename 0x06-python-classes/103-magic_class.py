#!/usr/bin/python3
<<<<<<< HEAD
"""Class docstring"""
=======
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
import math


class MagicClass:
<<<<<<< HEAD
    def __init__(self, radius=0):
        """Init docstring
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
                raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Area docstring"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Circumference docstring"""
=======
    """
    defines a circle
    """

    def __init__(self, radius=0):
        """
        initializes the circle
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        returns area of circle
        """
        return math.pi * self.__radius ** 2

    def circumference(self):
        """
        returns circumference of circle
        """
>>>>>>> f774a36c0b8a4ed3e362035cc43be47a8f5f50dc
        return 2 * math.pi * self.__radius
