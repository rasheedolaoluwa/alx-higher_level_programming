#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, inheriting from Rectangle."""

    def __init__(self, size):
        """Initializes a new Square instance.

        Validates 'size' using the integer_validator from the Rectangle class,
        then calls the Rectangle class constructor with 'size' as both width
        and height.

        Args:
            size (int): The length of the sides of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
