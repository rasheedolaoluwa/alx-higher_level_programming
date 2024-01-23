#!/usr/bin/python3

"""
This module defines the class Square.
"""

class Square:
    """
    Represents a square geometric shape.

    Attributes:
        __size (int): The length of the square's sides.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance with a specified size.

        Args:
            size (int, optional): The length of the sides of the square.
                                   Defaults to 0.

        Raises:
            TypeError: If 'size' is not an integer.
            ValueError: If 'size' is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
