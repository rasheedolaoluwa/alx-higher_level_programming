#!/usr/bin/python3
"""Module for defining the Rectangle class, inheriting from Base."""

from models.base import Base


class Rectangle(Base):
    """Class that represents a rectangle shape, derived from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle instance with dimensions and position.

        Parameters:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The horizontal margin from the left.
            y (int): The vertical margin from the top.
            id (int): An optional identifier for the rectangle.

        Raises:
            TypeError: Raised if width, height, x, or y are not integers.
            ValueError: Raised if width or height are less than or equal to 0,
                        or if x or y are negative.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Returns or sets the rectangle's width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Validates and sets the rectangle's width."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Returns or sets the rectangle's height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Validates and sets the rectangle's height."""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Returns or sets the x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Validates and sets the x-coordinate."""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Returns or sets the y-coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Validates and sets the y-coordinate."""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Prints the rectangle using '#' symbols to visualize its shape."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        print("\n" * self.y, end="")
        for h in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """Updates the rectangle's attributes using args or kwargs.

        Args:
            *args: Ordered arguments to update
            attributes (id, width, height, x, y).
            **kwargs: Key/value pairs to update attributes.
        """
        attributes = ["id", "width", "height", "x", "y"]
        if args:
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns a dictionary representation of the rectangle."""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}

    def __str__(self):
        """String representation for printing and str() conversion
        of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)
