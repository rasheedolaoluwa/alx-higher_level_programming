#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """
    Represents a rectangle.

    This class defines a rectangle with adjustable width and height,
    and keeps track of the number of Rectangle instances.
    It also allows for a customizable symbol for string representation.

    Attributes:
        number_of_instances (int): The number of Rectangle
        instances currently active.
        print_symbol (any): The symbol used for the string
        representation of the rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.

        Increments the number_of_instances counter upon
        each new instance creation.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieve or set the width of the Rectangle.

        Returns:
            int: The current width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the Rectangle.

        Validates and sets the width value.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieve or set the height of the Rectangle.

        Returns:
            int: The current height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the Rectangle.

        Validates and sets the height value.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate and return the area of the Rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate and return the perimeter of the Rectangle.

        Returns 0 if either width or height is 0.

        Returns:
            int: The perimeter of the rectangle, or 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Provide a printable representation of the Rectangle
        using the configured print symbol.

        Returns an empty string if width or height is 0.

        Returns:
            str: A string representation of the rectangle
            using the configured print symbol.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rec_line = [str(self.print_symbol) * self.__width for _ in
                    range(self.__height)]
        return "\n".join(rec_line)

    def __repr__(self):
        """
        Provide a string representation of the Rectangle for reproduction.

        Returns:
            str: The string representation of the rectangle.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Handle actions upon deletion of a Rectangle instance.

        Decreases the number of instances counter and prints a message.
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
