#!/usr/bin/python3
"""Defines a base class BaseGeometry for geometric calculations."""


class BaseGeometry:
    """Represents basic geometric shapes."""

    def area(self):
        """
        Method placeholder for area calculation.
        Raises an exception indicating it has not been implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a given value is a positive integer.

        Args:
            name (str): The name of the parameter being validated.
            value (int): The value to check as a positive integer.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than or equal to zero.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
