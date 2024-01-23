#!/usr/bin/python3

"""
This module defines the class Square.
"""

class Square:
    """
    Represents a square geometric shape.

    Attributes:
        __size (int): The size of the square's side.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The length of the sides of the square.
        """
        self.__size = size
