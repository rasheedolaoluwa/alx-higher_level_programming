#!/usr/bin/python3

"""
This module defines the class Square.
"""


class Square:
    """
    Represents a square geometric shape.

    Attributes:
        __size (int): The length of the square's sides,
        accessed through the size property.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance with a specified size.

        Args:
            size (int, optional): The length of the sides of the square.
            Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
