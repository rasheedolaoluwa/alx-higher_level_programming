#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """
    Represents a rectangle.

    Manages various properties and behaviors of a rectangle, such as area,
    perimeter, and visual representation. It tracks the total number of
    instances and allows for a customizable print symbol.

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (any): The symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.

        Increments the class variable 'number_of_instances'.

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
        Retrieve the width of the Rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set and validate the width of the Rectangle.

        Args:
            value (int): The new width for the rectangle.

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
            value (int): The new height for the rectangle.

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Determine and return the larger Rectangle based on area.

        Args:
            rect_1 (Rectangle): The first Rectangle to compare.
            rect_2 (Rectangle): The second Rectangle to compare.

        Raises:
            TypeError: If either of rect_1 or rect_2 is not a
            Rectangle instance.

        Returns:
            Rectangle: The Rectangle with the larger area or
            rect_1 if areas are equal.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Create a new Rectangle instance with width and height being the same.

        Args:
            size (int): The size for both width and height of the rectangle.

        Returns:
            Rectangle: A new Rectangle instance with equal width and height.
        """
        return cls(size, size)

    def __str__(self):
        """
        Provide a printable representation of the Rectangle
        using the print symbol.

        Returns an empty string if width or height is 0.

        Returns:
            str: String representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rec_line = [str(self.print_symbol) * self.__width
                    for _ in range(self.__height)]
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

        Decreases the 'number_of_instances' counter and prints
        a goodbye message.
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
