#!/usr/bin/python3

"""Define a MagicClass matching exactly a bytecode provided by Holberton."""

import math


class MagicClass:
    """
    Represents a circle with a specific radius.
    """

    def __init__(self, radius=0):
        """
        Initialize a MagicClass, which represents a circle.

        Arg:
            radius (float or int): The radius of the circle. Must be a number.

        Raises:
            TypeError: If the radius provided is neither an
            integer nor a float.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculate and return the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculate and return the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
