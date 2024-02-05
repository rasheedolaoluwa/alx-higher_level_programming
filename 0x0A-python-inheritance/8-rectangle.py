#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle, leveraging BaseGeometry for validation."""

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance, validating width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Validates width and height using BaseGeometry's integer_validator.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
