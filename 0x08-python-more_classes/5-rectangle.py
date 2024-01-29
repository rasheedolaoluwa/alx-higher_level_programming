#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """
    Represents a rectangle with modifiable width and height.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance with specified width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieve the width of the Rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set and validate the width of the Rectangle.

        Args:
            value (int): New width of the rectangle.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieve the height of the Rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set and validate the height of the Rectangle.

        Args:
            value (int): New height of the rectangle.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate and return the area of the Rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate and return the perimeter of the Rectangle.
        Returns 0 if either width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Provide a printable representation of the
        Rectangle using '#' characters.
        Returns an empty string if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rec_line = ["#" * self.__width for _ in range(self.__height)]
        return "\n".join(rec_line)

    def __repr__(self):
        """
        Provide a string representation of the Rectangle for reproduction.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Print a message upon deletion of a Rectangle instance.
        """
        print("Bye rectangle...")
