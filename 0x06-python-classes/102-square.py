#!/usr/bin/python3

"""Define a class Square."""

class Square:
    """
    Represents a square with a customizable size.
    """

    def __init__(self, size=0):
        """
        Initialize a new square.

        Args:
            size (int): The length of the sides of the square.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new size for the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
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

    def __eq__(self, other):
        """
        Check if this square is equal in area to another square.

        Args:
            other (Square): Another square to compare with.

        Returns:
            bool: True if areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Check if this square is not equal in area to another square.

        Args:
            other (Square): Another square to compare with.

        Returns:
            bool: True if areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Check if this square is less than another square in area.

        Args:
            other (Square): Another square to compare with.

        Returns:
            bool: True if this square's area is less than the other's, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Check if this square is less than or equal to another square in area.

        Args:
            other (Square): Another square to compare with.

        Returns:
            bool: True if this square's area is less than or equal to the other's, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Check if this square is greater than another square in area.

        Args:
            other (Square): Another square to compare with.

        Returns:
            bool: True if this square's area is greater than the other's, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Check if this square is greater than or equal to another square in area.

        Args:
            other (Square): Another square to compare with.

        Returns:
            bool: True if this square's area is greater than or equal to the other's, False otherwise.
        """
        return self.area() >= other.area()
