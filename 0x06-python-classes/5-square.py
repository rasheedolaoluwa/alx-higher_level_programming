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

    def __init__(self, size):
        """
        Initializes a new Square instance with a specified size.

        Args:
            size (int): The length of the sides of the square.
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

    def my_print(self):
        """
        Prints the square using the '#' character.

        If the size is 0, it prints an empty line.
        """
        for i in range(self.__size):
            print("#" * self.__size)
        if self.__size == 0:
            print("")
