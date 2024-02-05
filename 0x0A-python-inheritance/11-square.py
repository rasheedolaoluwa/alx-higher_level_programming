#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square, inheriting from Rectangle."""

    def __init__(self, size):
        """Initializes a new Square instance.

        Validates 'size' using Rectangle's integer validator, then initializes
        the Square with 'size' for both width and height.

        Args:
            size (int): The length of all sides of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
